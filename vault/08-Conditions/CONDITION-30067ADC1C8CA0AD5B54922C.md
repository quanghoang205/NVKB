---
entity_type: affectedcondition
id: CONDITION:30067ADC1C8CA0AD5B54922C
title: Điều kiện được công bố — CVE-2024-34161
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2024-34161
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2024-34161

When NGINX Plus or NGINX OSS are configured to use the HTTP/3 QUIC module and the network infrastructure supports a Maximum Transmission Unit (MTU) of 4096 or greater without fragmentation, undisclosed QUIC packets can cause NGINX worker processes to leak previously freed memory.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-C29AD4F277364724E51DC55B\|CVE:CVE-2024-34161: vendor_documented_conditions]] — "When NGINX Plus or NGINX OSS are configured to use the HTTP/3 QUIC module and the network infrastructure supports a Maximum Transmission Unit (MTU) of 4096 or greater without frag… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C3D1517BAEDAAEDC26809A8B: /containers/cna/descriptions — [[EVIDENCE-C3D1517BAEDAAEDC26809A8B\|CVE-2024-34161]] |




## Nguồn

[[EVIDENCE-C3D1517BAEDAAEDC26809A8B|CVE-2024-34161]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
