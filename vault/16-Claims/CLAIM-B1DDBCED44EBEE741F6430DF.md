---
entity_type: claim
id: CLAIM:B1DDBCED44EBEE741F6430DF
title: 'CVE:CVE-2026-42946: normal_component_behavior'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-42946: normal_component_behavior'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-42946: normal_component_behavior

`CLAIM:B1DDBCED44EBEE741F6430DF` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-42946|CVE-2026-42946]]. Predicate: `normal_component_behavior`.

```json
"Chuyển tiếp request đến SCGI server. Module được kích hoạt theo build và directive, không mặc nhiên tồn tại trong mọi deployment.\n\nChuyển tiếp request đến uwsgi server. Module được kích hoạt theo build và directive, không mặc nhiên tồn tại trong mọi deployment."
```

## Nguồn và phạm vi

Authority: NGINX official documentation. NGINX official documentation

[[EVIDENCE-18CAE6E6F4ABEAA0B33AAE49|Module ngx_http_scgi_module]], [[EVIDENCE-F7DAA4CC7BA1F02F3B8594D0|Module ngx_http_uwsgi_module]]

Locator: EVIDENCE:18CAE6E6F4ABEAA0B33AAE49: ngx_http_scgi_module; EVIDENCE:F7DAA4CC7BA1F02F3B8594D0: ngx_http_uwsgi_module

Phạm vi phiên bản: Legacy scope: consult evidence; not established for all releases

## Kiểm chứng độc lập

| Chiều kiểm chứng | Kết quả |
| --- | --- |
| Reference | AVAILABLE |
| Hash nguồn | HASH_MATCH |
| Trích xuất | NOT_CHECKED |
| Nguồn hỗ trợ | NOT_REVIEWED |
| Review | NOT_REVIEWED |
| Loại suy luận | SOURCE_STATEMENT |
| Legacy | VERIFIED — nhãn pipeline cũ |


Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

Same subject/predicate/value/authority is referenced in a later/current generation; retain observation.

Quan sát: 2026-11-25T02:40:43+00:00. Truy xuất: 2026-11-25T02:32:46+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
