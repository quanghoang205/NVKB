"""Workspace configuration; never depends on a particular machine path."""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass
class Config:
    root: Path
    settings: dict
    sources: dict
    scope: dict

    @classmethod
    def load(cls, root: Path | None = None) -> "Config":
        if root is None:
            env = os.environ.get("NVKB_ROOT")
            if env:
                root = Path(env)
            else:
                candidates = [Path.cwd(), *Path.cwd().parents, Path(__file__).resolve().parents[2]]
                root = next((p for p in candidates if (p / "ontology/nvkb.yaml").is_file()), Path.cwd())
        root = root.resolve()

        def read(name):
            path = root / "config" / f"{name}.yaml"
            if not path.exists():
                raise ValueError(f"NVKB project not found at {root}; use --root /path/to/NVKB")
            return yaml.safe_load(path.read_text())

        return cls(root, read("settings"), read("sources"), read("scope"))

    def path(self, relative: str) -> Path:
        return self.root / relative
