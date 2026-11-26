---
entity_type: claim
id: CLAIM:9AFAD0A2732228FDF13BB4F7
title: 'CVE:CVE-2026-48142: vendor_documented_conditions'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-48142: vendor_documented_conditions'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-48142: vendor_documented_conditions

`CLAIM:9AFAD0A2732228FDF13BB4F7` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-48142|CVE-2026-48142]]. Predicate: `vendor_documented_conditions`.

```json
"NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_charset_module module. When content is served or proxied through a location block with both source_charset utf-8; and a charset directive (for example, charset koi8-r;) configured, remote, unauthenticated attackers can send requests (in conjunction with conditions beyond their control) to cause a heap buffer over-read in the NGINX worker process, leading to limited disclosure of memory or a restart. \n\n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-CEA79C61B0BD293CD87C74F5|CVE-2026-48142]]

Locator: EVIDENCE:CEA79C61B0BD293CD87C74F5: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:28:26+00:00. Truy xuất: 2026-11-25T02:28:24+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
