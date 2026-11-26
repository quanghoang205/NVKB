---
entity_type: claim
id: CLAIM:EF7992CF2DC6A2CF77E3D846
title: 'CONTROL:PATCH-VERIFICATION: pilot_source_statement'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CONTROL:PATCH-VERIFICATION: pilot_source_statement'
tags:
- nginx
- claim
- provenance
---

# CONTROL:PATCH-VERIFICATION: pilot_source_statement

`CLAIM:EF7992CF2DC6A2CF77E3D846` · **CURRENT**

## Nhận định

Chủ thể: [[CONTROL-PATCH-VERIFICATION|Xác minh bản vá từ inventory và bằng chứng triển khai]]. Predicate: `pilot_source_statement`.

```json
"Bản sửa upstream do NGINX công bố cho CVE-2025-23419 là 1.26.3 và 1.27.4 theo nhánh."
```

## Nguồn và phạm vi

Authority: NGINX / F5. 

[[EVIDENCE-E19E68B2E196A0C50233787A|NGINX security advisories]]

Locator: li containing CVE-2025-23419

Phạm vi phiên bản: Official document snapshot retrieved 2026-11-25T04:12:10+00:00; deployment version not established

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

Reviewer: `nvkb-v1.2-ai-curator` · 2026-11-25T04:21:14+00:00

Read advisories at li containing CVE-2025-23419; compared the statement with the documented mechanism. Supports the bounded source statement; no independent implementation or human verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

Included in the current authored pilot; AI review is separate from temporal status.

Quan sát: 2026-11-25T04:21:14+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
