---
entity_type: claim
id: CLAIM:3BFD75B5D03E813DB051C1DB
title: 'CVE:CVE-2026-42055: v1.3:applicability'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-42055: v1.3:applicability'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-42055: v1.3:applicability

`CLAIM:3BFD75B5D03E813DB051C1DB` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-42055|CVE-2026-42055]]. Predicate: `v1.3:applicability`.

```json
"Proxy HTTP/2 hoặc gRPC, ignore_invalid_headers off và large_client_header_buffers lớn hơn 2 MB theo CNA; còn điều kiện ngoài kiểm soát tác nhân."
```

## Nguồn và phạm vi

Authority: CNA F5 / CVE Program. 

[[EVIDENCE-BF9ACFFDE37E8BFCD2CFC053|CVE-2026-42055.json: /containers/cna/descriptions/0/value]]

Locator: /containers/cna/descriptions/0/value

Phạm vi phiên bản: Document snapshot 2026-11-25T02:27:56+00:00; CVE versions are scoped separately.

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

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:28:19+00:00

Read the cited snapshot section and compared the authored bounded statement. Support is limited to the named product, conditions and documented impact; no independent root-cause verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

New source observation; source support is separate.

Quan sát: 2026-11-25T05:28:19+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
