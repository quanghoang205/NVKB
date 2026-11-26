---
entity_type: affectedcondition
id: CONDITION:EDE1CA8428825449CF47A3F5
title: Điều kiện được công bố — CVE-2026-42055
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-42055
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-42055

NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_proxy_v2_module and ngx_http_grpc_module modules. This vulnerability exists when the proxy_http_version to 2 or grpc_pass directives are used to proxy HTTP/2 traffic, the ignore_invalid_headers directive is set to off, and the large_client_header_buffers directive size is larger than 2 megabytes. A remote, unauthenticated attacker, along with conditions beyond their control, could send large headers while creating an upstream request. This may cause a heap-based buffer overflow in the NGINX worker process leading to a restart. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. 


Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-C797A23802EA624A73F69B04\|CVE:CVE-2026-42055: vendor_documented_conditions]] — "NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_proxy_v2_module and ngx_http_grpc_module modules. This vulnerability exists when the proxy_http_version to 2 … (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AFAA6A12EA44778C8BB2C34D: /containers/cna/descriptions — [[EVIDENCE-AFAA6A12EA44778C8BB2C34D\|CVE-2026-42055]] |




## Nguồn

[[EVIDENCE-AFAA6A12EA44778C8BB2C34D|CVE-2026-42055]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
