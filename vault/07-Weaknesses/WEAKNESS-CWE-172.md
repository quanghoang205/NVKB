---
entity_type: weakness
id: WEAKNESS:CWE-172
title: CWE-172 — Encoding Error
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-172 — Encoding Error
tags:
- nginx
- weakness
- knowledge
---

# CWE-172 — Encoding Error

Sai xử lý biểu diễn hoặc chuyển đổi encoding.

## Mục tiêu đo được

- Giải thích CWE-172 — Encoding Error bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Sai xử lý biểu diễn hoặc chuyển đổi encoding.

## Cơ chế hoạt động bình thường

Encoder/decoder tuân thủ cùng quy tắc và duy trì chiều dài đầu vào/đầu ra.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Encoder/decoder tuân thủ cùng quy tắc và duy trì chiều dài đầu vào/đầu ra.

## Nhóm lỗi liên quan

Encoding Error

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Kiểm tra encoding hợp lệ, kích thước đầu ra và các trường hợp ký tự nhiều byte.






## Quan hệ có định kiểu

- `CONTEXTUAL_ASSOCIATION` → [[IMPACT-UPSTREAM-MESSAGE-INTEGRITY|Vi phạm toàn vẹn message tới upstream]] — Nguồn 42926 nêu upstream request injection; không suy hậu quả ứng dụng tiếp theo. Lớp lỗi được CNA gán trong case này; impact là mô tả nguồn riêng, không suy từ CWE. **INTERPRETATION / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-81906E1C0397D03C5D9B4A6F\|WEAKNESS:CWE-172: definition]] — "Sai xử lý biểu diễn hoặc chuyển đổi encoding." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:97ABE046C832384B27C5D13B: Description / Potential Mitigations; topic=WEAKNESS:CWE-172 — [[EVIDENCE-97ABE046C832384B27C5D13B\|CWE - CWE-172: Improper Encoding or Decoding of Data (5.0)]] |
| [[CLAIM-CF848A7C389BB4158190612A\|WEAKNESS:CWE-172: normal_behavior]] — "Encoder/decoder tuân thủ cùng quy tắc và duy trì chiều dài đầu vào/đầu ra." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:97ABE046C832384B27C5D13B: Description / Potential Mitigations; topic=WEAKNESS:CWE-172 — [[EVIDENCE-97ABE046C832384B27C5D13B\|CWE - CWE-172: Improper Encoding or Decoding of Data (5.0)]] |
| [[CLAIM-7C2C20DF355D8BBDC77018C3\|WEAKNESS:CWE-172: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:97ABE046C832384B27C5D13B: Description / Potential Mitigations; topic=WEAKNESS:CWE-172 — [[EVIDENCE-97ABE046C832384B27C5D13B\|CWE - CWE-172: Improper Encoding or Decoding of Data (5.0)]] |
| [[CLAIM-D96FA7D4D4734F609AB456F5\|WEAKNESS:CWE-172: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:97ABE046C832384B27C5D13B: Description / Potential Mitigations; topic=WEAKNESS:CWE-172 — [[EVIDENCE-97ABE046C832384B27C5D13B\|CWE - CWE-172: Improper Encoding or Decoding of Data (5.0)]] |
| [[CLAIM-F1D52207C8D79D7A70A80336\|WEAKNESS:CWE-172: safety_assumptions]] — "Encoder/decoder tuân thủ cùng quy tắc và duy trì chiều dài đầu vào/đầu ra." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:97ABE046C832384B27C5D13B: Description / Potential Mitigations; topic=WEAKNESS:CWE-172 — [[EVIDENCE-97ABE046C832384B27C5D13B\|CWE - CWE-172: Improper Encoding or Decoding of Data (5.0)]] |
| [[CLAIM-6378539924E54D61C071F478\|WEAKNESS:CWE-172: related_failure_classes]] — "Encoding Error" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:97ABE046C832384B27C5D13B: Description / Potential Mitigations; topic=WEAKNESS:CWE-172 — [[EVIDENCE-97ABE046C832384B27C5D13B\|CWE - CWE-172: Improper Encoding or Decoding of Data (5.0)]] |
| [[CLAIM-F24248D5404D625771F4EB13\|WEAKNESS:CWE-172: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:97ABE046C832384B27C5D13B: Description / Potential Mitigations; topic=WEAKNESS:CWE-172 — [[EVIDENCE-97ABE046C832384B27C5D13B\|CWE - CWE-172: Improper Encoding or Decoding of Data (5.0)]] |
| [[CLAIM-D22914D24D7E6C0B2EF5206D\|WEAKNESS:CWE-172: defensive_principles]] — "Kiểm tra encoding hợp lệ, kích thước đầu ra và các trường hợp ký tự nhiều byte." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:97ABE046C832384B27C5D13B: Description / Potential Mitigations; topic=WEAKNESS:CWE-172 — [[EVIDENCE-97ABE046C832384B27C5D13B\|CWE - CWE-172: Improper Encoding or Decoding of Data (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-7285356524F3AD0BF37D5F1B|CVE-2026-42926]], [[EVIDENCE-97ABE046C832384B27C5D13B|CWE - CWE-172: Improper Encoding or Decoding of Data (5.0)]], [[EVIDENCE-C4A5449A62FA7F84636A2B3E|CVE-2026-95101]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

