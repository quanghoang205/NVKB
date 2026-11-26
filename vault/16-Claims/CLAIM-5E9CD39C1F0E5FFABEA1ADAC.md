---
entity_type: claim
id: CLAIM:5E9CD39C1F0E5FFABEA1ADAC
title: 'CONTROL:LEAST-PRIVILEGE: pilot_section:Điều khiển và giới hạn'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CONTROL:LEAST-PRIVILEGE: pilot_section:Điều khiển và giới hạn'
tags:
- nginx
- claim
- provenance
---

# CONTROL:LEAST-PRIVILEGE: pilot_section:Điều khiển và giới hạn

`CLAIM:5E9CD39C1F0E5FFABEA1ADAC` · **CURRENT**

## Nhận định

Chủ thể: [[CONTROL-LEAST-PRIVILEGE|Security invariants và trách nhiệm kiểm soát]]. Predicate: `pilot_section:Điều khiển và giới hạn`.

```json
"## Điều khiển và giới hạn\n\nPolicy ở server side tránh phụ thuộc đơn thuần vào trạng thái do client tự khai báo. Tách quyền của tiến trình và hạn chế tài nguyên có thể giảm hậu quả, nhưng không thay cập nhật bản vá hay sửa logic. Một worker chạy quyền hạn chế vẫn có thể truy cập dữ liệu mà ứng dụng đã cho phép nó đọc; ranh giới OS không giải quyết tự động quyền giữa khách hàng.\n\n"
```

## Nguồn và phạm vi

Authority: NVKB AI curation. 

[[EVIDENCE-7A43D63D03C50227DF951CF8|cwe863: #Potential_Mitigations]]

Locator: #Potential_Mitigations

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

Reviewer: `nvkb-v1.2-ai-curator` · 2026-11-25T04:21:08+00:00

Read cwe863 at #Potential_Mitigations; compared the statement with the documented mechanism. Mechanism is grounded in the cited section; examples, tradeoffs, invariant and assessment are authored interpretation, not vendor-confirmed facts. Human expert review pending.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

Included in the current authored pilot; AI review is separate from temporal status.

Quan sát: 2026-11-25T04:21:08+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
