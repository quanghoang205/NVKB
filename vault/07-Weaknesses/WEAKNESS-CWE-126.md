---
entity_type: weakness
id: WEAKNESS:CWE-126
title: CWE-126 — Buffer Over-read
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-126 — Buffer Over-read
tags:
- nginx
- weakness
- knowledge
---

# CWE-126 — Buffer Over-read

Đọc tiếp qua cuối buffer chứa dữ liệu.

## Mục tiêu đo được

- Giải thích CWE-126 — Buffer Over-read bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Đọc tiếp qua cuối buffer chứa dữ liệu.

## Cơ chế hoạt động bình thường

Parser theo dõi số byte còn lại, không dùng sentinel ngoài vùng hợp lệ.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Parser theo dõi số byte còn lại, không dùng sentinel ngoài vùng hợp lệ.

## Nhóm lỗi liên quan

Buffer Over-read

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Kiểm tra length trước đọc và xử lý input bị cắt ngắn.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-B6D2A95BD14C155B29EA8AC4\|WEAKNESS:CWE-126: definition]] — "Đọc tiếp qua cuối buffer chứa dữ liệu." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2739A81C1376F4477260234A: Description / Potential Mitigations; topic=WEAKNESS:CWE-126 — [[EVIDENCE-2739A81C1376F4477260234A\|CWE - CWE-126: Buffer Over-read (5.0)]] |
| [[CLAIM-379DECE7F0A36B9D04E25797\|WEAKNESS:CWE-126: normal_behavior]] — "Parser theo dõi số byte còn lại, không dùng sentinel ngoài vùng hợp lệ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2739A81C1376F4477260234A: Description / Potential Mitigations; topic=WEAKNESS:CWE-126 — [[EVIDENCE-2739A81C1376F4477260234A\|CWE - CWE-126: Buffer Over-read (5.0)]] |
| [[CLAIM-287E5D285FE17D543870B900\|WEAKNESS:CWE-126: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2739A81C1376F4477260234A: Description / Potential Mitigations; topic=WEAKNESS:CWE-126 — [[EVIDENCE-2739A81C1376F4477260234A\|CWE - CWE-126: Buffer Over-read (5.0)]] |
| [[CLAIM-1568B512E7C0922322C24D72\|WEAKNESS:CWE-126: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2739A81C1376F4477260234A: Description / Potential Mitigations; topic=WEAKNESS:CWE-126 — [[EVIDENCE-2739A81C1376F4477260234A\|CWE - CWE-126: Buffer Over-read (5.0)]] |
| [[CLAIM-90D3A0B9ABE7725A0229144C\|WEAKNESS:CWE-126: safety_assumptions]] — "Parser theo dõi số byte còn lại, không dùng sentinel ngoài vùng hợp lệ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2739A81C1376F4477260234A: Description / Potential Mitigations; topic=WEAKNESS:CWE-126 — [[EVIDENCE-2739A81C1376F4477260234A\|CWE - CWE-126: Buffer Over-read (5.0)]] |
| [[CLAIM-A985F686E280CBB94CBDD715\|WEAKNESS:CWE-126: related_failure_classes]] — "Buffer Over-read" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2739A81C1376F4477260234A: Description / Potential Mitigations; topic=WEAKNESS:CWE-126 — [[EVIDENCE-2739A81C1376F4477260234A\|CWE - CWE-126: Buffer Over-read (5.0)]] |
| [[CLAIM-54DED47C4CCE0AD3D0F9DB2C\|WEAKNESS:CWE-126: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2739A81C1376F4477260234A: Description / Potential Mitigations; topic=WEAKNESS:CWE-126 — [[EVIDENCE-2739A81C1376F4477260234A\|CWE - CWE-126: Buffer Over-read (5.0)]] |
| [[CLAIM-DA099B0D55F71810979AC552\|WEAKNESS:CWE-126: defensive_principles]] — "Kiểm tra length trước đọc và xử lý input bị cắt ngắn." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:2739A81C1376F4477260234A: Description / Potential Mitigations; topic=WEAKNESS:CWE-126 — [[EVIDENCE-2739A81C1376F4477260234A\|CWE - CWE-126: Buffer Over-read (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-2739A81C1376F4477260234A|CWE - CWE-126: Buffer Over-read (5.0)]], [[EVIDENCE-96277BC472ED92F8657D0FC0|CVE-2024-7347]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

