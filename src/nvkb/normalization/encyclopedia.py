"""Import explicitly authored research, preserving source observations and editions.

The YAML contains curator decisions, not generated conclusions. Snapshot/locator
checks here establish reproducibility, not semantic entailment.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from nvkb.config import utcnow
from nvkb.evidence.graph import Graph
from nvkb.evidence.semantics import review_claim
from nvkb.storage.canonical import Store, atomic_write, json_text, slug, stable_id

REVIEWER = "nvkb-v1.3-ai-curator"
MATURITIES = {
    "METADATA_ONLY",
    "TECHNICAL_DRAFT",
    "AI_REVIEWED",
    "INDEPENDENT_AGENT_REVIEWED",
    "HUMAN_APPROVED",
}
HEADINGS = [
    "Executive summary",
    "CVE identity và product scope",
    "Technical background",
    "Affected architecture",
    "Normal component behavior",
    "High-level failure mechanism",
    "Relevant security principles",
    "Vendor-documented applicability",
    "Affected và fixed versions",
    "Confirmed impact",
    "Potential impact và limitations",
    "Remediation principles",
    "Official mitigation",
    "Patch management considerations",
    "Related knowledge",
    "Learning objectives",
    "Discussion questions",
    "Claim-level evidence",
    "Unknown information",
    "Review status",
]


def wiki(identifier, label=None):
    target = identifier.removeprefix("CVE:") if identifier.startswith("CVE:") else slug(identifier)
    return "[[" + target + ("|" + label if label else "") + "]]"


class Curator:
    def __init__(self, root):
        self.root = Path(root)
        self.store = Store(self.root)
        self.graph = Graph(self.store)
        self.evidence = self.store.all("Evidence")
        self.manifest = {}

    def relationship(self, subject, predicate, target, refs, claims, **metadata):
        identifier = stable_id("REL", subject, predicate, target)
        try:
            old = self.store.get(identifier)
        except KeyError:
            old = {}
        if (
            old.get("reviewer_id") == REVIEWER
            and old.get("reviewed_at")
            and old.get("source_refs") == sorted(set(refs))
            and old.get("claim_refs") == list(claims)
            and old.get("rationale") == metadata.get("rationale")
        ):
            return identifier
        return self.graph.relationship(
            subject,
            predicate,
            target,
            refs,
            claims,
            reviewed_at=utcnow(),
            review_rationale=metadata["rationale"],
            evidence_locator="; ".join(sorted({self.store.get(r)["source_locator"] for r in refs})),
            **metadata,
        )

    def source(self, url):
        candidates = [e for e in self.evidence if e["source_url"] == url]
        if not candidates:
            extra = self.root / "data/curation/v1.3/additional-sources.json"
            sources = json.loads(extra.read_text()) if extra.exists() else {}
            if url not in sources:
                raise ValueError(f"No immutable source: {url}")
            item = sources[url]
        else:
            item = max(candidates, key=lambda e: e["retrieved_at"])
        path = self.root / item["local_snapshot_path"]
        if hashlib.sha256(path.read_bytes()).hexdigest() != item["content_hash"]:
            raise ValueError(f"Changed snapshot: {url}")
        snapshot = {k: item[k] for k in ["source_url", "retrieved_at", "content_hash", "local_snapshot_path"]}
        self.manifest[url] = snapshot
        return snapshot

    def claim(
        self, subject, predicate, value, url, locator, excerpt, *, interpretation=False, supplements=()
    ):
        snapshot = self.source(url)
        publisher = (
            "CNA F5 / CVE Program"
            if "cvelistV5" in url
            else (
                "IETF / RFC Editor"
                if "rfc-editor" in url
                else "CVE Program"
                if "cve-schema" in url
                else "MITRE CWE"
                if "cwe.mitre" in url
                else "NGINX / F5"
            )
        )
        ref = self.graph.evidence(
            snapshot,
            locator,
            publisher,
            url.rsplit("/", 1)[-1] + ": " + locator,
            "Scoped research evidence; read the linked Claim for interpretation.",
            "official_research",
        )
        refs = [ref]
        for supplement in supplements:
            extra = self.graph.evidence(
                self.source(supplement["source_url"]),
                "pre: official announcement paragraphs for " + subject.removeprefix("CVE:"),
                "NGINX / F5",
                "Official NGINX announcement",
                "Applicability scope comparison",
                "official_research",
            )
            refs.append(extra)
        cid = self.graph.claim(
            subject,
            "v1.3:" + predicate,
            value,
            refs,
            "NVKB AI curation" if interpretation else publisher,
            status="INFERRED" if interpretation else "UNVERIFIED",
            confidence=0.0,
            notes="Explicit authored review; no human approval or runtime verification.",
        )
        old = self.store.get(cid)
        if old.get("reviewer_id") != REVIEWER:
            review_claim(
                self.store,
                cid,
                support="PARTIAL" if interpretation else "SUPPORTED",
                reviewer_id=REVIEWER,
                reviewer_kind="AI",
                locator=locator,
                excerpt=excerpt,
                evidence_id=ref,
                inference="INTERPRETATION" if interpretation else "SOURCE_STATEMENT",
                rationale=(
                    "Read the cited snapshot section and compared the authored bounded statement. "
                    + (
                        "Source grounds the mechanism; ownership/invariant/teaching reasoning is author interpretation."
                        if interpretation
                        else "Support is limited to the named product, conditions and documented impact; no independent root-cause verification."
                    )
                ),
                version_scope="Document snapshot "
                + snapshot["retrieved_at"]
                + "; CVE versions are scoped separately.",
            )
            current = self.store.get(cid)
            current.update(
                extraction_status="MATCHED",
                source_authority=publisher,
                product_scope="NGINX OSS research edition; broader source scope kept explicit",
            )
            self.store.save(current)
        return cid, ref

    def knowledge(self, seed):
        item = self.store.get(seed["id"])
        fact, ref = self.claim(
            item["id"],
            "knowledge_fact",
            seed["source_fact"],
            seed["source"],
            seed["locator"],
            seed["excerpt"],
        )
        claims, sections = [fact], []
        for part in re.split(r"(?=^## )", seed["body"], flags=re.M):
            if not part.strip():
                continue
            title = part.splitlines()[0].removeprefix("## ")
            cid, _ = self.claim(
                item["id"],
                "knowledge:" + title,
                part.strip(),
                seed["source"],
                seed["locator"],
                seed["excerpt"],
                interpretation=True,
            )
            claims.append(cid)
            sections.append(
                part.rstrip() + "\n\n_Diễn giải tác giả; PARTIAL_: " + wiki(cid, "Claim của section") + "."
            )
        old_claims = set(item.get("research_claim_refs", [])) | set(item.get("claim_refs", []))
        for cid in old_claims - set(claims):
            old = self.store.get(cid)
            if old.get("lifecycle_status") == "CURRENT":
                old.update(
                    lifecycle_status="HISTORICAL",
                    review_reason="Preserved earlier knowledge edition; v1.3 has scoped replacement statements, not retroactive support.",
                )
                self.store.save(old)
        fields = dict(
            name=seed["name"],
            description=seed["source_fact"],
            definition=seed["source_fact"],
            article_body="Nguồn xác nhận: "
            + wiki(fact, "phạm vi tài liệu")
            + ".\n\n"
            + "\n\n".join(sections),
            prerequisites=seed["prerequisites"],
            learning_objectives=seed["objectives"],
            assessment=seed["assessment"],
            answer_explanations=seed["answer"],
            research_claim_refs=claims,
            claim_refs=claims,
            source_refs=[ref],
            editorial_maturity="AI_REVIEWED",
            curation_version="1.3.0",
            editorial_review_note="AI self-review of cited sources and authored reasoning; independent/human/learner review pending.",
            verification_limitations="Per-section interpretations remain PARTIAL; not a source-code audit or human approval.",
            related_knowledge=seed["prerequisites"],
            diagram="",
        )
        item.update(fields, curated_fields=sorted(fields))
        self.store.save(item)
        for prerequisite in seed["prerequisites"]:
            self.relationship(
                item["id"],
                "REQUIRES_KNOWLEDGE_OF",
                prerequisite,
                [ref],
                [fact],
                status="INFERRED",
                rationale="Mục tiêu '"
                + seed["objectives"][0]
                + "' cần mô hình "
                + self.store.get(prerequisite)["name"]
                + ". Quyết định sư phạm, không là fault location.",
                inference_type="PEDAGOGICAL",
                review_status="AI_REVIEWED",
                source_support_status="PARTIAL",
                reviewer_id=REVIEWER,
            )

    def article(self, seed, group, knowledge_ids):
        if seed.get("maturity") not in {"TECHNICAL_DRAFT", "AI_REVIEWED"}:
            raise ValueError("This importer cannot confer independent or human approval")
        item = self.store.get(seed["cve"])
        source_e = next(
            e
            for e in self.evidence
            if "CVEProject/cvelistV5" in e["source_url"] and seed["cve"] in e["source_url"]
        )
        url = source_e["source_url"]
        raw = json.loads((self.root / self.source(url)["local_snapshot_path"]).read_text())
        if raw["cveMetadata"]["cveId"] != seed["cve"]:
            raise ValueError("Wrong CVE snapshot")
        cna = raw["containers"]["cna"]
        # Small exact extraction witness; entailment decisions are the authored YAML.
        excerpt = next(d["value"] for d in cna["descriptions"] if d.get("lang") == "en").split()[0]
        pointer = (
            "/containers/cna/descriptions/"
            + str(next(i for i, d in enumerate(cna["descriptions"]) if d.get("lang") == "en"))
            + "/value"
        )
        ids, refs = {}, []
        identity = dict(
            cve_id=raw["cveMetadata"]["cveId"],
            state=raw["cveMetadata"]["state"],
            publication_date=raw["cveMetadata"].get("datePublished"),
            products=[a.get("product") for a in cna.get("affected", [])],
            problem_types=cna.get("problemTypes", []),
            research_product="NGINX Open Source",
        )
        ids["identity"], ref = self.claim(
            item["id"],
            "identity",
            identity,
            url,
            "/cveMetadata; /containers/cna/affected/*/product; /containers/cna/problemTypes",
            seed["cve"],
        )
        refs.append(ref)
        announcements = [
            e
            for e in self.evidence
            if e["id"] in item["source_refs"] and "mailman.nginx.org" in e["source_url"]
        ]
        announcements = list({e["source_url"]: e for e in announcements}.values())
        for field in ["applicability", "impact", "potential"]:
            cid, ref = self.claim(
                item["id"],
                field,
                seed[field],
                url,
                pointer,
                excerpt,
                interpretation=field == "potential",
                supplements=announcements if field == "applicability" else (),
            )
            ids[field] = cid
            refs.append(ref)
        cid, ref = self.claim(
            item["id"], "mechanism", seed["mechanism"], url, pointer, excerpt, interpretation=True
        )
        ids["mechanism"] = cid
        refs.append(ref)
        advisory = next(
            e
            for e in self.evidence
            if e["source_url"] == "https://nginx.org/en/security_advisories.html"
            and seed["cve"] in e["source_locator"]
        )
        soup = BeautifulSoup(
            (self.root / self.source(advisory["source_url"])["local_snapshot_path"]).read_text(),
            "html.parser",
        )
        entry = next(
            li.get_text(" ", strip=True) for li in soup.find_all("li") if seed["cve"] in li.get_text()
        )
        if (
            item["upstream_affected_expression"] not in entry
            or item["upstream_unaffected_expression"] not in entry
        ):
            raise ValueError("Version statement differs from reviewed advisory: " + seed["cve"])
        version_text = (
            "NGINX OSS: affected "
            + item["upstream_affected_expression"]
            + "; not vulnerable/fixed branches "
            + item["upstream_unaffected_expression"]
            + "."
        )
        ids["versions"], ref = self.claim(
            item["id"],
            "versions",
            version_text,
            advisory["source_url"],
            "li containing " + seed["cve"],
            seed["cve"],
        )
        refs.append(ref)
        scope_text = seed.get(
            "scope",
            "Phạm vi nghiên cứu: NGINX Open Source; bảng upstream không dùng làm bảng phiên bản NGINX Plus, Ingress, Unit hoặc njs.",
        )
        knowledge_ids = seed.get("knowledge", knowledge_ids)
        conflicts = list(item.get("unresolved_conflicts", []))
        for disagreement in seed.get("source_disagreements", []):
            compared = []
            for statement in disagreement["statements"]:
                cid, ref = self.claim(
                    item["id"],
                    disagreement["predicate"],
                    statement["value"],
                    statement["source"],
                    statement["locator"],
                    statement["excerpt"],
                )
                ids[statement["label"]] = cid
                refs.append(ref)
                compared.append(self.store.get(cid))
            conflict = self.graph.reconcile(item["id"], "v1.3:" + disagreement["predicate"], compared)
            if conflict:
                conflicts.append(conflict)
        related = " · ".join(wiki(k, self.store.get(k)["name"]) for k in knowledge_ids)

        def claimlink(field):
            return " " + wiki(ids[field], "Claim / locator") + "."

        mitigation = seed.get(
            "official_mitigation",
            "Nguồn advisory xác nhận remediation bằng các release sửa trong mục 9. Workaround riêng ngoài nâng cấp: UNKNOWN trong các nguồn đã review; không gán khuyến nghị thiết kế ở mục 12 thành mitigation chính thức.",
        )
        objectives = seed.get(
            "objectives",
            ["Giải thích invariant: " + seed["principle"], "Trả lời có evidence: " + seed["question"]],
        )
        texts = [
            seed["summary"],
            f"{item['cve_id']}; published {item['publication_date']}; {scope_text} CNA nguồn: F5 qua CVE Program. "
            + claimlink("identity"),
            related + ". Học mô hình chung ở các bài nền; phạm vi CVE lấy từ nguồn riêng bên dưới.",
            seed["architecture"] + claimlink("applicability"),
            seed["normal"] + " (Diễn giải mô hình từ bài nền.)",
            seed["mechanism"] + claimlink("mechanism"),
            seed["principle"] + " (Diễn giải phòng vệ.)",
            seed["applicability"] + claimlink("applicability"),
            version_text
            + claimlink("versions")
            + "\n\n"
            + seed["patch_note"]
            + " Các fix theo nhánh là ngoại lệ của khoảng affected tổng quát; không coi khoảng liền là tập hợp không có ngoại lệ.",
            seed["impact"] + claimlink("impact"),
            seed["potential"] + claimlink("potential"),
            seed["defense"] + " (Khuyến nghị tác giả; không phải workaround đã được vendor xác nhận.)",
            mitigation + claimlink("versions"),
            seed["patch_note"]
            + "\n\n"
            + wiki("CONCEPT:BACKPORT", "Đối chiếu package/backport")
            + " → "
            + wiki("CONTROL:PATCH-VERIFICATION", "xác minh bản chạy")
            + ". Bằng chứng inventory/runtime/signature chưa được cung cấp trong nghiên cứu tài liệu này.",
            related
            + "\n\nWeakness do CNA phân loại: "
            + " · ".join(wiki(k, self.store.get(k)["name"]) for k in item["related_weaknesses"])
            + ". CWE là taxonomy, không là bằng chứng fault location.",
            "\n".join("- " + x for x in objectives),
            seed["question"] + "\n\nGợi ý đáp án: " + seed["answer"],
            "\n".join("- " + field + ": " + wiki(cid, cid) for field, cid in ids.items())
            + "\n\nSource statement, author interpretation và unknown được tách trong từng Claim. Snapshot/hash dùng để tái kiểm tra, không thay việc đọc nguồn. Metadata cũ vẫn truy xuất qua lịch sử.",
            seed["unknown"],
            seed["maturity"]
            + " — AI biên soạn/review trong phạm vi tài liệu. Chưa có independent-agent review, human approval hoặc learner testing. "
            + seed.get(
                "review_gap",
                "Cần chuyên gia đối chiếu cơ chế với mã nguồn/bản vá và đánh giá sư phạm; không có xác minh trên hệ thống triển khai.",
            ),
        ]
        body = (
            "\n\n".join(
                "## " + str(i + 1) + ". " + heading + "\n\n" + value
                for i, (heading, value) in enumerate(zip(HEADINGS, texts))
            )
            + "\n"
        )
        if seed["maturity"] not in {"TECHNICAL_DRAFT", "AI_REVIEWED"}:
            raise ValueError("This importer cannot confer independent or human approval")
        fields = dict(
            research_body=body,
            research_group=group,
            editorial_maturity=seed["maturity"],
            editorial_review_note=texts[-1],
            research_claim_refs=list(ids.values()),
            educational_summary=seed["summary"],
            normal_component_behavior=seed["normal"],
            root_cause_summary=seed["mechanism"],
            security_assumption_violated=seed["principle"],
            documented_configuration_context=seed["applicability"],
            confirmed_impact=seed["impact"],
            potential_impact=seed["potential"],
            defensive_recommendations=[seed["defense"]],
            unknown_conditions=[
                seed["unknown"],
                "Chưa có bằng chứng binary/runtime hoặc independent/human technical review.",
            ],
            learning_objectives=objectives,
            curation_version="1.3.0",
            unresolved_conflicts=sorted(set(conflicts)),
            related_modules=item.get("related_modules", []),
            related_components=item.get("related_components", []),
            related_protocols=item.get("related_protocols", []),
        )
        for cid in set(item.get("research_claim_refs", [])) - set(ids.values()):
            prior = self.store.get(cid)
            prior.update(
                lifecycle_status="HISTORICAL",
                review_reason="Previous research edition; retained unchanged statement with original support decision.",
            )
            self.store.save(prior)
        for cid in item.get("claim_refs", []):
            prior = self.store.get(cid)
            if prior.get("lifecycle_status") == "CURRENT" and prior["predicate"] in {
                "educational_summary",
                "root_cause_summary",
                "normal_component_behavior",
                "security_assumption_violated",
                "confirmed_impact",
                "potential_impact",
                "defensive_recommendations",
            }:
                prior.update(
                    lifecycle_status="HISTORICAL",
                    review_reason="Earlier generated interpretation retained; the v1.3 article supplies bounded source claims and explicit author reasoning.",
                )
                self.store.save(prior)
        item.update(fields, curated_fields=sorted(fields))
        item["claim_refs"] = sorted(set(item.get("claim_refs", []) + list(ids.values())))
        item["source_refs"] = sorted(set(item["source_refs"] + refs))
        self.store.save(item)
        for target in knowledge_ids:
            self.relationship(
                item["id"],
                "learns_from",
                target,
                sorted(set(refs)),
                list(ids.values()),
                status="INFERRED",
                rationale="Đọc "
                + self.store.get(target)["name"]
                + " để thảo luận: "
                + seed["question"]
                + " Quan hệ học tập; không xác nhận fault location.",
                inference_type="PEDAGOGICAL",
                review_status="AI_REVIEWED",
                source_support_status="PARTIAL",
                reviewer_id=REVIEWER,
            )


def import_batch(root, name):
    root = Path(root)
    seed = yaml.safe_load((root / "data/curation/v1.3" / (name + ".yaml")).read_text())
    curator = Curator(root)
    for lesson in seed.get("knowledge", []):
        curator.knowledge(lesson)
    knowledge_ids = seed.get("shared_knowledge", [x["id"] for x in seed.get("knowledge", [])])
    for article in seed["articles"]:
        curator.article(article, seed["group"], knowledge_ids)
    path = root / "data/curation/v1.3/source-manifest.json"
    manifest = json.loads(path.read_text()) if path.exists() else {}
    manifest.update(curator.manifest)
    atomic_write(path, json_text(manifest))
    result = dict(
        batch=name,
        articles=[x["cve"] for x in seed["articles"]],
        knowledge=[x["id"] for x in seed.get("knowledge", [])],
        source_documents=len(curator.manifest),
        semantic_review="Authored AI decisions; structural validation is separate",
    )
    atomic_write(root / "reports/v1.3" / (name + "-import.json"), json_text(result))
    return result
