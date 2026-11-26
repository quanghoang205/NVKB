"""Independent provenance dimensions. Reading bytes never confers semantic approval."""

from __future__ import annotations

import hashlib
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from nvkb.config import utcnow

REVIEW_FIELDS = (
    "legacy_verification_status reference_availability source_integrity extraction_status "
    "source_support_status review_status inference_type reviewer_id reviewed_at review_rationale "
    "evidence_locator source_authority source_role authority_scope product_scope version_scope "
    "verification_limitations observed_at checked_at"
).split()


def initial_semantics(status="UNKNOWN"):
    return dict(
        legacy_verification_status=status,
        reference_availability="UNKNOWN",
        source_integrity="NOT_CHECKED",
        extraction_status="NOT_CHECKED",
        source_support_status="NOT_REVIEWED",
        review_status="NOT_REVIEWED",
        inference_type="INTERPRETATION" if status == "INFERRED" else "SOURCE_STATEMENT",
        verification_limitations="Legacy verification is ingestion provenance, not semantic or human approval.",
    )


def source_identity(url, publisher):
    host = urlparse(url).hostname or ""
    if host == "vulnerability.circl.lu":
        return "CVE Program / original CNA (see record)", "AGGREGATOR"
    if host in {"raw.githubusercontent.com", "www.cve.org", "cve.org"} and (
        "CVEProject" in url or "cve.org" in host
    ):
        return "CVE Program / original CNA (see record)", "DISTRIBUTION_CHANNEL"
    return publisher, "ORIGINAL_AUTHORITY"


def usable_text(text):
    soup = BeautifulSoup(text, "html.parser")
    for element in soup(["script", "style"]):
        element.decompose()
    visible = soup.get_text(" ", strip=True)
    shell = len(visible) < 500 and any(
        x in visible.lower()
        for x in (
            "doesn't work properly without javascript",
            "does not work properly without javascript",
            "please enable javascript",
        )
    )
    return visible if len(visible) >= 100 and not shell else ""


def inspect_evidence(root: Path, evidence):
    path = (root / evidence.get("local_snapshot_path", "")).resolve()
    available = path.is_relative_to(root.resolve()) and path.is_file()
    result = dict(
        reference_availability="AVAILABLE" if available else "MISSING", source_integrity="NOT_CHECKED"
    )
    if available:
        result["source_integrity"] = (
            "HASH_MATCH"
            if hashlib.sha256(path.read_bytes()).hexdigest() == evidence["content_hash"]
            else "MISMATCH"
        )
    return result


def review_claim(
    store,
    claim_id,
    *,
    support,
    reviewer_id,
    rationale,
    locator,
    excerpt,
    evidence_id,
    inference="SOURCE_STATEMENT",
    reviewer_kind="AI",
    version_scope="Not version-pinned; see source snapshot",
):
    """Record an explicit curator decision tied to exact bytes; excerpt presence is not entailment."""
    if support not in {"SUPPORTED", "PARTIAL", "UNSUPPORTED", "UNKNOWN"}:
        raise ValueError("Explicit source support decision required")
    if not all([reviewer_id.strip(), rationale.strip(), locator.strip()]):
        raise ValueError("Reviewer, rationale and exact locator required")
    if reviewer_kind not in {"AI", "HUMAN"}:
        raise ValueError("Reviewer kind must be explicit")
    claim = store.get(claim_id)
    if evidence_id not in claim["evidence_refs"]:
        raise ValueError("Review must use evidence attached to this claim")
    evidence = store.get(evidence_id)
    facets = inspect_evidence(store.root, evidence)
    path = store.root / evidence.get("local_snapshot_path", "")
    text = path.read_text(errors="replace") if facets["reference_availability"] == "AVAILABLE" else ""
    visible = usable_text(text)
    if support in {"SUPPORTED", "PARTIAL"}:
        if facets["source_integrity"] != "HASH_MATCH" or not visible:
            raise ValueError("Missing, altered or HTML shell source cannot support a claim")

        def normalized(x):
            return " ".join(x.split())

        if not excerpt or normalized(excerpt) not in normalized(visible):
            raise ValueError("Supporting excerpt not found in immutable snapshot")
    claim.update(
        facets,
        source_support_status=support,
        review_status="AI_REVIEWED" if reviewer_kind == "AI" else "HUMAN_APPROVED",
        reviewer_id=reviewer_id,
        reviewed_at=utcnow(),
        review_rationale=rationale,
        evidence_locator=locator,
        inference_type=inference,
        version_scope=version_scope,
    )
    # Deliberately do not modify the legacy verification/confidence fields.
    store.save(claim)
    return claim
