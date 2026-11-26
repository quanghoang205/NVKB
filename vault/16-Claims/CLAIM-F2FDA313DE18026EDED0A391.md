---
entity_type: claim
id: CLAIM:F2FDA313DE18026EDED0A391
title: 'CVE:CVE-2026-15176: related_components'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-15176: related_components'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-15176: related_components

`CLAIM:F2FDA313DE18026EDED0A391` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-15176|CVE-2026-15176]]. Predicate: `related_components`.

```json
"COMPONENT:MEMORY-POOL"
```

## Nguồn và phạm vi

Authority: NVKB curation. NVKB curation

[[EVIDENCE-0CCC16DDE68A1713FAED2329|CVE-2026-15176]], [[EVIDENCE-1B0139E19B8B90DB359F998D|NGINX security advisories]], [[EVIDENCE-3E9C443AD39E7D09329FCE25|CVE-2026-15176]], [[EVIDENCE-54767638C2D4C6C69DDCDC11|CVE-2026-15176]], [[EVIDENCE-68E2496B00A2AAA6C860517F|CVE-2026-15176]], [[EVIDENCE-A2D9EB6612FDF3E660D9122D|CVE-2026-15176]], [[EVIDENCE-B91587FE936225A889D5B550|CVE-2026-15176]], [[EVIDENCE-EEC3FBA90740148A47AD169F|CVE-2026-15176]]

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

CVE-2026-15176: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

CVE-2026-15176: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Quan sát: 2026-11-25T02:33:46+00:00. Truy xuất: 2026-11-25T02:18:10+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
