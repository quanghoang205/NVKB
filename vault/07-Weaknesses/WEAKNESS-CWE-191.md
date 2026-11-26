---
entity_type: weakness
id: WEAKNESS:CWE-191
title: CWE-191 — Integer Underflow
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-191 — Integer Underflow
tags:
- nginx
- weakness
- knowledge
---

# CWE-191 — Integer Underflow

Phép tính số nguyên vượt dưới miền biểu diễn và có thể wraparound.

## Mục tiêu đo được

- Giải thích CWE-191 — Integer Underflow bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Phép tính số nguyên vượt dưới miền biểu diễn và có thể wraparound.

## Cơ chế hoạt động bình thường

Trước phép trừ kích thước phải bảo đảm quan hệ các toán hạng hợp lệ.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Trước phép trừ kích thước phải bảo đảm quan hệ các toán hạng hợp lệ.

## Nhóm lỗi liên quan

Integer Underflow

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Dùng checked arithmetic và kiểm thử giá trị 0/biên nhỏ.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-D1FB696433A1B43AE36D5D47\|WEAKNESS:CWE-191: definition]] — "Phép tính số nguyên vượt dưới miền biểu diễn và có thể wraparound." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F92CFDA044BB160372AF06A6: Description / Potential Mitigations; topic=WEAKNESS:CWE-191 — [[EVIDENCE-F92CFDA044BB160372AF06A6\|CWE - CWE-191: Integer Underflow (Wrap or Wraparound) (5.0)]] |
| [[CLAIM-43D6852485BAC6D8869692A5\|WEAKNESS:CWE-191: normal_behavior]] — "Trước phép trừ kích thước phải bảo đảm quan hệ các toán hạng hợp lệ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F92CFDA044BB160372AF06A6: Description / Potential Mitigations; topic=WEAKNESS:CWE-191 — [[EVIDENCE-F92CFDA044BB160372AF06A6\|CWE - CWE-191: Integer Underflow (Wrap or Wraparound) (5.0)]] |
| [[CLAIM-37323B7127285DC1E7D72357\|WEAKNESS:CWE-191: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F92CFDA044BB160372AF06A6: Description / Potential Mitigations; topic=WEAKNESS:CWE-191 — [[EVIDENCE-F92CFDA044BB160372AF06A6\|CWE - CWE-191: Integer Underflow (Wrap or Wraparound) (5.0)]] |
| [[CLAIM-011584F01E1533C057F89C5C\|WEAKNESS:CWE-191: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F92CFDA044BB160372AF06A6: Description / Potential Mitigations; topic=WEAKNESS:CWE-191 — [[EVIDENCE-F92CFDA044BB160372AF06A6\|CWE - CWE-191: Integer Underflow (Wrap or Wraparound) (5.0)]] |
| [[CLAIM-5E7E98B7E5AEE1B1407ED617\|WEAKNESS:CWE-191: safety_assumptions]] — "Trước phép trừ kích thước phải bảo đảm quan hệ các toán hạng hợp lệ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F92CFDA044BB160372AF06A6: Description / Potential Mitigations; topic=WEAKNESS:CWE-191 — [[EVIDENCE-F92CFDA044BB160372AF06A6\|CWE - CWE-191: Integer Underflow (Wrap or Wraparound) (5.0)]] |
| [[CLAIM-616EE3AAE352CCCA47DC7FC1\|WEAKNESS:CWE-191: related_failure_classes]] — "Integer Underflow" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F92CFDA044BB160372AF06A6: Description / Potential Mitigations; topic=WEAKNESS:CWE-191 — [[EVIDENCE-F92CFDA044BB160372AF06A6\|CWE - CWE-191: Integer Underflow (Wrap or Wraparound) (5.0)]] |
| [[CLAIM-392CD039E3408056E325E810\|WEAKNESS:CWE-191: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F92CFDA044BB160372AF06A6: Description / Potential Mitigations; topic=WEAKNESS:CWE-191 — [[EVIDENCE-F92CFDA044BB160372AF06A6\|CWE - CWE-191: Integer Underflow (Wrap or Wraparound) (5.0)]] |
| [[CLAIM-80E0817E2B439302CAF96AD1\|WEAKNESS:CWE-191: defensive_principles]] — "Dùng checked arithmetic và kiểm thử giá trị 0/biên nhỏ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:F92CFDA044BB160372AF06A6: Description / Potential Mitigations; topic=WEAKNESS:CWE-191 — [[EVIDENCE-F92CFDA044BB160372AF06A6\|CWE - CWE-191: Integer Underflow (Wrap or Wraparound) (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-E5D6A097B43D7EB31179D3D5|CVE-2026-125283]], [[EVIDENCE-F03600C558EF2F690E6E4A14|CVE-2026-123007]], [[EVIDENCE-F92CFDA044BB160372AF06A6|CWE - CWE-191: Integer Underflow (Wrap or Wraparound) (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

