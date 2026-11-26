---
entity_type: affectedcondition
id: CONDITION:B2A10EEE71B7439239E31E5A
title: Điều kiện được công bố — CVE-2026-42926
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-42926
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-42926

When NGINX Open Source is configured to proxy HTTP/2 traffic by setting proxy_http_version to 2, and also uses proxy_set_body, an attacker may be able to inject frame headers and payload bytes to the upstream peer.  Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-DBB7983899F89C70F5642272\|CVE:CVE-2026-42926: vendor_documented_conditions]] — "When NGINX Open Source is configured to proxy HTTP/2 traffic by setting proxy_http_version to 2, and also uses proxy_set_body, an attacker may be able to inject frame headers and … (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:55DCAE249330189B1FE59BE1: /containers/cna/descriptions — [[EVIDENCE-55DCAE249330189B1FE59BE1\|CVE-2026-42926]] |




## Nguồn

[[EVIDENCE-55DCAE249330189B1FE59BE1|CVE-2026-42926]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
