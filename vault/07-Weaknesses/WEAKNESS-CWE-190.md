---
entity_type: weakness
id: WEAKNESS:CWE-190
title: CWE-190 — Integer overflow
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-190 — Integer overflow
tags:
- nginx
- weakness
- knowledge
---

# CWE-190 — Integer overflow

Kết quả số học vượt miền biểu diễn của kiểu số.

## Mục tiêu đo được

- Giải thích CWE-190 — Integer overflow bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Kết quả số học vượt miền biểu diễn của kiểu số.

## Cơ chế hoạt động bình thường

Phép cộng/nhân kích thước được kiểm tra trước khi cấp phát hoặc tính offset.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Giá trị trung gian và chuyển đổi signed/unsigned không làm thay đổi ý nghĩa.

## Nhóm lỗi liên quan

Integer overflow

## Tác động khi giả định bị vi phạm

Cấp phát thiếu, truy cập ngoài biên hoặc quyết định kiểm tra sai.

## Nguyên tắc phòng vệ

Dùng checked arithmetic và giới hạn đầu vào theo miền biểu diễn.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-61F797BB5E464D25D23CD985\|WEAKNESS:CWE-190: definition]] — "Kết quả số học vượt miền biểu diễn của kiểu số." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1B9FC54844FF757989EB9A57: Description / Potential Mitigations; topic=WEAKNESS:CWE-190 — [[EVIDENCE-1B9FC54844FF757989EB9A57\|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]] |
| [[CLAIM-6A8C1E22ECFADE9F7322B72B\|WEAKNESS:CWE-190: normal_behavior]] — "Phép cộng/nhân kích thước được kiểm tra trước khi cấp phát hoặc tính offset." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1B9FC54844FF757989EB9A57: Description / Potential Mitigations; topic=WEAKNESS:CWE-190 — [[EVIDENCE-1B9FC54844FF757989EB9A57\|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]] |
| [[CLAIM-825D86D5E886CC6772B01F71\|WEAKNESS:CWE-190: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1B9FC54844FF757989EB9A57: Description / Potential Mitigations; topic=WEAKNESS:CWE-190 — [[EVIDENCE-1B9FC54844FF757989EB9A57\|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]] |
| [[CLAIM-5E7E40BF2E23714BE9F6815D\|WEAKNESS:CWE-190: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1B9FC54844FF757989EB9A57: Description / Potential Mitigations; topic=WEAKNESS:CWE-190 — [[EVIDENCE-1B9FC54844FF757989EB9A57\|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]] |
| [[CLAIM-C526558AF533B6EBBA0E10CF\|WEAKNESS:CWE-190: safety_assumptions]] — "Giá trị trung gian và chuyển đổi signed/unsigned không làm thay đổi ý nghĩa." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1B9FC54844FF757989EB9A57: Description / Potential Mitigations; topic=WEAKNESS:CWE-190 — [[EVIDENCE-1B9FC54844FF757989EB9A57\|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]] |
| [[CLAIM-64778EEF761B9F5549DF273C\|WEAKNESS:CWE-190: related_failure_classes]] — "Integer overflow" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1B9FC54844FF757989EB9A57: Description / Potential Mitigations; topic=WEAKNESS:CWE-190 — [[EVIDENCE-1B9FC54844FF757989EB9A57\|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]] |
| [[CLAIM-2ABA11241A42D02E39C56771\|WEAKNESS:CWE-190: failure_impact]] — "Cấp phát thiếu, truy cập ngoài biên hoặc quyết định kiểm tra sai." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1B9FC54844FF757989EB9A57: Description / Potential Mitigations; topic=WEAKNESS:CWE-190 — [[EVIDENCE-1B9FC54844FF757989EB9A57\|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]] |
| [[CLAIM-CAE42BEC9EC8366886A00377\|WEAKNESS:CWE-190: defensive_principles]] — "Dùng checked arithmetic và giới hạn đầu vào theo miền biểu diễn." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1B9FC54844FF757989EB9A57: Description / Potential Mitigations; topic=WEAKNESS:CWE-190 — [[EVIDENCE-1B9FC54844FF757989EB9A57\|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-1B9FC54844FF757989EB9A57|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]], [[EVIDENCE-F9A1F1B9A78981951B3C0E64|CVE-2026-27784]], [[EVIDENCE-FA9426B951F6B8E59FF3E9A0|CWE - CWE-190: Integer Overflow or Wraparound (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

