---
entity_type: impact
id: IMPACT:CLIENT-AUTHENTICATION-POLICY
title: Vi phạm yêu cầu xác thực client certificate
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Vi phạm yêu cầu xác thực client certificate
tags:
- nginx
- impact
- knowledge
---

# Vi phạm yêu cầu xác thực client certificate

Tác động được CNA mô tả cho CVE-2025-23419; không tự suy process crash hay code execution.




## Định nghĩa

Policy context ở 23419 là ví dụ học về identity/authorization, không gộp hai thuật ngữ.





## Liên hệ và bước tiếp theo

[[COMPONENT-TLS-SESSION-LIFECYCLE|TLS resumption: state, ticket và policy hiện hành]], [[WEAKNESS-CWE-863|Incorrect Authorization]], [[CONTROL-LEAST-PRIVILEGE|Security invariants và trách nhiệm kiểm soát]]

## Quan hệ có định kiểu

- `CONTEXTUAL_ASSOCIATION` → [[CONTROL-LEAST-PRIVILEGE|Security invariants và trách nhiệm kiểm soát]] — Policy context ở 23419 là ví dụ học về identity/authorization, không gộp hai thuật ngữ. Control phục vụ quản trị hoặc giới hạn hậu quả; không chứng minh đã remediate runtime. **INTERPRETATION / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-845029643C22D44B870203EC\|CVE:CVE-2025-23419: case_source_scope]] — "CNA F5 mô tả tác động liên quan yêu cầu client-certificate authentication trong TLS session resumption; record phân loại CWE-863. Không công bố trong corpus này review mã nguồn độ… (mở Claim để đọc đủ) | CVE Program / CNA: F5 | CURRENT | SUPPORTED / AI_REVIEWED | /containers/cna/descriptions/0/value; /containers/cna/problemTypes/0/descriptions/0 — [[EVIDENCE-0B8DF862203E286BC8CA69B0\|case: /containers/cna/descriptions/0/value; /containers/cna/problemTypes/0/descriptions/0]] |
| [[CLAIM-8D23AFE0D3FDEADF28990AAA\|CVE:CVE-2025-23419: v1.3:impact]] — "Yêu cầu xác thực client certificate có thể bị bỏ qua theo CNA." | CNA F5 / CVE Program | CURRENT | SUPPORTED / AI_REVIEWED | /containers/cna/descriptions/0/value — [[EVIDENCE-1982F926ED09EC13B93A0EAB\|CVE-2025-23419.json: /containers/cna/descriptions/0/value]] |




## Phạm vi kiểm chứng

[[EVIDENCE-0B8DF862203E286BC8CA69B0|case: /containers/cna/descriptions/0/value; /containers/cna/problemTypes/0/descriptions/0]], [[EVIDENCE-1982F926ED09EC13B93A0EAB|CVE-2025-23419.json: /containers/cna/descriptions/0/value]]

Source-confirmed impact description; AI interpretation of category, human review pending.

Not an asset-level observation; source scope only.

[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

