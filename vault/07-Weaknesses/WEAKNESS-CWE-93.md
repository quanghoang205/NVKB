---
entity_type: weakness
id: WEAKNESS:CWE-93
title: CWE-93 — CRLF Injection
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-93 — CRLF Injection
tags:
- nginx
- weakness
- knowledge
---

# CWE-93 — CRLF Injection

Không xử lý đúng ký tự phân cách CR/LF khi tạo dữ liệu có cấu trúc dòng.

## Mục tiêu đo được

- Giải thích CWE-93 — CRLF Injection bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Không xử lý đúng ký tự phân cách CR/LF khi tạo dữ liệu có cấu trúc dòng.

## Cơ chế hoạt động bình thường

Dữ liệu và ký tự điều khiển framing phải được phân biệt khi tuần tự hóa.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Dữ liệu và ký tự điều khiển framing phải được phân biệt khi tuần tự hóa.

## Nhóm lỗi liên quan

CRLF Injection

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Dùng encoder theo giao thức và kiểm tra giá trị không được chứa dấu phân cách.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-3DEB79AA46C1BD0D874FC17A\|WEAKNESS:CWE-93: definition]] — "Không xử lý đúng ký tự phân cách CR/LF khi tạo dữ liệu có cấu trúc dòng." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D6FC4E12FED72955B93B5303: Description / Potential Mitigations; topic=WEAKNESS:CWE-93 — [[EVIDENCE-D6FC4E12FED72955B93B5303\|CWE - CWE-93: Improper Neutralization of CRLF Sequences (5.0)]] |
| [[CLAIM-A7E74D3787C72852B343470C\|WEAKNESS:CWE-93: normal_behavior]] — "Dữ liệu và ký tự điều khiển framing phải được phân biệt khi tuần tự hóa." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D6FC4E12FED72955B93B5303: Description / Potential Mitigations; topic=WEAKNESS:CWE-93 — [[EVIDENCE-D6FC4E12FED72955B93B5303\|CWE - CWE-93: Improper Neutralization of CRLF Sequences (5.0)]] |
| [[CLAIM-B4A7CCDBF35B61B3A5277CAB\|WEAKNESS:CWE-93: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D6FC4E12FED72955B93B5303: Description / Potential Mitigations; topic=WEAKNESS:CWE-93 — [[EVIDENCE-D6FC4E12FED72955B93B5303\|CWE - CWE-93: Improper Neutralization of CRLF Sequences (5.0)]] |
| [[CLAIM-C1A7347DA287C62E796C4FFD\|WEAKNESS:CWE-93: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D6FC4E12FED72955B93B5303: Description / Potential Mitigations; topic=WEAKNESS:CWE-93 — [[EVIDENCE-D6FC4E12FED72955B93B5303\|CWE - CWE-93: Improper Neutralization of CRLF Sequences (5.0)]] |
| [[CLAIM-96454F659377CA29AF45B8BF\|WEAKNESS:CWE-93: safety_assumptions]] — "Dữ liệu và ký tự điều khiển framing phải được phân biệt khi tuần tự hóa." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D6FC4E12FED72955B93B5303: Description / Potential Mitigations; topic=WEAKNESS:CWE-93 — [[EVIDENCE-D6FC4E12FED72955B93B5303\|CWE - CWE-93: Improper Neutralization of CRLF Sequences (5.0)]] |
| [[CLAIM-DB4AAA7A1BB0521D31B32D18\|WEAKNESS:CWE-93: related_failure_classes]] — "CRLF Injection" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D6FC4E12FED72955B93B5303: Description / Potential Mitigations; topic=WEAKNESS:CWE-93 — [[EVIDENCE-D6FC4E12FED72955B93B5303\|CWE - CWE-93: Improper Neutralization of CRLF Sequences (5.0)]] |
| [[CLAIM-AB01914CC118781E202D71FA\|WEAKNESS:CWE-93: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D6FC4E12FED72955B93B5303: Description / Potential Mitigations; topic=WEAKNESS:CWE-93 — [[EVIDENCE-D6FC4E12FED72955B93B5303\|CWE - CWE-93: Improper Neutralization of CRLF Sequences (5.0)]] |
| [[CLAIM-6161E52695D8475ECADCE557\|WEAKNESS:CWE-93: defensive_principles]] — "Dùng encoder theo giao thức và kiểm tra giá trị không được chứa dấu phân cách." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:D6FC4E12FED72955B93B5303: Description / Potential Mitigations; topic=WEAKNESS:CWE-93 — [[EVIDENCE-D6FC4E12FED72955B93B5303\|CWE - CWE-93: Improper Neutralization of CRLF Sequences (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-D6FC4E12FED72955B93B5303|CWE - CWE-93: Improper Neutralization of CRLF Sequences (5.0)]], [[EVIDENCE-F6B37E93E32E5B5F09F042E3|CVE-2026-28753]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

