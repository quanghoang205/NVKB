---
entity_type: affectedcondition
id: CONDITION:34B72E1A33DDB7BA6B5591BE
title: Điều kiện được công bố — CVE-2026-123007
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-123007
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-123007

This issue affects NGINX Plus or NGINX Open Source configurations that use HTTP/2. When NGINX processes undisclosed traffic, the flow control window can exceed the allowed threshold, potentially resulting in a heap buffer overflow typically followed by an NGINX worker segmentation fault. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.

Impact: An attacker could leverage this vulnerability to crash the NGINX worker process, corrupt its memory, or potentially execute code remotely. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-42B19A723C2FC319C2BE5AFD\|CVE:CVE-2026-123007: vendor_documented_conditions]] — "This issue affects NGINX Plus or NGINX Open Source configurations that use HTTP/2. When NGINX processes undisclosed traffic, the flow control window can exceed the allowed thresho… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C14C94F53F5BF0314B9F272C: /containers/cna/descriptions — [[EVIDENCE-C14C94F53F5BF0314B9F272C\|CVE-2026-123007]] |




## Nguồn

[[EVIDENCE-C14C94F53F5BF0314B9F272C|CVE-2026-123007]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
