---
entity_type: affectedcondition
id: CONDITION:F9D590FEDC8EB6B8DD9FA70F
title: Điều kiện được công bố — CVE-2026-60005
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- Điều kiện được công bố — CVE-2026-60005
tags:
- nginx
- affectedcondition
- knowledge
---

# Điều kiện được công bố — CVE-2026-60005

NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_slice_module module. When the slice directive and unnamed regex captures are configured or when a background cache update happens, unauthenticated attackers can send requests that may cause uninitialized memory access in the NGINX worker process, leading to limited disclosure of memory or a restart.

Impact:
This vulnerability may allow remote, unauthenticated attackers to have limited control to disclose memory contents or restart the NGINX worker process. There is no control plane exposure; this is a data plane issue only.
Note: The ngx_http_slice_module module is not enabled by default; it's enabled with the --with-http_slice_module configuration parameter.

Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

| Thuộc tính | Giá trị |
| --- | --- |



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-233E16440E83F4F2FA80E106\|CVE:CVE-2026-60005: vendor_documented_conditions]] — "NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_slice_module module. When the slice directive and unnamed regex captures are configured or when a background … (mở Claim để đọc đủ) | CVE Program / CNA | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:3C1D5978A2712727A1FFC37B: /containers/cna/descriptions — [[EVIDENCE-3C1D5978A2712727A1FFC37B\|CVE-2026-60005]] |




## Nguồn

[[EVIDENCE-3C1D5978A2712727A1FFC37B|CVE-2026-60005]]

Legacy: VERIFIED. Xem Claim để biết source support và hiệu lực; package comparison không xác minh binary đang chạy.

[[Patch-Management-Library|Patch Management Library]] · [[Research-Library|Research Library]]
