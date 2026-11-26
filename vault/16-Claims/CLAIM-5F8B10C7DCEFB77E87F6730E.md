---
entity_type: claim
id: CLAIM:5F8B10C7DCEFB77E87F6730E
title: 'CVE:CVE-2026-123640: normal_component_behavior'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-123640: normal_component_behavior'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-123640: normal_component_behavior

`CLAIM:5F8B10C7DCEFB77E87F6730E` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-123640|CVE-2026-123640]]. Predicate: `normal_component_behavior`.

```json
"Đọc metadata ClientHello mà không kết thúc TLS trong preread phase. Module được kích hoạt theo build và directive, không mặc nhiên tồn tại trong mọi deployment."
```

## Nguồn và phạm vi

Authority: NGINX official documentation. NGINX official documentation

[[EVIDENCE-21B6BE4730D195CB65EDBA55|Module ngx_stream_ssl_preread_module]]

Locator: EVIDENCE:21B6BE4730D195CB65EDBA55: ngx_stream_ssl_preread_module

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

Quan sát: 2026-11-25T02:40:29+00:00. Truy xuất: 2026-11-25T02:32:56+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
