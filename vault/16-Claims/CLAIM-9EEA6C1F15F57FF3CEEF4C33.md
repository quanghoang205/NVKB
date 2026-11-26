---
entity_type: claim
id: CLAIM:9EEA6C1F15F57FF3CEEF4C33
title: 'CVE:CVE-2026-125283: description'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-125283: description'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-125283: description

`CLAIM:9EEA6C1F15F57FF3CEEF4C33` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-125283|CVE-2026-125283]]. Predicate: `description`.

```json
"When NGINX Plus or NGINX Open Source is configured to use the try_files and alias directives with a map variable, certain combinations of regular expression captures in map and try_files can cause a segmentation fault in an NGINX worker process.\n\nImpact:\nAn attacker could leverage this vulnerability to cause an NGINX worker process to terminate unexpectedly. There is no control plane exposure; this is a data plane issue only.\n\n\n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-EBC00C4C250179C07BC479C5|CVE-2026-125283]]

Locator: EVIDENCE:EBC00C4C250179C07BC479C5: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:27:13+00:00. Truy xuất: 2026-11-25T02:27:11+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
