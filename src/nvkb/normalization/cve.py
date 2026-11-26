"""Transform vendor advisories and CVE 5.x records without erasing disagreements."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone

from bs4 import BeautifulSoup

from nvkb.collectors.sources import PRODUCTS, classify_product
from nvkb.evidence.graph import Graph
from nvkb.storage.canonical import Store, entity, stable_id
from nvkb.versioning.versions import parse_ranges

UNKNOWN = "Nguồn đã thu thập chưa cung cấp đủ thông tin; cần rà soát thủ công."


def normalize_date(value: str | None) -> str | None:
    if not value:
        return None
    date = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if date.tzinfo is None:
        date = date.replace(tzinfo=timezone.utc)
    return date.astimezone(timezone.utc).isoformat()


def seed_products(store: Store, evidence_ref: str):
    existing = {p["id"] for p in store.all("Product")}
    for key, (name, vendor, primary, url) in PRODUCTS.items():
        identifier = "PRODUCT:" + key
        if identifier in existing:
            continue
        store.save(
            entity(
                "Product",
                identifier,
                name,
                "Sản phẩm chính trong phạm vi."
                if primary
                else "Catalog phân tách sản phẩm; CVE không tự động nhập vào NGINX OSS.",
                [evidence_ref] if primary else [],
                "VERIFIED" if primary else "UNVERIFIED",
                vendor=vendor,
                in_primary_scope=primary,
                product_family=key,
            )
        )


def normalized_cve(
    store: Store,
    advisory: dict,
    vendor_snapshot: dict,
    cve_snapshot: dict | None,
    lookup_snapshot: dict | None = None,
    advisory_snapshot: dict | None = None,
    *,
    persist=True,
) -> dict:
    graph = Graph(store)
    cve_id = advisory["cve_id"]
    identifier = "CVE:" + cve_id
    vendor_ref = graph.evidence(
        vendor_snapshot,
        f"li containing {cve_id}",
        "NGINX / F5",
        "NGINX security advisories",
        f"{cve_id}: {advisory['title']}",
    )
    seed_products(store, vendor_ref)
    source_refs = [vendor_ref]
    claim_refs = []

    def claim(predicate, value, refs=None, authority="NGINX / F5", **kwargs):
        reference = graph.claim(identifier, predicate, value, refs or [vendor_ref], authority, **kwargs)
        claim_refs.append(reference)
        return reference

    claim("upstream_affected_expression", advisory["affected"])
    claim("upstream_unaffected_expression", advisory["fixed"])
    vendor_fixes = sorted(set(re.findall(r"(\d+\.\d+\.\d+)\+", advisory["fixed"])))
    fixed_claim = claim("upstream_fixed_releases", vendor_fixes)
    claim("title", advisory["title"])
    ranges, limitations = [], []
    try:
        for interval in parse_ranges(advisory["affected"]):
            rid = stable_id("RANGE", cve_id, interval)
            store.save(
                entity(
                    "VersionRange",
                    rid,
                    advisory["affected"],
                    "Khoảng phiên bản do upstream công bố.",
                    [vendor_ref],
                    product_id="PRODUCT:NGINX-OSS",
                    fixed_versions=vendor_fixes,
                    claim_refs=[claim_refs[0]],
                    **interval,
                )
            )
            ranges.append(rid)
    except ValueError as exc:
        limitations.append(str(exc))
    versions = []
    for version in vendor_fixes:
        vid = "VERSION:NGINX-" + version
        store.save(
            entity(
                "Version",
                vid,
                "NGINX " + version,
                "Upstream release được advisory xác định đã sửa lỗi.",
                [vendor_ref],
                product_id="PRODUCT:NGINX-OSS",
                version=version,
                branch="mainline" if int(version.split(".")[1]) % 2 else "stable",
                ecosystem="upstream",
            )
        )
        versions.append(vid)
        graph.relationship(identifier, "fixed_in", vid, [vendor_ref], [fixed_claim])
    patch_refs = []
    for url in advisory["patch_urls"]:
        pid = stable_id("PATCH", url)
        store.save(
            entity(
                "Patch",
                pid,
                url.rsplit("/", 1)[-1],
                "Bản vá được trang security advisories liên kết; chưa kiểm tra chữ ký PGP.",
                [vendor_ref],
                product_id="PRODUCT:NGINX-OSS",
                patch_url=url,
            )
        )
        claim("patch_url", url)
        patch_refs.append(pid)
    cve_data = json.loads(cve_snapshot["text"]) if cve_snapshot else {}
    lookup_data = json.loads(lookup_snapshot["text"]) if lookup_snapshot else {}
    metadata = cve_data.get("cveMetadata", {})
    if metadata and metadata.get("cveId") != cve_id:
        raise ValueError(f"CVE ID mismatch: {metadata.get('cveId')} != {cve_id}")
    cna = cve_data.get("containers", {}).get("cna", {})
    identity_verified = bool(metadata.get("datePublished") and metadata.get("state") == "PUBLISHED")
    publication = normalize_date(metadata.get("datePublished"))
    modified = normalize_date(metadata.get("dateUpdated"))
    description = (
        "\n\n".join(d["value"] for d in cna.get("descriptions", []) if d.get("lang", "").startswith("en"))
        or advisory["title"]
    )
    cve_ref = None
    if cve_snapshot:
        cve_ref = graph.evidence(
            cve_snapshot,
            "/cveMetadata",
            "CVE Program",
            cve_id,
            "Định danh, trạng thái và ngày công bố từ CVE Program.",
            "cve_record",
            published_at=publication,
            modified_at=modified,
        )
        source_refs.append(cve_ref)
        for field, value in [
            ("cve_id", cve_id),
            ("publication_date", publication),
            ("record_status", metadata.get("state")),
        ]:
            if value:
                claim(field, value, [cve_ref], "CVE Program")
        description_ref = graph.evidence(
            cve_snapshot,
            "/containers/cna/descriptions",
            "CVE Program / CNA",
            cve_id,
            "Mô tả và điều kiện do CNA công bố.",
            "cve_record",
        )
        source_refs.append(description_ref)
        claim("description", description, [description_ref], "CVE Program / CNA")
        claim("documented_configuration_context", description, [description_ref], "CVE Program / CNA")
    advisory_body = ""
    if advisory_snapshot:
        soup = BeautifulSoup(advisory_snapshot["text"], "html.parser")
        advisory_evidence = graph.evidence(
            advisory_snapshot,
            "advisory body",
            "NGINX / F5",
            soup.title.get_text(" ", strip=True) if soup.title else "NGINX security announcement",
            "Thông báo chi tiết liên kết từ danh sách advisory.",
        )
        source_refs.append(advisory_evidence)
        body = soup.find("pre") or soup.find("article") or soup
        advisory_body = body.get_text(" ", strip=True)
        claim("vendor_advisory_statement", advisory_body, [advisory_evidence])
    severities, weaknesses, conflicts, excluded = [], [], [], []
    metric_ref = None
    for source_name, data, snapshot in [
        ("CVE Program", cve_data, cve_snapshot),
        ("CIRCL mirror", lookup_data, lookup_snapshot),
    ]:
        if not snapshot:
            continue
        containers = [data.get("containers", {}).get("cna", {})] + data.get("containers", {}).get("adp", [])
        for index, container in enumerate(containers):
            authority = container.get("providerMetadata", {}).get("shortName", source_name)
            locator = "/containers/cna" if index == 0 else f"/containers/adp/{index - 1}"
            for metric in container.get("metrics", []):
                for key, value in metric.items():
                    if not key.startswith("cvss") or not isinstance(value, dict):
                        continue
                    metric_ref = graph.evidence(
                        snapshot,
                        locator + "/metrics",
                        source_name,
                        cve_id,
                        "Điểm CVSS giữ riêng theo scoring authority và phiên bản.",
                        "cve_record",
                    )
                    source_refs.append(metric_ref)
                    sid = stable_id("SEVERITY", cve_id, source_name, authority, value)
                    cid = claim(
                        "severity:" + source_name + ":" + authority + ":" + str(value.get("version")),
                        value,
                        [metric_ref],
                        authority,
                    )
                    store.save(
                        entity(
                            "Severity",
                            sid,
                            f"{cve_id} CVSS {value.get('version', '')} {authority}",
                            "Đánh giá của nguồn; không thay thế đánh giá từ authority khác.",
                            [metric_ref],
                            subject_entity_id=identifier,
                            scoring_authority=authority + " via " + source_name,
                            cvss_version=str(value.get("version", "unknown")),
                            cvss_vector=value.get("vectorString", ""),
                            **(
                                {"cvss_score": value["baseScore"]}
                                if value.get("baseScore") is not None
                                else {}
                            ),
                            severity_label=value.get("baseSeverity", "UNKNOWN"),
                            metric_json=json.dumps(value, sort_keys=True),
                            claim_refs=[cid],
                        )
                    )
                    severities.append(sid)
        affected_ref = graph.evidence(
            snapshot,
            "/containers/cna/affected",
            source_name,
            cve_id,
            "Sản phẩm và phiên bản được CNA liệt kê.",
            "cve_record",
        )
        source_refs.append(affected_ref)
        for product in data.get("containers", {}).get("cna", {}).get("affected", []):
            pid = classify_product(product.get("product", ""))
            if pid != "PRODUCT:NGINX-OSS":
                excluded.append(dict(name=product.get("product"), product_id=pid, source=source_name))
                continue
            claim("affected_products", [pid], [affected_ref], source_name)
            claim("cna_version_data:" + source_name, product.get("versions", []), [affected_ref], source_name)
            # Only reconcile an explicit fixed boundary, not an arbitrary unaffected release.
            changes = sorted(
                {
                    change["at"]
                    for version in product.get("versions", [])
                    for change in version.get("changes", [])
                    if change.get("status") == "unaffected"
                    and re.fullmatch(r"\d+\.\d+\.\d+", change.get("at", ""))
                }
            )
            if changes:
                other = claim("upstream_fixed_releases", changes, [affected_ref], source_name)
                conflict = graph.reconcile(
                    identifier, "upstream_fixed_releases", [store.get(fixed_claim), store.get(other)]
                )
                if conflict:
                    conflicts.append(conflict)
    if cve_snapshot:
        for problem in cna.get("problemTypes", []):
            for desc in problem.get("descriptions", []):
                cwe = desc.get("cweId")
                if not cwe or not re.fullmatch(r"CWE-\d+", cwe):
                    continue
                ref = graph.evidence(
                    cve_snapshot,
                    "/containers/cna/problemTypes",
                    "CVE Program / CNA",
                    cve_id,
                    "Phân loại CWE được CNA gán.",
                    "cve_record",
                )
                source_refs.append(ref)
                wid = "WEAKNESS:" + cwe
                try:
                    existing = store.get(wid)
                except KeyError:
                    existing = entity("Weakness", wid, cwe, desc.get("description", cwe), [ref], cwe_id=cwe)
                existing["source_refs"] = sorted(set(existing["source_refs"] + [ref]))
                store.save(existing)
                weaknesses.append(wid)
                cid = claim("related_weaknesses", wid, [ref], "CVE Program / CNA")
                graph.relationship(identifier, "classified_as", wid, [ref], [cid])
    references = []
    for url in sorted(
        set(advisory["advisory_urls"] + [r["url"] for r in cna.get("references", []) if "url" in r])
    ):
        rid = stable_id("REFERENCE", url)
        store.save(
            entity(
                "Reference",
                rid,
                url.rsplit("/", 1)[-1],
                "Tài liệu được nguồn chính thức dẫn chiếu; nội dung không mặc nhiên đã xác minh.",
                [cve_ref or vendor_ref],
                source_url=url,
                document_title=url.rsplit("/", 1)[-1],
            )
        )
        references.append(rid)
    conditions = []
    if cve_snapshot and description:
        cid = stable_id("CONDITION", cve_id)
        condition_claim = claim(
            "vendor_documented_conditions", description, [description_ref], "CVE Program / CNA"
        )
        store.save(
            entity(
                "AffectedCondition",
                cid,
                f"Điều kiện được công bố — {cve_id}",
                description,
                [description_ref],
                claim_refs=[condition_claim],
            )
        )
        conditions.append(cid)
    severity_vendor_id = stable_id("SEVERITY", cve_id, "nginx_label")
    vendor_severity_claim = claim("vendor_severity_label", advisory["severity"])
    store.save(
        entity(
            "Severity",
            severity_vendor_id,
            "NGINX severity: " + advisory["severity"],
            "Nhãn severity từ upstream; không tự ánh xạ thành CVSS.",
            [vendor_ref],
            subject_entity_id=identifier,
            severity_label=advisory["severity"],
            scoring_authority="NGINX / F5",
            claim_refs=[vendor_severity_claim],
        )
    )
    severities.append(severity_vendor_id)
    status = (
        "CONFLICTED"
        if conflicts
        else ("VERIFIED" if identity_verified and ranges and versions else "UNVERIFIED")
    )
    summary = f"Advisory {cve_id} ghi nhận: {advisory['title']}. Phạm vi upstream: {advisory['affected']}. Bản sửa được công bố: {advisory['fixed']}."
    root_cause = "Nguồn phân loại lỗi: " + advisory["title"] + ". "
    root_cause += "Chưa có phân tích root cause ở mức mã nguồn đã được duyệt; không suy diễn chi tiết vượt quá advisory."
    item = entity(
        "Vulnerability",
        identifier,
        cve_id,
        description,
        source_refs,
        status,
        cve_id=cve_id,
        title=advisory["title"],
        cve_year=int(cve_id.split("-")[1]),
        record_status=metadata.get("state", "MISSING_METADATA"),
        affected_products=["PRODUCT:NGINX-OSS"],
        affected_version_ranges=ranges,
        fixed_versions=versions,
        unaffected_versions=[],
        distribution_status=[],
        related_components=[],
        related_modules=[],
        related_protocols=[],
        related_weaknesses=sorted(set(weaknesses)),
        normal_component_behavior=UNKNOWN,
        root_cause_summary=root_cause,
        security_assumption_violated=UNKNOWN,
        security_boundary=UNKNOWN,
        vendor_documented_conditions=[description] if cve_snapshot else [],
        affected_feature_description=advisory["title"],
        documented_configuration_context=description if cve_snapshot else UNKNOWN,
        documented_exclusions=[],
        unknown_conditions=[UNKNOWN],
        applicability_limitations="Inventory phiên bản không xác định cấu hình đang hoạt động. "
        + " ".join(limitations),
        direct_impact=description if cve_snapshot else advisory["title"],
        confidentiality_impact="Xem từng CVSS metric có authority; không hợp nhất điểm số.",
        integrity_impact="Xem từng CVSS metric có authority; không hợp nhất điểm số.",
        availability_impact="Xem từng CVSS metric có authority; không hợp nhất điểm số.",
        affected_process=UNKNOWN,
        documented_privilege_context=UNKNOWN,
        confirmed_impact="Tác động được nhà cung cấp công bố trong mô tả; chưa kiểm thử độc lập.",
        potential_impact=UNKNOWN,
        impact_limitations="Không suy diễn tác động cao hơn nguồn công bố.",
        severity_refs=sorted(set(severities)),
        fixed_release_refs=versions,
        patch_refs=patch_refs,
        official_mitigation_refs=[],
        distribution_backports=[],
        defensive_recommendations=[
            "Lập inventory nội bộ, chọn bản sửa đúng nhánh và xác minh package/backport của distribution."
        ],
        remediation_limitations="Fixed release chỉ nói về CVE này, không bảo đảm release còn được hỗ trợ hoặc đã sửa mọi CVE.",
        claim_refs=sorted(set(claim_refs)),
        unresolved_conflicts=sorted(set(conflicts)),
        condition_refs=conditions,
        impact_refs=[],
        reference_refs=references,
        last_verified_at=vendor_snapshot["retrieved_at"],
        upstream_affected_expression=advisory["affected"],
        upstream_unaffected_expression=advisory["fixed"],
        educational_summary=summary,
        learning_objectives=[
            "Truy vết phiên bản ảnh hưởng và bản vá đến nguồn gốc.",
            "Phân biệt điều kiện công bố với giả định chưa xác minh.",
        ],
        unsupported_fields=sorted(
            set(cna)
            - {
                "providerMetadata",
                "title",
                "datePublic",
                "problemTypes",
                "affected",
                "descriptions",
                "references",
                "metrics",
            }
        ),
    )
    if publication:
        item.update(publication_date=publication, publication_year=int(publication[:4]))
    if advisory_body:
        item["vendor_documented_conditions"].append(advisory_body)
        item["documented_configuration_context"] += "\n\nThông báo upstream bổ sung:\n" + advisory_body
    if modified:
        item["last_modified_date"] = modified
    if persist:
        store.save(item)
    graph.relationship(identifier, "affects", "PRODUCT:NGINX-OSS", [vendor_ref], [claim_refs[0]])
    return {"record": item, "excluded_products": excluded}
