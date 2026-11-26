---
entity_type: affectedcondition
id: CONDITION:BEB13FA96D2B95DB3A349D86
title: Điều kiện được công bố — CVE-2026-113425
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-113425
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-113425

When NGINX Plus or NGINX Open Source is configured as a mail proxy, undisclosed traffic can cause a use-after-free in an nginx worker process. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.

Impact:
A remote unauthenticated attacker may crash an nginx worker process or corrupt its memory, disrupting service. Remote code execution is a potential impact. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-3910B19C2F694F1AAA1E0840\|CVE:CVE-2026-113425: vendor_documented_conditions]] — "When NGINX Plus or NGINX Open Source is configured as a mail proxy, undisclosed traffic can cause a use-after-free in an nginx worker process. Additionally, attackers can execute … (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2C74501240903031F91BB707: /containers/cna/descriptions — [[EVIDENCE-2C74501240903031F91BB707\|CVE-2026-113425]] |




## Nguồn

[[EVIDENCE-2C74501240903031F91BB707|CVE-2026-113425]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
