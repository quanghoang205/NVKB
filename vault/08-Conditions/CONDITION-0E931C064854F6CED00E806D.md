---
entity_type: affectedcondition
id: CONDITION:0E931C064854F6CED00E806D
title: Điều kiện được công bố — CVE-2026-95101
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-95101
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-95101

Description
NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_v3_module module. When using HTTP/3 with 

proxy_request_buffering on directive, an unauthenticated attacker may be able to inject data in the proxied request.

Impact


This vulnerability may allow remote attackers to 

inject data in the proxied request.  There is no control plane exposure; this is a data plane issue only.






Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-E4D7DB96114C7592E3827033\|CVE:CVE-2026-95101: vendor_documented_conditions]] — "Description\nNGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_v3_module module. When using HTTP/3 with \n\nproxy_request_buffering on directive, an unauthenti… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A59E329248E28B36814C7E0F: /containers/cna/descriptions — [[EVIDENCE-A59E329248E28B36814C7E0F\|CVE-2026-95101]] |




## Nguồn

[[EVIDENCE-A59E329248E28B36814C7E0F|CVE-2026-95101]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
