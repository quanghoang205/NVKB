---
entity_type: weakness
id: WEAKNESS:CWE-789
title: CWE-789 — Excessive Memory Allocation
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-789 — Excessive Memory Allocation
tags:
- nginx
- weakness
- knowledge
---

# CWE-789 — Excessive Memory Allocation

Kích thước cấp phát bộ nhớ vượt ngân sách hợp lý do giá trị đầu vào.

## Mục tiêu đo được

- Giải thích CWE-789 — Excessive Memory Allocation bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Kích thước cấp phát bộ nhớ vượt ngân sách hợp lý do giá trị đầu vào.

## Cơ chế hoạt động bình thường

Kích thước allocation phải được kiểm tra theo giới hạn và khả năng xử lý.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Kích thước allocation phải được kiểm tra theo giới hạn và khả năng xử lý.

## Nhóm lỗi liên quan

Excessive Memory Allocation

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Đặt trần tài nguyên, xử lý lỗi cấp phát và giới hạn các giá trị dẫn xuất.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-CF4F61C3B6DD32688EB91E57\|WEAKNESS:CWE-789: definition]] — "Kích thước cấp phát bộ nhớ vượt ngân sách hợp lý do giá trị đầu vào." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:10D1CE64C7D374A3FFA0935A: Description / Potential Mitigations; topic=WEAKNESS:CWE-789 — [[EVIDENCE-10D1CE64C7D374A3FFA0935A\|CWE - CWE-789: Memory Allocation with Excessive Size Value (5.0)]] |
| [[CLAIM-7078653912747AD75E7C88D0\|WEAKNESS:CWE-789: normal_behavior]] — "Kích thước allocation phải được kiểm tra theo giới hạn và khả năng xử lý." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:10D1CE64C7D374A3FFA0935A: Description / Potential Mitigations; topic=WEAKNESS:CWE-789 — [[EVIDENCE-10D1CE64C7D374A3FFA0935A\|CWE - CWE-789: Memory Allocation with Excessive Size Value (5.0)]] |
| [[CLAIM-AF35BD6FA6555EA77A6187BB\|WEAKNESS:CWE-789: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:10D1CE64C7D374A3FFA0935A: Description / Potential Mitigations; topic=WEAKNESS:CWE-789 — [[EVIDENCE-10D1CE64C7D374A3FFA0935A\|CWE - CWE-789: Memory Allocation with Excessive Size Value (5.0)]] |
| [[CLAIM-24758A84B57E6462FF16036A\|WEAKNESS:CWE-789: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:10D1CE64C7D374A3FFA0935A: Description / Potential Mitigations; topic=WEAKNESS:CWE-789 — [[EVIDENCE-10D1CE64C7D374A3FFA0935A\|CWE - CWE-789: Memory Allocation with Excessive Size Value (5.0)]] |
| [[CLAIM-EDD45578614494D98D51972B\|WEAKNESS:CWE-789: safety_assumptions]] — "Kích thước allocation phải được kiểm tra theo giới hạn và khả năng xử lý." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:10D1CE64C7D374A3FFA0935A: Description / Potential Mitigations; topic=WEAKNESS:CWE-789 — [[EVIDENCE-10D1CE64C7D374A3FFA0935A\|CWE - CWE-789: Memory Allocation with Excessive Size Value (5.0)]] |
| [[CLAIM-99D57B2B61C409A4E7118C81\|WEAKNESS:CWE-789: related_failure_classes]] — "Excessive Memory Allocation" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:10D1CE64C7D374A3FFA0935A: Description / Potential Mitigations; topic=WEAKNESS:CWE-789 — [[EVIDENCE-10D1CE64C7D374A3FFA0935A\|CWE - CWE-789: Memory Allocation with Excessive Size Value (5.0)]] |
| [[CLAIM-9473A915B2CEC1A7A96BF589\|WEAKNESS:CWE-789: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:10D1CE64C7D374A3FFA0935A: Description / Potential Mitigations; topic=WEAKNESS:CWE-789 — [[EVIDENCE-10D1CE64C7D374A3FFA0935A\|CWE - CWE-789: Memory Allocation with Excessive Size Value (5.0)]] |
| [[CLAIM-7D30B296B7A7F29953AE3048\|WEAKNESS:CWE-789: defensive_principles]] — "Đặt trần tài nguyên, xử lý lỗi cấp phát và giới hạn các giá trị dẫn xuất." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:10D1CE64C7D374A3FFA0935A: Description / Potential Mitigations; topic=WEAKNESS:CWE-789 — [[EVIDENCE-10D1CE64C7D374A3FFA0935A\|CWE - CWE-789: Memory Allocation with Excessive Size Value (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-10D1CE64C7D374A3FFA0935A|CWE - CWE-789: Memory Allocation with Excessive Size Value (5.0)]], [[EVIDENCE-ECF1840A41504F1DC886C7C7|CVE-2026-42946]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

