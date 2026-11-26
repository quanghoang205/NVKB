"""Deterministic Obsidian notes; human content and edited generated notes are protected."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

from nvkb.storage.canonical import Store, atomic_write, json_text, slug

FOLDERS = {
    "Claim": "16-Claims",
    "Advisory": "01-Advisories",
    "Vulnerability": "01-CVE",
    "Product": "02-Products",
    "Version": "03-Versions",
    "VersionRange": "03-Versions",
    "Component": "04-Architecture",
    "DeploymentArchitecture": "04-Architecture",
    "Module": "05-Modules",
    "ConfigurationDirective": "05-Modules",
    "Protocol": "06-Protocols",
    "Weakness": "07-Weaknesses",
    "AffectedCondition": "08-Conditions",
    "Impact": "09-Impacts",
    "Severity": "09-Impacts",
    "Patch": "10-Patches",
    "DistributionPackage": "10-Patches",
    "Mitigation": "11-Mitigations",
    "SecurityControl": "11-Mitigations",
    "Reference": "12-References",
    "Evidence": "12-References",
    "LearningObjective": "14-Learning-Paths",
}
SECTIONS = [
    ("definition", "Định nghĩa"),
    ("normal_behavior", "Cơ chế hoạt động bình thường"),
    ("architecture_position", "Vị trí trong kiến trúc"),
    ("security_boundary", "Security boundary"),
    ("safety_assumptions", "Giả định an toàn"),
    ("related_failure_classes", "Nhóm lỗi liên quan"),
    ("failure_impact", "Tác động khi giả định bị vi phạm"),
    ("defensive_principles", "Nguyên tắc phòng vệ"),
]


def filename(item):
    if item["entity_type"] == "Vulnerability":
        return item["cve_id"]
    if item["id"] == "PRODUCT:NGINX-OSS":
        return "NGINX-Open-Source"
    return slug(item["id"])


def severity_groups(item, entities):
    groups = {}
    for identifier in item.get("severity_refs", []):
        row = entities[identifier]
        key = row.get("assessment_key", identifier)
        group = groups.setdefault(
            key,
            dict(
                authority=row.get("original_authority", row["scoring_authority"]),
                score=row.get("cvss_score", row.get("severity_label", "UNKNOWN")),
                vector=row.get("cvss_vector", "Not a CVSS vector"),
                ids=[],
            ),
        )
        group["ids"].append(identifier)
    return list(groups.values())


def frontmatter(item):
    data = dict(
        entity_type=item["entity_type"].lower(),
        id=item["id"],
        title=item["name"],
        verification_status=item["verification_status"],
        generated=True,
        schema_version=item.get("schema_version", "1.2.0"),
        aliases=[item["name"]],
        tags=[
            "nginx",
            item["entity_type"].lower(),
            "provenance" if item["entity_type"] in {"Evidence", "Claim", "Reference"} else "knowledge",
        ],
    )
    if item.get("editorial_maturity"):
        data["editorial_maturity"] = item["editorial_maturity"]
    if item["entity_type"] == "Vulnerability":
        data.update(
            cve_id=item["cve_id"],
            title=item["title"],
            publication_year=item.get("publication_year"),
            cve_year=item["cve_year"],
            products=item["affected_products"],
            modules=item["related_modules"],
            protocols=item["related_protocols"],
            weaknesses=item["related_weaknesses"],
            fixed_versions=item["fixed_versions"],
            last_verified_at=item["last_verified_at"],
        )
        for key in ["products", "modules", "protocols", "weaknesses", "fixed_versions", "last_verified_at"]:
            data.pop(key, None)
    return "---\n" + yaml.safe_dump(data, allow_unicode=True, sort_keys=False).strip() + "\n---\n"


def check_vault(root: Path) -> dict:
    vault = root / "vault"
    paths = sorted(vault.rglob("*.md"))
    resolved_paths = {p.resolve() for p in paths}
    stems = Counter(p.stem for p in paths)
    broken, invalid, ambiguous = [], [], []
    for path in paths:
        text = path.read_text()
        if text.startswith("---\n"):
            try:
                metadata = yaml.safe_load(text.split("---", 2)[1])
                if not isinstance(metadata, dict):
                    raise ValueError("Frontmatter must be a mapping")
            except (ValueError, yaml.YAMLError) as exc:
                invalid.append(f"{path.name}: {exc}")
        else:
            invalid.append(f"{path.name}: missing frontmatter")
        for target in re.findall(r"\[\[([^\]]+)\]\]", text):
            target = target.split("|", 1)[0].rstrip("\\").split("#", 1)[0]
            if not target:
                continue
            stem = Path(target).name.removesuffix(".md")
            if "/" in target:
                relative = target.removesuffix(".md") + ".md"
                candidates = [(vault / relative).resolve(), (path.parent / relative).resolve()]
                if not any(p.is_relative_to(vault.resolve()) and p in resolved_paths for p in candidates):
                    broken.append(f"{path.name} -> {target}")
            elif stem not in stems:
                broken.append(f"{path.name} -> {target}")
            elif stems[stem] > 1 and "/" not in target:
                ambiguous.append(f"{path.name} -> {target}")
    return dict(
        notes=len(paths),
        broken_links=broken,
        invalid_frontmatter=invalid,
        ambiguous_links=ambiguous,
        ok=not (broken or invalid or ambiguous),
    )


def build_vault(root: Path, *, dry_run=False) -> dict:
    items = Store(root).all()
    entities = {x["id"]: x for x in items}
    by_subject, by_assessment = defaultdict(list), defaultdict(list)
    for row in items:
        if row["entity_type"] == "Relationship":
            if row.get("relationship_disposition") != "WITHDRAWN_UNSUPPORTED":
                by_subject[row["subject_entity_id"]].append(row)
        elif row["entity_type"] == "Severity" and row.get("assessment_key"):
            by_assessment[row["assessment_key"]].append(row["id"])
    env = Environment(
        loader=FileSystemLoader(root / "templates"),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
    )
    env.filters["table_text"] = lambda value: str(value).replace("|", "&#124;").replace("\n", "<br>")
    env.filters["table_link"] = lambda value: value.replace("|", "\\|")
    env.filters["claim_preview"] = lambda value: (
        (str(value)[:180] + ("… (mở Claim để đọc đủ)" if len(str(value)) > 180 else ""))
        .replace("[[", "⟦")
        .replace("]]", "⟧")
        .replace("|", "&#124;")
        .replace("\n", " ")
    )

    def links(ids):
        return ", ".join(
            "[["
            + filename(entities[i])
            + "|"
            + " ".join(entities[i]["name"].split()).replace("|", "/").replace("[[", "⟦").replace("]]", "⟧")
            + "]]"
            for i in ids
            if i in entities and entities[i]["entity_type"] in FOLDERS
        )

    output = {}
    for item in items:
        kind = item["entity_type"]
        if kind not in FOLDERS:
            continue
        template = {
            "Vulnerability": "cve",
            "Evidence": "evidence",
            "Claim": "claim",
            "Component": "architecture",
            "DeploymentArchitecture": "architecture",
            "Module": "module",
            "Protocol": "protocol",
            "Weakness": "weakness",
            "LearningObjective": "learning_path",
            "Severity": "severity",
            "Version": "version",
            "VersionRange": "version",
            "DistributionPackage": "distribution_package",
            "Impact": "impact",
            "Mitigation": "mitigation",
        }.get(kind, "knowledge" if item.get("definition") else "data") + ".md.j2"
        detail = {
            k: v
            for k, v in item.items()
            if k
            not in {
                "id",
                "name",
                "description",
                "entity_type",
                "created_at",
                "updated_at",
                "source_refs",
                "schema_version",
                "verification_status",
            }
        }
        text = env.get_template(template).render(
            item=item,
            frontmatter=frontmatter(item),
            links=links,
            claims=[entities[c] for c in item.get("claim_refs", []) if c in entities],
            sections=SECTIONS,
            details=json_text(detail) if not item.get("definition") else "",
            data_fields={k: v for k, v in detail.items() if k not in {"claim_refs", "article_body"}},
            relationships=by_subject[item["id"]],
            equivalents=[i for i in by_assessment.get(item.get("assessment_key"), []) if i != item["id"]],
            severity_groups=severity_groups(item, entities),
        )
        output[f"{FOLDERS[kind]}/{filename(item)}.md"] = text

    def note(path, title, content):
        output[path] = (
            "---\ngenerated: true\nentity_type: navigation\n---\n# " + title + "\n\n" + content + "\n"
        )

    cves = [i for i in items if i["entity_type"] == "Vulnerability"]
    years = Counter(v.get("publication_year", "UNKNOWN") for v in cves)
    verified = sum(v["verification_status"] in {"VERIFIED", "CORROBORATED"} for v in cves)
    status = Counter(v["verification_status"] for v in cves)
    latest = max((v.get("last_verified_at", "") for v in cves), default="Chưa đồng bộ")
    year_links = []
    configured_years = yaml.safe_load((root / "config/scope.yaml").read_text())["publication_years"]
    for year in sorted(set(configured_years) | {y for y in years if isinstance(y, int)}):
        name = f"MOC-CVE-{year}"
        year_links.append(f"[[{name}]]: {years[year]}")
        note(
            f"00-Home/{name}.md",
            f"CVE công bố năm {year}",
            links([v["id"] for v in cves if v.get("publication_year") == year]) or "Chưa có record.",
        )
    for name, kinds in {
        "NGINX-Architecture": ["Component", "DeploymentArchitecture"],
        "HTTP": ["Protocol"],
        "TLS": ["Protocol"],
        "Memory-Safety": ["Weakness"],
        "Modules": ["Module"],
        "Patch-Management": ["Patch", "Version", "DistributionPackage"],
        "Learning-Paths": ["LearningObjective"],
    }.items():
        chosen = [x for x in items if x["entity_type"] in kinds]
        if name == "HTTP":
            chosen = [x for x in chosen if "HTTP" in x["id"] or "QUIC" in x["id"]]
        if name == "TLS":
            chosen = [x for x in chosen if "TLS" in x["id"]]
        if name == "Memory-Safety":
            chosen = [
                x
                for x in chosen
                if x.get("cwe_id")
                in {"CWE-119", "CWE-125", "CWE-787", "CWE-416", "CWE-415", "CWE-476", "CWE-190", "CWE-191"}
            ]
        if name == "NGINX-Architecture":
            chosen = [x for x in chosen if not x["id"].startswith("CONCEPT:")]
        note(f"00-Home/MOC-{name}.md", name, links([x["id"] for x in chosen]) or "Đang bổ sung.")
    for report, name in [
        ("DATA_QUALITY_REPORT.md", "Data-Quality"),
        ("SOURCE_CONFLICTS.md", "Source-Conflicts"),
        ("COVERAGE_REPORT.md", "Coverage"),
        ("MISSING_INFORMATION.md", "Missing-Information"),
    ]:
        path = root / "reports" / report
        note(
            f"00-Home/{name}.md",
            name,
            path.read_text() if path.exists() else "Chạy nvkb report để cập nhật báo cáo.",
        )
    note(
        "00-Home/Research-Guide.md",
        "Ghi chép nghiên cứu",
        "Đặt ghi chép riêng trong `13-Research/` và bài giảng trong `15-Lectures/`. Builder bảo vệ hai thư mục này và từ chối ghi đè note generated đã bị sửa.\n\nMẫu bài giảng trong `99-Templates/`. [[Missing-Information]] liệt kê câu hỏi còn mở.",
    )
    modules = Counter(m for v in cves for m in v["related_modules"])
    module_text = "\n".join(f"- {links([m])}: {n} CVE" for m, n in sorted(modules.items()))
    note(
        "00-Home/Knowledge-Taxonomy.md",
        "Knowledge taxonomy",
        "\n".join(
            f"- {kind}: {sum(i['entity_type'] == kind for i in items)}"
            for kind in sorted({i["entity_type"] for i in items})
        )
        + "\n\n```mermaid\ngraph LR\nV[Vulnerability] --> C[Claim]\nC --> E[Evidence]\nE --> S[Snapshot SHA256]\nV --> M[Module / Protocol / Weakness]\nV --> P[Fixed release / Distribution backport]\n```\n",
    )
    note(
        "00-Home/NVKB-Home.md",
        "NVKB — thư viện tri thức NGINX",
        "[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]] · [[Patch-Management-Library|Patch Management Library]]\n\n"
        f"Kho tri thức cục bộ có provenance. Canonical JSON là nguồn chuẩn; SQLite và vault có thể tái tạo.\n\n"
        f"**{len(cves)} CVE đã thu thập; {verified} record có nhãn ingestion VERIFIED/CORROBORATED legacy.** Nhãn này không phải semantic approval.\n\n"
        + " · ".join(year_links)
        + "\n\n"
        + module_text
        + "\n\n"
        + "[[MOC-NGINX-Architecture]] · [[MOC-HTTP]] · [[MOC-TLS]] · [[MOC-Memory-Safety]] · [[MOC-Modules]]\n\n"
        + "[[Knowledge-Taxonomy]] · [[MOC-Patch-Management]] · [[MOC-Learning-Paths]] · [[Research-Guide]]\n\n"
        + "[[Data-Quality]] · [[Coverage]] · [[Source-Conflicts]] · [[Missing-Information]]\n\n"
        + f"Trạng thái: `{dict(status)}`. Lần đối chiếu nguồn gần nhất: {latest}.",
    )
    note(
        "00-Home/Research-Library.md",
        "Research Library",
        "Tra cứu sự kiện nguồn và lịch sử: "
        + " · ".join(year_links)
        + "\n\n[[Provenance-Graph]] · [[Data-Quality]] · [[Source-Conflicts]]\n\nMở CVE → bảng Claim → Evidence. Claim có giá trị, hiệu lực và review riêng. PENDING_REVIEW không được coi là dữ kiện hiện hành đã duyệt.",
    )
    note(
        "00-Home/Learning-Library.md",
        "Learning Library",
        links(["LEARNING:PATH-01"])
        + "\n\n[[MOC-NGINX-Architecture]] · [[MOC-TLS]] · [[MOC-Learning-Paths]] · [[Learning-Graph]] · [[Technical-Knowledge-Graph]]\n\nPilot là bản biên soạn với AI self-review; human expert review và learner evaluation còn PENDING.",
    )
    note(
        "00-Home/Patch-Management-Library.md",
        "Patch Management Library",
        links(["CONTROL:PATCH-VERIFICATION", "CONCEPT:BACKPORT", "CVE:CVE-2025-23419"])
        + "\n\n[[Version-Management|Bảng quản lý phiên bản]] · [[MOC-Patch-Management]]\n\nPhân biệt advisory fix, package status, lifecycle/EOL, KEV và runtime. Chỉ đối chiếu inventory quản trị viên cung cấp; không suy ra binary đã vá từ banner.",
    )
    version_rows = ["| Upstream release | Branch | Nguồn |", "| --- | --- | --- |"]
    for row in items:
        if row["entity_type"] == "Version":
            version_rows.append(
                "| "
                + links([row["id"]]).replace("|", "\\|")
                + " | "
                + row.get("branch", "UNKNOWN")
                + " | "
                + links(row["source_refs"]).replace("|", "\\|")
                + " |"
            )
    package_rows = ["| Distribution / release | Fixed package | Source status |", "| --- | --- | --- |"]
    for row in items:
        if row["entity_type"] == "DistributionPackage" and row.get("cve_ref") == "CVE:CVE-2025-23419":
            package_rows.append(
                "| "
                + links([row["id"]]).replace("|", "\\|")
                + " | "
                + row.get("fixed_version", "UNKNOWN")
                + " | "
                + row.get("patch_status", "unknown")
                + " |"
            )
    note(
        "00-Home/Version-Management.md",
        "Bảng quản lý phiên bản",
        "Catalogue release quan sát được, không phải mọi release đã phát hành. Nhãn nguồn không attest binary.\n\n"
        + "\n".join(version_rows)
        + "\n\n## Package provenance — CVE-2025-23419\n\n"
        + "\n".join(package_rows)
        + "\n\nKEV/lifecycle/runtime là chiều riêng; [[Patch-Management-Library]].",
    )
    for label, layer, description in [
        (
            "Provenance-Graph",
            "PROVENANCE",
            "Claim → Evidence → Source; metadata không chứng minh entailment.",
        ),
        (
            "Technical-Knowledge-Graph",
            "TECHNICAL",
            "Quan hệ cơ chế có phạm vi; KEYWORD_ASSOCIATION không chứng minh vị trí lỗi.",
        ),
        ("Learning-Graph", "LEARNING", "Prerequisite, thứ tự và đánh giá là quyết định sư phạm."),
    ]:
        rows = [
            r
            for r in items
            if r["entity_type"] == "Relationship"
            and r.get("graph_layer") == layer
            and r.get("relationship_disposition") != "WITHDRAWN_UNSUPPORTED"
        ]
        body = (
            description
            + "\n\nBộ lọc graph gợi ý: `tag:provenance` cho provenance; `-tag:provenance` cho bài học. Settings cá nhân giữ nguyên.\n\n"
        )
        body += "\n".join(
            "- "
            + links([r["subject_entity_id"]])
            + " → `"
            + r["predicate"]
            + "` → "
            + links([r["object_entity_id"]])
            + " ("
            + r.get("review_status", "NOT_REVIEWED")
            + ")"
            for r in rows
        )
        note("00-Home/" + label + ".md", label, body)
    note(
        "99-Templates/Research-Template.md",
        "Mẫu ghi chú nghiên cứu",
        "Sao chép vào `13-Research/`, đổi generated thành false.\n\n## Câu hỏi\n\n## Nhận định\n\n## Bằng chứng và locator\n\n## Giới hạn\n",
    )
    output["99-Templates/Lecture-Template.md"] = env.get_template("lecture.md.j2").render(
        title="Mẫu bài giảng"
    )
    from nvkb.rendering.encyclopedia import add_encyclopedia_navigation

    add_encyclopedia_navigation(items, note, links)
    if any(i.get("curation_version") == "1.3.0" for i in cves):
        for home in ["NVKB-Home", "Learning-Library", "Research-Library"]:
            output["00-Home/" + home + ".md"] += (
                "\n\n[[MOC-CVE-Encyclopedia|CVE Encyclopedia]] · [[MOC-CVE-by-Publication-Year|Theo năm công bố]]"
                " · [[MOC-Protocol-Security|Protocol Security]] · [[MOC-HTTP-Processing|HTTP Processing]]"
                " · [[MOC-Media-Processing|Media Processing]] · [[MOC-Defensive-Engineering|Defensive Engineering]]"
                " · [[MOC-Research-Review-Queue|Research Review Queue]]\n"
            )
    vault = root / "vault"
    manifest_path = vault / ".nvkb-generated.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    protected = []
    for relative, text in output.items():
        path = vault / relative
        if path.exists() and path.read_text() != text:
            if (
                relative not in manifest
                or hashlib.sha256(path.read_bytes()).hexdigest() != manifest[relative]
            ):
                protected.append(relative)
    if protected:
        raise ValueError(
            "Protected authored/edited content; move edits to 13-Research before regenerating: "
            + ", ".join(protected)
        )
    if dry_run:
        return dict(planned_notes=len(output), dry_run=True)
    for relative, text in output.items():
        path = vault / relative
        if not path.exists() or path.read_text() != text:
            atomic_write(path, text)
        manifest[relative] = hashlib.sha256(text.encode()).hexdigest()
    atomic_write(manifest_path, json_text(manifest))
    # Core plugins only. Never replace existing personal Obsidian settings.
    core = vault / ".obsidian/core-plugins.json"
    if not core.exists():
        atomic_write(
            core,
            json_text(
                [
                    "file-explorer",
                    "global-search",
                    "switcher",
                    "graph",
                    "backlink",
                    "outgoing-link",
                    "properties",
                    "page-preview",
                    "templates",
                ]
            ),
        )
    return check_vault(root)
