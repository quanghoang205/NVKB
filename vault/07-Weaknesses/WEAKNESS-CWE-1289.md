---
entity_type: weakness
id: WEAKNESS:CWE-1289
title: CWE-1289 — Unsafe Equivalence in Input
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-1289 — Unsafe Equivalence in Input
tags:
- nginx
- weakness
- knowledge
---

# CWE-1289 — Unsafe Equivalence in Input

Xem hai biểu diễn input là tương đương khi phép tương đương không an toàn.

## Mục tiêu đo được

- Giải thích CWE-1289 — Unsafe Equivalence in Input bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Xem hai biểu diễn input là tương đương khi phép tương đương không an toàn.

## Cơ chế hoạt động bình thường

Quy tắc chuẩn hóa và so sánh phải giữ nguyên ý nghĩa bảo mật.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Quy tắc chuẩn hóa và so sánh phải giữ nguyên ý nghĩa bảo mật.

## Nhóm lỗi liên quan

Unsafe Equivalence in Input

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Xác định canonical representation và kiểm tra cùng policy ở các lớp.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-67B9EC490C46CCA2495C828C\|WEAKNESS:CWE-1289: definition]] — "Xem hai biểu diễn input là tương đương khi phép tương đương không an toàn." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:89A71DECA0CDA7465848AA99: Description / Potential Mitigations; topic=WEAKNESS:CWE-1289 — [[EVIDENCE-89A71DECA0CDA7465848AA99\|CWE - CWE-1289: Improper Validation of Unsafe Equivalence in Input (5.0)]] |
| [[CLAIM-43CEBCA8B3B3D6D96B86DAA8\|WEAKNESS:CWE-1289: normal_behavior]] — "Quy tắc chuẩn hóa và so sánh phải giữ nguyên ý nghĩa bảo mật." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:89A71DECA0CDA7465848AA99: Description / Potential Mitigations; topic=WEAKNESS:CWE-1289 — [[EVIDENCE-89A71DECA0CDA7465848AA99\|CWE - CWE-1289: Improper Validation of Unsafe Equivalence in Input (5.0)]] |
| [[CLAIM-AFADD1530EEF781CB56C34DD\|WEAKNESS:CWE-1289: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:89A71DECA0CDA7465848AA99: Description / Potential Mitigations; topic=WEAKNESS:CWE-1289 — [[EVIDENCE-89A71DECA0CDA7465848AA99\|CWE - CWE-1289: Improper Validation of Unsafe Equivalence in Input (5.0)]] |
| [[CLAIM-A21E9F3B0A0B446717C068DD\|WEAKNESS:CWE-1289: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:89A71DECA0CDA7465848AA99: Description / Potential Mitigations; topic=WEAKNESS:CWE-1289 — [[EVIDENCE-89A71DECA0CDA7465848AA99\|CWE - CWE-1289: Improper Validation of Unsafe Equivalence in Input (5.0)]] |
| [[CLAIM-685852DDEF91C87533D0CC36\|WEAKNESS:CWE-1289: safety_assumptions]] — "Quy tắc chuẩn hóa và so sánh phải giữ nguyên ý nghĩa bảo mật." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:89A71DECA0CDA7465848AA99: Description / Potential Mitigations; topic=WEAKNESS:CWE-1289 — [[EVIDENCE-89A71DECA0CDA7465848AA99\|CWE - CWE-1289: Improper Validation of Unsafe Equivalence in Input (5.0)]] |
| [[CLAIM-8654A56DFD4A5C620D3DE936\|WEAKNESS:CWE-1289: related_failure_classes]] — "Unsafe Equivalence in Input" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:89A71DECA0CDA7465848AA99: Description / Potential Mitigations; topic=WEAKNESS:CWE-1289 — [[EVIDENCE-89A71DECA0CDA7465848AA99\|CWE - CWE-1289: Improper Validation of Unsafe Equivalence in Input (5.0)]] |
| [[CLAIM-AD784617D468CBD33821C150\|WEAKNESS:CWE-1289: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:89A71DECA0CDA7465848AA99: Description / Potential Mitigations; topic=WEAKNESS:CWE-1289 — [[EVIDENCE-89A71DECA0CDA7465848AA99\|CWE - CWE-1289: Improper Validation of Unsafe Equivalence in Input (5.0)]] |
| [[CLAIM-9B8E1E02AAFC4CA4B14072BE\|WEAKNESS:CWE-1289: defensive_principles]] — "Xác định canonical representation và kiểm tra cùng policy ở các lớp." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:89A71DECA0CDA7465848AA99: Description / Potential Mitigations; topic=WEAKNESS:CWE-1289 — [[EVIDENCE-89A71DECA0CDA7465848AA99\|CWE - CWE-1289: Improper Validation of Unsafe Equivalence in Input (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-423B8012C6D7EE5916766C00|CVE-2026-120967]], [[EVIDENCE-71362C6FD38E82A400DFCC59|CVE-2026-123640]], [[EVIDENCE-89A71DECA0CDA7465848AA99|CWE - CWE-1289: Improper Validation of Unsafe Equivalence in Input (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

