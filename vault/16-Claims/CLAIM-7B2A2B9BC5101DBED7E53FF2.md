---
entity_type: claim
id: CLAIM:7B2A2B9BC5101DBED7E53FF2
title: 'CVE:CVE-2026-113425: documented_configuration_context'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-113425: documented_configuration_context'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-113425: documented_configuration_context

`CLAIM:7B2A2B9BC5101DBED7E53FF2` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-113425|CVE-2026-113425]]. Predicate: `documented_configuration_context`.

```json
"When NGINX Plus or NGINX Open Source is configured as a mail proxy, undisclosed traffic can cause a use-after-free in an nginx worker process. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.\n\nImpact:\nA remote unauthenticated attacker may crash an nginx worker process or corrupt its memory, disrupting service. Remote code execution is a potential impact. There is no control plane exposure; this is a data plane issue only.\n\n\n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-2C74501240903031F91BB707|CVE-2026-113425]]

Locator: EVIDENCE:2C74501240903031F91BB707: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:26:38+00:00. Truy xuất: 2026-11-25T02:26:35+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
