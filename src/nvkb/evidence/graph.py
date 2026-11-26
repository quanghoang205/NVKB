"""Claim-level provenance and field-specific conflict reconciliation."""

from __future__ import annotations

import json

from nvkb.config import utcnow
from nvkb.storage.canonical import Store, entity, json_text, slug, stable_id


class Graph:
    def __init__(self, store: Store):
        self.store = store

    def evidence(
        self,
        snapshot: dict,
        locator: str,
        publisher: str,
        title: str,
        paraphrase: str,
        source_type="advisory",
        **dates,
    ) -> str:
        identifier = stable_id("EVIDENCE", snapshot["source_url"], locator, snapshot["content_hash"])
        item = entity(
            "Evidence",
            identifier,
            title,
            paraphrase,
            status="VERIFIED",
            evidence_id=identifier,
            publisher=publisher,
            document_title=title,
            source_type=source_type,
            source_locator=locator,
            paraphrase=paraphrase,
            **{k: snapshot[k] for k in ["source_url", "retrieved_at", "content_hash", "local_snapshot_path"]},
            **{k: v for k, v in dates.items() if v},
        )
        from nvkb.evidence.semantics import inspect_evidence, source_identity

        item.update(inspect_evidence(self.store.root, item))
        item["source_authority"], item["source_role"] = source_identity(snapshot["source_url"], publisher)
        item["evidence_locator"] = locator
        try:
            old = self.store.get(identifier)
        except KeyError:
            old = None
        if old:
            if snapshot.get("checked_at") and snapshot["checked_at"] != old.get("checked_at"):
                old["checked_at"] = snapshot["checked_at"]
                self.store.save(old)
            return identifier
        self.store.save(item)
        return identifier

    def claim(
        self,
        subject: str,
        predicate: str,
        value,
        refs: list[str],
        authority: str,
        status="VERIFIED",
        notes="",
        confidence=1.0,
    ) -> str:
        serialized = json.dumps(value, ensure_ascii=False, sort_keys=True)
        identifier = stable_id("CLAIM", subject, predicate, authority, serialized, sorted(refs))
        item = entity(
            "Claim",
            identifier,
            f"{subject}: {predicate}",
            notes or predicate,
            refs,
            status,
            claim_id=identifier,
            subject_entity_id=subject,
            predicate=predicate,
            claim_value=serialized,
            evidence_refs=sorted(refs),
            authority=authority,
            confidence=confidence,
            reviewer_notes=notes,
        )
        from nvkb.evidence.lifecycle import observe

        self.store.save(observe(self.store, item))
        return identifier

    def relationship(
        self,
        subject: str,
        predicate: str,
        target: str,
        refs: list[str],
        claims=(),
        status="VERIFIED",
        **metadata,
    ):
        from nvkb.evidence.relationships import contract

        rule = contract(self.store.root, predicate)
        if rule is None:
            raise ValueError(f"Unknown relationship predicate: {predicate}")
        identifier = stable_id("REL", subject, predicate, target)
        try:
            old = self.store.get(identifier)
        except KeyError:
            old = None
        if old and not metadata and old.get("reviewed_at"):
            # Ingestion can propose new evidence, but cannot undo a curator's
            # scoped decision (including withdrawal of a keyword association).
            new_refs = sorted(set(refs) - set(old.get("source_refs", [])))
            new_claims = sorted(set(claims) - set(old.get("claim_refs", [])))
            if new_refs or new_claims:
                task_id = stable_id("REVIEW", identifier, new_refs, new_claims)
                path = self.store.root / "data/review_tasks" / (slug(task_id) + ".json")
                if not path.exists():
                    self.store.write_aux(
                        path,
                        json_text(
                            dict(
                                id=task_id,
                                status="PENDING",
                                reason="REVIEWED_RELATIONSHIP_NEW_EVIDENCE",
                                relationship_id=identifier,
                                proposed_source_refs=new_refs,
                                proposed_claim_refs=new_claims,
                                observed_at=utcnow(),
                            )
                        ),
                    )
            return identifier
        if (
            old
            and not metadata
            and old.get("source_refs") == sorted(set(refs))
            and sorted(old.get("claim_refs", [])) == sorted(claims)
        ):
            return identifier
        self.store.save(
            entity(
                "Relationship",
                identifier,
                predicate,
                f"{subject} {predicate} {target}",
                refs,
                status,
                subject_entity_id=subject,
                predicate=predicate,
                object_entity_id=target,
                claim_refs=list(claims),
                graph_layer=rule["annotations"]["graph_layer"],
                semantic_meaning=rule["description"],
                direction="subject_to_object",
                rationale=metadata.pop(
                    "rationale", "Legacy source association; needs semantic review. " + rule["description"]
                ),
                version_scope=metadata.pop(
                    "version_scope", "See source evidence; no implicit all-version applicability"
                ),
                review_required=True,
                **metadata,
            )
        )
        return identifier

    def reconcile(self, subject: str, predicate: str, claims: list[dict]) -> str | None:
        """Only compare claims with the same semantic predicate; preserve every authority."""
        values = {c["claim_value"] for c in claims}
        conflicting = len(values) > 1
        if predicate == "upstream_fixed_releases":
            # A partial list does not deny fixes on branches it does not mention.
            # Compare only explicitly stated fixes on the SAME upstream branch.
            by_branch = {}
            for claim in claims:
                for version in json.loads(claim["claim_value"]):
                    branch = tuple(version.split(".")[:2])
                    by_branch.setdefault(branch, set()).add(version)
            conflicting = any(len(versions) > 1 for versions in by_branch.values())
        if not conflicting:
            ids = {c["id"] for c in claims}
            for path in (self.store.root / "data/conflicts").glob("*.json"):
                record = json.loads(path.read_text())
                if (
                    record["subject_entity_id"] == subject
                    and record["predicate"] == predicate
                    and set(record["claim_refs"]) == ids
                    and record["status"] == "CONFLICTED"
                ):
                    record.update(
                        status="RESOLVED",
                        resolved_at=utcnow(),
                        resolution="Partial branch lists are compatible; absence of a branch is not an assertion that it is unfixed.",
                    )
                    self.store.write_aux(path, json_text(record))
            for claim in claims:
                if claim["verification_status"] == "CONFLICTED":
                    claim["verification_status"] = "VERIFIED"
                    self.store.save(claim)
            return None
        identifier = stable_id("CONFLICT", subject, predicate, sorted(c["id"] for c in claims))
        record = dict(
            id=identifier,
            subject_entity_id=subject,
            predicate=predicate,
            claim_refs=[c["id"] for c in claims],
            status="CONFLICTED",
            resolution=None,
            reviewer_notes="Cần đối chiếu phạm vi, nhánh và thời điểm của từng nguồn.",
        )
        for claim in claims:
            claim["verification_status"] = "CONFLICTED"
            self.store.save(claim)
        self.store.write_aux(
            self.store.root / "data/conflicts" / (slug(identifier) + ".json"), json_text(record)
        )
        return identifier
