---
entity_type: claim
id: CLAIM:CE5C3BC7DDCD97661F656F70
title: 'CVE:CVE-2026-27784: related_components'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-27784: related_components'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-27784: related_components

`CLAIM:CE5C3BC7DDCD97661F656F70` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2026-27784|CVE-2026-27784]]. Predicate: `related_components`.

```json
"COMPONENT:MEMORY-POOL"
```

## Nguồn và phạm vi

Authority: NVKB curation. NVKB curation

[[EVIDENCE-034B9E939C5C808F81C15395|CVE-2026-27784]], [[EVIDENCE-09931024439D883417DF7C1E|CVE-2026-27784]], [[EVIDENCE-0D4014BF77D9F9D500D748A6|CVE-2026-27784]], [[EVIDENCE-80D33BBF70F07DB821F5232D|NGINX security advisories]], [[EVIDENCE-81B3967C5EC538FED72F0479|CVE-2026-27784]], [[EVIDENCE-8E4D40009FADB7881E537AEE|CVE-2026-27784]], [[EVIDENCE-CB51A2751C96FB09AD144653|CVE-2026-27784]], [[EVIDENCE-E3A0312E8EBA339353ECC94F|CVE-2026-27784]], [[EVIDENCE-E8DE35A5DB92D9CBD839982A|CVE-2026-27784]], [[EVIDENCE-F9A1F1B9A78981951B3C0E64|CVE-2026-27784]]

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

CVE-2026-27784: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

CVE-2026-27784: nguồn mô tả lớp lỗi bộ nhớ nhưng không xác định pool là fault location. Rút association sinh từ buffer keyword khỏi technical view; học ownership qua learns_from có scope riêng.

Quan sát: 2026-11-25T02:33:48+00:00. Truy xuất: 2026-11-25T02:18:10+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
