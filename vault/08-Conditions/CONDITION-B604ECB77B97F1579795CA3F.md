---
entity_type: affectedcondition
id: CONDITION:B604ECB77B97F1579795CA3F
title: Điều kiện được công bố — CVE-2026-42934
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-42934
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-42934

NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_charset_module module. When charset, source_charset, and charset_map and proxy_pass with disabled buffering ("off") directives are configured, unauthenticated attackers can send requests that with conditions beyond the attackers' control to cause a heap buffer over-read in the NGINX worker process, leading to limited disclosure of memory or a restart.



 Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-DBDEFE41D355AFFC83500B10\|CVE:CVE-2026-42934: vendor_documented_conditions]] — "NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_charset_module module. When charset, source_charset, and charset_map and proxy_pass with disabled buffering (… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AB6E40B85C793808DE349809: /containers/cna/descriptions — [[EVIDENCE-AB6E40B85C793808DE349809\|CVE-2026-42934]] |




## Nguồn

[[EVIDENCE-AB6E40B85C793808DE349809|CVE-2026-42934]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
