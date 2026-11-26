---
entity_type: affectedcondition
id: CONDITION:F6F93544F7DC84AC8A52182C
title: Điều kiện được công bố — CVE-2024-31079
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2024-31079
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2024-31079

When NGINX Plus or NGINX OSS are configured to use the HTTP/3 QUIC module, undisclosed HTTP/3 requests can cause NGINX worker processes to terminate or cause other potential impact. This attack requires that a request be specifically timed during the connection draining process, which the attacker has no visibility and limited influence over.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-B951285F44C4C9C48496E1F0\|CVE:CVE-2024-31079: vendor_documented_conditions]] — "When NGINX Plus or NGINX OSS are configured to use the HTTP/3 QUIC module, undisclosed HTTP/3 requests can cause NGINX worker processes to terminate or cause other potential impac… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:4B3FF00AD62E27AE79FF8311: /containers/cna/descriptions — [[EVIDENCE-4B3FF00AD62E27AE79FF8311\|CVE-2024-31079]] |




## Nguồn

[[EVIDENCE-4B3FF00AD62E27AE79FF8311|CVE-2024-31079]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
