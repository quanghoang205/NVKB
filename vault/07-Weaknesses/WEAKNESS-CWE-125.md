---
entity_type: weakness
id: WEAKNESS:CWE-125
title: CWE-125 — Out-of-bounds read
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-125 — Out-of-bounds read
tags:
- nginx
- weakness
- knowledge
---

# CWE-125 — Out-of-bounds read

Đọc ngoài giới hạn một vùng bộ nhớ hợp lệ.

## Mục tiêu đo được

- Giải thích CWE-125 — Out-of-bounds read bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Đọc ngoài giới hạn một vùng bộ nhớ hợp lệ.

## Cơ chế hoạt động bình thường

Index và offset được kiểm tra trong phạm vi đối tượng trước khi đọc.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Offset, chiều dài và vòng đời đối tượng đều còn hợp lệ.

## Nhóm lỗi liên quan

Out-of-bounds read

## Tác động khi giả định bị vi phạm

Đọc nhầm dữ liệu, crash hoặc lộ bộ nhớ theo advisory.

## Nguyên tắc phòng vệ

Kiểm tra biên ở mọi đường đọc và bảo đảm parser xử lý dữ liệu bị cắt ngắn.






## Quan hệ có định kiểu

- `CONTEXTUAL_ASSOCIATION` → [[IMPACT-LIMITED-MEMORY-DISCLOSURE|Tiết lộ bộ nhớ giới hạn]] — Nguồn 48142 nêu limited disclosure; chưa xác định loại dữ liệu. Quyền thấp giảm phạm vi tiếp cận, không sửa over-read. Lớp lỗi được CNA gán trong case này; impact là mô tả nguồn riêng, không suy từ CWE. **INTERPRETATION / PARTIAL**.
- `CONTEXTUAL_ASSOCIATION` → [[IMPACT-WORKER-TERMINATION|Worker termination trong phạm vi process]] — Nguồn 7347 nêu worker kết thúc; không mở rộng thành host/root compromise. Lớp lỗi được CNA gán trong case này; impact là mô tả nguồn riêng, không suy từ CWE. **INTERPRETATION / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-5DEB8014C341BE35357890C9\|WEAKNESS:CWE-125: definition]] — "Đọc ngoài giới hạn một vùng bộ nhớ hợp lệ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A8E0CD4EC39541F68F84D25F: Description / Potential Mitigations; topic=WEAKNESS:CWE-125 — [[EVIDENCE-A8E0CD4EC39541F68F84D25F\|CWE - CWE-125: Out-of-bounds Read (5.0)]] |
| [[CLAIM-A1B7C779890BE13284E0DD94\|WEAKNESS:CWE-125: normal_behavior]] — "Index và offset được kiểm tra trong phạm vi đối tượng trước khi đọc." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A8E0CD4EC39541F68F84D25F: Description / Potential Mitigations; topic=WEAKNESS:CWE-125 — [[EVIDENCE-A8E0CD4EC39541F68F84D25F\|CWE - CWE-125: Out-of-bounds Read (5.0)]] |
| [[CLAIM-CF0568F5EC23A1332C2819D6\|WEAKNESS:CWE-125: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A8E0CD4EC39541F68F84D25F: Description / Potential Mitigations; topic=WEAKNESS:CWE-125 — [[EVIDENCE-A8E0CD4EC39541F68F84D25F\|CWE - CWE-125: Out-of-bounds Read (5.0)]] |
| [[CLAIM-7DE7C35B3E8D337642CEA73F\|WEAKNESS:CWE-125: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A8E0CD4EC39541F68F84D25F: Description / Potential Mitigations; topic=WEAKNESS:CWE-125 — [[EVIDENCE-A8E0CD4EC39541F68F84D25F\|CWE - CWE-125: Out-of-bounds Read (5.0)]] |
| [[CLAIM-F814B1AF6B6225E3FAC62503\|WEAKNESS:CWE-125: safety_assumptions]] — "Offset, chiều dài và vòng đời đối tượng đều còn hợp lệ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A8E0CD4EC39541F68F84D25F: Description / Potential Mitigations; topic=WEAKNESS:CWE-125 — [[EVIDENCE-A8E0CD4EC39541F68F84D25F\|CWE - CWE-125: Out-of-bounds Read (5.0)]] |
| [[CLAIM-9A3AF95D2E9086CDC8F1F65B\|WEAKNESS:CWE-125: related_failure_classes]] — "Out-of-bounds read" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A8E0CD4EC39541F68F84D25F: Description / Potential Mitigations; topic=WEAKNESS:CWE-125 — [[EVIDENCE-A8E0CD4EC39541F68F84D25F\|CWE - CWE-125: Out-of-bounds Read (5.0)]] |
| [[CLAIM-0F417F14B72717121BEF2EF4\|WEAKNESS:CWE-125: failure_impact]] — "Đọc nhầm dữ liệu, crash hoặc lộ bộ nhớ theo advisory." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A8E0CD4EC39541F68F84D25F: Description / Potential Mitigations; topic=WEAKNESS:CWE-125 — [[EVIDENCE-A8E0CD4EC39541F68F84D25F\|CWE - CWE-125: Out-of-bounds Read (5.0)]] |
| [[CLAIM-320ABAF1E3A39289B2BB897E\|WEAKNESS:CWE-125: defensive_principles]] — "Kiểm tra biên ở mọi đường đọc và bảo đảm parser xử lý dữ liệu bị cắt ngắn." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:A8E0CD4EC39541F68F84D25F: Description / Potential Mitigations; topic=WEAKNESS:CWE-125 — [[EVIDENCE-A8E0CD4EC39541F68F84D25F\|CWE - CWE-125: Out-of-bounds Read (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-662C7E7EF279A8418B10DAAC|CVE-2026-42934]], [[EVIDENCE-7BB1B2DFE97D5E0D0A8019E0|CVE-2025-53859]], [[EVIDENCE-A8E0CD4EC39541F68F84D25F|CWE - CWE-125: Out-of-bounds Read (5.0)]], [[EVIDENCE-C64041668867A3477B753896|CVE-2026-48142]], [[EVIDENCE-F43E09B91F0D0A09B4E42149|CWE - CWE-125: Out-of-bounds Read (5.0)]], [[EVIDENCE-FB2A7E51F617D62E623BB202|CVE-2026-32647]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

