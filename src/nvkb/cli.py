"""Small local CLI. Canonical JSON remains the source of truth."""

from __future__ import annotations

import csv
import json
import logging
import logging.config
import platform
import shutil
import sqlite3
from functools import wraps
from pathlib import Path
from typing import Annotated

import typer
import yaml
from rich.console import Console
from rich.table import Table

from nvkb.collectors.http import SourceError
from nvkb.collectors.pipeline import sync as run_sync
from nvkb.config import Config
from nvkb.database.sqlite import build_database
from nvkb.database.sqlite import search as query
from nvkb.rendering.vault import build_vault
from nvkb.reporting.reports import export as run_export
from nvkb.reporting.reports import report as run_report
from nvkb.reporting.reports import stats as get_stats
from nvkb.storage.canonical import Store, atomic_write, json_text
from nvkb.validation.checks import generate_schema
from nvkb.validation.checks import validate as run_validate
from nvkb.versioning.versions import assess

app = typer.Typer(help="NVKB: local evidence-first NGINX knowledge library.", no_args_is_help=True)
console = Console()


def guarded(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except (ValueError, KeyError, OSError, sqlite3.Error, SourceError) as exc:
            console.print(f"[red]Error:[/red] {exc}", markup=True)
            logging.getLogger("nvkb").error("%s", exc)
            raise typer.Exit(1) from exc

    return wrapped


@app.callback()
def configure(
    ctx: typer.Context, root: Annotated[Path | None, typer.Option(help="NVKB workspace root.")] = None
):
    ctx.obj = root


def config(ctx):
    cfg = Config.load(ctx.obj)
    logging.config.dictConfig(yaml.safe_load(cfg.path("config/logging.yaml").read_text()))
    log = cfg.path("logs/nvkb.log")
    log.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("nvkb")
    if not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
        handler = logging.FileHandler(log)
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
    return cfg


@app.command()
@guarded
def doctor(ctx: typer.Context):
    """Check interpreter, dependencies, SQLite and local project health (offline)."""
    from importlib.metadata import version

    cfg = config(ctx)
    db = sqlite3.connect(":memory:")
    try:
        db.execute("CREATE VIRTUAL TABLE probe USING fts5(body)")
        fts = True
    except sqlite3.OperationalError:
        fts = False
    db.close()
    console.print_json(
        data=dict(
            root=str(cfg.root),
            python=platform.python_version(),
            sqlite=sqlite3.sqlite_version,
            fts5=fts,
            git=bool(shutil.which("git")),
            uv=bool(shutil.which("uv") or cfg.path(".tools/uv").exists()),
            dependencies={
                name: version(name)
                for name in ["linkml", "linkml-runtime", "pyvulnerabilitylookup", "typer", "jinja2"]
            },
            network="Not requested; public requests occur only during sync/enrich",
        )
    )


@app.command()
@guarded
def init(ctx: typer.Context, dry_run: bool = False):
    """Initialize missing data directories in this checked-out project."""
    cfg = config(ctx)
    from nvkb.storage.canonical import COLLECTIONS

    folders = [
        "data/raw",
        "data/history",
        "data/conflicts",
        "data/quarantine",
        "data/exports",
        "database",
        "logs",
        "reports",
        "vault/13-Research",
        "vault/15-Lectures",
    ]
    folders += ["data/canonical/" + v for v in COLLECTIONS.values()]
    if not dry_run:
        for folder in folders:
            cfg.path(folder).mkdir(parents=True, exist_ok=True)
    console.print_json(data=dict(dry_run=dry_run, directories=folders))


@app.command()
@guarded
def schema(ctx: typer.Context):
    """Generate JSON Schema and documentation directly from LinkML."""
    cfg = config(ctx)
    generate_schema(cfg.root)
    from linkml.generators.docgen import DocGenerator

    DocGenerator(
        str(cfg.path("ontology/nvkb.yaml")), directory=str(cfg.path("ontology/generated/docs"))
    ).serialize()
    console.print("Generated JSON Schema and ontology documentation.")


@app.command()
@guarded
def sync(
    ctx: typer.Context,
    year: int | None = None,
    cve: str | None = None,
    offline: bool = False,
    refresh: bool = False,
    dry_run: bool = False,
):
    """Collect official inventory by PUBLICATION year; cache and persist evidence."""
    cfg = config(ctx)
    from nvkb.normalization.enrichment import enrich_cve

    result = run_sync(
        cfg,
        year=year,
        cve_id=cve,
        offline=offline,
        refresh=refresh,
        dry_run=dry_run,
        progress=console.print,
        enrich=enrich_cve,
    )
    console.print_json(
        data={
            k: v for k, v in result.items() if k not in {"excluded_products", "changes", "excluded_by_date"}
        }
    )
    if result.get("failures"):
        raise typer.Exit(2)


@app.command()
@guarded
def enrich(ctx: typer.Context, offline: bool = False):
    """Import curated Vietnamese knowledge with official-source provenance."""
    from nvkb.normalization.enrichment import build_corpus, enrich_cve

    cfg = config(ctx)
    console.print_json(data=build_corpus(cfg, offline=offline, progress=console.print))
    store = Store(cfg.root)
    for item in store.all("Vulnerability"):
        enrich_cve(item, store)
        store.save(item)


@app.command()
@guarded
def validate(ctx: typer.Context):
    """Validate generated schema, references, dates, versions and evidence hashes."""
    result = run_validate(config(ctx).root)
    console.print_json(data=result)
    if not result["ok"]:
        raise typer.Exit(1)


@app.command("build-db")
@guarded
def build_db(ctx: typer.Context, dry_run: bool = False):
    """Rebuild SQLite atomically from canonical JSON; no network."""
    cfg = config(ctx)
    check = run_validate(cfg.root)
    if not check["ok"]:
        raise ValueError("Canonical validation failed; run nvkb validate")
    console.print_json(data=dict(dry_run=True) if dry_run else build_database(cfg.root))


@app.command("build-vault")
@guarded
def vault(ctx: typer.Context, dry_run: bool = False):
    """Render Obsidian notes, preserving authored content and personal settings."""
    console.print_json(data=build_vault(config(ctx).root, dry_run=dry_run))


@app.command()
@guarded
def build(ctx: typer.Context, dry_run: bool = False):
    """Validate and rebuild all local views/exports, completely offline."""
    cfg = config(ctx)
    result = run_validate(cfg.root)
    if not result["ok"]:
        raise ValueError(f"Canonical validation failed: {result['errors'][:5]}")
    build_vault(cfg.root, dry_run=True)  # preflight authored-content protection
    if dry_run:
        console.print("Dry run: validation passed; no build outputs written.")
        return
    database = build_database(cfg.root)
    build_vault(cfg.root)
    run_report(cfg.root)
    rendered = build_vault(cfg.root)
    console.print_json(data=dict(database=database, vault=rendered))
    if not rendered["ok"]:
        raise typer.Exit(1)


@app.command()
@guarded
def stats(ctx: typer.Context):
    """Count canonical records, graph, evidence, sources and publication years."""
    console.print_json(data=get_stats(config(ctx).root))


@app.command()
@guarded
def search(ctx: typer.Context, text: str, year: int | None = None, cve_year: int | None = None):
    """Search local SQLite. --year means publication year; --cve-year filters ID year."""
    rows = query(config(ctx).root, text, year, cve_year)
    table = Table("ID", "Name", "Verification")
    for row in rows:
        table.add_row(row["id"], row.get("title", row["name"]), row["verification_status"])
    console.print(table)
    console.print(f"{len(rows)} result(s).")


@app.command()
@guarded
def show(ctx: typer.Context, identifier: str):
    """Show canonical JSON by entity ID or CVE identifier."""
    console.print_json(data=Store(config(ctx).root).get(identifier))


@app.command("claims")
@guarded
def claims(ctx: typer.Context, subject: str, view: str = "current"):
    """Query current claims by default; --view history/review/all preserves distinctions."""
    from nvkb.database.views import query_claims

    if view not in {"current", "history", "review", "all"}:
        raise ValueError("view must be current, history, review or all")
    if subject.startswith("CVE-"):
        subject = "CVE:" + subject
    console.print_json(data=query_claims(config(ctx).root, subject, view=view))


@app.command()
@guarded
def sources(ctx: typer.Context):
    """List configured public sources."""
    console.print_json(data=config(ctx).sources)


@app.command()
@guarded
def conflicts(ctx: typer.Context):
    """List preserved source conflicts requiring manual review."""
    console.print_json(
        data=[json.loads(p.read_text()) for p in sorted(config(ctx).path("data/conflicts").glob("*.json"))]
    )


@app.command("export")
@guarded
def export_records(ctx: typer.Context, format: str = "jsonl", output: Path | None = None):
    """Export CVE master index to csv or jsonl."""
    console.print(str(run_export(config(ctx).root, format, output)))


@app.command()
@guarded
def report(ctx: typer.Context):
    """Compute coverage, quality, conflicts, missing information and history reports."""
    result = run_report(config(ctx).root)
    console.print_json(data=result["stats"])


@app.command()
@guarded
def update(ctx: typer.Context, offline: bool = False, dry_run: bool = False):
    """Refresh public sources and rebuild local views; authored notes remain protected."""
    cfg = config(ctx)
    from nvkb.normalization.enrichment import enrich_cve

    run = run_sync(
        cfg, offline=offline, refresh=not offline, dry_run=dry_run, progress=console.print, enrich=enrich_cve
    )
    if not dry_run:
        build(ctx)
    if run.get("failures"):
        raise typer.Exit(2)


@app.command("assess-inventory")
@guarded
def assess_inventory(ctx: typer.Context, inventory: Path, output: Path | None = None):
    """Compare administrator-supplied JSON/CSV inventory with documented patches."""
    cfg = config(ctx)
    if inventory.suffix.lower() == ".csv":
        with inventory.open(newline="") as stream:
            assets = list(csv.DictReader(stream))
    else:
        assets = json.loads(inventory.read_text())
    if not isinstance(assets, list) or any(not isinstance(a, dict) or not a.get("asset_id") for a in assets):
        raise ValueError("Inventory must be a list of objects with asset_id")
    if len({a["asset_id"] for a in assets}) != len(assets):
        raise ValueError("Duplicate asset_id in inventory")
    records = Store(cfg.root).all()
    entities = {i["id"]: i for i in records}
    results = [assess(a, v, entities) for a in assets for v in records if v["entity_type"] == "Vulnerability"]
    if output:
        atomic_write(output, json_text(results))
        console.print(f"Wrote {len(results)} assessments: {output}")
    else:
        console.print_json(data=results)


if __name__ == "__main__":
    app()
