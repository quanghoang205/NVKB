---
entity_type: claim
id: CLAIM:7DF65C8FCDB0F8FB720485A2
title: 'CVE:CVE-2024-31079: root_cause_summary'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2024-31079: root_cause_summary'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2024-31079: root_cause_summary

`CLAIM:7DF65C8FCDB0F8FB720485A2` · **HISTORICAL**

## Nhận định

Chủ thể: [[CVE-2024-31079|CVE-2024-31079]]. Predicate: `root_cause_summary`.

```json
"Nguồn phân loại vấn đề: Stack overflow and use-after-free in HTTP/3.\n\nCWE-121 — Stack-based Buffer Overflow: Ghi vượt dung lượng buffer đặt trên stack.\n\nĐây là giải thích lớp lỗi theo CWE mà CNA gán, không phải kết luận về dòng mã gây lỗi. Chưa có source-code root cause review độc lập."
```

## Nguồn và phạm vi

Authority: NVKB curation. NVKB curation

[[EVIDENCE-4B3FF00AD62E27AE79FF8311|CVE-2024-31079]], [[EVIDENCE-794F9317F5F0B67AF541B6D4|CVE-2024-31079]], [[EVIDENCE-88FD4BD53DD070C91FA2F618|CVE-2024-31079]], [[EVIDENCE-ADE803DD55AF1C4D6A59D83F|[nginx-announce] nginx security advisory (CVE-2024-31079, CVE-2024-32760, CVE-2024-34161, CVE-2024-35200)]], [[EVIDENCE-B4D32A47B3A297FDD04BD433|CVE-2024-31079]], [[EVIDENCE-D5DCCCCBE408A7A73B44E5E4|NGINX security advisories]], [[EVIDENCE-E28D8CD66261432B86752BDA|CVE-2024-31079]], [[EVIDENCE-E82D0A2225F7B3513B5228A7|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]], [[EVIDENCE-EB0E96F78DD1953C76E01A4A|CVE-2024-31079]], [[EVIDENCE-F0A6006AC984A73AFF370C66|CVE-2024-31079]]

Locator: EVIDENCE:4B3FF00AD62E27AE79FF8311: /containers/cna/descriptions; EVIDENCE:794F9317F5F0B67AF541B6D4: /containers/cna/problemTypes; EVIDENCE:88FD4BD53DD070C91FA2F618: /containers/cna/metrics; EVIDENCE:ADE803DD55AF1C4D6A59D83F: advisory body; EVIDENCE:B4D32A47B3A297FDD04BD433: /containers/cna/affected; EVIDENCE:D5DCCCCBE408A7A73B44E5E4: li containing CVE-2024-31079; EVIDENCE:E28D8CD66261432B86752BDA: /containers/cna/affected; EVIDENCE:E82D0A2225F7B3513B5228A7: Description / Potential Mitigations; topic=WEAKNESS:CWE-121; EVIDENCE:EB0E96F78DD1953C76E01A4A: /containers/cna/metrics; EVIDENCE:F0A6006AC984A73AFF370C66: /cveMetadata

Phạm vi phiên bản: Legacy scope: consult evidence; not established for all releases

## Kiểm chứng độc lập

| Chiều kiểm chứng | Kết quả |
| --- | --- |
| Reference | AVAILABLE |
| Hash nguồn | HASH_MATCH |
| Trích xuất | NOT_CHECKED |
| Nguồn hỗ trợ | NOT_REVIEWED |
| Review | NOT_REVIEWED |
| Loại suy luận | INTERPRETATION |
| Legacy | INFERRED — nhãn pipeline cũ |


Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

Earlier generated interpretation retained; the v1.3 article supplies bounded source claims and explicit author reasoning.

Quan sát: 2026-11-25T02:49:08+00:00. Truy xuất: 2026-11-25T02:18:10+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
