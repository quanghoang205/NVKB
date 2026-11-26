---
entity_type: affectedcondition
id: CONDITION:B7E8704DAA3B778DAEB6E764
title: Điều kiện được công bố — CVE-2026-42946
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-42946
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-42946

A vulnerability exists in the ngx_http_scgi_module and ngx_http_uwsgi_module modules that may result in excessive memory allocation or an over-read of data. When scgi_pass or uwsgi_pass is configured, an unauthenticated attacker with man-in-the-middle (MITM) ability to control responses from an upstream server may be able to read the memory of the NGINX worker process or restart it.  Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-B70A286503EE51504FCB4811\|CVE:CVE-2026-42946: vendor_documented_conditions]] — "A vulnerability exists in the ngx_http_scgi_module and ngx_http_uwsgi_module modules that may result in excessive memory allocation or an over-read of data. When scgi_pass or uwsg… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:3EFC2338173D38F29F1B5E2F: /containers/cna/descriptions — [[EVIDENCE-3EFC2338173D38F29F1B5E2F\|CVE-2026-42946]] |




## Nguồn

[[EVIDENCE-3EFC2338173D38F29F1B5E2F|CVE-2026-42946]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
