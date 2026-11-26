---
entity_type: affectedcondition
id: CONDITION:4273934B0FFE79F2ED4AC09C
title: Điều kiện được công bố — CVE-2026-40701
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-40701
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-40701

NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_ssl_module module when the ssl_verify_client directive is set to "on" or "optional," and the ssl_ocsp directive is set to "on" or the leaf parameters are configured with a resolver. With this configuration, an unauthenticated attacker can send requests along with conditions beyond its control that may cause a heap-use-after-free error in the NGINX worker process. This vulnerability may result in limited modification of data or the NGINX worker process restarting.



 Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-1EF701037BEB53AD17CFFED7\|CVE:CVE-2026-40701: vendor_documented_conditions]] — "NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_ssl_module module when the ssl_verify_client directive is set to \"on\" or \"optional,\" and the ssl_ocsp dir… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:4AA885ADF0AAD59294FEEFE5: /containers/cna/descriptions — [[EVIDENCE-4AA885ADF0AAD59294FEEFE5\|CVE-2026-40701]] |




## Nguồn

[[EVIDENCE-4AA885ADF0AAD59294FEEFE5|CVE-2026-40701]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
