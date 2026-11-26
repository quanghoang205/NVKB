---
entity_type: claim
id: CLAIM:47621DBFBE46E6DAD3EDAFA5
title: 'CVE:CVE-2026-15176: description'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-15176: description'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-15176: description

`CLAIM:47621DBFBE46E6DAD3EDAFA5` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-15176|CVE-2026-15176]]. Predicate: `description`.

```json
"A vulnerability exists in NGINX Plus and NGINX Open Source when a location is configured that uses the alias directive together with rewrite and a set or return directive referencing the $request_filename variable. Alternatively, the same result could be achieved when the $request_filename variable is used in an access log format directive. An unauthenticated attacker along with conditions beyond their control can exploit this vulnerability by sending crafted HTTP requests. This may cause a heap buffer overflow in the NGINX worker process leading to a restart. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.\n\nImpact:\nThis vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or to possibly trigger a code execution. There is no control plane exposure; this is a data plane issue only.\n\n\n\n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-A2D9EB6612FDF3E660D9122D|CVE-2026-15176]]

Locator: EVIDENCE:A2D9EB6612FDF3E660D9122D: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:27:21+00:00. Truy xuất: 2026-11-25T02:27:19+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
