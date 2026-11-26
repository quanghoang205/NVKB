---
entity_type: affectedcondition
id: CONDITION:7DCE01E4EB7730F0A1088A20
title: Điều kiện được công bố — CVE-2026-97205
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-97205
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-97205

NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_core_module module. When asynchronous file I/O (AIO) is enabled in certain configurations, processing a Server Side Includes (SSI) page containing “include virtual” commands may trigger a Use-After-Free (UAF) in the NGINX worker process. This may cause memory corruption or a worker process crash. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.

Impact:
This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system, corrupt its memory, or possibly trigger code execution. There is no control plane exposure; this is a data plane issue only.




Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-EE430783452E96549E55B38A\|CVE:CVE-2026-97205: vendor_documented_conditions]] — "NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_core_module module. When asynchronous file I/O (AIO) is enabled in certain configurations, processing a Serve… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DA58A8C9C64BBC27B381CA6F: /containers/cna/descriptions — [[EVIDENCE-DA58A8C9C64BBC27B381CA6F\|CVE-2026-97205]] |




## Nguồn

[[EVIDENCE-DA58A8C9C64BBC27B381CA6F|CVE-2026-97205]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
