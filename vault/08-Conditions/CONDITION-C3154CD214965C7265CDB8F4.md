---
entity_type: affectedcondition
id: CONDITION:C3154CD214965C7265CDB8F4
title: Điều kiện được công bố — CVE-2026-118899
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-118899
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-118899

When using the listen directive with the ssl parameter in the http block with TLSv1.3 enabled, an attacker can use a specially crafted TLS connection to cause an infinite loop in the NGINX worker process while reading the HTTP request body. As a result, the worker process stops accepting new connections and processing existing connections. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

Impact: This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) of NGINX. There is no control plane exposure; this is a data plane issue only.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-3BA2D82371BF5BE34A7854A4\|CVE:CVE-2026-118899: vendor_documented_conditions]] — "When using the listen directive with the ssl parameter in the http block with TLSv1.3 enabled, an attacker can use a specially crafted TLS connection to cause an infinite loop in … (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D7C987F4E116133786DC9C36: /containers/cna/descriptions — [[EVIDENCE-D7C987F4E116133786DC9C36\|CVE-2026-118899]] |




## Nguồn

[[EVIDENCE-D7C987F4E116133786DC9C36|CVE-2026-118899]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
