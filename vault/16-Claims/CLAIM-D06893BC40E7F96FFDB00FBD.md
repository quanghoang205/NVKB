---
entity_type: claim
id: CLAIM:D06893BC40E7F96FFDB00FBD
title: 'MODULE:NGX-STREAM-SSL-MODULE: v1.3:knowledge_fact'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'MODULE:NGX-STREAM-SSL-MODULE: v1.3:knowledge_fact'
tags:
- nginx
- claim
- provenance
---

# MODULE:NGX-STREAM-SSL-MODULE: v1.3:knowledge_fact

`CLAIM:D06893BC40E7F96FFDB00FBD` · **CURRENT**

## Nhận định

Chủ thể: [[MODULE-NGX-STREAM-SSL-MODULE|Stream TLS — chứng thư, policy và trạng thái OCSP]]. Predicate: `v1.3:knowledge_fact`.

```json
"Module stream SSL có các directive riêng để xác minh client certificate và OCSP; ssl_ocsp yêu cầu policy xác minh chứng thư thích hợp và resolver cho tên OCSP responder."
```

## Nguồn và phạm vi

Authority: NGINX / F5. 

[[EVIDENCE-3A43D6C5BBCD84195240076C|ngx_stream_ssl_module.html: #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache]]

Locator: #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache

Phạm vi phiên bản: Document snapshot 2026-11-25T02:32:56+00:00; CVE versions are scoped separately.

## Kiểm chứng độc lập

| Chiều kiểm chứng | Kết quả |
| --- | --- |
| Reference | AVAILABLE |
| Hash nguồn | HASH_MATCH |
| Trích xuất | MATCHED |
| Nguồn hỗ trợ | SUPPORTED |
| Review | AI_REVIEWED |
| Loại suy luận | SOURCE_STATEMENT |
| Legacy | UNVERIFIED — nhãn pipeline cũ |

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:15:02+00:00

Read the cited snapshot section and compared the authored bounded statement. Support is limited to the named product, conditions and documented impact; no independent root-cause verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

New source observation; source support is separate.

Quan sát: 2026-11-25T05:15:02+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
