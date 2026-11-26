---
entity_type: claim
id: CLAIM:57DC5126394D1D17CFA98AAF
title: 'CVE:CVE-2026-95101: related_components'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-95101: related_components'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-95101: related_components

`CLAIM:57DC5126394D1D17CFA98AAF` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-95101|CVE-2026-95101]]. Predicate: `related_components`.

```json
"COMPONENT:MEMORY-POOL"
```

## Nguồn và phạm vi

Authority: NVKB curation. NVKB curation

[[EVIDENCE-0C7486A2233AE015DC7FB8C1|NGINX security advisories]], [[EVIDENCE-1EDD266ED7B0B613E2F7C3DD|CVE-2026-95101]], [[EVIDENCE-278A0675E65AFCDAE97BE8D3|CVE-2026-95101]], [[EVIDENCE-7EC7AFAB177164F5C7B6934B|CVE-2026-95101]], [[EVIDENCE-8CF50ADB53DA7699EF6F5D8B|CVE-2026-95101]], [[EVIDENCE-A59E329248E28B36814C7E0F|CVE-2026-95101]], [[EVIDENCE-C4A5449A62FA7F84636A2B3E|CVE-2026-95101]], [[EVIDENCE-EB7D6436B7498FEEC6E51ECE|CVE-2026-95101]]

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

CVE-2026-95101: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

CVE-2026-95101: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Quan sát: 2026-11-25T02:33:57+00:00. Truy xuất: 2026-11-25T02:18:10+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
