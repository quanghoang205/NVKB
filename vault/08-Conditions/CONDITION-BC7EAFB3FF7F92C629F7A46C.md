---
entity_type: affectedcondition
id: CONDITION:BC7EAFB3FF7F92C629F7A46C
title: Điều kiện được công bố — CVE-2026-42530
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-42530
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-42530

NGINX Open Source has a vulnerability in the ngx_http_v3_module module. When NGINX Open Source is configured to use the HTTP/3 QUIC module, a remote unauthenticated attacker along with conditions beyond their control can use a specially crafted HTTP/3 session to reopen a QPACK encoder stream. This may cause a Use-after-Free in the NGINX worker process leading to a restart. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.  


Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-B79FCA2945E919243A939FB0\|CVE:CVE-2026-42530: vendor_documented_conditions]] — "NGINX Open Source has a vulnerability in the ngx_http_v3_module module. When NGINX Open Source is configured to use the HTTP/3 QUIC module, a remote unauthenticated attacker along… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:898F2A102B93CD30807B88FB: /containers/cna/descriptions — [[EVIDENCE-898F2A102B93CD30807B88FB\|CVE-2026-42530]] |




## Nguồn

[[EVIDENCE-898F2A102B93CD30807B88FB|CVE-2026-42530]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
