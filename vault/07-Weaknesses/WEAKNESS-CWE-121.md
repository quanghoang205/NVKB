---
entity_type: weakness
id: WEAKNESS:CWE-121
title: CWE-121 — Stack-based Buffer Overflow
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-121 — Stack-based Buffer Overflow
tags:
- nginx
- weakness
- knowledge
---

# CWE-121 — Stack-based Buffer Overflow

Ghi vượt dung lượng buffer đặt trên stack.

## Mục tiêu đo được

- Giải thích CWE-121 — Stack-based Buffer Overflow bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Ghi vượt dung lượng buffer đặt trên stack.

## Cơ chế hoạt động bình thường

Dung lượng biến cục bộ và chiều dài dữ liệu phải được kiểm tra trước thao tác ghi.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Dung lượng biến cục bộ và chiều dài dữ liệu phải được kiểm tra trước thao tác ghi.

## Nhóm lỗi liên quan

Stack-based Buffer Overflow

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Kiểm tra biên, tránh cấp phát stack không giới hạn và dùng compiler hardening.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-DFFA1081F2A98320C22E68C2\|WEAKNESS:CWE-121: definition]] — "Ghi vượt dung lượng buffer đặt trên stack." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:E82D0A2225F7B3513B5228A7: Description / Potential Mitigations; topic=WEAKNESS:CWE-121 — [[EVIDENCE-E82D0A2225F7B3513B5228A7\|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]] |
| [[CLAIM-6D4D9254FC0FA4854C1EA331\|WEAKNESS:CWE-121: normal_behavior]] — "Dung lượng biến cục bộ và chiều dài dữ liệu phải được kiểm tra trước thao tác ghi." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:E82D0A2225F7B3513B5228A7: Description / Potential Mitigations; topic=WEAKNESS:CWE-121 — [[EVIDENCE-E82D0A2225F7B3513B5228A7\|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]] |
| [[CLAIM-DEB9A16E7C60ED426C2B0051\|WEAKNESS:CWE-121: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:E82D0A2225F7B3513B5228A7: Description / Potential Mitigations; topic=WEAKNESS:CWE-121 — [[EVIDENCE-E82D0A2225F7B3513B5228A7\|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]] |
| [[CLAIM-2FEED9A6B40696DB6BE49DA4\|WEAKNESS:CWE-121: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:E82D0A2225F7B3513B5228A7: Description / Potential Mitigations; topic=WEAKNESS:CWE-121 — [[EVIDENCE-E82D0A2225F7B3513B5228A7\|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]] |
| [[CLAIM-2950BB06ED131155B50B8F5E\|WEAKNESS:CWE-121: safety_assumptions]] — "Dung lượng biến cục bộ và chiều dài dữ liệu phải được kiểm tra trước thao tác ghi." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:E82D0A2225F7B3513B5228A7: Description / Potential Mitigations; topic=WEAKNESS:CWE-121 — [[EVIDENCE-E82D0A2225F7B3513B5228A7\|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]] |
| [[CLAIM-00475FDDDBED8045C5E275D7\|WEAKNESS:CWE-121: related_failure_classes]] — "Stack-based Buffer Overflow" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:E82D0A2225F7B3513B5228A7: Description / Potential Mitigations; topic=WEAKNESS:CWE-121 — [[EVIDENCE-E82D0A2225F7B3513B5228A7\|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]] |
| [[CLAIM-02818C62C5952D32E129F4E0\|WEAKNESS:CWE-121: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:E82D0A2225F7B3513B5228A7: Description / Potential Mitigations; topic=WEAKNESS:CWE-121 — [[EVIDENCE-E82D0A2225F7B3513B5228A7\|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]] |
| [[CLAIM-BC2CB0006843D89EA714C6B1\|WEAKNESS:CWE-121: defensive_principles]] — "Kiểm tra biên, tránh cấp phát stack không giới hạn và dùng compiler hardening." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:E82D0A2225F7B3513B5228A7: Description / Potential Mitigations; topic=WEAKNESS:CWE-121 — [[EVIDENCE-E82D0A2225F7B3513B5228A7\|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-794F9317F5F0B67AF541B6D4|CVE-2024-31079]], [[EVIDENCE-E82D0A2225F7B3513B5228A7|CWE - CWE-121: Stack-based Buffer Overflow (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

