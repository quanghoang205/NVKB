---
entity_type: claim
id: CLAIM:2A9BBAC05A678D9EB8496D1E
title: 'CVE:CVE-2026-118899: v1.3:applicability'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-118899: v1.3:applicability'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-118899: v1.3:applicability

`CLAIM:2A9BBAC05A678D9EB8496D1E` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-118899|CVE-2026-118899]]. Predicate: `v1.3:applicability`.

```json
"HTTP listener bật ssl và TLS 1.3 theo CNA; không gán lỗi cho mọi stream TLS hoặc mọi phiên bản giao thức."
```

## Nguồn và phạm vi

Authority: CNA F5 / CVE Program. 

[[EVIDENCE-77FD57EAEDF8E5D26DB3E0AC|CVE-2026-118899.json: /containers/cna/descriptions/0/value]]

Locator: /containers/cna/descriptions/0/value

Phạm vi phiên bản: Document snapshot 2026-11-25T02:26:39+00:00; CVE versions are scoped separately.

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

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:15:12+00:00

Read the cited snapshot section and compared the authored bounded statement. Support is limited to the named product, conditions and documented impact; no independent root-cause verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

New source observation; source support is separate.

Quan sát: 2026-11-25T05:15:12+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
