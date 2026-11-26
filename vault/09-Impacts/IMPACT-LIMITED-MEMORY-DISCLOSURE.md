---
entity_type: impact
id: IMPACT:LIMITED-MEMORY-DISCLOSURE
title: Tiết lộ bộ nhớ giới hạn
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Tiết lộ bộ nhớ giới hạn
tags:
- nginx
- impact
- knowledge
---

# Tiết lộ bộ nhớ giới hạn

Nguồn 48142 nêu limited disclosure; chưa xác định loại dữ liệu. Quyền thấp giảm phạm vi tiếp cận, không sửa over-read.




## Định nghĩa

Nguồn 48142 nêu limited disclosure; chưa xác định loại dữ liệu. Quyền thấp giảm phạm vi tiếp cận, không sửa over-read.





## Liên hệ và bước tiếp theo

[[MODULE-NGX-HTTP-CHARSET-MODULE|Charset filter — chuyển mã trên các buffer]], [[WEAKNESS-CWE-125|CWE-125 — Out-of-bounds read]], [[CONTROL-LEAST-PRIVILEGE|Security invariants và trách nhiệm kiểm soát]]

## Quan hệ có định kiểu

- `CONTEXTUAL_ASSOCIATION` → [[CONTROL-LEAST-PRIVILEGE|Security invariants và trách nhiệm kiểm soát]] — Nguồn 48142 nêu limited disclosure; chưa xác định loại dữ liệu. Quyền thấp giảm phạm vi tiếp cận, không sửa over-read. Control phục vụ quản trị hoặc giới hạn hậu quả; không chứng minh đã remediate runtime. **INTERPRETATION / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-1F1AD10346013DFE5FC4AF7B\|CVE:CVE-2026-48142: v1.3:impact]] — "Limited disclosure của bộ nhớ hoặc worker restart được CNA nêu." | CNA F5 / CVE Program | CURRENT | SUPPORTED / AI_REVIEWED | /containers/cna/descriptions/0/value — [[EVIDENCE-664AF4C9941A1A284D028AE8\|CVE-2026-48142.json: /containers/cna/descriptions/0/value]] |




## Phạm vi kiểm chứng

[[EVIDENCE-664AF4C9941A1A284D028AE8|CVE-2026-48142.json: /containers/cna/descriptions/0/value]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.

Not an asset-level observation; source scope only.

[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

