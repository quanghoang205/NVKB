---
entity_type: claim
id: CLAIM:1B4E0EA27F5C3843FAFE7D7A
title: 'CVE:CVE-2026-97629: description'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-97629: description'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-97629: description

`CLAIM:1B4E0EA27F5C3843FAFE7D7A` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-97629|CVE-2026-97629]]. Predicate: `description`.

```json
"Description\nWhen NGINX Plus or NGINX Open Source is configured with ssl_session_cache \n\nshared:name:size\n\nwithout an explicit ssl_session_ticket_key file directives to automatically rotate SSL session ticket keys, a remote unauthenticated attacker is able to forge client SSL sessions \n\nin a non-deterministic manner that is beyond the attacker's control. An attacker could leverage this vulnerability to bypass verification of client certificates.\n\nImpact\n\n\nThis vulnerability can lead to the exposure of resources or functionality to unintended actors, possibly providing attackers with access to sensitive information. There is no control plane exposure; this is a data plane issue only.\n\n\n\n\n\n\nNote: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-B82A818F173B70E95BF7A4CA|CVE-2026-97629]]

Locator: EVIDENCE:B82A818F173B70E95BF7A4CA: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:28:57+00:00. Truy xuất: 2026-11-25T02:28:55+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
