---
entity_type: affectedcondition
id: CONDITION:A5678AC816B8CD260B06524E
title: Điều kiện được công bố — CVE-2026-90439
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-90439
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-90439

NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_v3_module module. When using HTTP/3 with OpenSSL versions <= OpenSSL 3.5.0 under certain configurations, a limited heap buffer overflow could happen while processing a TLS handshake. This can happen in a non-deterministic manner that is beyond the attacker's control. This may cause a heap buffer overflow in the NGINX worker process leading to a restart and/or limited data corruption.

Impact:
This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or limited data corruption. There is no control plane exposure; this is a data plane issue only.




Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-289726F6C70FA81F15F5EBAC\|CVE:CVE-2026-90439: vendor_documented_conditions]] — "NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_v3_module module. When using HTTP/3 with OpenSSL versions <= OpenSSL 3.5.0 under certain configurations, a li… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2C3479DA69C20FDBA07AC92B: /containers/cna/descriptions — [[EVIDENCE-2C3479DA69C20FDBA07AC92B\|CVE-2026-90439]] |




## Nguồn

[[EVIDENCE-2C3479DA69C20FDBA07AC92B|CVE-2026-90439]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
