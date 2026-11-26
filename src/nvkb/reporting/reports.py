"""Derived exports and honest coverage/quality accounting."""

from __future__ import annotations

import csv
import io
import json
from collections import Counter
from pathlib import Path

from nvkb.config import utcnow
from nvkb.rendering.vault import check_vault
from nvkb.storage.canonical import Store, atomic_write, json_text
from nvkb.validation.checks import validate


def stats(root: Path) -> dict:
    items = Store(root).all()
    counts = Counter(i["entity_type"] for i in items)
    cves = [i for i in items if i["entity_type"] == "Vulnerability"]
    pipeline = root / "data/pipeline-last.json"
    run = json.loads(pipeline.read_text()) if pipeline.exists() else {}
    return dict(
        discovered=len(run.get("discovered", [])),
        in_scope=len(run.get("in_scope", [])),
        collected=len(cves),
        verified=sum(i["verification_status"] in {"VERIFIED", "CORROBORATED"} for i in cves),
        verified_meaning="Legacy ingestion label; not measured factual accuracy or semantic approval",
        claim_lifecycle=dict(
            Counter(i.get("lifecycle_status", "PENDING_REVIEW") for i in items if i["entity_type"] == "Claim")
        ),
        claim_source_support=dict(
            Counter(
                i.get("source_support_status", "NOT_REVIEWED") for i in items if i["entity_type"] == "Claim"
            )
        ),
        claim_review=dict(
            Counter(i.get("review_status", "NOT_REVIEWED") for i in items if i["entity_type"] == "Claim")
        ),
        awaiting_review=sum(i["verification_status"] not in {"VERIFIED", "CORROBORATED"} for i in cves),
        entities=len(items),
        relationships=counts["Relationship"],
        evidence_records=counts["Evidence"],
        claims=counts["Claim"],
        notes=len(list((root / "vault").rglob("*.md"))),
        unresolved_conflicts=sum(
            json.loads(p.read_text()).get("status") == "CONFLICTED"
            for p in (root / "data/conflicts").glob("*.json")
        ),
        failed_source_requests=sum("url" in failure for failure in run.get("failures", [])),
        normalization_failures=sum(
            failure.get("stage") == "normalization" for failure in run.get("failures", [])
        ),
        publication_years=dict(
            sorted(Counter(str(v.get("publication_year", "UNKNOWN")) for v in cves).items())
        ),
        cve_id_years=dict(sorted(Counter(str(v["cve_year"]) for v in cves).items())),
        entity_types=dict(sorted(counts.items())),
        database_bytes=(root / "database/nvkb.sqlite").stat().st_size
        if (root / "database/nvkb.sqlite").exists()
        else 0,
    )


def export(root: Path, format="jsonl", destination: Path | None = None) -> Path:
    records = Store(root).all("Vulnerability")
    destination = destination or root / f"data/exports/CVE_MASTER_INDEX.{format}"
    if format == "jsonl":
        content = "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in records)
    elif format == "csv":
        fields = [
            "cve_id",
            "title",
            "publication_date",
            "publication_year",
            "cve_year",
            "verification_status",
            "affected_products",
            "upstream_affected_expression",
            "upstream_unaffected_expression",
            "fixed_versions",
            "related_modules",
            "related_protocols",
            "related_weaknesses",
            "source_refs",
            "last_verified_at",
        ]
        stream = io.StringIO()
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    f: ";".join(record[f]) if isinstance(record.get(f), list) else record.get(f, "")
                    for f in fields
                }
            )
        content = stream.getvalue()
    else:
        raise ValueError("Export format must be csv or jsonl")
    atomic_write(destination, content)
    # Graph is also independently consumable by local research tools.
    if format == "jsonl":
        for kind, name in [("Relationship", "relationships"), ("Evidence", "evidence"), ("Claim", "claims")]:
            atomic_write(
                root / f"data/exports/{name}.jsonl",
                "".join(
                    json.dumps(i, ensure_ascii=False, sort_keys=True) + "\n" for i in Store(root).all(kind)
                ),
            )
    return destination


def report(root: Path) -> dict:
    snapshot = stats(root)
    quality = validate(root)
    vault = check_vault(root)
    items = Store(root).all()
    cves = [i for i in items if i["entity_type"] == "Vulnerability"]
    claims = [i for i in items if i["entity_type"] == "Claim"]
    run_path = root / "data/pipeline-last.json"
    run = json.loads(run_path.read_text()) if run_path.exists() else {}
    reports = root / "reports"
    reports.mkdir(exist_ok=True)
    stamp = f"Ngày tạo báo cáo (UTC): {utcnow()}. Số liệu tính từ canonical JSON và manifest pipeline.\n\n"

    def write(name, title, body):
        atomic_write(reports / name, f"# {title}\n\n{stamp}{body}\n")

    coverage = ["| Chỉ tiêu | Kết quả |", "| --- | ---: |"]
    for key in [
        "discovered",
        "in_scope",
        "collected",
        "verified",
        "awaiting_review",
        "failed_source_requests",
    ]:
        coverage.append(f"| {key} | {snapshot[key]} |")
    coverage += [
        f"| schema_valid_entities | {quality['schema_valid']} |",
        f"| excluded_by_publication_date | {len(run.get('excluded_by_date', []))} |",
        f"| publication_date_unknown | {len(run.get('awaiting_metadata', []))} |",
    ]
    coverage += [
        "",
        "Discovery là toàn bộ CVE trong trang advisory NGINX ở thời điểm snapshot; in_scope được lọc bằng ngày công bố từ CVE Program.",
        "Không khẳng định đã kiểm kê mọi CVE trong hệ sinh thái NGINX; các sản phẩm khác và các advisory không có trên trang upstream nằm ngoài inventory ban đầu.",
        "",
        "## Theo năm công bố",
        json_text(snapshot["publication_years"]),
        "## Theo năm CVE ID",
        json_text(snapshot["cve_id_years"]),
        "## Sản phẩm loại khỏi phạm vi OSS",
    ]
    excluded = sorted({str(p.get("name")) for p in run.get("excluded_products", [])})
    coverage += [f"- {name}" for name in excluded] or [
        "- Không có sản phẩm ngoài phạm vi trong metadata đã xử lý."
    ]
    coverage += ["", "## Lỗi nguồn", "```json", json_text(run.get("failures", [])), "```"]
    write("COVERAGE_REPORT.md", "Báo cáo coverage", "\n".join(coverage))
    missing_versions = [v["cve_id"] for v in cves if not v["affected_version_ranges"]]
    missing_fixes = [v["cve_id"] for v in cves if not v["fixed_versions"]]
    q = {k: v for k, v in quality.items() if k != "errors"}
    q.update(
        broken_link_count=len(vault["broken_links"]),
        invalid_frontmatter=len(vault["invalid_frontmatter"]),
        source_conflict_count=snapshot["unresolved_conflicts"],
        missing_version_information=len(missing_versions),
        missing_remediation_information=len(missing_fixes),
    )
    write(
        "DATA_QUALITY_REPORT.md",
        "Chất lượng dữ liệu",
        "```json\n"
        + json_text(q)
        + "```\n\n"
        + "Schema-valid không đồng nghĩa factual verification. VERIFIED là nhãn ingestion legacy; semantic source support, extraction, lifecycle và reviewer approval là các chiều riêng. Không có tỷ lệ factual accuracy toàn corpus đã đo.\n\n"
        + "## Lỗi chi tiết\n\n```json\n"
        + json_text(quality["errors"] + vault["broken_links"] + vault["invalid_frontmatter"])
        + "```\n",
    )
    conflicts = [json.loads(p.read_text()) for p in sorted((root / "data/conflicts").glob("*.json"))]
    write(
        "SOURCE_CONFLICTS.md",
        "Mâu thuẫn nguồn",
        f"Unresolved: {snapshot['unresolved_conflicts']}.\n\n"
        + "\n\n".join("```json\n" + json_text(c) + "```" for c in conflicts),
    )
    unverified = [c for c in claims if c.get("review_status") != "HUMAN_APPROVED"]
    write(
        "UNVERIFIED_CLAIMS.md",
        "Claims cần rà soát",
        f"Số claim chưa có human approval: {len(unverified)}. AI_REVIEWED không phải human approval.\n\n"
        + "\n".join(
            f"- `{c['id']}` — {c['subject_entity_id']} / {c['predicate']} / {c['verification_status']}: {c['reviewer_notes']}"
            for c in unverified
        ),
    )
    missing = []
    for v in cves:
        missing.append(
            f"- **{v['cve_id']}**: "
            + "; ".join(v["unknown_conditions"])
            + (" Thiếu distribution backport evidence." if not v["distribution_status"] else "")
        )
    write(
        "MISSING_INFORMATION.md",
        "Thông tin còn thiếu",
        "\n".join(missing)
        + "\n\nV1.2 có pilot, snapshot Ubuntu hẹp và provenance KEV; xem PATCH_INTELLIGENCE_REPORT.md để biết refresh failures và scope. RPM, lifecycle từng nhánh NGINX và source-code root cause review vẫn chưa hoàn tất. UNKNOWN không phải NOT_APPLICABLE.\n",
    )
    history = [json.loads(p.read_text()) for p in sorted((root / "data/history").glob("*.json"))]
    write(
        "UPDATE_HISTORY.md",
        "Lịch sử thay đổi",
        f"{len(history)} sự kiện; snapshot trước/sau trong `data/history/`.\n\n"
        + "\n".join(
            f"- {e['changed_at']} — {e['entity_id']}: {e['action']}"
            for e in sorted(history, key=lambda e: e["changed_at"])
        ),
    )
    write(
        "BUILD_REPORT.md",
        "Báo cáo build",
        "```json\n"
        + json_text(snapshot)
        + "```\n\n"
        + f"Validation: {quality['ok']}. Vault structural check: {vault['ok']}. GUI Obsidian chưa kiểm tra trực tiếp.\n",
    )
    atomic_write(reports / "metrics.json", json_text(dict(stats=snapshot, quality=q, vault=vault)))
    export(root, "csv")
    export(root, "jsonl")
    return dict(stats=snapshot, quality=q, vault=vault)
