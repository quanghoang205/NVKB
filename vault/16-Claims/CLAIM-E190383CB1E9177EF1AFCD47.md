---
entity_type: claim
id: CLAIM:E190383CB1E9177EF1AFCD47
title: 'CVE:CVE-2026-90439: documented_configuration_context'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-90439: documented_configuration_context'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-90439: documented_configuration_context

`CLAIM:E190383CB1E9177EF1AFCD47` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-90439|CVE-2026-90439]]. Predicate: `documented_configuration_context`.

```json
"NGINX Plus and NGINX Open Source have a vulnerability in the ngx_http_v3_module module. When using HTTP/3 with OpenSSL versions <= OpenSSL 3.5.0 under certain configurations, a limited heap buffer overflow could happen while processing a TLS handshake. This can happen in a non-deterministic manner that is beyond the attacker's control. This may cause a heap buffer overflow in the NGINX worker process leading to a restart and/or limited data corruption.\n\nImpact:\nThis vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or limited data corruption. There is no control plane exposure; this is a data plane issue only.\n\n\n\n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-2C3479DA69C20FDBA07AC92B|CVE-2026-90439]]

Locator: EVIDENCE:2C3479DA69C20FDBA07AC92B: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:28:37+00:00. Truy xuất: 2026-11-25T02:28:35+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
