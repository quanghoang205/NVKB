"""Discovery -> cache -> normalize -> reconcile -> validate -> persist."""

from __future__ import annotations

import json
from datetime import date

from nvkb.collectors.distribution import debian_packages
from nvkb.collectors.http import Fetcher, SourceError
from nvkb.collectors.sources import cve_url, discover
from nvkb.config import Config, utcnow
from nvkb.normalization.cve import normalized_cve
from nvkb.storage.canonical import Store, atomic_write, json_text


def sync(
    config: Config,
    *,
    year=None,
    cve_id=None,
    offline=False,
    refresh=False,
    dry_run=False,
    progress=print,
    enrich=None,
) -> dict:
    if dry_run:
        return dict(
            dry_run=True,
            action="Discover official inventory, fetch public CVE records, normalize and persist",
            year=year,
            cve_id=cve_id,
            offline=offline,
            writes=0,
        )
    store = Store(config.root)
    fetcher = Fetcher(config, offline=offline, refresh=refresh)
    years = [year] if year else config.scope["publication_years"]
    cutoff = date.fromisoformat(str(config.scope.get("as_of", date.today().isoformat())))
    results = dict(
        started_at=utcnow(),
        as_of=cutoff.isoformat(),
        scope_years=years,
        offline=offline,
        discovered=[],
        in_scope=[],
        retrieved=[],
        awaiting_metadata=[],
        excluded_by_date=[],
        excluded_products=[],
        failures=[],
        changes={},
        partial=bool(cve_id or year),
    )
    try:
        if not config.sources["nginx"].get("enabled", True):
            raise ValueError("NGINX discovery source is disabled")
        vendor = fetcher.fetch(config.sources["nginx"]["url"], "nginx")
        inventory = discover(vendor["text"], vendor["source_url"])
        results["discovered"] = [r["cve_id"] for r in inventory]
        if cve_id:
            inventory = [r for r in inventory if r["cve_id"] == cve_id]
            if not inventory:
                raise ValueError(f"CVE is not in official NGINX inventory: {cve_id}")
        atomic_write(
            config.path("data/raw/nginx/discovery.json"),
            json_text(
                dict(
                    source_url=vendor["source_url"], retrieved_at=vendor["retrieved_at"], advisories=inventory
                )
            ),
        )
        for number, advisory in enumerate(inventory, 1):
            identifier = advisory["cve_id"]
            program, lookup, detail = None, None, None
            if config.sources["cve"].get("enabled", True):
                try:
                    program = fetcher.fetch(
                        cve_url(config.sources["cve"]["root"], identifier), "cve", expect_json=True
                    )
                except SourceError as exc:
                    progress(f"Metadata unavailable: {identifier}: {exc}")
            metadata = json.loads(program["text"]).get("cveMetadata", {}) if program else {}
            publication = metadata.get("datePublished")
            if publication:
                published = date.fromisoformat(publication[:10])
                if published.year not in years or published > cutoff:
                    results["excluded_by_date"].append(dict(cve_id=identifier, publication_date=publication))
                    continue
                results["in_scope"].append(identifier)
            else:
                results["awaiting_metadata"].append(identifier)
                # Retain a record with unknown publication date; never silently exclude by CVE ID year.
            progress(f"[{number}/{len(inventory)}] {identifier}: metadata, evidence, versions")
            if config.sources["vulnerability_lookup"].get("enabled", True):
                try:
                    url = (
                        config.sources["vulnerability_lookup"]["url"].rstrip("/")
                        + "/api/vulnerability/"
                        + identifier
                    )
                    lookup = fetcher.fetch(url, "vulnerability_lookup", sdk_id=identifier)
                except SourceError as exc:
                    progress(f"CIRCL unavailable: {exc}")
            for url in advisory["advisory_urls"]:
                if "mailman.nginx.org/" in url:
                    try:
                        detail = fetcher.fetch(url, "nginx")
                    except SourceError:
                        pass
            try:
                with store.transaction():
                    normalized = normalized_cve(
                        store, advisory, vendor, program, lookup, detail, persist=False
                    )
                    record = normalized["record"]
                    results["excluded_products"].extend(normalized["excluded_products"])
                    if config.sources.get("debian", {}).get("enabled", True):
                        try:
                            distro = fetcher.fetch(
                                "https://security-tracker.debian.org/tracker/" + identifier, "distribution"
                            )
                            packages = debian_packages(distro, record, store)
                            record["distribution_status"] = record["distribution_backports"] = packages
                        except SourceError:
                            pass
                    if enrich:
                        enrich(record, store)
                    results["changes"][identifier] = store.save(record)
                    from nvkb.validation.checks import validate

                    check = validate(config.root, store.all(), focus_ids=store.pending_ids)
                    if not check["ok"]:
                        raise ValueError(f"Canonical validation failed: {check['errors'][:3]}")
                results["changes"][identifier] = store.last_commit_changes[record["id"]]
                results["retrieved"].append(identifier)
            except (ValueError, KeyError, TypeError) as exc:
                failed = dict(cve_id=identifier, error=str(exc), stage="normalization")
                results["failures"].append(failed)
                atomic_write(config.path(f"data/quarantine/{identifier}.json"), json_text(failed))
                progress(f"Quarantined {identifier}: {exc}")
        results["failures"].extend(fetcher.failures)
        results["finished_at"] = utcnow()
        path = "data/pipeline-last-partial.json" if results["partial"] else "data/pipeline-last.json"
        atomic_write(config.path(path), json_text(results))
        atomic_write(
            config.path("logs/pipeline-" + results["started_at"].replace(":", "-") + ".json"),
            json_text(results),
        )
        return results
    finally:
        fetcher.close()
