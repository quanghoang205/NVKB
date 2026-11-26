---
entity_type: claim
id: CLAIM:8420D3AD6B2B9DDFE275BF7C
title: 'CVE:CVE-2026-42945: related_components'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-42945: related_components'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-42945: related_components

`CLAIM:8420D3AD6B2B9DDFE275BF7C` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-42945|CVE-2026-42945]]. Predicate: `related_components`.

```json
"COMPONENT:MEMORY-POOL"
```

## Nguồn và phạm vi

Authority: NVKB curation. NVKB curation

[[EVIDENCE-32FA0944FAC2777E62ABDC55|CVE-2026-42945]], [[EVIDENCE-3736739F84F851A4D69EDC0D|CVE-2026-42945]], [[EVIDENCE-3A64681628B462A9B4A1EB19|CVE-2026-42945]], [[EVIDENCE-83C382F9031A721F86C84AE8|CVE-2026-42945]], [[EVIDENCE-8BD094C55AE576DA927DC8CE|CVE-2026-42945]], [[EVIDENCE-94BAD2DEB5AC33DA6B9AF3E0|CVE-2026-42945]], [[EVIDENCE-9A41A4C86EE0F14F74983A61|NGINX security advisories]], [[EVIDENCE-9E32087168F6A187D0C0545D|CVE-2026-42945]], [[EVIDENCE-D7499FAAD66ACA4A6C462E03|CVE-2026-42945]], [[EVIDENCE-DC1432949B4CBBFA7575048F|CVE-2026-42945]]

Locator: /containers/cna/descriptions

Phạm vi phiên bản: Not version-pinned; see source snapshot

## Kiểm chứng độc lập

| Chiều kiểm chứng | Kết quả |
| --- | --- |
| Reference | AVAILABLE |
| Hash nguồn | HASH_MATCH |
| Trích xuất | NOT_CHECKED |
| Nguồn hỗ trợ | UNSUPPORTED |
| Review | AI_REVIEWED |
| Loại suy luận | KEYWORD_ASSOCIATION |
| Legacy | INFERRED — nhãn pipeline cũ |

Reviewer: `nvkb-v1.3-relationship-curator` · 2026-11-25T05:51:11+00:00

CVE-2026-42945: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

CVE-2026-42945: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Quan sát: 2026-11-25T02:33:53+00:00. Truy xuất: 2026-11-25T02:18:10+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
