"""Import the authored pilot with section-level observations and explicit AI review metadata."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from nvkb.evidence.graph import Graph
from nvkb.evidence.migration import write_csv
from nvkb.evidence.semantics import review_claim
from nvkb.storage.canonical import Store, atomic_write, entity, json_text, slug

PUBLISHERS = {
    "development": "NGINX / F5",
    "control": "NGINX / F5",
    "request": "NGINX / F5",
    "ssl": "NGINX / F5",
    "advisories": "NGINX / F5",
    "tls13": "IETF / RFC Editor",
    "cwe863": "MITRE CWE",
    "cwe287": "MITRE CWE",
    "debian": "Debian Security Team",
    "case": "CVE Program / CNA: F5",
    "cve_schema": "CVE Program",
    "lifecycle": "Canonical / Ubuntu",
}


def import_pilot(root: Path):
    store, manifest = Store(root), json.loads((root / "data/curation/v1.2/source-manifest.json").read_text())
    graph = Graph(store)
    lessons = yaml.safe_load((root / "data/curation/v1.2/pilot.yaml").read_text())
    facets = yaml.safe_load((root / "data/curation/v1.2/pilot-facets.yaml").read_text())
    reviewed, lesson_ids = [], [x["id"] for x in lessons]
    source_refs = set()

    def add_reviewed(subject, predicate, value, key, locator, excerpt, inference="SOURCE_STATEMENT"):
        snapshot = manifest[key]
        if "error" in snapshot:
            raise ValueError(f"Pilot source unavailable: {key}: {snapshot['error']}")
        ref = graph.evidence(
            snapshot, locator, PUBLISHERS[key], f"{key}: {locator}", value[:280], "official_research"
        )
        cid = graph.claim(
            subject,
            predicate,
            value,
            [ref],
            PUBLISHERS[key] if inference == "SOURCE_STATEMENT" else "NVKB AI curation",
            status="UNVERIFIED" if inference == "SOURCE_STATEMENT" else "INFERRED",
            confidence=0.0,
            notes="Confidence is not a measured factual probability; see source_support_status and review metadata.",
        )
        review_claim(
            store,
            cid,
            support="SUPPORTED" if inference == "SOURCE_STATEMENT" else "PARTIAL",
            reviewer_id="nvkb-v1.2-ai-curator",
            reviewer_kind="AI",
            rationale=(
                f"Read {key} at {locator}; compared the statement with the documented mechanism. "
                + (
                    "Supports the bounded source statement; no independent implementation or human verification."
                    if inference == "SOURCE_STATEMENT"
                    else "Mechanism is grounded in the cited section; examples, tradeoffs, invariant and assessment are authored interpretation, not vendor-confirmed facts. Human expert review pending."
                )
            ),
            locator=locator,
            excerpt=excerpt,
            evidence_id=ref,
            inference=inference,
            version_scope="RFC 8446 TLS 1.3 (2018)"
            if key == "tls13"
            else "Official document snapshot retrieved "
            + snapshot["retrieved_at"]
            + "; deployment version not established",
        )
        claim = store.get(cid)
        claim.update(
            lifecycle_status="CURRENT",
            review_reason="Included in the current authored pilot; AI review is separate from temporal status.",
        )
        store.save(claim)
        reviewed.append(cid)
        source_refs.add(ref)
        return cid, ref

    for number, seed in enumerate(lessons):
        try:
            item = store.get(seed["id"])
        except KeyError:
            item = entity("Component", seed["id"], seed["name"], seed["source_claim"], status="INFERRED")
        claim, ref = add_reviewed(
            item["id"],
            "pilot_source_statement",
            seed["source_claim"],
            seed["source"],
            seed["locator"],
            seed["excerpt"],
        )
        fact_link = "[[" + slug(claim) + "|nhận định nguồn: " + claim + "]]"
        body = seed["article_body"].replace("{C1}", fact_link)
        claims = [claim]
        annotated = []
        for section in re.split(r"(?=^## )", body, flags=re.M):
            if not section.strip():
                continue
            title = section.splitlines()[0].removeprefix("## ")
            cid, _ = add_reviewed(
                item["id"],
                "pilot_section:" + title,
                section,
                seed["source"],
                seed["locator"],
                seed["excerpt"],
                "INTERPRETATION",
            )
            claims.append(cid)
            annotated.append(
                section.rstrip()
                + "\n\n_Diễn giải biên soạn; source support PARTIAL, AI self-review_: [["
                + slug(cid)
                + "|Claim theo section]].\n"
            )
        for old_id in item.get("claim_refs", []):
            if old_id not in claims:
                old = store.get(old_id)
                old.update(
                    lifecycle_status="HISTORICAL",
                    review_reason="Preserved earlier knowledge edition; current lesson has independently scoped section claims.",
                )
                store.save(old)
        item.update(
            name=seed["name"],
            description=seed["source_claim"],
            definition=seed["source_claim"],
            article_body="\n".join(annotated),
            learning_objectives=seed["learning_objectives"],
            prerequisites=seed["prerequisites"],
            assessment=seed["assessment"],
            answer_explanations=seed["answer_explanations"].replace("{C1}", fact_link),
            diagram=seed["diagram"],
            claim_refs=claims,
            source_refs=[ref],
            curation_version="1.2.0",
            related_knowledge=list(
                dict.fromkeys(
                    seed["prerequisites"]
                    + ([lesson_ids[number + 1]] if number + 1 < len(lesson_ids) else [])
                    + ["LEARNING:PATH-01"]
                )
            ),
            verification_status="INFERRED",
            verification_limitations="AI self-review of a scoped source statement and authored interpretations; human technical/pedagogical review and learner evaluation PENDING.",
            version_scope="See per-claim source snapshot/version scope",
            limitations="No deployment inspection or source-code root cause verification. Statements beyond cited mechanism are interpretations.",
        )
        item.update(facets.get(item["id"], {}))
        item["normal_behavior"] = item["description"]
        store.save(item)
    path = store.get("LEARNING:PATH-01")
    for old_id in path.get("claim_refs", []):
        old = store.get(old_id)
        old.update(lifecycle_status="HISTORICAL", review_reason="Earlier learning path edition preserved.")
        store.save(old)
    sequence = "\n".join(
        f"{i + 1}. [[{slug(seed['id'])}|{seed['name']}]] — " + seed["learning_objectives"][0]
        for i, seed in enumerate(lessons)
    )
    path.update(
        name="NGINX Architecture, TLS Security & Patch Verification",
        description="Pilot 12 bài ghép bao phủ 14 chủ đề, có prerequisite DAG, assessment và capstone. Bản AI self-reviewed để chuyên gia thẩm định.",
        curation_version="1.2.0",
        claim_refs=[],
        source_refs=sorted(source_refs),
        prerequisites=[],
        related_knowledge=lesson_ids + ["CVE:CVE-2025-23419"],
        learning_objectives=[
            "Vẽ và giải thích lifecycle process/connection/request với owner đúng.",
            "Phân biệt TLS authentication, application authorization và session policy.",
            "Lập kết luận patch có scope từ advisory/package/inventory và phát hiện claim thiếu chứng cứ.",
        ],
        article_body="""## Đầu vào và cách sử dụng

Cần biết socket, process, HTTP request/response và cách đọc bảng phiên bản. Nếu chưa vững, đọc các liên kết nền trong bài đầu và ghi câu hỏi trước khi đi tiếp. Ước lượng biên tập: 6–9 giờ đọc và bài tập; chưa đo trên người học. Mỗi bài ghi prerequisite; thứ tự dưới đây đi từ ownership đến policy rồi tới provenance của bản vá.

## Tiến trình có lý do

"""
        + sequence
        + """

## Tổng hợp: CVE-2025-23419

[[CVE-2025-23419|Case study có provenance]] nối kiến trúc/session policy với đọc advisory và backport. Không yêu cầu tái hiện lỗ hổng. Người học phải tách lời vendor khỏi giải thích invariant và ghi UNKNOWN cho thông tin thiếu.

## Chuẩn đầu ra

Hoàn thành câu hỏi trong từng bài; sau đó làm capstone độc lập trước khi mở đáp án. Rubric dùng 11 tiêu chí, mỗi tiêu chí 0–3, tổng 33. Mốc đề xuất 26/33 và không có lỗi nghiêm trọng về terminology/source support. Đây là ngưỡng biên tập, chưa được learner-tested. Điểm bài tập không tự trở thành human approval cho corpus.

## Gate review

AI self-review: đã có per-claim metadata. Independent agent review: NOT_PERFORMED. Human technical review: PENDING. Human pedagogy review: PENDING. Learner study: PENDING. Không dùng nhãn peer-reviewed.
""",
        assessment="""Capstone (tài liệu giấy, không kết nối hệ thống):

1. Vẽ master/worker reload và hai request trên một keepalive connection; gắn owner của pool.
2. Giải thích tại sao session resumption không cấp mọi quyền cho mọi virtual server; phân biệt định nghĩa CWE-863 với mô tả authentication trong CNA.
3. Với inventory mẫu A = Debian bookworm nginx 1.22.1-9+deb12u1, origin UNKNOWN, runtime evidence trống: lập năm cột advisory/package/lifecycle/KEV/runtime.
4. Phê bình nhận định “hash khớp + CVE mirror đồng ý + không trong KEV = đã vá an toàn”. Chỉ ra từng bước suy luận thiếu chứng cứ.
5. Thiết kế trên giấy policy cho endpoint đòi client certificate: phân biệt mode `optional` với yêu cầu mọi client phải được xác thực; nêu dữ liệu cần kiểm tra trước quyết định. Không triển khai hoặc thử bypass.
""",
        answer_explanations="""1. Master điều phối; worker mới/cũ có thể cùng sống; request pools A/B có lifetime riêng với connection. Xem bài master/connection/pool.
2. Resumption dùng state/PSK, policy authorization vẫn cần đúng context. Giữ classification CNA và tên MITRE chuẩn; không gọi title+CWE là root-cause review.
3. Package đạt ngưỡng tracker theo inventory; upstream banner không dùng thay comparator Debian. Lifecycle UNKNOWN nếu không có nguồn đúng scope; KEV chỉ có nghĩa theo snapshot/freshness; runtime UNKNOWN. Origin chưa biết → manual review. Không gọi asset đã được attest.
4. Hash là integrity; mirror chung authority không độc lập; absence KEV không phủ định exploitation; không có chứng cứ deployment. Cần claim support và runtime evidence riêng.
5. Theo module SSL, `optional` yêu cầu certificate nhưng chỉ xác minh nếu có, không tương đương mọi client phải có certificate. Phải nêu policy, trust store, context và phiên bản; không suy từ một directive rằng application authorization đã đúng. Nguồn đọc thêm: [NGINX ssl_verify_client](https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_verify_client).

Rubric chi tiết trong reports/PILOT_CURRICULUM_REPORT.md và ACADEMIC_REVIEW_QUEUE.md; người chấm phải ghi bằng chứng cho mỗi điểm, không dùng độ dài bài làm làm tiêu chí.
""",
        verification_limitations="Curriculum is authored pedagogy; no human approval or measured learner outcomes.",
        diagram="",
    )
    store.save(path)
    for i, seed in enumerate(lessons):
        item = store.get(seed["id"])
        for prerequisite in seed["prerequisites"]:
            graph.relationship(
                seed["id"],
                "REQUIRES_KNOWLEDGE_OF",
                prerequisite,
                item["source_refs"],
                status="INFERRED",
                rationale=f"Cần {store.get(prerequisite)['name']} để giải thích mục tiêu: {seed['learning_objectives'][0]}",
                inference_type="PEDAGOGICAL",
            )
        if i + 1 < len(lessons):
            graph.relationship(
                seed["id"],
                "PRECEDES",
                lesson_ids[i + 1],
                item["source_refs"],
                status="INFERRED",
                rationale="Thứ tự pilot chuyển từ cơ chế vừa học sang mục tiêu kế tiếp; là quyết định sư phạm, chưa learner-tested.",
                inference_type="PEDAGOGICAL",
            )
        graph.relationship(
            seed["id"],
            "ASSESSED_BY",
            path["id"],
            item["source_refs"],
            status="INFERRED",
            rationale="Capstone yêu cầu vận dụng cơ chế này; đáp án và rubric nằm trong learning path.",
            inference_type="PEDAGOGICAL",
        )
    for subject, predicate, target, rationale in [
        (
            "COMPONENT:MASTER-PROCESS",
            "PART_OF",
            "DEPLOYMENT:REVERSE-PROXY",
            "Master điều phối lifecycle tiến trình trong deployment đa tiến trình được mô tả.",
        ),
        (
            "COMPONENT:CONNECTION-LIFECYCLE",
            "DEPENDS_ON",
            "COMPONENT:EVENT-DRIVEN",
            "Connection tiến triển qua các sự kiện I/O và timer; không phải proof về một CVE.",
        ),
        (
            "COMPONENT:MEMORY-POOL",
            "PARTICIPATES_IN",
            "COMPONENT:CONNECTION-LIFECYCLE",
            "Pool gắn với lifetime đối tượng; scope của pool phải được phân biệt với socket.",
        ),
        (
            "COMPONENT:TLS-SESSION-LIFECYCLE",
            "PARTICIPATES_IN",
            "PROTOCOL:TLS",
            "Resumption là cơ chế TLS theo RFC 8446; không kết luận fault location.",
        ),
        (
            "PROTOCOL:TLS",
            "CONTEXTUAL_ASSOCIATION",
            "WEAKNESS:CWE-863",
            "TLS authentication và authorization có quan hệ context nhưng không đồng nghĩa.",
        ),
    ]:
        item = store.get(subject)
        graph.relationship(
            subject,
            predicate,
            target,
            item["source_refs"],
            status="INFERRED",
            rationale=rationale,
            inference_type="INTERPRETATION",
        )
    case = store.get("CVE:CVE-2025-23419")
    case_claim, case_ref = add_reviewed(
        case["id"],
        "case_source_scope",
        "CNA F5 mô tả tác động liên quan yêu cầu client-certificate authentication trong TLS session resumption; record phân loại CWE-863. Không công bố trong corpus này review mã nguồn độc lập.",
        "case",
        "/containers/cna/descriptions/0/value; /containers/cna/problemTypes/0/descriptions/0",
        "client certificate authentication",
    )
    fix_claim, fix_ref = add_reviewed(
        case["id"],
        "case_documented_fix",
        "NGINX công bố fixes 1.26.3 và 1.27.4 theo nhánh.",
        "advisories",
        "li containing CVE-2025-23419",
        "1.27.4+, 1.26.3+",
    )
    case["claim_refs"] = sorted(set(case["claim_refs"] + [case_claim, fix_claim]))
    case.update(
        curation_version="1.2.0",
        research_body=f"""## Case study: phạm vi nguồn và diễn giải

**Dữ kiện do nguồn xác nhận:** [[{slug(case_claim)}|Claim CNA và locator JSON]]; [[{slug(fix_claim)}|Claim bản sửa upstream]]. Phạm vi là NGINX OSS trong corpus; thông tin Plus không được nhập lẫn. Conditions đọc từ record, không suy từ tiêu đề.

**Kiến thức nền:** [[PROTOCOL-TLS|TLS 1.3]], [[COMPONENT-TLS-SESSION-LIFECYCLE|resumption]], [[WEAKNESS-CWE-863|Incorrect Authorization]]. RFC 8446 là nền TLS 1.3, không chứng minh mọi chi tiết implementation của các phiên bản NGINX bị ảnh hưởng.

**Diễn giải invariant:** context xác thực của phiên được dùng lại phải phù hợp policy của server được chọn. Đây là diễn giải mức nguyên lý, không phải source-code root cause đã được review; không có exploit chain hoặc procedure kiểm chứng bypass.

**Tác động:** nguồn mô tả yêu cầu xác thực có thể không được giữ. CVSS có confidentiality impact theo metric CNA; không dùng nó để khẳng định dữ liệu nào đã bị truy cập. Process scope, privilege context và hậu quả của deployment cụ thể chưa biết; không suy crash hoặc code execution.

**Remediation:** đối chiếu release cố định theo nhánh và package đúng distribution. Không có review chữ ký patch/binary trong đợt này. Runtime vẫn cần bằng chứng quản trị viên cung cấp.

**Mục tiêu học:** phân biệt authentication/authorization; đọc branch fixes; chỉ ra giới hạn của việc suy nguyên nhân từ CWE. **Câu hỏi thảo luận:** vì sao CVE Program và aggregator cùng record không là hai đánh giá độc lập? **Đáp án:** chúng chuyển tiếp cùng authority; cần giữ kênh để truy vết, không tăng corroboration count.

**Bài tập phòng vệ:** lập bảng năm chiều patch/package/lifecycle/KEV/runtime từ inventory giả định trong [[LEARNING-PATH-01|pilot]]. Không tạo traffic. Human expert review còn PENDING.
""",
    )
    impact = entity(
        "Impact",
        "IMPACT:CLIENT-AUTHENTICATION-POLICY",
        "Vi phạm yêu cầu xác thực client certificate",
        "Tác động được CNA mô tả cho CVE-2025-23419; không tự suy process crash hay code execution.",
        [case_ref],
        "INFERRED",
        definition="Yêu cầu xác thực client certificate không được duy trì trong context mà CNA nêu.",
        applicable_context="Chỉ điều kiện CNA của CVE-2025-23419.",
        limitations="Không xác minh deployment hoặc tác động thực tế; xem scope CNA.",
        claim_refs=[case_claim],
        related_knowledge=["WEAKNESS:CWE-863", "COMPONENT:TLS-SESSION-LIFECYCLE"],
        verification_limitations="Source-confirmed impact description; AI interpretation of category, human review pending.",
    )
    mitigation = entity(
        "Mitigation",
        "MITIGATION:UPSTREAM-FIX-2025-23419",
        "Cập nhật bản sửa đúng nhánh cho CVE-2025-23419",
        "Biện pháp remediation được công bố, không phải workaround chưa có nguồn.",
        [fix_ref],
        "INFERRED",
        definition="Chọn release chứa bản sửa theo advisory hoặc backport chính thức đúng distribution/release.",
        applicable_context="NGINX OSS và phạm vi CVE-2025-23419.",
        limitations="Version comparison không attest binary/process; không mở rộng sang Plus hoặc package tùy biến.",
        claim_refs=[fix_claim],
        related_knowledge=["CONTROL:PATCH-VERIFICATION", "CONCEPT:BACKPORT"],
        verification_limitations="Advisory version evidence only; runtime and patch signatures not verified.",
    )
    store.save(impact)
    store.save(mitigation)
    case["impact_refs"] = sorted(set(case.get("impact_refs", []) + [impact["id"]]))
    case["official_mitigation_refs"] = sorted(
        set(case.get("official_mitigation_refs", []) + [mitigation["id"]])
    )
    store.save(case)
    graph.relationship(
        case["id"],
        "MITIGATED_BY",
        mitigation["id"],
        [fix_ref],
        [fix_claim],
        status="INFERRED",
        rationale="Advisory fixe(s) provide version-based remediation; no runtime attestation.",
        inference_type="INTERPRETATION",
    )
    rows = [
        {
            k: store.get(cid).get(k, "")
            for k in [
                "id",
                "subject_entity_id",
                "predicate",
                "source_support_status",
                "review_status",
                "reviewer_id",
                "reviewed_at",
                "review_rationale",
                "evidence_locator",
                "version_scope",
            ]
        }
        for cid in reviewed
    ]
    write_csv(root / "reports/EVIDENCE_REVIEW_LEDGER.csv", rows)
    result = dict(
        lesson_ids=lesson_ids,
        reviewed_claims=reviewed,
        lessons=len(lessons),
        human_approved=0,
        independent_agent_review="NOT_PERFORMED",
    )
    atomic_write(root / "reports/v1.2/pilot-import.json", json_text(result))
    return result
