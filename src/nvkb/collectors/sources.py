"""Parsing official source formats and product boundaries."""

from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

CVE_PATTERN = re.compile(r"CVE-\d{4}-\d{4,}")
PRODUCTS = {
    "NGINX-OSS": ("NGINX Open Source", "NGINX / F5", True, "https://nginx.org/en/"),
    "NGINX-PLUS": ("NGINX Plus", "F5", False, "https://docs.nginx.com/nginx/"),
    "NGINX-UNIT": ("NGINX Unit", "NGINX / F5", False, "https://unit.nginx.org/"),
    "NGINX-GATEWAY-FABRIC": (
        "NGINX Gateway Fabric",
        "F5",
        False,
        "https://docs.nginx.com/nginx-gateway-fabric/",
    ),
    "F5-NGINX-INGRESS": (
        "F5 NGINX Ingress Controller",
        "F5",
        False,
        "https://docs.nginx.com/nginx-ingress-controller/",
    ),
    "COMMUNITY-INGRESS-NGINX": (
        "Kubernetes community ingress-nginx",
        "Kubernetes",
        False,
        "https://github.com/kubernetes/ingress-nginx",
    ),
    "NGINX-NJS": ("NGINX njs", "NGINX / F5", False, "https://nginx.org/en/docs/njs/"),
    "THIRD-PARTY-MODULES": ("Third-party modules", "Various", False, "https://nginx.org/en/docs/"),
    "THIRD-PARTY-DEPENDENCIES": (
        "Third-party dependencies",
        "Various",
        False,
        "https://nginx.org/en/docs/configure.html",
    ),
}


def classify_product(name: str) -> str | None:
    value = name.strip().lower()
    exact = {v[0].lower(): "PRODUCT:" + k for k, v in PRODUCTS.items()}
    return exact.get(value) or {
        "nginx": "PRODUCT:NGINX-OSS",
        "nginx open source": "PRODUCT:NGINX-OSS",
        "ingress-nginx": "PRODUCT:COMMUNITY-INGRESS-NGINX",
    }.get(value)


def discover(html: str, url: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    records = {}
    for li in soup.find_all("li"):
        text = li.get_text("\n", strip=True)
        ids = CVE_PATTERN.findall(text)
        if not ids or "Vulnerable:" not in text:
            continue
        flat = li.get_text(" ", strip=True)
        fixed = re.search(r"Not vulnerable:\s*(.*?)\s*Vulnerable:", flat)
        affected = re.search(r"(?<!Not )Vulnerable:\s*(.*?)(?:The patch|$)", flat)
        severity = re.search(r"Severity:\s*(\w+)", flat)
        for cve in sorted(set(ids)):
            row = dict(
                cve_id=cve,
                title=text.splitlines()[0],
                severity=severity.group(1) if severity else "unknown",
                affected=affected.group(1).strip() if affected else "",
                fixed=fixed.group(1).strip() if fixed else "",
                advisory_urls=[
                    urljoin(url, a["href"])
                    for a in li.find_all("a", href=True)
                    if a.get_text(strip=True) == "Advisory"
                ],
                patch_urls=[
                    urljoin(url, a["href"])
                    for a in li.find_all("a", href=True)
                    if a.get_text(strip=True) == "The patch"
                ],
            )
            if cve in records and records[cve] != row:
                raise ValueError(f"Conflicting duplicate advisory: {cve}")
            records[cve] = row
    if not records:
        raise ValueError("No advisories parsed; source format may have changed")
    return sorted(records.values(), key=lambda row: row["cve_id"])


def cve_url(root: str, identifier: str) -> str:
    if not CVE_PATTERN.fullmatch(identifier):
        raise ValueError(f"Invalid CVE identifier: {identifier}")
    _, year, number = identifier.split("-")
    return f"{root}/{year}/{number[:-3]}xxx/{identifier}.json"
