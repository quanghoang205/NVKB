---
entity_type: claim
id: CLAIM:CF7FD907DFB73B7BB9656D98
title: 'CVE:CVE-2026-27651: documented_configuration_context'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-27651: documented_configuration_context'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-27651: documented_configuration_context

`CLAIM:CF7FD907DFB73B7BB9656D98` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-27651|CVE-2026-27651]]. Predicate: `documented_configuration_context`.

```json
"When the ngx_mail_auth_http_module module is enabled on NGINX Plus or NGINX Open Source, undisclosed requests can cause worker processes to terminate. This issue may occur when (1) CRAM-MD5 or APOP authentication is enabled, and (2) the authentication server permits retry by returning the Auth-Wait response header. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-62FBFBCCE074909D2E2ABE91|CVE-2026-27651]]

Locator: EVIDENCE:62FBFBCCE074909D2E2ABE91: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:27:28+00:00. Truy xuất: 2026-11-25T02:27:27+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
