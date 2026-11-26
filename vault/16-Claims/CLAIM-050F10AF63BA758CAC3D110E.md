---
entity_type: claim
id: CLAIM:050F10AF63BA758CAC3D110E
title: 'CVE:CVE-2026-90439: related_components'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-90439: related_components'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-90439: related_components

`CLAIM:050F10AF63BA758CAC3D110E` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-90439|CVE-2026-90439]]. Predicate: `related_components`.

```json
"COMPONENT:MEMORY-POOL"
```

## Nguồn và phạm vi

Authority: NVKB curation. NVKB curation

[[EVIDENCE-2C3479DA69C20FDBA07AC92B|CVE-2026-90439]], [[EVIDENCE-54EAAC75D1E52B666B8C855A|CVE-2026-90439]], [[EVIDENCE-55674A60244B91435EFF0035|CVE-2026-90439]], [[EVIDENCE-8A5EFD9F2F8B58978470483B|CVE-2026-90439]], [[EVIDENCE-9CACCA6E8BBE80A22AD98B06|CVE-2026-90439]], [[EVIDENCE-A71EC4E15514D61BE101A79A|NGINX security advisories]], [[EVIDENCE-C94AB35CB1BA18616960E146|CVE-2026-90439]], [[EVIDENCE-E22B6DDECF64286781AE8961|CVE-2026-90439]]

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

CVE-2026-90439: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

CVE-2026-90439: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Quan sát: 2026-11-25T02:33:55+00:00. Truy xuất: 2026-11-25T02:18:10+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
