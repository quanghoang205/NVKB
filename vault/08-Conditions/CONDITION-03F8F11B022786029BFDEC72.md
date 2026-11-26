---
entity_type: affectedcondition
id: CONDITION:03F8F11B022786029BFDEC72
title: Điều kiện được công bố — CVE-2026-123640
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-123640
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-123640

Description
When NGINX Plus or NGINX Open Source is configured with the ngx_stream_ssl_preread_module module, a specially crafted ClientHello message from an unauthenticated attacker causes forged values of the ngx_stream_ssl_preread_module variables, affecting virtual server selection. In addition, it may also cause a disagreement with a proxied server terminating the SSL/TLS connection without Transport Layer Security (TLS) 1.3 support.

Impact
This vulnerability may allow an attacker to forge values of the ngx_stream_ssl_preread_module variables and bypass the NGINX systems stream routing segmentation. As a result, the attacker may be able to route the connection to a privileged or internal backend that should be unreachable and gain access to sensitive information. There is no control plane exposure; this is a data plane issue only.






Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-2B804F91E67D105D319FD9CC\|CVE:CVE-2026-123640: vendor_documented_conditions]] — "Description\nWhen NGINX Plus or NGINX Open Source is configured with the ngx_stream_ssl_preread_module module, a specially crafted ClientHello message from an unauthenticated atta… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:3F321A701805CF3F6CD8D45D: /containers/cna/descriptions — [[EVIDENCE-3F321A701805CF3F6CD8D45D\|CVE-2026-123640]] |




## Nguồn

[[EVIDENCE-3F321A701805CF3F6CD8D45D|CVE-2026-123640]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
