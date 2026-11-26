"""Scoped public package/catalogue provenance, never target discovery or runtime probing."""

from __future__ import annotations

import re
from datetime import datetime, timezone

from bs4 import BeautifulSoup

from nvkb.evidence.graph import Graph
from nvkb.storage.canonical import entity, stable_id


def ubuntu_rows(text):
    soup = BeautifulSoup(text, "html.parser")
    rows = []
    for table in soup.find_all("table"):
        headings = [x.get_text(" ", strip=True) for x in table.select("thead th")]
        if headings != ["Package", "Ubuntu Release", "Status"]:
            continue
        package = ""
        for row in table.select("tbody tr"):
            header = row.find("th")
            if header:
                package = header.get_text(" ", strip=True)
            cells = row.find_all("td", recursive=False)
            if package != "nginx" or len(cells) != 2:
                continue
            release_node = cells[0].find("span")
            if not release_node:
                continue
            release = release_node.get_text(" ", strip=True)
            status_text = " ".join(cells[1].get_text(" ", strip=True).split())
            match = re.fullmatch(r"Fixed in (\S+)", status_text)
            status = (
                "fixed"
                if match
                else "not-affected"
                if status_text == "Not affected"
                else "affected"
                if status_text in {"Needed", "Vulnerable"}
                else "unknown"
            )
            rows.append(
                dict(
                    release=release,
                    patch_status=status,
                    fixed_version=match[1] if match else "",
                    source_status=status_text,
                )
            )
    if not rows:
        raise ValueError("No recognizable Ubuntu package rows; manual source review required")
    return rows


def import_ubuntu(store, snapshot, vulnerability):
    graph = Graph(store)
    identifiers = []
    for row in ubuntu_rows(snapshot["text"]):
        identifier = stable_id("PACKAGE", vulnerability["cve_id"], "ubuntu", row["release"], "nginx")
        ref = graph.evidence(
            snapshot,
            f"table Package/Ubuntu Release/Status; package=nginx; release={row['release']}",
            "Canonical / Ubuntu",
            vulnerability["cve_id"],
            row["source_status"],
            "distribution_tracker",
        )
        cid = graph.claim(identifier, "distribution_patch_status", row, [ref], "Canonical / Ubuntu")
        claim = store.get(cid)
        claim.update(
            extraction_status="MATCHED",
            source_support_status="NOT_REVIEWED",
            review_status="NOT_REVIEWED",
            evidence_locator=f"Ubuntu package nginx / {row['release']}",
            retrieved_at=snapshot["retrieved_at"],
        )
        store.save(claim)
        store.save(
            entity(
                "DistributionPackage",
                identifier,
                f"nginx / Ubuntu {row['release']} / {vulnerability['cve_id']}",
                "Release-specific official package statement. Source-row extraction, not runtime verification.",
                [ref],
                product_id="PRODUCT:NGINX-OSS",
                distribution="ubuntu",
                release=row["release"],
                package_name="nginx",
                ecosystem="ubuntu",
                cve_ref=vulnerability["id"],
                fixed_version=row["fixed_version"],
                patch_status=row["patch_status"],
                claim_refs=[cid],
                verification_limitations="Snapshot-backed extraction; source refresh/curator mapping and runtime remain separate.",
            )
        )
        graph.relationship(
            vulnerability["id"],
            "distribution_fix",
            identifier,
            [ref],
            [cid],
            rationale="Official Ubuntu row for the exact CVE, release and source package; does not attest installed/running binary.",
        )
        identifiers.append(identifier)
    return identifiers


def kev_membership(cve_id, catalogue, *, retrieved_at, now=None, max_age_hours=48, refresh_failed=False):
    now = now or datetime.now(timezone.utc)
    age = (now - datetime.fromisoformat(retrieved_at.replace("Z", "+00:00"))).total_seconds() / 3600
    rows = catalogue.get("vulnerabilities")
    valid = isinstance(rows, list) and bool(rows) and catalogue.get("count") == len(rows)
    if not valid:
        return dict(status="UNKNOWN", snapshot_status="UNKNOWN", reason="Malformed/incomplete catalogue")
    snapshot = "PRESENT" if any(row.get("cveID") == cve_id for row in rows) else "ABSENT_AT_SNAPSHOT"
    current = "UNKNOWN" if refresh_failed or age < 0 or age > max_age_hours else snapshot
    return dict(
        status=current,
        snapshot_status=snapshot,
        catalogue_version=catalogue.get("catalogVersion", "UNKNOWN"),
        age_hours=round(age, 2),
        reason="Membership only; absence is not safety or non-exploitation evidence.",
    )


def lifecycle_state(end_month, now=None):
    month = (now or datetime.now(timezone.utc)).strftime("%Y-%m")
    if not re.fullmatch(r"\d{4}-\d{2}", end_month):
        return "UNKNOWN"
    return (
        "STANDARD_WINDOW_ENDED"
        if month > end_month
        else "STANDARD_WINDOW_OPEN"
        if month < end_month
        else "UNKNOWN"
    )
