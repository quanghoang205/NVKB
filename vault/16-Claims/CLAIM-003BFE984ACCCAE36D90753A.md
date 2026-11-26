---
entity_type: claim
id: CLAIM:003BFE984ACCCAE36D90753A
title: 'WEAKNESS:CWE-863: pilot_section:Cơ chế quyết định quyền'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'WEAKNESS:CWE-863: pilot_section:Cơ chế quyết định quyền'
tags:
- nginx
- claim
- provenance
---

# WEAKNESS:CWE-863: pilot_section:Cơ chế quyết định quyền

`CLAIM:003BFE984ACCCAE36D90753A` · **CURRENT**

## Nhận định

Chủ thể: [[WEAKNESS-CWE-863|Incorrect Authorization]]. Predicate: `pilot_section:Cơ chế quyết định quyền`.

```json
"## Cơ chế quyết định quyền\n\nMô hình khái niệm: nhận subject/context → xác định resource và action → nạp policy áp dụng → kiểm tra điều kiện → cho phép hoặc từ chối. Một kiểm tra hiện diện nhưng bỏ qua một chiều cần thiết của policy có thể thuộc lớp Incorrect Authorization. Không có kiểm tra và kiểm tra sai là hai mô tả cần phân biệt; chỉ gán CWE cụ thể khi có bằng chứng thích hợp.\n\n"
```

## Nguồn và phạm vi

Authority: NVKB AI curation. 

[[EVIDENCE-3F3B7A9F2EE582122C10045B|cwe863: #Description; #Potential_Mitigations]]

Locator: #Description; #Potential_Mitigations

Phạm vi phiên bản: Official document snapshot retrieved 2026-11-25T04:10:42+00:00; deployment version not established

## Kiểm chứng độc lập

| Chiều kiểm chứng | Kết quả |
| --- | --- |
| Reference | AVAILABLE |
| Hash nguồn | HASH_MATCH |
| Trích xuất | NOT_CHECKED |
| Nguồn hỗ trợ | PARTIAL |
| Review | AI_REVIEWED |
| Loại suy luận | INTERPRETATION |
| Legacy | INFERRED — nhãn pipeline cũ |

Reviewer: `nvkb-v1.2-ai-curator` · 2026-11-25T04:21:04+00:00

Read cwe863 at #Description; #Potential_Mitigations; compared the statement with the documented mechanism. Mechanism is grounded in the cited section; examples, tradeoffs, invariant and assessment are authored interpretation, not vendor-confirmed facts. Human expert review pending.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

Included in the current authored pilot; AI review is separate from temporal status.

Quan sát: 2026-11-25T04:21:03+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
