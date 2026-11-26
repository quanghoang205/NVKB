---
entity_type: affectedcondition
id: CONDITION:7EDD2DC25184D325B60F9301
title: Điều kiện được công bố — CVE-2026-32647
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-32647
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-32647

NGINX Open Source and NGINX Plus have a vulnerability in the ngx_http_mp4_module module, which might allow an attacker to trigger a buffer over-read or over-write to the NGINX worker memory resulting in its termination or possibly code execution, using a specially crafted MP4 file. This issue affects NGINX Open Source and NGINX Plus if it is built with the ngx_http_mp4_module module and the mp4 directive is used in the configuration file. Additionally, the attack is possible only if an attacker can trigger the processing of a specially crafted MP4 file with the ngx_http_mp4_module module. 


Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-C7BDD334107387E36997B4E8\|CVE:CVE-2026-32647: vendor_documented_conditions]] — "NGINX Open Source and NGINX Plus have a vulnerability in the ngx_http_mp4_module module, which might allow an attacker to trigger a buffer over-read or over-write to the NGINX wor… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:ED5DE28FAC8FF32E7DA3A310: /containers/cna/descriptions — [[EVIDENCE-ED5DE28FAC8FF32E7DA3A310\|CVE-2026-32647]] |




## Nguồn

[[EVIDENCE-ED5DE28FAC8FF32E7DA3A310|CVE-2026-32647]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
