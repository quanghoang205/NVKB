---
entity_type: claim
id: CLAIM:98DC4F5447FA6EF9A4CA7BC6
title: 'CVE:CVE-2025-23419: description'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2025-23419: description'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2025-23419: description

`CLAIM:98DC4F5447FA6EF9A4CA7BC6` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2025-23419|CVE-2025-23419]]. Predicate: `description`.

```json
"When multiple server blocks are configured to share the same IP address and port, an attacker can use session resumption to bypass client certificate authentication requirements on these servers. This vulnerability arises when  TLS Session Tickets https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_session_ticket_key  are used and/or the  SSL session cache https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_session_cache  are used in the default server and the default server is performing client certificate authentication.  \n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-AF1B942825307CEF770EBBF0|CVE-2025-23419]]

Locator: EVIDENCE:AF1B942825307CEF770EBBF0: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:21:55+00:00. Truy xuất: 2026-11-25T02:21:55+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
