---
entity_type: affectedcondition
id: CONDITION:9708A25239ED66F69C8EABA3
title: Điều kiện được công bố — CVE-2026-97629
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-97629
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-97629

Description
When NGINX Plus or NGINX Open Source is configured with ssl_session_cache 

shared:name:size

without an explicit ssl_session_ticket_key file directives to automatically rotate SSL session ticket keys, a remote unauthenticated attacker is able to forge client SSL sessions 

in a non-deterministic manner that is beyond the attacker's control. An attacker could leverage this vulnerability to bypass verification of client certificates.

Impact


This vulnerability can lead to the exposure of resources or functionality to unintended actors, possibly providing attackers with access to sensitive information. There is no control plane exposure; this is a data plane issue only.






Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-57DEE5EDB93893ED20C6B49B\|CVE:CVE-2026-97629: vendor_documented_conditions]] — "Description\nWhen NGINX Plus or NGINX Open Source is configured with ssl_session_cache \n\nshared:name:size\n\nwithout an explicit ssl_session_ticket_key file directives to automa… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:B82A818F173B70E95BF7A4CA: /containers/cna/descriptions — [[EVIDENCE-B82A818F173B70E95BF7A4CA\|CVE-2026-97629]] |




## Nguồn

[[EVIDENCE-B82A818F173B70E95BF7A4CA|CVE-2026-97629]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
