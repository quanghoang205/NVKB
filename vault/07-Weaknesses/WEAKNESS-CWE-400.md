---
entity_type: weakness
id: WEAKNESS:CWE-400
title: CWE-400 — Resource exhaustion
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-400 — Resource exhaustion
tags:
- nginx
- weakness
- knowledge
---

# CWE-400 — Resource exhaustion

Tiêu thụ tài nguyên mà không có giới hạn phù hợp.

## Mục tiêu đo được

- Giải thích CWE-400 — Resource exhaustion bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Tiêu thụ tài nguyên mà không có giới hạn phù hợp.

## Cơ chế hoạt động bình thường

Hệ thống giữ hạn mức CPU, RAM, kết nối và thời gian cho từng đơn vị công việc.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Chi phí xử lý không tăng ngoài ngân sách khi trạng thái thay đổi.

## Nhóm lỗi liên quan

Resource exhaustion

## Tác động khi giả định bị vi phạm

Suy giảm availability.

## Nguyên tắc phòng vệ

Đo nguồn lực, đặt hạn mức và timeout dựa trên workload.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-73F2E957993B6988FA280889\|WEAKNESS:CWE-400: definition]] — "Tiêu thụ tài nguyên mà không có giới hạn phù hợp." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:74C44A41A6BA4045B073D6AB: Description / Potential Mitigations; topic=WEAKNESS:CWE-400 — [[EVIDENCE-74C44A41A6BA4045B073D6AB\|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]] |
| [[CLAIM-9A88AE98E43CA7D49CF10C13\|WEAKNESS:CWE-400: normal_behavior]] — "Hệ thống giữ hạn mức CPU, RAM, kết nối và thời gian cho từng đơn vị công việc." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:74C44A41A6BA4045B073D6AB: Description / Potential Mitigations; topic=WEAKNESS:CWE-400 — [[EVIDENCE-74C44A41A6BA4045B073D6AB\|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]] |
| [[CLAIM-ED01D31BC3B6BB0AB676DF76\|WEAKNESS:CWE-400: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:74C44A41A6BA4045B073D6AB: Description / Potential Mitigations; topic=WEAKNESS:CWE-400 — [[EVIDENCE-74C44A41A6BA4045B073D6AB\|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]] |
| [[CLAIM-D30D3C024D9D8788B9793B17\|WEAKNESS:CWE-400: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:74C44A41A6BA4045B073D6AB: Description / Potential Mitigations; topic=WEAKNESS:CWE-400 — [[EVIDENCE-74C44A41A6BA4045B073D6AB\|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]] |
| [[CLAIM-F051CD0376B4FD43C1ACEAFD\|WEAKNESS:CWE-400: safety_assumptions]] — "Chi phí xử lý không tăng ngoài ngân sách khi trạng thái thay đổi." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:74C44A41A6BA4045B073D6AB: Description / Potential Mitigations; topic=WEAKNESS:CWE-400 — [[EVIDENCE-74C44A41A6BA4045B073D6AB\|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]] |
| [[CLAIM-0C615F17B2CDC66A1C2EDEE5\|WEAKNESS:CWE-400: related_failure_classes]] — "Resource exhaustion" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:74C44A41A6BA4045B073D6AB: Description / Potential Mitigations; topic=WEAKNESS:CWE-400 — [[EVIDENCE-74C44A41A6BA4045B073D6AB\|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]] |
| [[CLAIM-D84C9125F768D91DC11635AB\|WEAKNESS:CWE-400: failure_impact]] — "Suy giảm availability." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:74C44A41A6BA4045B073D6AB: Description / Potential Mitigations; topic=WEAKNESS:CWE-400 — [[EVIDENCE-74C44A41A6BA4045B073D6AB\|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]] |
| [[CLAIM-FAA88F5D0DECD0B03B566759\|WEAKNESS:CWE-400: defensive_principles]] — "Đo nguồn lực, đặt hạn mức và timeout dựa trên workload." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:74C44A41A6BA4045B073D6AB: Description / Potential Mitigations; topic=WEAKNESS:CWE-400 — [[EVIDENCE-74C44A41A6BA4045B073D6AB\|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-0838953B2BE98F7124CC4F87|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]], [[EVIDENCE-74C44A41A6BA4045B073D6AB|CWE - CWE-400: Uncontrolled Resource Consumption (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

