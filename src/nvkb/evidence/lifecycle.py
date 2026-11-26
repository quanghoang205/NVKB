"""Conservative temporal claim management, with explicit supersession and review tasks."""

from __future__ import annotations

import json

from nvkb.config import utcnow
from nvkb.storage.canonical import json_text, slug, stable_id


def assertion_key(claim):
    return stable_id(
        "ASSERTION", claim["subject_entity_id"], claim["predicate"], json.loads(claim["claim_value"])
    )


def stream_key(claim, entities):
    locators = sorted(
        (entities[r]["source_url"], entities[r]["source_locator"])
        for r in claim["evidence_refs"]
        if r in entities
    )
    return claim["subject_entity_id"], claim["predicate"], claim["authority"], locators


def observe(store, claim):
    """A changed statement in a source stream requests review; it does not assert falsity."""
    entities = {x["id"]: x for x in store.all()}
    if claim["id"] in entities:
        return entities[claim["id"]]
    claim.update(
        lifecycle_status="CURRENT",
        observed_at=utcnow(),
        assertion_key=assertion_key(claim),
        review_reason="New source observation; source support is separate.",
    )
    predecessors = [
        x
        for x in entities.values()
        if x["entity_type"] == "Claim"
        and x.get("lifecycle_status", "CURRENT") == "CURRENT"
        and stream_key(x, entities) == stream_key(claim, entities)
        and x["claim_value"] != claim["claim_value"]
    ]
    if predecessors:
        claim.update(
            lifecycle_status="PENDING_REVIEW",
            review_reason="Source stream changed; curator must decide supersession or compatible multi-value observation.",
        )
        identifier = stable_id("REVIEW", claim["id"], sorted(x["id"] for x in predecessors))
        task = dict(
            id=identifier,
            status="PENDING",
            reason="SOURCE_STATEMENT_CHANGED",
            new_claim=claim["id"],
            prior_claims=[x["id"] for x in predecessors],
            observed_at=claim["observed_at"],
        )
        store.write_aux(store.root / "data/review_tasks" / (slug(identifier) + ".json"), json_text(task))
        for old in predecessors:
            old.update(lifecycle_status="PENDING_REVIEW", review_reason=claim["review_reason"])
            store.save(old)
    return claim


def supersede(store, old_id, new_id, *, reason, effective_at=None):
    if old_id == new_id or not reason.strip():
        raise ValueError("Distinct claims and explicit supersession rationale required")
    old, new = store.get(old_id), store.get(new_id)
    if old["entity_type"] != "Claim" or new["entity_type"] != "Claim":
        raise ValueError("Supersession endpoints must be claims")
    keys = ("subject_entity_id", "predicate", "authority")
    if any(old[k] != new[k] for k in keys):
        raise ValueError("Supersession must preserve subject, predicate and authority")
    # Reject cycles even when superseding a prior generation after repeated updates.
    pending, seen = [new_id], set()
    while pending:
        current = pending.pop()
        if current == old_id:
            raise ValueError("Supersession cycle")
        if current not in seen:
            seen.add(current)
            pending.extend(store.get(current).get("superseded_by", []))
    when = effective_at or utcnow()
    old.update(
        lifecycle_status="SUPERSEDED",
        valid_until=when,
        review_reason=reason,
        superseded_by=sorted(set(old.get("superseded_by", []) + [new_id])),
    )
    new.update(
        lifecycle_status="CURRENT",
        valid_from=when,
        review_reason=reason,
        supersedes=sorted(set(new.get("supersedes", []) + [old_id])),
    )
    with store.transaction():
        store.save(old)
        store.save(new)


def claims_for(store, subject, *, history=False):
    return [
        x
        for x in store.all("Claim")
        if x["subject_entity_id"] == subject and (history or x.get("lifecycle_status") == "CURRENT")
    ]
