---
entity_type: claim
id: CLAIM:33F17EB1F74A9BABE2D8EAC4
title: 'CVE:CVE-2026-93479: description'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-93479: description'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-93479: description

`CLAIM:33F17EB1F74A9BABE2D8EAC4` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-93479|CVE-2026-93479]]. Predicate: `description`.

```json
"A vulnerability exists in NGINX Plus and NGINX Open Source when a map directive uses regex matching and the root directive or access log format references the map's regex capture variables before referencing the map output variable. Alternatively, the same result could be achieved by using a non-cacheable variable in a string expression under certain conditions. An unauthenticated attacker along with conditions beyond their control can exploit this vulnerability by sending crafted HTTP requests. This may cause a heap buffer overflow in the NGINX worker process leading to a restart. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.\n\nImpact: \nThis vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or to possibly trigger a code execution. There is no control plane exposure; this is a data plane issue only.\n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-A311A0B415C8E4750AB331AD|CVE-2026-93479]]

Locator: EVIDENCE:A311A0B415C8E4750AB331AD: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:28:45+00:00. Truy xuất: 2026-11-25T02:28:42+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
