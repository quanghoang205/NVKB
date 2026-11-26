---
entity_type: claim
id: CLAIM:77D6D61E63E1D30E731EDB2F
title: 'CVE:CVE-2026-42934: v1.3:applicability'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-42934: v1.3:applicability'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-42934: v1.3:applicability

`CLAIM:77D6D61E63E1D30E731EDB2F` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-42934|CVE-2026-42934]]. Predicate: `v1.3:applicability`.

```json
"charset, source_charset, charset_map và proxy_pass với buffering off được CNA nêu; có điều kiện ngoài kiểm soát tác nhân."
```

## Nguồn và phạm vi

Authority: CNA F5 / CVE Program. 

[[EVIDENCE-C5FCC8D4BF4A615B0AA8C3BE|CVE-2026-42934.json: /containers/cna/descriptions/0/value]]

Locator: /containers/cna/descriptions/0/value

Phạm vi phiên bản: Document snapshot 2026-11-25T02:28:11+00:00; CVE versions are scoped separately.

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

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:24:25+00:00

Read the cited snapshot section and compared the authored bounded statement. Support is limited to the named product, conditions and documented impact; no independent root-cause verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

New source observation; source support is separate.

Quan sát: 2026-11-25T05:24:25+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
