---
entity_type: claim
id: CLAIM:C33206CCAD749D5BCBB66D25
title: 'CVE:CVE-2024-32760: v1.3:applicability'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2024-32760: v1.3:applicability'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2024-32760: v1.3:applicability

`CLAIM:C33206CCAD749D5BCBB66D25` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2024-32760|CVE-2024-32760]]. Predicate: `v1.3:applicability`.

```json
"NGINX sử dụng HTTP/3 QUIC; announcement yêu cầu build module và listener quic."
```

## Nguồn và phạm vi

Authority: CNA F5 / CVE Program. 

[[EVIDENCE-7E7E46950AC8899989EA5ACB|Official NGINX announcement]], [[EVIDENCE-E21D878695933F48541A305B|CVE-2024-32760.json: /containers/cna/descriptions/0/value]]

Locator: /containers/cna/descriptions/0/value

Phạm vi phiên bản: Document snapshot 2026-11-25T02:26:16+00:00; CVE versions are scoped separately.

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

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:31:55+00:00

Read the cited snapshot section and compared the authored bounded statement. Support is limited to the named product, conditions and documented impact; no independent root-cause verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

New source observation; source support is separate.

Quan sát: 2026-11-25T05:31:55+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
