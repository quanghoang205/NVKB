---
entity_type: claim
id: CLAIM:9E86B06F8E8B9CA8500B39BC
title: 'CVE:CVE-2026-56434: related_components'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-56434: related_components'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-56434: related_components

`CLAIM:9E86B06F8E8B9CA8500B39BC` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-56434|CVE-2026-56434]]. Predicate: `related_components`.

```json
"COMPONENT:MEMORY-POOL"
```

## Nguồn và phạm vi

Authority: NVKB curation. NVKB curation

[[EVIDENCE-03C2467C91A6D22077768FBC|CVE-2026-56434]], [[EVIDENCE-1729A41D4AF1446592600F42|NGINX security advisories]], [[EVIDENCE-3791CC5E20A071F2F7E13CFD|CVE-2026-56434]], [[EVIDENCE-46DA921D33C4B32EE8D009E7|CVE-2026-56434]], [[EVIDENCE-596E210E185279F943621E04|CVE-2026-56434]], [[EVIDENCE-5F38EA689F4892FB28385F6D|CVE-2026-56434]], [[EVIDENCE-82B053F4877AA363ECB539C7|CVE-2026-56434]], [[EVIDENCE-D4407539F1B8A1CE04978E33|CVE-2026-56434]]

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

Reviewer: `nvkb-v1.3-relationship-curator` · 2026-11-25T05:51:09+00:00

CVE-2026-56434: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

CVE-2026-56434: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Quan sát: 2026-11-25T02:33:55+00:00. Truy xuất: 2026-11-25T02:18:10+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
