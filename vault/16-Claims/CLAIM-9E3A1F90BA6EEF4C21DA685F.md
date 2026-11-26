---
entity_type: claim
id: CLAIM:9E3A1F90BA6EEF4C21DA685F
title: 'CVE:CVE-2026-28755: vendor_documented_conditions'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-28755: vendor_documented_conditions'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-28755: vendor_documented_conditions

`CLAIM:9E3A1F90BA6EEF4C21DA685F` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-28755|CVE-2026-28755]]. Predicate: `vendor_documented_conditions`.

```json
"NGINX Plus and NGINX Open Source have a vulnerability in the ngx_stream_ssl_module module due to the improper handling of revoked certificates when configured with the ssl_verify_client on and ssl_ocsp on directives, allowing the TLS handshake to succeed even after an OCSP check identifies the certificate as revoked.   \n\n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-F7FF2FC88326C4B1BA396C64|CVE-2026-28755]]

Locator: EVIDENCE:F7FF2FC88326C4B1BA396C64: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:27:44+00:00. Truy xuất: 2026-11-25T02:27:41+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
