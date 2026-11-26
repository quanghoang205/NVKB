---
entity_type: affectedcondition
id: CONDITION:7D811FBFB34C6AA823E36071
title: Điều kiện được công bố — CVE-2026-123634
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-123634
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-123634

This issue occurs when NGINX Plus or NGINX Open Source is configured as a proxy, the proxied server name includes variables, and a Server Side Includes (SSI) or mirror directive sends a subrequest to a location that resolves the same server name. Under these conditions, a specially crafted HTTP request may cause a use-after-free condition in a worker process. An attacker may also be able to execute code if Address Space Layout Randomization (ASLR) is disabled or the attacker can bypass ASLR.

Impact: 
An attacker could leverage this vulnerability to crash the NGINX worker process, corrupt its memory, or perform remote code execution (RCE)



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-75E64B241997FF88342CF04F\|CVE:CVE-2026-123634: vendor_documented_conditions]] — "This issue occurs when NGINX Plus or NGINX Open Source is configured as a proxy, the proxied server name includes variables, and a Server Side Includes (SSI) or mirror directive s… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A2163880C26D9E0DFAE927BB: /containers/cna/descriptions — [[EVIDENCE-A2163880C26D9E0DFAE927BB\|CVE-2026-123634]] |




## Nguồn

[[EVIDENCE-A2163880C26D9E0DFAE927BB|CVE-2026-123634]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
