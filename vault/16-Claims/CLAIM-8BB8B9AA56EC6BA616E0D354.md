---
entity_type: claim
id: CLAIM:8BB8B9AA56EC6BA616E0D354
title: 'CVE:CVE-2026-118899: documented_configuration_context'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-118899: documented_configuration_context'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-118899: documented_configuration_context

`CLAIM:8BB8B9AA56EC6BA616E0D354` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-118899|CVE-2026-118899]]. Predicate: `documented_configuration_context`.

```json
"When using the listen directive with the ssl parameter in the http block with TLSv1.3 enabled, an attacker can use a specially crafted TLS connection to cause an infinite loop in the NGINX worker process while reading the HTTP request body. As a result, the worker process stops accepting new connections and processing existing connections. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.\n\nImpact: This vulnerability allows a remote, unauthenticated attacker to cause a denial-of-service (DoS) of NGINX. There is no control plane exposure; this is a data plane issue only.\n\n\n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-D7C987F4E116133786DC9C36|CVE-2026-118899]]

Locator: EVIDENCE:D7C987F4E116133786DC9C36: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:26:42+00:00. Truy xuất: 2026-11-25T02:26:39+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
