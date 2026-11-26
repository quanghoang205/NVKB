---
entity_type: weakness
id: WEAKNESS:CWE-120
title: CWE-120 — Buffer overflow
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-120 — Buffer overflow
tags:
- nginx
- weakness
- knowledge
---

# CWE-120 — Buffer overflow

Ghi dữ liệu vượt dung lượng buffer đích.

## Mục tiêu đo được

- Giải thích CWE-120 — Buffer overflow bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Ghi dữ liệu vượt dung lượng buffer đích.

## Cơ chế hoạt động bình thường

Độ dài đầu vào phải được kiểm tra so với vùng đích trước thao tác sao chép.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Kích thước được tính không tràn và bao gồm mọi byte phụ trợ.

## Nhóm lỗi liên quan

Buffer overflow

## Tác động khi giả định bị vi phạm

Hỏng bộ nhớ hoặc crash tùy vị trí và điều kiện.

## Nguyên tắc phòng vệ

Kiểm tra capacity/length, dùng API có giới hạn và công cụ phát hiện lỗi bộ nhớ.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-B78EE973DB8F00DCF089639C\|WEAKNESS:CWE-120: definition]] — "Ghi dữ liệu vượt dung lượng buffer đích." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:BF818BD2C0248E0A0E1C69B0: Description / Potential Mitigations; topic=WEAKNESS:CWE-120 — [[EVIDENCE-BF818BD2C0248E0A0E1C69B0\|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]] |
| [[CLAIM-06F2FEDE03706BBBF3920B06\|WEAKNESS:CWE-120: normal_behavior]] — "Độ dài đầu vào phải được kiểm tra so với vùng đích trước thao tác sao chép." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:BF818BD2C0248E0A0E1C69B0: Description / Potential Mitigations; topic=WEAKNESS:CWE-120 — [[EVIDENCE-BF818BD2C0248E0A0E1C69B0\|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]] |
| [[CLAIM-438875123DF87062EE3E12D9\|WEAKNESS:CWE-120: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:BF818BD2C0248E0A0E1C69B0: Description / Potential Mitigations; topic=WEAKNESS:CWE-120 — [[EVIDENCE-BF818BD2C0248E0A0E1C69B0\|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]] |
| [[CLAIM-E78186414DF73521660AED51\|WEAKNESS:CWE-120: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:BF818BD2C0248E0A0E1C69B0: Description / Potential Mitigations; topic=WEAKNESS:CWE-120 — [[EVIDENCE-BF818BD2C0248E0A0E1C69B0\|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]] |
| [[CLAIM-64D93046220EC97D6093B60E\|WEAKNESS:CWE-120: safety_assumptions]] — "Kích thước được tính không tràn và bao gồm mọi byte phụ trợ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:BF818BD2C0248E0A0E1C69B0: Description / Potential Mitigations; topic=WEAKNESS:CWE-120 — [[EVIDENCE-BF818BD2C0248E0A0E1C69B0\|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]] |
| [[CLAIM-C64065B5FD47088F5F8B96D3\|WEAKNESS:CWE-120: related_failure_classes]] — "Buffer overflow" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:BF818BD2C0248E0A0E1C69B0: Description / Potential Mitigations; topic=WEAKNESS:CWE-120 — [[EVIDENCE-BF818BD2C0248E0A0E1C69B0\|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]] |
| [[CLAIM-2E0C14C0590DB868EF90A1B2\|WEAKNESS:CWE-120: failure_impact]] — "Hỏng bộ nhớ hoặc crash tùy vị trí và điều kiện." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:BF818BD2C0248E0A0E1C69B0: Description / Potential Mitigations; topic=WEAKNESS:CWE-120 — [[EVIDENCE-BF818BD2C0248E0A0E1C69B0\|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]] |
| [[CLAIM-AD8FC3996A06E0EA0EACB0CC\|WEAKNESS:CWE-120: defensive_principles]] — "Kiểm tra capacity/length, dùng API có giới hạn và công cụ phát hiện lỗi bộ nhớ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:BF818BD2C0248E0A0E1C69B0: Description / Potential Mitigations; topic=WEAKNESS:CWE-120 — [[EVIDENCE-BF818BD2C0248E0A0E1C69B0\|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-28D21A886526208768AB863F|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]], [[EVIDENCE-BF818BD2C0248E0A0E1C69B0|CWE - CWE-120: Buffer Copy without Checking Size of Input (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

