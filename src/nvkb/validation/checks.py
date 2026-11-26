"""Structural validation is separate from factual verification."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

import jsonschema
from linkml_runtime.utils.schemaview import SchemaView

from nvkb.storage.canonical import atomic_write
from nvkb.versioning.versions import compare


def generate_schema(root: Path):
    from linkml.generators.jsonschemagen import JsonSchemaGenerator

    content = JsonSchemaGenerator(str(root / "ontology/nvkb.yaml"), top_class="Entity").serialize()
    atomic_write(root / "ontology/generated/nvkb.schema.json", content + "\n")


def validate(root: Path, items: list[dict] | None = None, focus_ids: set | None = None) -> dict:
    schema_path = root / "ontology/generated/nvkb.schema.json"
    if not schema_path.exists():
        raise ValueError("Generate the LinkML JSON Schema first: nvkb schema")
    schema = json.loads(schema_path.read_text())
    view = SchemaView(str(root / "ontology/nvkb.yaml"))
    records = (
        [json.loads(p.read_text()) for p in sorted((root / "data/canonical").glob("*/*.json"))]
        if items is None
        else items
    )
    counts = Counter(item.get("id", "<missing-id>") for item in records)
    entities = {item.get("id", "<missing-id>"): item for item in records}
    result = dict(
        records=len(records),
        schema_valid=0,
        schema_invalid=0,
        errors=[],
        duplicates=sum(n - 1 for n in counts.values()),
        dangling_references=0,
        evidence_missing=0,
        snapshot_errors=0,
        date_errors=0,
        version_errors=0,
        claims=0,
        claims_with_evidence=0,
    )
    definitions = "$defs" if "$defs" in schema else "definitions"
    verified_snapshots = set()

    def error(item, category, message):
        result["errors"].append(
            dict(entity_id=item.get("id", "<missing-id>"), category=category, message=message)
        )

    for item in records:
        if focus_ids is not None and item.get("id") not in focus_ids:
            continue
        kind = item.get("entity_type", "")
        if kind not in view.all_classes():
            error(item, "schema", f"Unknown entity_type {kind}")
            result["schema_invalid"] += 1
            continue
        specific = {**schema, "$ref": f"#/{definitions}/{kind}"}
        specific.pop("properties", None)
        specific.pop("required", None)
        specific.pop("additionalProperties", None)
        specific.pop("type", None)
        validator = jsonschema.Draft202012Validator(specific, format_checker=jsonschema.FormatChecker())
        failures = list(validator.iter_errors(item))
        result["schema_invalid" if failures else "schema_valid"] += 1
        for failure in failures:
            error(item, "schema", f"{'.'.join(str(p) for p in failure.path)}: {failure.message}")
        if failures:
            continue
        if kind == "Relationship":
            from nvkb.evidence.relationships import relationship_errors

            for message in relationship_errors(root, item, entities):
                error(item, "relationship_semantics", message)
        if item.get("review_status") in {"AI_REVIEWED", "HUMAN_APPROVED"}:
            for field in ["reviewer_id", "reviewed_at", "review_rationale", "evidence_locator"]:
                if not item.get(field):
                    error(item, "review_metadata", f"Missing {field}")
        if kind == "Claim":
            if item.get("source_support_status") in {"SUPPORTED", "PARTIAL"} and item.get(
                "review_status"
            ) not in {"AI_REVIEWED", "HUMAN_APPROVED"}:
                error(item, "review_metadata", "Source support requires explicit reviewer decision")
            if (
                item.get("inference_type") == "KEYWORD_ASSOCIATION"
                and item.get("source_support_status") == "SUPPORTED"
            ):
                error(item, "review_metadata", "Keyword match is not semantic source support")
            for field, reverse in [("supersedes", "superseded_by"), ("superseded_by", "supersedes")]:
                for target in item.get(field, []):
                    if target in entities and item["id"] not in entities[target].get(reverse, []):
                        error(item, "supersession", f"Nonreciprocal {field}: {target}")
            if (
                item.get("valid_from")
                and item.get("valid_until")
                and item["valid_from"] > item["valid_until"]
            ):
                error(item, "lifecycle", "Validity interval is reversed")
        if kind == "Vulnerability":
            if item["id"] != "CVE:" + item["cve_id"]:
                error(item, "identity", "Entity ID does not match cve_id")
            if item.get("cve_year") != int(item["cve_id"].split("-")[1]):
                result["date_errors"] += 1
                error(item, "date", "cve_year does not match CVE ID year")
            if item.get("publication_date") and item.get("publication_year") != int(
                item["publication_date"][:4]
            ):
                result["date_errors"] += 1
                error(item, "date", "publication_year does not match publication_date")
        for slot in view.class_induced_slots(kind):
            if slot.range in view.all_classes() and slot.name in item:
                values = item[slot.name] if slot.multivalued else [item[slot.name]]
                for reference in values or []:
                    if reference not in entities:
                        result["dangling_references"] += 1
                        error(item, "reference", f"{slot.name}: missing {reference}")
                    elif (
                        slot.range not in {"Entity", "KnowledgeEntity"}
                        and entities[reference]["entity_type"] != slot.range
                    ):
                        result["dangling_references"] += 1
                        error(
                            item,
                            "reference",
                            f"{slot.name}: expected {slot.range}, got {entities[reference]['entity_type']}",
                        )
        if (
            kind != "Evidence"
            and item["verification_status"] in {"VERIFIED", "CORROBORATED"}
            and not item.get("source_refs")
        ):
            result["evidence_missing"] += 1
            error(item, "evidence", "Verified entity has no evidence")
        if kind == "Claim":
            result["claims"] += 1
            if item.get("evidence_refs") and all(r in entities for r in item["evidence_refs"]):
                result["claims_with_evidence"] += 1
            elif item["verification_status"] in {"VERIFIED", "CORROBORATED"}:
                result["evidence_missing"] += 1
                error(item, "evidence", "Verified claim has no usable evidence")
        if kind == "Evidence":
            path = item.get("local_snapshot_path")
            if path and (path, item["content_hash"]) not in verified_snapshots:
                snapshot = (root / path).resolve()
                if (
                    not snapshot.is_relative_to(root.resolve())
                    or not snapshot.is_file()
                    or hashlib.sha256(snapshot.read_bytes()).hexdigest() != item["content_hash"]
                ):
                    result["snapshot_errors"] += 1
                    error(item, "snapshot", f"Missing or altered snapshot: {path}")
                verified_snapshots.add((path, item["content_hash"]))
        try:
            for earlier, later in [("created_at", "updated_at"), ("publication_date", "last_modified_date")]:
                if (
                    item.get(earlier)
                    and item.get(later)
                    and datetime.fromisoformat(item[earlier].replace("Z", "+00:00"))
                    > datetime.fromisoformat(item[later].replace("Z", "+00:00"))
                ):
                    result["date_errors"] += 1
                    error(item, "date", f"{earlier} is after {later}")
        except ValueError as exc:
            result["date_errors"] += 1
            error(item, "date", str(exc))
        if kind == "VersionRange":
            try:
                if (
                    item.get("lower")
                    and item.get("upper")
                    and compare(item["lower"], item["upper"], item["ecosystem"]) > 0
                ):
                    raise ValueError("Lower version exceeds upper version")
            except ValueError as exc:
                result["version_errors"] += 1
                error(item, "version", str(exc))
    from nvkb.evidence.relationships import prerequisite_cycles

    for node in prerequisite_cycles(records):
        error(entities[node], "learning_graph", "Prerequisite cycle")
    result["ok"] = not result["errors"] and result["duplicates"] == 0
    return result
