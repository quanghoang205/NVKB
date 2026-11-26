"""Atomic canonical storage with content-based history and stable identifiers."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import tempfile
from contextlib import contextmanager
from pathlib import Path

from nvkb.config import utcnow

COLLECTIONS = {
    "Advisory": "advisories",
    "Vulnerability": "vulnerabilities",
    "Product": "products",
    "Version": "versions",
    "VersionRange": "version_ranges",
    "Module": "modules",
    "Component": "components",
    "Protocol": "protocols",
    "Weakness": "weaknesses",
    "AffectedCondition": "conditions",
    "Impact": "impacts",
    "Severity": "severities",
    "Patch": "patches",
    "Mitigation": "mitigations",
    "Evidence": "evidence",
    "Reference": "references",
    "Claim": "claims",
    "Relationship": "relationships",
    "ConfigurationDirective": "configuration_directives",
    "DistributionPackage": "distribution_packages",
    "DeploymentArchitecture": "deployment_architectures",
    "SecurityControl": "security_controls",
    "LearningObjective": "learning_objectives",
}


def stable_id(prefix: str, *values) -> str:
    payload = json.dumps(values, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return f"{prefix}:{hashlib.sha256(payload.encode()).hexdigest()[:24].upper()}"


def slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")


def json_text(data) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def atomic_write(path: Path, content: str | bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = content.encode() if isinstance(content, str) else content
    fd, temporary = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def entity(kind: str, identifier: str, name: str, description: str, refs=(), status="VERIFIED", **fields):
    now = utcnow()
    if kind in {"Claim", "Evidence", "Relationship"}:
        from nvkb.evidence.semantics import initial_semantics

        fields = {**initial_semantics(status), **fields}
    return dict(
        id=identifier,
        name=name,
        description=description,
        entity_type=kind,
        schema_version="1.2.0",
        created_at=now,
        updated_at=now,
        source_refs=sorted(set(refs)),
        verification_status=status,
        **fields,
    )


class Store:
    def __init__(self, root: Path):
        self.root = root
        self._cache = None
        self._pending = None
        self._pending_aux = None
        self.last_commit_changes = {}

    def path_for(self, item: dict) -> Path:
        return self.root / "data/canonical" / COLLECTIONS[item["entity_type"]] / (slug(item["id"]) + ".json")

    def save(self, item: dict) -> str:
        path = self.path_for(item)
        old = json.loads(path.read_text()) if path.exists() else None
        if old and old["id"] != item["id"]:
            raise ValueError(f"Canonical filename collision: {old['id']} and {item['id']}")
        if self._pending is not None:
            for pending in self._pending.values():
                if pending["id"] != item["id"] and self.path_for(pending) == path:
                    raise ValueError(f"Canonical filename collision: {pending['id']} and {item['id']}")
            self._pending[item["id"]] = copy.deepcopy(item)
            return "staged"
        if old:
            item["created_at"] = old["created_at"]
            if old.get("curated_fields") and not item.get("curated_fields"):
                for field in old["curated_fields"]:
                    if field in old:
                        item[field] = copy.deepcopy(old[field])
                item["curated_fields"] = list(old["curated_fields"])
                # Keep traceable prior observations as well as the current
                # research edition; lifecycle decides what is current.
                for field in ["claim_refs", "source_refs", "unresolved_conflicts"]:
                    if field in old or field in item:
                        item[field] = sorted(set(item.get(field, []) + old.get(field, [])))
            if item["entity_type"] == "Severity":
                for field in ["assessment_key", "original_authority", "distribution_channel"]:
                    if field in old and field not in item:
                        item[field] = old[field]
            if item["entity_type"] == "Vulnerability":
                for field in [
                    "kev_status",
                    "kev_snapshot_status",
                    "kev_catalogue_version",
                    "kev_evidence_id",
                    "kev_checked_at",
                    "lifecycle_status",
                    "lifecycle_rationale",
                ]:
                    if field in old and field not in item:
                        item[field] = old[field]
                for field in ["impact_refs", "official_mitigation_refs"]:
                    item[field] = sorted(set(item.get(field, []) + old.get(field, [])))
                for field in ["distribution_status", "distribution_backports"]:
                    extras = [r for r in old.get(field, []) if self.get(r).get("distribution") != "debian"]
                    item[field] = sorted(set(item.get(field, []) + extras))
            if old.get("curation_version") and not item.get("curation_version"):
                item["curation_version"] = old["curation_version"]
                for field in [
                    "research_body",
                    "article_body",
                    "prerequisites",
                    "assessment",
                    "answer_explanations",
                    "diagram",
                ]:
                    if field in old:
                        item[field] = old[field]
                curated_claims = [
                    c
                    for c in old.get("claim_refs", [])
                    if self.get(c).get("reviewer_id") == "nvkb-v1.2-ai-curator"
                ]
                item["claim_refs"] = sorted(set(item.get("claim_refs", []) + curated_claims))
            if item["entity_type"] in {"Version", "Product", "Weakness", "Patch", "Reference"}:
                item["source_refs"] = sorted(set(item["source_refs"] + old.get("source_refs", [])))

            def meaningful(d):
                return {k: v for k, v in d.items() if k not in {"updated_at", "created_at"}}

            if meaningful(old) == meaningful(item):
                item["updated_at"] = old["updated_at"]
                if self._cache is not None:
                    self._cache[item["id"]] = copy.deepcopy(item)
                return "unchanged"
        item["updated_at"] = utcnow()
        text = json_text(item)
        history_id = stable_id("HISTORY", item["id"], text)
        event = dict(
            id=history_id,
            entity_id=item["id"],
            action="modified" if old else "created",
            changed_at=item["updated_at"],
            before=old,
            after=item,
        )
        atomic_write(self.root / "data/history" / (slug(history_id) + ".json"), json_text(event))
        atomic_write(path, text)
        if self._cache is not None:
            self._cache[item["id"]] = copy.deepcopy(item)
        return event["action"]

    def all(self, kind: str | None = None) -> list[dict]:
        if self._cache is None:
            paths = sorted((self.root / "data/canonical").glob("*/*.json"))
            self._cache = {item["id"]: item for path in paths for item in [json.loads(path.read_text())]}
        combined = {**self._cache, **(self._pending or {})}
        return [
            copy.deepcopy(item)
            for _, item in sorted(combined.items())
            if kind is None or item["entity_type"] == kind
        ]

    def get(self, identifier: str) -> dict:
        if self._cache is None:
            self.all()
        combined = {**self._cache, **(self._pending or {})}
        key = identifier if identifier in combined else "CVE:" + identifier
        return copy.deepcopy(combined[key])

    def write_aux(self, path: Path, content: str):
        if self._pending_aux is not None:
            self._pending_aux[path] = content
        else:
            atomic_write(path, content)

    @property
    def pending_ids(self):
        return set(self._pending or {})

    @contextmanager
    def transaction(self):
        """Stage one source record for validation. Each committed file uses atomic replacement."""
        if self._pending is not None:
            raise ValueError("Nested canonical transactions are not supported")
        self._pending, self._pending_aux = {}, {}
        try:
            yield self
            pending, auxiliary = self._pending, self._pending_aux
            self._pending = self._pending_aux = None
            self.last_commit_changes = {}
            for item in pending.values():
                self.last_commit_changes[item["id"]] = self.save(item)
            for path, content in auxiliary.items():
                atomic_write(path, content)
        finally:
            self._pending = self._pending_aux = None
