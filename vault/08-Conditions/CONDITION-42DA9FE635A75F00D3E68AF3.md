---
entity_type: affectedcondition
id: CONDITION:42DA9FE635A75F00D3E68AF3
title: Điều kiện được công bố — CVE-2024-24989
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2024-24989
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2024-24989

When NGINX Plus or NGINX OSS are configured to use the HTTP/3 QUIC module, undisclosed requests can cause NGINX worker processes to terminate.

Note: The HTTP/3 QUIC module is not enabled by default and is considered experimental. For more information, refer to  Support for QUIC and HTTP/3 https://nginx.org/en/docs/quic.html .



NOTE: Software versions which have reached End of Technical Support (EoTS) are not evaluated

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-90F2B51CF2DEDEDE626A4DDB\|CVE:CVE-2024-24989: vendor_documented_conditions]] — "When NGINX Plus or NGINX OSS are configured to use the HTTP/3 QUIC module, undisclosed requests can cause NGINX worker processes to terminate.\n\nNote: The HTTP/3 QUIC module is n… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D7C1C7751911E167923A1A43: /containers/cna/descriptions — [[EVIDENCE-D7C1C7751911E167923A1A43\|CVE-2024-24989]] |




## Nguồn

[[EVIDENCE-D7C1C7751911E167923A1A43|CVE-2024-24989]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
