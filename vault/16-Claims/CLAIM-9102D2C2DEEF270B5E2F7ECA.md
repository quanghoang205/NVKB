---
entity_type: claim
id: CLAIM:9102D2C2DEEF270B5E2F7ECA
title: 'CVE:CVE-2025-23419: v1.3:applicability'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2025-23419: v1.3:applicability'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2025-23419: v1.3:applicability

`CLAIM:9102D2C2DEEF270B5E2F7ECA` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2025-23419|CVE-2025-23419]]. Predicate: `v1.3:applicability`.

```json
"Nhiều server block cùng IP/port; default server có client-certificate authentication và session tickets và/hoặc cache. Announcement bổ sung OpenSSL, TLS 1.3 và resumption."
```

## Nguồn và phạm vi

Authority: CNA F5 / CVE Program. 

[[EVIDENCE-1982F926ED09EC13B93A0EAB|CVE-2025-23419.json: /containers/cna/descriptions/0/value]]

Locator: /containers/cna/descriptions/0/value

Phạm vi phiên bản: Document snapshot 2026-11-25T04:13:42+00:00; CVE versions are scoped separately.

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

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:15:05+00:00

Read the cited snapshot section and compared the authored bounded statement. Support is limited to the named product, conditions and documented impact; no independent root-cause verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

Previous research edition; retained unchanged statement with original support decision.

Quan sát: 2026-11-25T05:15:05+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
