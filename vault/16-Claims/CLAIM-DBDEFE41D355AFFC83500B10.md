---
entity_type: claim
id: CLAIM:DBDEFE41D355AFFC83500B10
title: 'CVE:CVE-2026-42934: vendor_documented_conditions'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-42934: vendor_documented_conditions'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-42934: vendor_documented_conditions

`CLAIM:DBDEFE41D355AFFC83500B10` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-42934|CVE-2026-42934]]. Predicate: `vendor_documented_conditions`.

```json
"NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_charset_module module. When charset, source_charset, and charset_map and proxy_pass with disabled buffering (\"off\") directives are configured, unauthenticated attackers can send requests that with conditions beyond the attackers' control to cause a heap buffer over-read in the NGINX worker process, leading to limited disclosure of memory or a restart.\n\n\n\n Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-AB6E40B85C793808DE349809|CVE-2026-42934]]

Locator: EVIDENCE:AB6E40B85C793808DE349809: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:28:14+00:00. Truy xuất: 2026-11-25T02:28:11+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
