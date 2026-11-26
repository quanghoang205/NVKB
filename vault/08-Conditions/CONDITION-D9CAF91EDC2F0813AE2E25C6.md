---
entity_type: affectedcondition
id: CONDITION:D9CAF91EDC2F0813AE2E25C6
title: Điều kiện được công bố — CVE-2026-125283
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-125283
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-125283

When NGINX Plus or NGINX Open Source is configured to use the try_files and alias directives with a map variable, certain combinations of regular expression captures in map and try_files can cause a segmentation fault in an NGINX worker process.

Impact:
An attacker could leverage this vulnerability to cause an NGINX worker process to terminate unexpectedly. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-B1E59A1A346C14A782BF1F92\|CVE:CVE-2026-125283: vendor_documented_conditions]] — "When NGINX Plus or NGINX Open Source is configured to use the try_files and alias directives with a map variable, certain combinations of regular expression captures in map and tr… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:EBC00C4C250179C07BC479C5: /containers/cna/descriptions — [[EVIDENCE-EBC00C4C250179C07BC479C5\|CVE-2026-125283]] |




## Nguồn

[[EVIDENCE-EBC00C4C250179C07BC479C5|CVE-2026-125283]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
