---
entity_type: claim
id: CLAIM:3CA083E16D8B951F2A41FEBE
title: 'COMPONENT:VIRTUAL-HOSTS: normal_behavior'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'COMPONENT:VIRTUAL-HOSTS: normal_behavior'
tags:
- nginx
- claim
- provenance
---

# COMPONENT:VIRTUAL-HOSTS: normal_behavior

`CLAIM:3CA083E16D8B951F2A41FEBE` · **CURRENT**

## Nhận định

Chủ thể: [[COMPONENT-VIRTUAL-HOSTS|Virtual hosts]]. Predicate: `normal_behavior`.

```json
"NGINX chọn nhóm listen theo địa chỉ/cổng và đối chiếu tên server; default server thuộc socket listen. TLS có bước chọn theo SNI."
```

## Nguồn và phạm vi

Authority: NGINX / F5. NGINX / F5

[[EVIDENCE-FDB9B691A2BFB99A8CC78B34|How nginx processes a request]]

Locator: EVIDENCE:FDB9B691A2BFB99A8CC78B34: Name-based virtual servers; topic=COMPONENT:VIRTUAL-HOSTS

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

Referenced in current read model; not a factual accuracy decision.

Quan sát: 2026-11-25T02:44:16+00:00. Truy xuất: 2026-11-25T02:28:09+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
