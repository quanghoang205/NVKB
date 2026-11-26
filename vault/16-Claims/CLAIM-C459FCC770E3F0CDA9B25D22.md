---
entity_type: claim
id: CLAIM:C459FCC770E3F0CDA9B25D22
title: 'MODULE:NGX-HTTP-SSI-MODULE: v1.3:knowledge_fact'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'MODULE:NGX-HTTP-SSI-MODULE: v1.3:knowledge_fact'
tags:
- nginx
- claim
- provenance
---

# MODULE:NGX-HTTP-SSI-MODULE: v1.3:knowledge_fact

`CLAIM:C459FCC770E3F0CDA9B25D22` · **CURRENT**

## Nhận định

Chủ thể: [[MODULE-NGX-HTTP-SSI-MODULE|SSI và subrequest — công việc con, output và cleanup]]. Predicate: `v1.3:knowledge_fact`.

```json
"SSI module xử lý lệnh trong response và có thể đưa nội dung khác vào qua include; việc này khác với gửi response nguyên trạng."
```

## Nguồn và phạm vi

Authority: NGINX / F5. 

[[EVIDENCE-E407E38B58D01A696505E388|ngx_http_ssi_module.html: Introduction;]]

Locator: Introduction;

Phạm vi phiên bản: Document snapshot 2026-11-25T02:32:49+00:00; CVE versions are scoped separately.

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

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:24:17+00:00

Read the cited snapshot section and compared the authored bounded statement. Support is limited to the named product, conditions and documented impact; no independent root-cause verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

New source observation; source support is separate.

Quan sát: 2026-11-25T05:24:17+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
