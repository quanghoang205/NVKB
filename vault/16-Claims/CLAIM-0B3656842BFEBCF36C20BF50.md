---
entity_type: claim
id: CLAIM:0B3656842BFEBCF36C20BF50
title: 'CVE:CVE-2024-24989: v1.3:applicability'
verification_status: UNVERIFIED
generated: true
schema_version: 1.2.0
aliases:
- 'CVE:CVE-2024-24989: v1.3:applicability'
tags:
- nginx
- claim
- provenance
---

# CVE:CVE-2024-24989: v1.3:applicability

`CLAIM:0B3656842BFEBCF36C20BF50` · **CURRENT**

## Nhận định

Chủ thể: [[CVE-2024-24989|CVE-2024-24989]]. Predicate: `v1.3:applicability`.

```json
"Build và cấu hình sử dụng HTTP/3 QUIC module; module không bật mặc định và được nguồn mô tả là experimental. Bài này dùng version scope OSS."
```

## Nguồn và phạm vi

Authority: CNA F5 / CVE Program. 

[[EVIDENCE-AE7C4E1B7BC7576206D4E954|Official NGINX announcement]], [[EVIDENCE-B3BCCE5ED0DA5392D153C089|CVE-2024-24989.json: /containers/cna/descriptions/0/value]]

Locator: /containers/cna/descriptions/0/value

Phạm vi phiên bản: Document snapshot 2026-11-25T02:26:03+00:00; CVE versions are scoped separately.

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

Reviewer: `nvkb-v1.3-ai-curator` · 2026-11-25T05:31:50+00:00

Read the cited snapshot section and compared the authored bounded statement. Support is limited to the named product, conditions and documented impact; no independent root-cause verification.

Legacy verification is ingestion provenance, not semantic or human approval.

## Vòng đời

New source observation; source support is separate.

Quan sát: 2026-11-25T05:31:50+00:00. Truy xuất: UNKNOWN.

Hiệu lực từ: UNKNOWN; đến: UNKNOWN.

Thay thế: Không ghi nhận.

Được thay bởi: Không ghi nhận.

[[Research-Library|Research Library]] · [[Learning-Library|Learning Library]]
