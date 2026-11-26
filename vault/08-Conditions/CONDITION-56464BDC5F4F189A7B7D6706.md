---
entity_type: affectedcondition
id: CONDITION:56464BDC5F4F189A7B7D6706
title: Điều kiện được công bố — CVE-2026-123633
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-123633
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-123633

When NGINX Plus or NGINX Open Source is configured to use HTTP/2 for client connections and proxy client requests to a backend, a specially crafted request can result in use-after-free in the worker process, if this process is running low on worker_connections. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.




Impact:



This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or may allow a code execution. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-1227DCF1874FAC97427C6D17\|CVE:CVE-2026-123633: vendor_documented_conditions]] — "When NGINX Plus or NGINX Open Source is configured to use HTTP/2 for client connections and proxy client requests to a backend, a specially crafted request can result in use-after… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F35057971FC6ABBD47BA4E7F: /containers/cna/descriptions — [[EVIDENCE-F35057971FC6ABBD47BA4E7F\|CVE-2026-123633]] |




## Nguồn

[[EVIDENCE-F35057971FC6ABBD47BA4E7F|CVE-2026-123633]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
