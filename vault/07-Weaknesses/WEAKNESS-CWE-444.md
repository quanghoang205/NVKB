---
entity_type: weakness
id: WEAKNESS:CWE-444
title: CWE-444 — Request parsing inconsistencies
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-444 — Request parsing inconsistencies
tags:
- nginx
- weakness
- knowledge
---

# CWE-444 — Request parsing inconsistencies

Các thành phần hiểu khác nhau về ranh giới hoặc nội dung request.

## Mục tiêu đo được

- Giải thích CWE-444 — Request parsing inconsistencies bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Các thành phần hiểu khác nhau về ranh giới hoặc nội dung request.

## Cơ chế hoạt động bình thường

Mỗi hop diễn giải thống nhất framing và loại bỏ trường hợp mơ hồ.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Không có bất đồng parser giữa frontend và backend.

## Nhóm lỗi liên quan

Request parsing inconsistencies

## Tác động khi giả định bị vi phạm

Định tuyến hoặc ghép thông điệp sai theo context triển khai.

## Nguyên tắc phòng vệ

Cập nhật proxy/backend và chuẩn hóa chính sách xử lý thông điệp không hợp lệ.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-C0FF0282B8BC5AE57410C9A2\|WEAKNESS:CWE-444: definition]] — "Các thành phần hiểu khác nhau về ranh giới hoặc nội dung request." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:5C04483DC3CB040209557469: Description / Potential Mitigations; topic=WEAKNESS:CWE-444 — [[EVIDENCE-5C04483DC3CB040209557469\|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]] |
| [[CLAIM-B7B30DAC096534045CD89E91\|WEAKNESS:CWE-444: normal_behavior]] — "Mỗi hop diễn giải thống nhất framing và loại bỏ trường hợp mơ hồ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:5C04483DC3CB040209557469: Description / Potential Mitigations; topic=WEAKNESS:CWE-444 — [[EVIDENCE-5C04483DC3CB040209557469\|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]] |
| [[CLAIM-28659600EFE92C9B8F04E7D0\|WEAKNESS:CWE-444: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:5C04483DC3CB040209557469: Description / Potential Mitigations; topic=WEAKNESS:CWE-444 — [[EVIDENCE-5C04483DC3CB040209557469\|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]] |
| [[CLAIM-15608430D2F2AD90B14B260F\|WEAKNESS:CWE-444: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:5C04483DC3CB040209557469: Description / Potential Mitigations; topic=WEAKNESS:CWE-444 — [[EVIDENCE-5C04483DC3CB040209557469\|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]] |
| [[CLAIM-0C495438D05CA158EA72C085\|WEAKNESS:CWE-444: safety_assumptions]] — "Không có bất đồng parser giữa frontend và backend." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:5C04483DC3CB040209557469: Description / Potential Mitigations; topic=WEAKNESS:CWE-444 — [[EVIDENCE-5C04483DC3CB040209557469\|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]] |
| [[CLAIM-C00173795BF9FE9BDC50A2F9\|WEAKNESS:CWE-444: related_failure_classes]] — "Request parsing inconsistencies" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:5C04483DC3CB040209557469: Description / Potential Mitigations; topic=WEAKNESS:CWE-444 — [[EVIDENCE-5C04483DC3CB040209557469\|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]] |
| [[CLAIM-A7E3E177300327096C87218C\|WEAKNESS:CWE-444: failure_impact]] — "Định tuyến hoặc ghép thông điệp sai theo context triển khai." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:5C04483DC3CB040209557469: Description / Potential Mitigations; topic=WEAKNESS:CWE-444 — [[EVIDENCE-5C04483DC3CB040209557469\|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]] |
| [[CLAIM-430DD9583B749AF06C6B4BF4\|WEAKNESS:CWE-444: defensive_principles]] — "Cập nhật proxy/backend và chuẩn hóa chính sách xử lý thông điệp không hợp lệ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:5C04483DC3CB040209557469: Description / Potential Mitigations; topic=WEAKNESS:CWE-444 — [[EVIDENCE-5C04483DC3CB040209557469\|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-5C04483DC3CB040209557469|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]], [[EVIDENCE-C67CBD8D65FDA0EC66099A3F|CWE - CWE-444: Inconsistent Interpretation of HTTP Requests (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

