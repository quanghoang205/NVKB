---
entity_type: claim
id: CLAIM:762AD8E58CD989EB1B6A88AE
title: 'CVE:CVE-2024-24989: vendor_advisory_statement'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2024-24989: vendor_advisory_statement'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2024-24989: vendor_advisory_statement

`CLAIM:762AD8E58CD989EB1B6A88AE` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2024-24989|CVE-2024-24989]]. Predicate: `vendor_advisory_statement`.

```json
"Two security issues were identified in nginx HTTP/3 implementation,\nwhich might allow an attacker that uses a specially crafted QUIC session\nto cause a worker process crash (CVE-2024-24989, CVE-2024-24990) or\nmight have potential other impact (CVE-2024-24990).\n\nThe issues affect nginx compiled with the ngx_http_v3_module (not\ncompiled by default) if the \"quic\" option of the \"listen\" directive\nis used in a configuration file.\n\nThe issue affects nginx 1.25.0 - 1.25.3.\nThe issue is fixed in nginx 1.25.4.\n\n\n-- \nSergey Kandaurov"
```

## Nguồn và phạm vi

Authority: NGINX / F5. NGINX / F5

[[EVIDENCE-0BF4E4CC924225F0C7F5F039|[nginx-announce] nginx security advisory (CVE-2024-24989, CVE-2024-24990)]]

Locator: EVIDENCE:0BF4E4CC924225F0C7F5F039: advisory body

Phạm vi phiên bản: Legacy scope: consult evidence; not established for all releases

## Kiểm chứng độc lập

| Chiều kiểm chứng | Kết quả |
| --- | --- |
| Reference | AVAILABLE |
| Hash nguồn | HASH_MATCH |
| Trích xuất | NOT_CHECKED |
| Nguồn hỗ trợ | NOT_REVIEWED |
| Review | NOT_REVIEWED |
| Loại suy luận | SOURCE_STATEMENT |
| Legacy | VERIFIED — nhãn pipeline cũ |


Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

Referenced in current read model; not a factual accuracy decision.

Quan sát: 2026-11-25T02:40:15+00:00. Truy xuất: 2026-11-25T02:26:07+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
