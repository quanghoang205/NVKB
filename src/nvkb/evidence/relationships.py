"""Typed relationship contracts sourced from LinkML; no keyword truth promotion."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import yaml


@lru_cache(maxsize=8)
def contracts(schema_path: str, mtime: int):
    schema = yaml.safe_load(Path(schema_path).read_text())
    return schema["enums"]["RelationshipPredicate"]["permissible_values"]


def contract(root, predicate):
    path = root / "ontology/nvkb.yaml"
    return contracts(str(path), path.stat().st_mtime_ns).get(predicate)


def relationship_errors(root, item, entities):
    rule = contract(root, item["predicate"])
    if not rule:
        return ["Unknown typed relationship predicate"]
    annotations = rule["annotations"]
    errors = []
    for field, allowed in [("subject_entity_id", "domain_types"), ("object_entity_id", "range_types")]:
        endpoint = entities.get(item[field])
        if endpoint and endpoint["entity_type"] not in annotations[allowed].split(","):
            errors.append(
                f"{item['predicate']} {field}: {endpoint['entity_type']} outside {annotations[allowed]}"
            )
    if item.get("review_status") == "HUMAN_APPROVED" and item.get("inference_type") == "KEYWORD_ASSOCIATION":
        errors.append("Keyword association cannot be approved as a semantic fact")
    if item.get("schema_version") == "1.2.0" and not item.get("rationale"):
        errors.append("Relationship rationale required in v1.2")
    return errors


def prerequisite_cycles(items):
    edges = {}
    for item in items:
        if item["entity_type"] == "Relationship" and item["predicate"] == "REQUIRES_KNOWLEDGE_OF":
            edges.setdefault(item["subject_entity_id"], []).append(item["object_entity_id"])
    visiting, visited, cycles = set(), set(), []

    def visit(node):
        if node in visiting:
            cycles.append(node)
            return
        if node in visited:
            return
        visiting.add(node)
        for target in edges.get(node, []):
            visit(target)
        visiting.remove(node)
        visited.add(node)

    for node in edges:
        visit(node)
    return cycles
