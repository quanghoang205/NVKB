---
entity_type: weakness
id: WEAKNESS:CWE-349
title: CWE-349 — Untrusted Data with Trusted Data
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-349 — Untrusted Data with Trusted Data
tags:
- nginx
- weakness
- knowledge
---

# CWE-349 — Untrusted Data with Trusted Data

Chấp nhận dữ liệu không tin cậy bổ sung cùng dữ liệu được xem là tin cậy.

## Mục tiêu đo được

- Giải thích CWE-349 — Untrusted Data with Trusted Data bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Chấp nhận dữ liệu không tin cậy bổ sung cùng dữ liệu được xem là tin cậy.

## Cơ chế hoạt động bình thường

Nguồn gốc và phạm vi của từng phần dữ liệu phải được giữ riêng qua quá trình hợp nhất.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Nguồn gốc và phạm vi của từng phần dữ liệu phải được giữ riêng qua quá trình hợp nhất.

## Nhóm lỗi liên quan

Untrusted Data with Trusted Data

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Theo dõi provenance, framing và quyền của từng nguồn dữ liệu.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-BCCCBBF12BB8910E3DE93B35\|WEAKNESS:CWE-349: definition]] — "Chấp nhận dữ liệu không tin cậy bổ sung cùng dữ liệu được xem là tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:8AD94753451D74F7F738AEA6: Description / Potential Mitigations; topic=WEAKNESS:CWE-349 — [[EVIDENCE-8AD94753451D74F7F738AEA6\|CWE - CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data (5.0)]] |
| [[CLAIM-AF70DE6A330585B16DE3C1A0\|WEAKNESS:CWE-349: normal_behavior]] — "Nguồn gốc và phạm vi của từng phần dữ liệu phải được giữ riêng qua quá trình hợp nhất." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:8AD94753451D74F7F738AEA6: Description / Potential Mitigations; topic=WEAKNESS:CWE-349 — [[EVIDENCE-8AD94753451D74F7F738AEA6\|CWE - CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data (5.0)]] |
| [[CLAIM-3D9D29089EB1E262AF2EFD8A\|WEAKNESS:CWE-349: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:8AD94753451D74F7F738AEA6: Description / Potential Mitigations; topic=WEAKNESS:CWE-349 — [[EVIDENCE-8AD94753451D74F7F738AEA6\|CWE - CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data (5.0)]] |
| [[CLAIM-356F1624D9EAE4074F2C5DAD\|WEAKNESS:CWE-349: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:8AD94753451D74F7F738AEA6: Description / Potential Mitigations; topic=WEAKNESS:CWE-349 — [[EVIDENCE-8AD94753451D74F7F738AEA6\|CWE - CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data (5.0)]] |
| [[CLAIM-D3D5084FCF6DEF9BB5195031\|WEAKNESS:CWE-349: safety_assumptions]] — "Nguồn gốc và phạm vi của từng phần dữ liệu phải được giữ riêng qua quá trình hợp nhất." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:8AD94753451D74F7F738AEA6: Description / Potential Mitigations; topic=WEAKNESS:CWE-349 — [[EVIDENCE-8AD94753451D74F7F738AEA6\|CWE - CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data (5.0)]] |
| [[CLAIM-148C2588642A882AA8F53787\|WEAKNESS:CWE-349: related_failure_classes]] — "Untrusted Data with Trusted Data" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:8AD94753451D74F7F738AEA6: Description / Potential Mitigations; topic=WEAKNESS:CWE-349 — [[EVIDENCE-8AD94753451D74F7F738AEA6\|CWE - CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data (5.0)]] |
| [[CLAIM-7D7EB98A8314079DD2029C24\|WEAKNESS:CWE-349: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:8AD94753451D74F7F738AEA6: Description / Potential Mitigations; topic=WEAKNESS:CWE-349 — [[EVIDENCE-8AD94753451D74F7F738AEA6\|CWE - CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data (5.0)]] |
| [[CLAIM-D8BC36E7C775548591BD9D4D\|WEAKNESS:CWE-349: defensive_principles]] — "Theo dõi provenance, framing và quyền của từng nguồn dữ liệu." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:8AD94753451D74F7F738AEA6: Description / Potential Mitigations; topic=WEAKNESS:CWE-349 — [[EVIDENCE-8AD94753451D74F7F738AEA6\|CWE - CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-390C6877B8808296F820D86C|CVE-2026-1642]], [[EVIDENCE-8AD94753451D74F7F738AEA6|CWE - CWE-349: Acceptance of Extraneous Untrusted Data With Trusted Data (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

