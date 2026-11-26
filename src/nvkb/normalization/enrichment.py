"""Vietnamese teaching corpus with explicit distinction between source facts and synthesis."""

from __future__ import annotations

import re

import yaml
from bs4 import BeautifulSoup

from nvkb.collectors.http import Fetcher, SourceError
from nvkb.config import Config
from nvkb.evidence.graph import Graph
from nvkb.storage.canonical import Store, entity

KNOWLEDGE_FIELDS = [
    "definition",
    "normal_behavior",
    "architecture_position",
    "security_boundary",
    "safety_assumptions",
    "related_failure_classes",
    "failure_impact",
    "defensive_principles",
]


def build_corpus(config: Config, offline=False, progress=print):
    store = Store(config.root)
    graph = Graph(store)
    fetcher = Fetcher(config, offline=offline)
    seeds = yaml.safe_load(config.path("data/curation/knowledge.yaml").read_text())
    failures, imported = [], []
    memo = {}
    try:
        for seed in seeds:
            try:
                existing = store.get(seed["id"])
            except KeyError:
                existing = None
            if existing and existing.get("curation_version") == "1.2.0":
                imported.append(seed["id"])
                continue
            url = seed["url"]
            progress("Knowledge: " + seed["name"])
            try:
                snapshot = memo.get(url)
                if snapshot is None:
                    snapshot = fetcher.fetch(url, "documentation")
                    memo[url] = snapshot
                soup = BeautifulSoup(snapshot["text"], "html.parser")
                visible = soup.get_text(" ", strip=True)
                javascript_shell = len(visible) < 500 and any(
                    marker in visible.lower()
                    for marker in (
                        "doesn't work properly without javascript",
                        "does not work properly without javascript",
                        "please enable javascript",
                    )
                )
                if len(visible) < 100 or javascript_shell:
                    raise ValueError("Document does not expose usable text")
                publisher = (
                    "NGINX / F5"
                    if "nginx.org/" in url
                    else "IETF / RFC Editor"
                    if "rfc-editor.org" in url
                    else "MITRE CWE"
                    if "cwe.mitre.org" in url
                    else "Debian Security Team"
                    if "debian.org" in url
                    else "FIRST"
                    if "first.org" in url
                    else "CVE Program"
                )
                ref = graph.evidence(
                    snapshot,
                    seed["locator"] + "; topic=" + seed["id"],
                    publisher,
                    soup.title.get_text(" ", strip=True) if soup.title else seed["name"],
                    seed["definition"],
                    "technical_documentation",
                )
                claims = []
                for field in KNOWLEDGE_FIELDS:
                    direct = field in {"definition", "normal_behavior"} and seed["entity_type"] not in {
                        "LearningObjective",
                        "SecurityControl",
                    }
                    claims.append(
                        graph.claim(
                            seed["id"],
                            field,
                            seed[field],
                            [ref],
                            publisher,
                            status="VERIFIED" if direct else "INFERRED",
                            confidence=1.0 if direct else 0.8,
                            notes="Diễn giải tiếng Việt từ tài liệu nguồn."
                            if direct
                            else "Tổng hợp sư phạm/phòng vệ; không phải kết luận CVE cụ thể từ nhà cung cấp.",
                        )
                    )
                fields = {f: seed[f] for f in KNOWLEDGE_FIELDS}
                fields.update(
                    related_knowledge=seed.get("related_knowledge", []),
                    claim_refs=claims,
                    learning_objectives=[
                        "Giải thích " + seed["name"] + " bằng cơ chế và ranh giới tin cậy.",
                        "Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.",
                    ],
                    diagram=seed.get("diagram", ""),
                )
                if seed["entity_type"] == "Weakness":
                    fields["cwe_id"] = seed["id"].split(":", 1)[1]
                store.save(
                    entity(
                        seed["entity_type"],
                        seed["id"],
                        seed["name"],
                        seed["definition"],
                        [ref],
                        "INFERRED",
                        **fields,
                    )
                )
                imported.append(seed["id"])
            except (SourceError, ValueError) as exc:
                failures.append(dict(id=seed["id"], source_url=url, error=str(exc)))
                progress("Knowledge source unavailable: " + str(exc))
        available = {i["id"] for i in store.all()}
        for identifier in imported:
            item = store.get(identifier)
            if item.get("curation_version") == "1.2.0":
                continue
            unresolved = [r for r in item.get("related_knowledge", []) if r not in available]
            if unresolved:
                item["related_knowledge"] = [r for r in item["related_knowledge"] if r in available]
                store.save(item)
                failures.append(dict(id=identifier, missing_related=unresolved))
            for target in item.get("related_knowledge", []):
                graph.relationship(identifier, "learns_from", target, item["source_refs"], status="INFERRED")
        from nvkb.storage.canonical import atomic_write, json_text

        result = dict(imported=len(imported), failures=failures)
        atomic_write(config.path("reports/knowledge-import.json"), json_text(result))
        return result
    finally:
        fetcher.close()


def enrich_cve(item: dict, store: Store):
    available = {i["id"]: i for i in store.all()}
    graph = Graph(store)
    text = (item["title"] + " " + item["description"]).lower()
    modules = []
    for module in available.values():
        if module["entity_type"] == "Module" and module["name"].lower() in text:
            modules.append((module["id"], "VERIFIED"))
    aliases = [
        ("http/3", "MODULE:NGX-HTTP-V3-MODULE"),
        ("http/2", "MODULE:NGX-HTTP-V2-MODULE"),
        ("ssl session", "MODULE:NGX-HTTP-SSL-MODULE"),
        ("mail proxy", "MODULE:NGX-MAIL-PROXY-MODULE"),
    ]
    for term, target in aliases:
        if term in text and target in available and target not in [m[0] for m in modules]:
            modules.append((target, "INFERRED"))
    protocols = []
    for term, target in [
        (r"http/3", "HTTP-3"),
        (r"http/2", "HTTP-2"),
        (r"\btls\b|\bssl\b", "TLS"),
        (r"\bquic\b", "QUIC"),
        (r"\bdns\b|\bresolver\b", "DNS"),
        (r"\bsmtp\b", "SMTP"),
        (r"\bpop3\b", "POP3"),
        (r"\bimap\b", "IMAP"),
    ]:
        pid = "PROTOCOL:" + target
        if re.search(term, text) and pid in available:
            protocols.append(pid)
    components = []
    for term, key in [
        ("worker", "WORKER-PROCESS"),
        ("resolver", "CONNECTION-LIFECYCLE"),
        ("session", "VIRTUAL-HOSTS"),
        ("request body", "HTTP-REQUEST-LIFECYCLE"),
        ("buffer", "MEMORY-POOL"),
    ]:
        cid = "COMPONENT:" + key
        if term in text and cid in available:
            components.append(cid)
    item["related_modules"] = sorted(set(m[0] for m in modules))
    item["related_protocols"] = sorted(set(protocols))
    item["related_components"] = sorted(set(components))
    refs = item["source_refs"]
    for predicate, pairs in [
        ("related_modules", modules),
        ("related_protocols", [(p, "INFERRED") for p in protocols]),
        ("related_components", [(p, "INFERRED") for p in components]),
    ]:
        for target, status in pairs:
            cid = graph.claim(
                item["id"],
                predicate,
                target,
                refs,
                "NVKB curation",
                status=status,
                confidence=1.0 if status == "VERIFIED" else 0.8,
                notes="Module được nêu tên trực tiếp trong nguồn."
                if status == "VERIFIED"
                else "Liên kết ngữ cảnh học tập; không chứng minh thành phần là root cause.",
            )
            item["claim_refs"] = sorted(set(item["claim_refs"] + [cid]))
            graph.relationship(item["id"], predicate, target, refs, [cid], status)
    if modules:
        behaviors = [available[m[0]].get("normal_behavior", "") for m in modules]
        item["normal_component_behavior"] = "\n\n".join(b for b in behaviors if b)
        behavior_refs = sorted({ref for m in modules for ref in available[m[0]]["source_refs"]})
        cid = graph.claim(
            item["id"],
            "normal_component_behavior",
            item["normal_component_behavior"],
            behavior_refs,
            "NGINX official documentation",
            status="VERIFIED",
            notes="Cơ chế module từ tài liệu nguồn; không khẳng định là root cause.",
        )
        item["claim_refs"] = sorted(set(item["claim_refs"] + [cid]))
    if "worker process" in text:
        item["affected_process"] = "NGINX worker process (được nêu trực tiếp trong mô tả nguồn)."
        cid = graph.claim(item["id"], "affected_process", item["affected_process"], refs, "CVE Program / CNA")
        item["claim_refs"] = sorted(set(item["claim_refs"] + [cid]))
    educational = [
        available[w] for w in item["related_weaknesses"] if w in available and available[w].get("definition")
    ]
    if educational:
        item["root_cause_summary"] = "Nguồn phân loại vấn đề: " + item["title"] + ".\n\n"
        item["root_cause_summary"] += "\n\n".join(w["name"] + ": " + w["definition"] for w in educational)
        item["root_cause_summary"] += (
            "\n\nĐây là giải thích lớp lỗi theo CWE mà CNA gán, không phải kết luận về dòng mã gây lỗi. Chưa có source-code root cause review độc lập."
        )
        item["security_assumption_violated"] = "\n".join(w["safety_assumptions"] for w in educational)
        item["security_boundary"] = "\n".join(sorted({w["security_boundary"] for w in educational}))
        class_refs = sorted({r for w in educational for r in w["source_refs"]} | set(refs))
        for field in ["root_cause_summary", "security_assumption_violated", "security_boundary"]:
            cid = graph.claim(
                item["id"],
                field,
                item[field],
                class_refs,
                "NVKB curation",
                status="INFERRED",
                confidence=0.8,
                notes="CWE-based teaching explanation; specific code-level root cause not independently reviewed.",
            )
            item["claim_refs"] = sorted(set(item["claim_refs"] + [cid]))
    if item["cve_id"] == "CVE-2025-23419":
        item["educational_summary"] = (
            "Lỗi liên quan việc dùng lại phiên TLS giữa các server block cùng địa chỉ/cổng. Theo mô tả CNA, "
            "điều kiện bao gồm session ticket và/hoặc session cache tại default server có xác thực chứng chỉ client. "
            "Bài học là context xác thực của phiên phải phù hợp với chính sách server đang xử lý; đây là phân tích "
            "nguyên lý từ advisory, chưa phải phân tích mã nguồn độc lập. Upstream công bố bản sửa 1.26.3 và 1.27.4."
        )
        item["root_cause_summary"] = (
            "CNA mô tả việc tái sử dụng session TLS có thể vượt chính sách xác thực chứng chỉ client giữa các "
            "server block chia sẻ listener. Ranh giới cần bảo toàn là liên kết giữa phiên đã xác thực và policy "
            "của virtual server. Nguyên nhân ở mức dòng mã chưa được duyệt trong corpus này."
        )
        item["security_assumption_violated"] = (
            "Ngữ cảnh phiên được resume phải thỏa chính sách client-certificate authentication của server được chọn (diễn giải sư phạm)."
        )
        item["security_boundary"] = (
            "TLS session context ↔ chính sách client authentication của virtual server."
        )
        item["unknown_conditions"] = [
            "Chưa kiểm tra cấu hình hoặc feature của bất kỳ tài sản thực tế nào.",
            "Chưa phân tích độc lập bản vá ở mức dòng mã.",
        ]
        for field in [
            "educational_summary",
            "root_cause_summary",
            "security_assumption_violated",
            "security_boundary",
        ]:
            cid = graph.claim(
                item["id"],
                field,
                item[field],
                refs,
                "NVKB curation",
                status="INFERRED",
                confidence=0.9,
                notes="Diễn giải tiếng Việt phục vụ giảng dạy từ mô tả CNA và advisory; không bổ sung điều kiện khai thác.",
            )
            item["claim_refs"] = sorted(set(item["claim_refs"] + [cid]))
