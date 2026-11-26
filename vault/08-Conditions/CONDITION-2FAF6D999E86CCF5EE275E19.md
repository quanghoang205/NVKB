---
entity_type: affectedcondition
id: CONDITION:2FAF6D999E86CCF5EE275E19
title: Điều kiện được công bố — CVE-2026-120993
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-120993
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-120993

When NGINX Plus or NGINX Open Source is configured to use the ngx_stream_ssl_module module with dynamic certificate loading and the ngx_stream_proxy_module module with the proxy_protocol v2 directive, an abbreviated SSL handshake can cause a worker process to terminate.

Impact:
This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system. This is a data plane vulnerability only; there is no control plane exposure.



Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-9B8AFC1B9D13A98964C2C548\|CVE:CVE-2026-120993: vendor_documented_conditions]] — "When NGINX Plus or NGINX Open Source is configured to use the ngx_stream_ssl_module module with dynamic certificate loading and the ngx_stream_proxy_module module with the proxy_p… (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F6857C92B501A144D475D010: /containers/cna/descriptions — [[EVIDENCE-F6857C92B501A144D475D010\|CVE-2026-120993]] |




## Nguồn

[[EVIDENCE-F6857C92B501A144D475D010|CVE-2026-120993]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
