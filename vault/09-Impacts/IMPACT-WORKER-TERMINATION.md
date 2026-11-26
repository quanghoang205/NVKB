---
entity_type: impact
id: IMPACT:WORKER-TERMINATION
title: Worker termination trong phạm vi process
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Worker termination trong phạm vi process
tags:
- nginx
- impact
- knowledge
---

# Worker termination trong phạm vi process

Nguồn 7347 nêu worker kết thúc; không mở rộng thành host/root compromise.




## Định nghĩa

Nguồn 7347 nêu worker kết thúc; không mở rộng thành host/root compromise.





## Liên hệ và bước tiếp theo

[[MODULE-NGX-HTTP-MP4-MODULE|MP4 pseudo-streaming và ranh giới metadata]], [[WEAKNESS-CWE-125|CWE-125 — Out-of-bounds read]], [[CONTROL-PATCH-VERIFICATION|Xác minh bản vá từ inventory và bằng chứng triển khai]]

## Quan hệ có định kiểu

- `CONTEXTUAL_ASSOCIATION` → [[CONTROL-PATCH-VERIFICATION|Xác minh bản vá từ inventory và bằng chứng triển khai]] — Nguồn 7347 nêu worker kết thúc; không mở rộng thành host/root compromise. Control phục vụ quản trị hoặc giới hạn hậu quả; không chứng minh đã remediate runtime. **INTERPRETATION / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-BE7C8F9998324B4A0E258D23\|CVE:CVE-2024-7347: v1.3:impact]] — "CNA xác nhận khả năng over-read bộ nhớ worker và làm worker kết thúc. Không có xác nhận rằng bộ nhớ đó được gửi ra client." | CNA F5 / CVE Program | CURRENT | SUPPORTED / AI_REVIEWED | /containers/cna/descriptions/0/value — [[EVIDENCE-DD31363C4E8C1F210DB23B4E\|CVE-2024-7347.json: /containers/cna/descriptions/0/value]] |




## Phạm vi kiểm chứng

[[EVIDENCE-DD31363C4E8C1F210DB23B4E|CVE-2024-7347.json: /containers/cna/descriptions/0/value]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.

Not an asset-level observation; source scope only.

[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

