---
entity_type: claim
id: CLAIM:6E9C09DFC7BF99BCA44FC968
title: 'CVE:CVE-2026-28753: vendor_documented_conditions'
verification_status: VERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2026-28753: vendor_documented_conditions'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2026-28753: vendor_documented_conditions

`CLAIM:6E9C09DFC7BF99BCA44FC968` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2026-28753|CVE-2026-28753]]. Predicate: `vendor_documented_conditions`.

```json
"NGINX Plus and NGINX Open Source have a vulnerability in the ngx_mail_smtp_module module due to the improper handling of CRLF sequences in DNS responses. This allows an attacker-controlled DNS server to inject arbitrary headers into SMTP upstream requests, leading to potential request manipulation. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated."
```

## Nguồn và phạm vi

Authority: CVE Program / CNA. CVE Program / CNA

[[EVIDENCE-B08BA542EDDE73461AFF4370|CVE-2026-28753]]

Locator: EVIDENCE:B08BA542EDDE73461AFF4370: /containers/cna/descriptions

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

Quan sát: 2026-11-25T02:27:40+00:00. Truy xuất: 2026-11-25T02:27:37+00:00.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
