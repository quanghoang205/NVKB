---
entity_type: claim
id: CLAIM:6CD26CD56BB6E15833ED7C6D
title: 'CVE:CVE-2024-31079: v1.3:applicability'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2024-31079: v1.3:applicability'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2024-31079: v1.3:applicability

`CLAIM:6CD26CD56BB6E15833ED7C6D` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2024-31079|CVE-2024-31079]]. Predicate: `v1.3:applicability`.

```json
"HTTP/3 QUIC module được sử dụng; CNA còn nêu điều kiện thời gian trong draining nằm ngoài khả năng quan sát và chịu ảnh hưởng hạn chế của tác nhân."
```

## Nguồn và phạm vi

Authority: CNA F5 / CVE Program. 

[[EVIDENCE-23FEC271923D72AB95F66E42|CVE-2024-31079.json: /containers/cna/descriptions/0/value]], [[EVIDENCE-5898F37D2E2632B90CE3B73D|Official NGINX announcement]]

Locator: /containers/cna/descriptions/0/value

Phạm vi phiên bản: Document snapshot 2026-11-25T02:26:12+00:00; CVE versions are scoped separately.

## Kiểm chứng độc lập

| Chiều kiểm chứng | Kết quả |
| --- | --- |
| Reference | AVAILABLE |
| Hash nguồn | HASH_MATCH |
| Trích xuất | MATCHED |
| Nguồn hỗ trợ | SUPPORTED |
| Review | AI_REVIEWED |
| Loại suy luận | SOURCE_STATEMENT |
| Legacy | UNVERIFIED — nhãn pipeline cũ |

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:31:53+00:00

Read the cited snapshot section and compared the authored bounded statement. Support is limited to the named product, conditions and documented impact; no independent root-cause verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

New source observation; source support is separate.

Quan sát: 2026-11-25T05:31:53+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
