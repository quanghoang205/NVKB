---
entity_type: claim
id: CLAIM:A376C2D4C581FE3E0CE9A18D
title: 'CVE:CVE-2026-32647: related_components'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-32647: related_components'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-32647: related_components

`CLAIM:A376C2D4C581FE3E0CE9A18D` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-32647|CVE-2026-32647]]. Predicate: `related_components`.

```json
"COMPONENT:MEMORY-POOL"
```

## Nguồn và phạm vi

Authority: NVKB curation. NVKB curation

[[EVIDENCE-1696EE213A5424E97075EA01|CVE-2026-32647]], [[EVIDENCE-198C480BD0F040C0B875841A|CVE-2026-32647]], [[EVIDENCE-280FFDADEB891CC9C19C62D0|CVE-2026-32647]], [[EVIDENCE-3E16F0C4F9C825A40E41DD71|CVE-2026-32647]], [[EVIDENCE-50E46DFFEBA88B1049A4FD9B|CVE-2026-32647]], [[EVIDENCE-5DFD44D1745EC65F51418FC1|CVE-2026-32647]], [[EVIDENCE-99EFFF4C70D5B2FC77D9645D|CVE-2026-32647]], [[EVIDENCE-C59266D723B685ACE2719D33|NGINX security advisories]], [[EVIDENCE-ED5DE28FAC8FF32E7DA3A310|CVE-2026-32647]], [[EVIDENCE-FB2A7E51F617D62E623BB202|CVE-2026-32647]]

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

CVE-2026-32647: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

CVE-2026-32647: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Quan sát: 2026-11-25T02:33:49+00:00. Truy xuất: 2026-11-25T02:18:10+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
