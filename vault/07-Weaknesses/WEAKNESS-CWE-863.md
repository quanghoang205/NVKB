---
entity_type: weakness
id: WEAKNESS:CWE-863
title: Incorrect Authorization
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Incorrect Authorization
tags:
- nginx
- weakness
- knowledge
---

# Incorrect Authorization

CWE-863 là Incorrect Authorization: có thực hiện kiểm tra quyền nhưng kiểm tra đó không đúng.

## Mục tiêu đo được

- Phân loại đúng bốn phát biểu về authentication, authorization, access control và session management.
- Giải thích vì sao giữ CWE do CNA gán mà không đổi nghĩa thuật ngữ.


Kiến thức tiên quyết: [[COMPONENT-TLS-SESSION-LIFECYCLE|TLS resumption: state, ticket và policy hiện hành]].

## Thuật ngữ chuẩn

Tên MITRE là Incorrect Authorization. [[CLAIM-240685A26BEC532BD8384C22|nhận định nguồn: CLAIM:240685A26BEC532BD8384C22]] Authentication hỏi chủ thể là ai hoặc có bằng chứng identity phù hợp không; authorization hỏi chủ thể được làm hành động nào trên tài nguyên nào trong context hiện tại. Identity verification là việc kiểm chứng một khai báo danh tính theo cơ chế đã chọn. Access control là cơ chế thực thi chính sách truy cập; session management duy trì và giới hạn context qua nhiều trao đổi. Các lớp này liên quan nhưng không thể thay tên cho nhau.

_Diễn giải biên soạn; source support PARTIAL, AI self-review_: [[CLAIM-5128F1868A36791671D8B1FF|Claim theo section]].

## Cơ chế quyết định quyền

Mô hình khái niệm: nhận subject/context → xác định resource và action → nạp policy áp dụng → kiểm tra điều kiện → cho phép hoặc từ chối. Một kiểm tra hiện diện nhưng bỏ qua một chiều cần thiết của policy có thể thuộc lớp Incorrect Authorization. Không có kiểm tra và kiểm tra sai là hai mô tả cần phân biệt; chỉ gán CWE cụ thể khi có bằng chứng thích hợp.

_Diễn giải biên soạn; source support PARTIAL, AI self-review_: [[CLAIM-003BFE984ACCCAE36D90753A|Claim theo section]].

## Ranh giới và invariant

Diễn giải phòng vệ: quyết định phải dựa trên context đáng tin và tài nguyên thực sự đang được truy cập. Kiểm tra vai trò không luôn giải quyết quyền giữa hai người cùng vai trò. MITRE ghi nhận giới hạn này trong phần mitigations; do đó RBAC là công cụ, không là bảo đảm mọi kiểm tra theo object đều đúng.

_Diễn giải biên soạn; source support PARTIAL, AI self-review_: [[CLAIM-08CC6C5677653679D8CD9DC8|Claim theo section]].

## Liên hệ case study

CNA gán CWE-863 cho CVE-2025-23419 trong khi mô tả nói về yêu cầu xác thực chứng chỉ client và TLS session resumption. Hai điều này được trình bày song song: tên taxonomy chuẩn giữ nguyên, câu mô tả sản phẩm giữ provenance riêng. Không đổi CWE thành lớp authentication vì suy đoán, và không đổi tên CWE-863 thành 'Authentication policy violation'. Cần nguồn CNA khác hoặc review được ghi nhận trước khi sửa classification.

_Diễn giải biên soạn; source support PARTIAL, AI self-review_: [[CLAIM-FA30BE9D7F3893451E81F661|Claim theo section]].

## Bài tập giấy, tradeoff và giới hạn

Xét A có chứng thư hợp lệ nhưng chưa có quyền đọc tài liệu T. Kênh TLS xác thực A không trả lời quyền đọc T. Policy tập trung giảm phân tán nhưng cần truyền context tin cậy; policy cục bộ giảm phụ thuộc nhưng dễ thiếu nhất quán. Đó là tradeoff thiết kế, không là remediation cụ thể đã được vendor công bố.

Không suy root cause cấp mã nguồn từ nhãn CWE. Câu hỏi mở của một deployment là nơi thực thi policy, sự sống của context phiên và phiên bản đang chạy; bài không xác minh các thông tin đó.

_Diễn giải biên soạn; source support PARTIAL, AI self-review_: [[CLAIM-338BC1201E71F65F7A468BDF|Claim theo section]].



## Tự đánh giá

1. Client certificate hợp lệ nhưng tài khoản không có quyền đọc object: kiểm tra còn thiếu thuộc lớp nào?
2. CNA nói client authentication nhưng gán CWE-863: curator có được tự đổi CWE không?

## Đáp án và giải thích

1. Authorization theo object/context. Authentication thành công không cấp mọi quyền.
2. Không. Giữ tên chuẩn [[CLAIM-240685A26BEC532BD8384C22|nhận định nguồn: CLAIM:240685A26BEC532BD8384C22]], giữ classification nguồn và nêu giới hạn; không biến diễn giải thành correction không chứng cứ. 0–2 điểm mỗi câu.

## Liên hệ và bước tiếp theo

[[COMPONENT-TLS-SESSION-LIFECYCLE|TLS resumption: state, ticket và policy hiện hành]], [[CONTROL-LEAST-PRIVILEGE|Security invariants và trách nhiệm kiểm soát]], [[LEARNING-PATH-01|NGINX Architecture, TLS Security & Patch Verification]]

## Quan hệ có định kiểu

- `PRECEDES` → [[CONTROL-LEAST-PRIVILEGE|Security invariants và trách nhiệm kiểm soát]] — Thứ tự pilot chuyển từ cơ chế vừa học sang mục tiêu kế tiếp; là quyết định sư phạm, chưa learner-tested. **PEDAGOGICAL / NOT_REVIEWED**.
- `CONTEXTUAL_ASSOCIATION` → [[IMPACT-CLIENT-AUTHENTICATION-POLICY|Vi phạm yêu cầu xác thực client certificate]] — Policy context ở 23419 là ví dụ học về identity/authorization, không gộp hai thuật ngữ. Lớp lỗi được CNA gán trong case này; impact là mô tả nguồn riêng, không suy từ CWE. **INTERPRETATION / PARTIAL**.
- `ASSESSED_BY` → [[LEARNING-PATH-01|NGINX Architecture, TLS Security & Patch Verification]] — Capstone yêu cầu vận dụng cơ chế này; đáp án và rubric nằm trong learning path. **PEDAGOGICAL / NOT_REVIEWED**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-TLS-SESSION-LIFECYCLE|TLS resumption: state, ticket và policy hiện hành]] — Cần TLS resumption: state, ticket và policy hiện hành để giải thích mục tiêu: Phân loại đúng bốn phát biểu về authentication, authorization, access control và session management. **PEDAGOGICAL / NOT_REVIEWED**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-240685A26BEC532BD8384C22\|WEAKNESS:CWE-863: pilot_source_statement]] — "CWE-863 là Incorrect Authorization: có thực hiện kiểm tra quyền nhưng kiểm tra đó không đúng." | MITRE CWE | CURRENT | SUPPORTED / AI_REVIEWED | #Description; #Potential_Mitigations — [[EVIDENCE-3F3B7A9F2EE582122C10045B\|cwe863: #Description; #Potential_Mitigations]] |
| [[CLAIM-5128F1868A36791671D8B1FF\|WEAKNESS:CWE-863: pilot_section:Thuật ngữ chuẩn]] — "## Thuật ngữ chuẩn\n\nTên MITRE là Incorrect Authorization. ⟦CLAIM-240685A26BEC532BD8384C22&#124;nhận định nguồn: CLAIM:240685A26BEC532BD8384C22⟧ Authentication hỏi chủ thể là ai hoặ… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #Description; #Potential_Mitigations — [[EVIDENCE-3F3B7A9F2EE582122C10045B\|cwe863: #Description; #Potential_Mitigations]] |
| [[CLAIM-003BFE984ACCCAE36D90753A\|WEAKNESS:CWE-863: pilot_section:Cơ chế quyết định quyền]] — "## Cơ chế quyết định quyền\n\nMô hình khái niệm: nhận subject/context → xác định resource và action → nạp policy áp dụng → kiểm tra điều kiện → cho phép hoặc từ chối. Một kiểm tra… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #Description; #Potential_Mitigations — [[EVIDENCE-3F3B7A9F2EE582122C10045B\|cwe863: #Description; #Potential_Mitigations]] |
| [[CLAIM-08CC6C5677653679D8CD9DC8\|WEAKNESS:CWE-863: pilot_section:Ranh giới và invariant]] — "## Ranh giới và invariant\n\nDiễn giải phòng vệ: quyết định phải dựa trên context đáng tin và tài nguyên thực sự đang được truy cập. Kiểm tra vai trò không luôn giải quyết quyền g… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #Description; #Potential_Mitigations — [[EVIDENCE-3F3B7A9F2EE582122C10045B\|cwe863: #Description; #Potential_Mitigations]] |
| [[CLAIM-FA30BE9D7F3893451E81F661\|WEAKNESS:CWE-863: pilot_section:Liên hệ case study]] — "## Liên hệ case study\n\nCNA gán CWE-863 cho CVE-2025-23419 trong khi mô tả nói về yêu cầu xác thực chứng chỉ client và TLS session resumption. Hai điều này được trình bày song so… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #Description; #Potential_Mitigations — [[EVIDENCE-3F3B7A9F2EE582122C10045B\|cwe863: #Description; #Potential_Mitigations]] |
| [[CLAIM-338BC1201E71F65F7A468BDF\|WEAKNESS:CWE-863: pilot_section:Bài tập giấy, tradeoff và giới hạn]] — "## Bài tập giấy, tradeoff và giới hạn\n\nXét A có chứng thư hợp lệ nhưng chưa có quyền đọc tài liệu T. Kênh TLS xác thực A không trả lời quyền đọc T. Policy tập trung giảm phân tá… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #Description; #Potential_Mitigations — [[EVIDENCE-3F3B7A9F2EE582122C10045B\|cwe863: #Description; #Potential_Mitigations]] |




## Phạm vi kiểm chứng

[[EVIDENCE-2BE634B44A5BFFF65B2BE48B|CVE-2025-23419]], [[EVIDENCE-3F3B7A9F2EE582122C10045B|cwe863: #Description; #Potential_Mitigations]], [[EVIDENCE-50210F852D6BA196DDD0E202|CWE - CWE-863: Incorrect Authorization (5.0)]], [[EVIDENCE-BA3B0AEE884498D2B3876382|CVE-2026-28755]], [[EVIDENCE-BCF67241230218EB4C26F27C|CWE - CWE-863: Incorrect Authorization (5.0)]]

AI self-review of a scoped source statement and authored interpretations; human technical/pedagogical review and learner evaluation PENDING.

No deployment inspection or source-code root cause verification. Statements beyond cited mechanism are interpretations.

[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

