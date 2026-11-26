---
entity_type: weakness
id: WEAKNESS:CWE-823
title: CWE-823 — Out-of-range Pointer Offset
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-823 — Out-of-range Pointer Offset
tags:
- nginx
- weakness
- knowledge
---

# CWE-823 — Out-of-range Pointer Offset

Dùng offset con trỏ nằm ngoài vùng đối tượng hợp lệ.

## Mục tiêu đo được

- Giải thích CWE-823 — Out-of-range Pointer Offset bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Dùng offset con trỏ nằm ngoài vùng đối tượng hợp lệ.

## Cơ chế hoạt động bình thường

Phép tính địa chỉ phải giữ con trỏ trong phạm vi vùng nhớ được sở hữu.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Phép tính địa chỉ phải giữ con trỏ trong phạm vi vùng nhớ được sở hữu.

## Nhóm lỗi liên quan

Out-of-range Pointer Offset

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Kiểm tra cả offset và số byte truy cập trước khi tạo/giải tham chiếu con trỏ.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-6DBC54DE46838C31FB9F2A83\|WEAKNESS:CWE-823: definition]] — "Dùng offset con trỏ nằm ngoài vùng đối tượng hợp lệ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:90C3D812878A1FE5CC409A23: Description / Potential Mitigations; topic=WEAKNESS:CWE-823 — [[EVIDENCE-90C3D812878A1FE5CC409A23\|CWE - CWE-823: Use of Out-of-range Pointer Offset (5.0)]] |
| [[CLAIM-9F16AA3256747818611A68F5\|WEAKNESS:CWE-823: normal_behavior]] — "Phép tính địa chỉ phải giữ con trỏ trong phạm vi vùng nhớ được sở hữu." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:90C3D812878A1FE5CC409A23: Description / Potential Mitigations; topic=WEAKNESS:CWE-823 — [[EVIDENCE-90C3D812878A1FE5CC409A23\|CWE - CWE-823: Use of Out-of-range Pointer Offset (5.0)]] |
| [[CLAIM-534EC6E449F83585DF836246\|WEAKNESS:CWE-823: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:90C3D812878A1FE5CC409A23: Description / Potential Mitigations; topic=WEAKNESS:CWE-823 — [[EVIDENCE-90C3D812878A1FE5CC409A23\|CWE - CWE-823: Use of Out-of-range Pointer Offset (5.0)]] |
| [[CLAIM-34551A0564208C1024FA11D5\|WEAKNESS:CWE-823: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:90C3D812878A1FE5CC409A23: Description / Potential Mitigations; topic=WEAKNESS:CWE-823 — [[EVIDENCE-90C3D812878A1FE5CC409A23\|CWE - CWE-823: Use of Out-of-range Pointer Offset (5.0)]] |
| [[CLAIM-7EE9E1726626D8EA43AAC578\|WEAKNESS:CWE-823: safety_assumptions]] — "Phép tính địa chỉ phải giữ con trỏ trong phạm vi vùng nhớ được sở hữu." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:90C3D812878A1FE5CC409A23: Description / Potential Mitigations; topic=WEAKNESS:CWE-823 — [[EVIDENCE-90C3D812878A1FE5CC409A23\|CWE - CWE-823: Use of Out-of-range Pointer Offset (5.0)]] |
| [[CLAIM-A2D8D58B3EE3C5C71D4B5E95\|WEAKNESS:CWE-823: related_failure_classes]] — "Out-of-range Pointer Offset" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:90C3D812878A1FE5CC409A23: Description / Potential Mitigations; topic=WEAKNESS:CWE-823 — [[EVIDENCE-90C3D812878A1FE5CC409A23\|CWE - CWE-823: Use of Out-of-range Pointer Offset (5.0)]] |
| [[CLAIM-59DF8A2D5574DE8B7594F875\|WEAKNESS:CWE-823: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:90C3D812878A1FE5CC409A23: Description / Potential Mitigations; topic=WEAKNESS:CWE-823 — [[EVIDENCE-90C3D812878A1FE5CC409A23\|CWE - CWE-823: Use of Out-of-range Pointer Offset (5.0)]] |
| [[CLAIM-326093C7EE52F5F4154AE02F\|WEAKNESS:CWE-823: defensive_principles]] — "Kiểm tra cả offset và số byte truy cập trước khi tạo/giải tham chiếu con trỏ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:90C3D812878A1FE5CC409A23: Description / Potential Mitigations; topic=WEAKNESS:CWE-823 — [[EVIDENCE-90C3D812878A1FE5CC409A23\|CWE - CWE-823: Use of Out-of-range Pointer Offset (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-90C3D812878A1FE5CC409A23|CWE - CWE-823: Use of Out-of-range Pointer Offset (5.0)]], [[EVIDENCE-ECF1840A41504F1DC886C7C7|CVE-2026-42946]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

