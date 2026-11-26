---
entity_type: weakness
id: WEAKNESS:CWE-415
title: CWE-415 — Double free
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-415 — Double free
tags:
- nginx
- weakness
- knowledge
---

# CWE-415 — Double free

Giải phóng cùng tài nguyên bộ nhớ nhiều lần.

## Mục tiêu đo được

- Giải thích CWE-415 — Double free bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Giải phóng cùng tài nguyên bộ nhớ nhiều lần.

## Cơ chế hoạt động bình thường

Mỗi allocation có một đường ownership quyết định giải phóng; các đường lỗi không lặp cleanup.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Các nhánh cleanup và finalization phối hợp nhất quán.

## Nhóm lỗi liên quan

Double free

## Tác động khi giả định bị vi phạm

Hỏng allocator state hoặc crash.

## Nguyên tắc phòng vệ

Thiết kế ownership rõ ràng, cleanup có trạng thái và kiểm thử nhánh lỗi.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-55AC3AE44EAEE714251323CA\|WEAKNESS:CWE-415: definition]] — "Giải phóng cùng tài nguyên bộ nhớ nhiều lần." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C2CD8A5F4F470AAECCF5C8F6: Description / Potential Mitigations; topic=WEAKNESS:CWE-415 — [[EVIDENCE-C2CD8A5F4F470AAECCF5C8F6\|CWE - CWE-415: Double Free (5.0)]] |
| [[CLAIM-B7BD2CB702D7D514B0B932DA\|WEAKNESS:CWE-415: normal_behavior]] — "Mỗi allocation có một đường ownership quyết định giải phóng; các đường lỗi không lặp cleanup." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C2CD8A5F4F470AAECCF5C8F6: Description / Potential Mitigations; topic=WEAKNESS:CWE-415 — [[EVIDENCE-C2CD8A5F4F470AAECCF5C8F6\|CWE - CWE-415: Double Free (5.0)]] |
| [[CLAIM-11683AF797C1E8C897415D06\|WEAKNESS:CWE-415: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C2CD8A5F4F470AAECCF5C8F6: Description / Potential Mitigations; topic=WEAKNESS:CWE-415 — [[EVIDENCE-C2CD8A5F4F470AAECCF5C8F6\|CWE - CWE-415: Double Free (5.0)]] |
| [[CLAIM-79DEFB9489363621A0C2B612\|WEAKNESS:CWE-415: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C2CD8A5F4F470AAECCF5C8F6: Description / Potential Mitigations; topic=WEAKNESS:CWE-415 — [[EVIDENCE-C2CD8A5F4F470AAECCF5C8F6\|CWE - CWE-415: Double Free (5.0)]] |
| [[CLAIM-0856F05973EAF0B45105BE8D\|WEAKNESS:CWE-415: safety_assumptions]] — "Các nhánh cleanup và finalization phối hợp nhất quán." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C2CD8A5F4F470AAECCF5C8F6: Description / Potential Mitigations; topic=WEAKNESS:CWE-415 — [[EVIDENCE-C2CD8A5F4F470AAECCF5C8F6\|CWE - CWE-415: Double Free (5.0)]] |
| [[CLAIM-AD8E0B7DACE0D245B29C3DB9\|WEAKNESS:CWE-415: related_failure_classes]] — "Double free" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C2CD8A5F4F470AAECCF5C8F6: Description / Potential Mitigations; topic=WEAKNESS:CWE-415 — [[EVIDENCE-C2CD8A5F4F470AAECCF5C8F6\|CWE - CWE-415: Double Free (5.0)]] |
| [[CLAIM-CFB0C46AD308C0C6051F3DA6\|WEAKNESS:CWE-415: failure_impact]] — "Hỏng allocator state hoặc crash." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C2CD8A5F4F470AAECCF5C8F6: Description / Potential Mitigations; topic=WEAKNESS:CWE-415 — [[EVIDENCE-C2CD8A5F4F470AAECCF5C8F6\|CWE - CWE-415: Double Free (5.0)]] |
| [[CLAIM-E699E5790A8132CF096C0294\|WEAKNESS:CWE-415: defensive_principles]] — "Thiết kế ownership rõ ràng, cleanup có trạng thái và kiểm thử nhánh lỗi." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:C2CD8A5F4F470AAECCF5C8F6: Description / Potential Mitigations; topic=WEAKNESS:CWE-415 — [[EVIDENCE-C2CD8A5F4F470AAECCF5C8F6\|CWE - CWE-415: Double Free (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-0F318B013600D8CC562EC9BA|CWE - CWE-415: Double Free (5.0)]], [[EVIDENCE-C2CD8A5F4F470AAECCF5C8F6|CWE - CWE-415: Double Free (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

