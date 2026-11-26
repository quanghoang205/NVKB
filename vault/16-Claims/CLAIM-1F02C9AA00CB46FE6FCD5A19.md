---
entity_type: claim
id: CLAIM:1F02C9AA00CB46FE6FCD5A19
title: 'MODULE:NGX-STREAM-SSL-PREREAD-MODULE: v1.3:knowledge:Tradeoff và phòng vệ'
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- 'MODULE:NGX-STREAM-SSL-PREREAD-MODULE: v1.3:knowledge:Tradeoff và phòng vệ'
tags:
- nginx
- claim
- provenance
---

# MODULE:NGX-STREAM-SSL-PREREAD-MODULE: v1.3:knowledge:Tradeoff và phòng vệ

`CLAIM:1F02C9AA00CB46FE6FCD5A19` · **CURRENT**

## Nhận định

Chủ thể: [[MODULE-NGX-STREAM-SSL-PREREAD-MODULE|TLS preread — routing metadata và giới hạn tin cậy]]. Predicate: `v1.3:knowledge:Tradeoff và phòng vệ`.

```json
"## Tradeoff và phòng vệ\n\nKhông terminate TLS cho phép backend giữ vai trò bảo mật đầu cuối nhưng làm proxy có ít thông tin đã xác thực hơn. Cần kiểm soát tập backend được định tuyến và policy độc lập tại backend. Giữ version support của backend trong tài liệu thiết kế. Đây là nguyên tắc phòng vệ, không là cấu hình workaround đã được vendor xác nhận cho một CVE."
```

## Nguồn và phạm vi

Authority: NVKB AI curation. 

[[EVIDENCE-4BA76FA5ED0E407DE3B76040|ngx_stream_ssl_preread_module.html: Introduction;]]

Locator: Introduction;

Phạm vi phiên bản: Document snapshot 2026-11-25T02:32:56+00:00; CVE versions are scoped separately.

## Kiểm chứng độc lập

| Chiều kiểm chứng | Kết quả |
| --- | --- |
| Reference | AVAILABLE |
| Hash nguồn | HASH_MATCH |
| Trích xuất | MATCHED |
| Nguồn hỗ trợ | PARTIAL |
| Review | AI_REVIEWED |
| Loại suy luận | INTERPRETATION |
| Legacy | INFERRED — nhãn pipeline cũ |

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:15:05+00:00

Read the cited snapshot section and compared the authored bounded statement. Source grounds the mechanism; ownership/invariant/teaching reasoning is author interpretation.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

New source observation; source support is separate.

Quan sát: 2026-11-25T05:15:05+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
