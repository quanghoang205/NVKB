"""Debian fixed-version tables; never infer a backport from upstream version text."""

from __future__ import annotations

from bs4 import BeautifulSoup

from nvkb.evidence.graph import Graph
from nvkb.storage.canonical import Store, entity, stable_id


def debian_packages(snapshot: dict, vulnerability: dict, store: Store) -> list[str]:
    soup = BeautifulSoup(snapshot["text"], "html.parser")
    graph = Graph(store)
    result = []
    for table in soup.find_all("table"):
        rows = table.find_all("tr")
        if not rows:
            continue
        headers = [c.get_text(" ", strip=True) for c in rows[0].find_all(["th", "td"])]
        if headers[:4] != ["Package", "Type", "Release", "Fixed Version"]:
            continue
        package_name = ""
        for row in rows[1:]:
            cells = [c.get_text(" ", strip=True) for c in row.find_all(["th", "td"])]
            if len(cells) < 4:
                continue
            package_name = cells[0] or package_name
            if package_name != "nginx" or cells[1] != "source":
                continue
            release = cells[2].strip("()")
            fixed = cells[3]
            status = "fixed"
            if fixed == "(not affected)":
                status, fixed = "not-affected", ""
            elif not fixed or fixed.startswith("("):
                status, fixed = "unknown", ""
            identifier = stable_id("PACKAGE", vulnerability["cve_id"], "debian", release, package_name)
            ref = graph.evidence(
                snapshot,
                f"table Fixed Version; package=nginx; release={cells[2]}",
                "Debian Security Team",
                vulnerability["cve_id"],
                f"Debian {release}: fixed_version={fixed or 'not specified'}, status={status}.",
                "distribution_tracker",
            )
            value = dict(distribution="debian", release=release, fixed_version=fixed, patch_status=status)
            cid = graph.claim(identifier, "distribution_patch_status", value, [ref], "Debian Security Team")
            store.save(
                entity(
                    "DistributionPackage",
                    identifier,
                    f"nginx / Debian {release} / {vulnerability['cve_id']}",
                    "Trạng thái source package đúng release; không ánh xạ sang Ubuntu hoặc RPM.",
                    [ref],
                    product_id="PRODUCT:NGINX-OSS",
                    distribution="debian",
                    release=release,
                    package_name=package_name,
                    ecosystem="debian",
                    cve_ref=vulnerability["id"],
                    fixed_version=fixed,
                    patch_status=status,
                    claim_refs=[cid],
                )
            )
            graph.relationship(vulnerability["id"], "distribution_fix", identifier, [ref], [cid])
            result.append(identifier)
    return result
