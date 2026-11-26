"""NVKB v1.2 additive migration: preserve IDs, byte snapshots and original observations."""

from __future__ import annotations

import csv
import io
import json
from collections import Counter, defaultdict

from nvkb.evidence.lifecycle import assertion_key
from nvkb.evidence.relationships import contract
from nvkb.evidence.semantics import initial_semantics, inspect_evidence, source_identity
from nvkb.storage.canonical import Store, atomic_write, json_text, stable_id

SHELL_IDS = {"EVIDENCE:1107C2FF02EE37D4946300CE", "EVIDENCE:A7E3093DD56E544722EF8FDD"}


def write_csv(path, rows):
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]) if rows else ["id"])
    writer.writeheader()
    writer.writerows(rows)
    atomic_write(path, stream.getvalue())


def migrate(root):
    out = root / "reports/v1.2"
    receipt = out / "migration-receipt.json"
    if receipt.exists():
        return json.loads(receipt.read_text())
    if not (out / "baseline-manifest.json").exists() or not (out / "baseline-v1.1.tar.gz").exists():
        raise ValueError("A preserved baseline manifest and archive are required")
    store = Store(root)
    items = store.all()
    entities = {x["id"]: x for x in items}
    claims = [x for x in items if x["entity_type"] == "Claim"]
    used = {c for x in items for c in x.get("claim_refs", [])}
    signatures = defaultdict(list)
    for c in claims:
        signatures[(c["subject_entity_id"], c["predicate"], c["claim_value"], c["authority"])].append(c)
    baseline = {
        row["id"]: row
        for row in csv.DictReader((root / "reports/audit-v1.1/claim-support-ledger.csv").open())
    }
    orphan_rows, legacy_rows, unsupported_rows, relation_rows, learn_rows, impact_rows = (
        [],
        [],
        [],
        [],
        [],
        [],
    )
    for item in items:
        kind = item["entity_type"]
        item["schema_version"] = "1.2.0"
        if kind in {"Claim", "Evidence", "Relationship"}:
            for k, v in initial_semantics(item["verification_status"]).items():
                item.setdefault(k, v)
        if kind == "Evidence":
            item.update(inspect_evidence(root, item))
            item["evidence_locator"] = item["source_locator"]
            item["source_authority"], item["source_role"] = source_identity(
                item["source_url"], item["publisher"]
            )
            if item["id"] in SHELL_IDS:
                item.update(
                    source_support_status="UNSUPPORTED",
                    review_rationale="EV-01: HTML shell; no source text supports the linked statements.",
                )
        if kind == "Claim":
            refs = [entities[r] for r in item["evidence_refs"]]
            item.update(
                assertion_key=assertion_key(item),
                observation_key=stable_id("OBSERVATION", item["id"]),
                observed_at=item["created_at"],
                retrieved_at=min(r["retrieved_at"] for r in refs),
                authority_scope=item["authority"],
                source_authority=item["authority"],
                product_scope=item["subject_entity_id"],
                version_scope="Legacy scope: consult evidence; not established for all releases",
                evidence_locator="; ".join(r["id"] + ": " + r["source_locator"] for r in refs),
                reference_availability="AVAILABLE"
                if all(inspect_evidence(root, r)["reference_availability"] == "AVAILABLE" for r in refs)
                else "MISSING",
                source_integrity="HASH_MATCH"
                if all(inspect_evidence(root, r)["source_integrity"] == "HASH_MATCH" for r in refs)
                else "MISMATCH",
            )
            subject = entities[item["subject_entity_id"]]
            actual = subject.get(item["predicate"])
            value = json.loads(item["claim_value"])
            signature = (item["subject_entity_id"], item["predicate"], item["claim_value"], item["authority"])
            same = [c for c in signatures[signature] if c["id"] in used and c["id"] != item["id"]]
            state, reason, rationale = (
                "CURRENT",
                "CURRENT_REFERENCE",
                "Referenced in current read model; not a factual accuracy decision.",
            )
            if item["id"] not in used:
                if same:
                    state, reason, rationale = (
                        "HISTORICAL",
                        "HISTORICAL_GENERATION",
                        "Same subject/predicate/value/authority is referenced in a later/current generation; retain observation.",
                    )
                elif isinstance(actual, list) and value in actual:
                    state, reason, rationale = (
                        "PENDING_REVIEW",
                        "SCALAR_LIST_REPRESENTATION",
                        "Scalar is a member of current list; not a contradiction. Link repair requires review.",
                    )
                elif actual == value:
                    state, reason, rationale = (
                        "PENDING_REVIEW",
                        "MISSING_RELATIONSHIP",
                        "Value equals current field but lacks claim_refs; no automatic assertion of intent.",
                    )
                elif actual is not None:
                    state, reason, rationale = (
                        "PENDING_REVIEW",
                        "CHANGED_INTERPRETATION",
                        "Current field differs; curator must distinguish elaboration, changed interpretation or updated source.",
                    )
                else:
                    state, reason, rationale = (
                        "PENDING_REVIEW",
                        "UNKNOWN_REASON",
                        "No matching current field or observation; validity unknown.",
                    )
                orphan_rows.append(
                    dict(
                        id=item["id"],
                        subject=item["subject_entity_id"],
                        predicate=item["predicate"],
                        disposition=reason,
                        lifecycle_status=state,
                        matching_current_ids=";".join(c["id"] for c in same),
                        rationale=rationale,
                    )
                )
            elif (
                actual is not None
                and isinstance(value, str)
                and isinstance(actual, str)
                and value != actual
                and value not in actual
            ):
                state, reason, rationale = (
                    "PENDING_REVIEW",
                    "CHANGED_INTERPRETATION",
                    "Referenced claim differs from current field; review rather than silently treating both as current.",
                )
            item.update(lifecycle_status=state, disposition_reason=reason, review_reason=rationale)
            if SHELL_IDS.intersection(item["evidence_refs"]):
                item.update(
                    source_support_status="UNSUPPORTED",
                    review_rationale="EV-01: preserved HTML shell does not support this claim; replacement source review required.",
                )
                unsupported_rows.append(
                    dict(
                        id=item["id"],
                        predicate=item["predicate"],
                        legacy_status=item["verification_status"],
                        source_support_status="UNSUPPORTED",
                        decision="Preserve original claim and evidence; no automatic transfer of support to a replacement source",
                    )
                )
            row = baseline.get(item["id"])
            if row and row["baseline_status"] == "VERIFIED":
                legacy_rows.append(
                    dict(
                        id=item["id"],
                        v1_0_status="VERIFIED",
                        v1_1_status=item["verification_status"],
                        v1_2_legacy_status=item["legacy_verification_status"],
                        extraction_status=item["extraction_status"],
                        source_support_status=item["source_support_status"],
                        review_status=item["review_status"],
                        meaning="Legacy ingestion flag, not semantic approval",
                    )
                )
        if kind == "Severity":
            authority = item["scoring_authority"].split(" / ")[-1]
            # Audit signature explicitly identifies original CNA; retain its reviewed grouping key.
            item.update(
                original_authority=authority,
                distribution_channel=item["scoring_authority"],
                assessment_key=stable_id(
                    "ASSESSMENT",
                    item["subject_entity_id"],
                    authority,
                    item.get("cvss_score"),
                    item.get("cvss_vector"),
                ),
            )
        if kind == "Relationship":
            rule = contract(root, item["predicate"])
            item.update(
                graph_layer=rule["annotations"]["graph_layer"],
                semantic_meaning=rule["description"],
                direction="subject_to_object",
                rationale="Legacy association: "
                + rule["description"]
                + ". Source references alone do not establish causation.",
                version_scope="Legacy evidence scope; no all-version generalization",
                review_required=True,
            )
            if item["verification_status"] == "INFERRED":
                item["inference_type"] = (
                    "PEDAGOGICAL" if item["predicate"] == "learns_from" else "KEYWORD_ASSOCIATION"
                )
                relation_rows.append(
                    dict(
                        id=item["id"],
                        subject=item["subject_entity_id"],
                        predicate=item["predicate"],
                        object=item["object_entity_id"],
                        status="PENDING",
                        rationale=item["rationale"],
                    )
                )
            if item["predicate"] == "learns_from":
                item["rationale"] = (
                    f"{entities[item['subject_entity_id']]['name']} recommends {entities[item['object_entity_id']]['name']} as background. This legacy curriculum choice has no measured learner validation; not a technical causal edge."
                )
                learn_rows.append(
                    dict(
                        id=item["id"],
                        rationale=item["rationale"],
                        reviewer="NVKB v1.2 AI self-review",
                        status="PENDING_HUMAN_CURRICULUM_REVIEW",
                    )
                )
        store.save(item)
    # Group the exact 94 audited pairs in the read model without deleting either observation.
    groups = json.loads((root / "reports/audit-v1.1/semantic-duplicates.json").read_text())
    for group in groups["severity_same_original_authority"]:
        signature = json.loads(group["signature"])
        for identifier in group["ids"]:
            item = store.get(identifier)
            item.update(original_authority=signature[-1], assessment_key=stable_id("ASSESSMENT", *signature))
            store.save(item)
    old_label = "Authentication policy violation / Incorrect Authorization"
    for item in store.all():
        affected = [k for k, v in item.items() if isinstance(v, str) and old_label in v]
        if affected:
            impact_rows.append(
                dict(
                    id=item["id"],
                    type=item["entity_type"],
                    fields=";".join(affected),
                    action="Preserved historical observation"
                    if item["entity_type"] == "Claim"
                    else "Canonical terminology correction; classification unchanged",
                )
            )
        if item["id"] == "WEAKNESS:CWE-863":
            item["name"] = "Incorrect Authorization"
            item["verification_limitations"] = (
                "MITRE CWE-863 is authorization, not authentication. CVE classification unchanged."
            )
            store.save(item)
        elif item["entity_type"] == "Vulnerability" and affected:
            for k in affected:
                item[k] = item[k].replace(old_label, "Incorrect Authorization")
            store.save(item)
    seed_path = root / "data/curation/knowledge.yaml"
    atomic_write(seed_path, seed_path.read_text().replace(old_label, "Incorrect Authorization"))
    for name, rows in [
        ("orphan-disposition.csv", orphan_rows),
        ("legacy-verified-review.csv", legacy_rows),
        ("unsupported-source-review.csv", unsupported_rows),
        ("inferred-relationship-review.csv", relation_rows),
        ("learns-from-rationale.csv", learn_rows),
        ("taxonomy-impact.csv", impact_rows),
    ]:
        write_csv(out / name, rows)
    # Complete pre-migration ID impact index; IDs and reference destinations are unchanged.
    impact = {
        x["id"]: {
            "canonical_path": str(store.path_for(x).relative_to(root)),
            "action": "RETAIN_ID",
            "incoming_ids": [
                y["id"]
                for y in items
                if any(x["id"] == v or isinstance(v, list) and x["id"] in v for v in y.values())
            ],
        }
        for x in items
    }
    atomic_write(out / "id-impact-map.json", json_text(impact))
    result = dict(
        records_before=len(items),
        records_after=len(store.all()),
        retained_ids=len(set(entities) & {x["id"] for x in store.all()}),
        baseline_orphans=len(orphan_rows),
        legacy_verified_examined=len(legacy_rows),
        unsupported_claims=len(unsupported_rows),
        inferred_relationships=len(relation_rows),
        learns_from_rationales=len(learn_rows),
        severity_groups=len(groups["severity_same_original_authority"]),
        logical_duplicate_groups=len(groups["claim_same_value"]),
        dispositions=dict(Counter(r["disposition"] for r in orphan_rows)),
    )
    atomic_write(receipt, json_text(result))
    return result
