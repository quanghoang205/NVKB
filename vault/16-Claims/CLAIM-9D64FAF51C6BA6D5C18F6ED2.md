---
entity_type: claim
id: CLAIM:9D64FAF51C6BA6D5C18F6ED2
title: 'CONCEPT:BACKPORT: pilot_source_statement'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CONCEPT:BACKPORT: pilot_source_statement'
tags:
- nginx
- claim
- provenance
---

# CONCEPT:BACKPORT: pilot_source_statement

`CLAIM:9D64FAF51C6BA6D5C18F6ED2` · **CURRENT**

## Nhận định

Chủ thể: [[CONCEPT-BACKPORT|Upstream version và distribution backport]]. Predicate: `pilot_source_statement`.

```json
"Debian tracker ghi fixed source-package version của nginx cho bookworm là 1.22.1-9+deb12u1 đối với CVE-2025-23419."
```

## Nguồn và phạm vi

Authority: Debian Security Team. 

[[EVIDENCE-80187DCEBADB8A87EBAC7B6E|CVE-2025-23419]]

Locator: table Fixed Version; package=nginx; release=bookworm

Phạm vi phiên bản: Official document snapshot retrieved 2026-11-25T04:12:54+00:00; deployment version not established

## Kiểm chứng độc lập

| Chiều kiểm chứng | Kết quả |
| --- | --- |
| Reference | AVAILABLE |
| Hash nguồn | HASH_MATCH |
| Trích xuất | NOT_CHECKED |
| Nguồn hỗ trợ | SUPPORTED |
| Review | AI_REVIEWED |
| Loại suy luận | SOURCE_STATEMENT |
| Legacy | UNVERIFIED — nhãn pipeline cũ |

Reviewer: `nvkb-v1.2-ai-curator` · 2026-11-25T04:21:11+00:00

Read debian at table Fixed Version; package=nginx; release=bookworm; compared the statement with the documented mechanism. Supports the bounded source statement; no independent implementation or human verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

Included in the current authored pilot; AI review is separate from temporal status.

Quan sát: 2026-11-25T04:21:11+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
