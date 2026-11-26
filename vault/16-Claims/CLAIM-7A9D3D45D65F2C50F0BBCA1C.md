---
entity_type: claim
id: CLAIM:7A9D3D45D65F2C50F0BBCA1C
title: 'CVE:CVE-2024-35200: vendor_advisory_statement'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2024-35200: vendor_advisory_statement'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2024-35200: vendor_advisory_statement

`CLAIM:7A9D3D45D65F2C50F0BBCA1C` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2024-35200|CVE-2024-35200]]. Predicate: `vendor_advisory_statement`.

```json
"Hello!\n\nFour security issues were identified in nginx HTTP/3 implementation, which\nmight allow an attacker that uses a specially crafted QUIC session to cause\na worker process crash (CVE-2024-31079, CVE-2024-32760, CVE-2024-35200),\nworker process memory disclosure on systems with MTU larger than 4096\nbytes (CVE-2024-34161), or might have potential other impact (CVE-2024-31079,\nCVE-2024-32760).\n\nThe issues affect nginx compiled with the experimental ngx_http_v3_module\n(not compiled by default) if the \"quic\" option of the \"listen\" directive\nis used in a configuration file.\n\nThe issues affect nginx 1.25.0-1.25.5, 1.26.0.\nThe issues are fixed in nginx 1.27.0, 1.26.1.\n\nThanks to Nils Bars of CISPA.\n\n\n-- \nSergey Kandaurov"
```

## Nguồn và phạm vi

Authority: NGINX / F5. NGINX / F5

[[EVIDENCE-ADE803DD55AF1C4D6A59D83F|[nginx-announce] nginx security advisory (CVE-2024-31079, CVE-2024-32760, CVE-2024-34161, CVE-2024-35200)]]

Locator: EVIDENCE:ADE803DD55AF1C4D6A59D83F: advisory body

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

Quan sát: 2026-11-25T02:40:19+00:00. Truy xuất: 2026-11-25T02:26:15+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
