---
entity_type: claim
id: CLAIM:6366B4CD6CCC173E297B2D2D
title: 'CVE:CVE-2026-42934: related_components'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-42934: related_components'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-42934: related_components

`CLAIM:6366B4CD6CCC173E297B2D2D` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-42934|CVE-2026-42934]]. Predicate: `related_components`.

```json
"COMPONENT:MEMORY-POOL"
```

## Nguồn và phạm vi

Authority: NVKB curation. NVKB curation

[[EVIDENCE-0F3AAED1C80B201D753C0C7D|CVE-2026-42934]], [[EVIDENCE-45386D7260F8A021FA642272|CVE-2026-42934]], [[EVIDENCE-61274833A24B2819EF33D8A3|NGINX security advisories]], [[EVIDENCE-662C7E7EF279A8418B10DAAC|CVE-2026-42934]], [[EVIDENCE-7437F7F7F59D47F5642B61C4|CVE-2026-42934]], [[EVIDENCE-8018563939CFD1B6D984B5B2|CVE-2026-42934]], [[EVIDENCE-AB46026A75280CA89AFB224F|CVE-2026-42934]], [[EVIDENCE-AB6E40B85C793808DE349809|CVE-2026-42934]]

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

CVE-2026-42934: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

CVE-2026-42934: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Quan sát: 2026-11-25T02:33:53+00:00. Truy xuất: 2026-11-25T02:18:10+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
