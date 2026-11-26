---
entity_type: affectedcondition
id: CONDITION:1770D9D4BD8DA06265DDF330
title: Điều kiện được công bố — CVE-2025-23419
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2025-23419
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2025-23419

When multiple server blocks are configured to share the same IP address and port, an attacker can use session resumption to bypass client certificate authentication requirements on these servers. This vulnerability arises when  TLS Session Tickets https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_session_ticket_key  are used and/or the  SSL session cache https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_session_cache  are used in the default server and the default server is performing client certificate authentication.  

Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-925298B1835027A9E5CD9329\|CVE:CVE-2025-23419: vendor_documented_conditions]] — "When multiple server blocks are configured to share the same IP address and port, an attacker can use session resumption to bypass client certificate authentication requirements o… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AF1B942825307CEF770EBBF0: /containers/cna/descriptions — [[EVIDENCE-AF1B942825307CEF770EBBF0\|CVE-2025-23419]] |




## Nguồn

[[EVIDENCE-AF1B942825307CEF770EBBF0|CVE-2025-23419]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
