---
entity_type: weakness
id: WEAKNESS:CWE-476
title: CWE-476 — NULL pointer dereference
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-476 — NULL pointer dereference
tags:
- nginx
- weakness
- knowledge
---

# CWE-476 — NULL pointer dereference

Truy cập qua con trỏ NULL.

## Mục tiêu đo được

- Giải thích CWE-476 — NULL pointer dereference bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Truy cập qua con trỏ NULL.

## Cơ chế hoạt động bình thường

Kết quả allocation/lookup được kiểm tra trước khi dùng trường dữ liệu.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Đường lỗi không tiếp tục như đường thành công.

## Nhóm lỗi liên quan

NULL pointer dereference

## Tác động khi giả định bị vi phạm

Worker có thể kết thúc bất thường.

## Nguyên tắc phòng vệ

Kiểm tra trả về, lan truyền lỗi và bao phủ trạng thái đối tượng chưa khởi tạo.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-2F1F49392C62D738B7D70DC3\|WEAKNESS:CWE-476: definition]] — "Truy cập qua con trỏ NULL." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AA8B7EDD8456037A5C73C2CB: Description / Potential Mitigations; topic=WEAKNESS:CWE-476 — [[EVIDENCE-AA8B7EDD8456037A5C73C2CB\|CWE - CWE-476: NULL Pointer Dereference (5.0)]] |
| [[CLAIM-E426C33A617090C36325C055\|WEAKNESS:CWE-476: normal_behavior]] — "Kết quả allocation/lookup được kiểm tra trước khi dùng trường dữ liệu." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AA8B7EDD8456037A5C73C2CB: Description / Potential Mitigations; topic=WEAKNESS:CWE-476 — [[EVIDENCE-AA8B7EDD8456037A5C73C2CB\|CWE - CWE-476: NULL Pointer Dereference (5.0)]] |
| [[CLAIM-2444707C27FA1DB386D48C23\|WEAKNESS:CWE-476: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AA8B7EDD8456037A5C73C2CB: Description / Potential Mitigations; topic=WEAKNESS:CWE-476 — [[EVIDENCE-AA8B7EDD8456037A5C73C2CB\|CWE - CWE-476: NULL Pointer Dereference (5.0)]] |
| [[CLAIM-3424F64786B0099032F38AD5\|WEAKNESS:CWE-476: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AA8B7EDD8456037A5C73C2CB: Description / Potential Mitigations; topic=WEAKNESS:CWE-476 — [[EVIDENCE-AA8B7EDD8456037A5C73C2CB\|CWE - CWE-476: NULL Pointer Dereference (5.0)]] |
| [[CLAIM-1FB32BB0993D099CE413E717\|WEAKNESS:CWE-476: safety_assumptions]] — "Đường lỗi không tiếp tục như đường thành công." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AA8B7EDD8456037A5C73C2CB: Description / Potential Mitigations; topic=WEAKNESS:CWE-476 — [[EVIDENCE-AA8B7EDD8456037A5C73C2CB\|CWE - CWE-476: NULL Pointer Dereference (5.0)]] |
| [[CLAIM-D70BFCEF94EAEACBA219C71D\|WEAKNESS:CWE-476: related_failure_classes]] — "NULL pointer dereference" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AA8B7EDD8456037A5C73C2CB: Description / Potential Mitigations; topic=WEAKNESS:CWE-476 — [[EVIDENCE-AA8B7EDD8456037A5C73C2CB\|CWE - CWE-476: NULL Pointer Dereference (5.0)]] |
| [[CLAIM-493E54EA1A523D15248A3CE0\|WEAKNESS:CWE-476: failure_impact]] — "Worker có thể kết thúc bất thường." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AA8B7EDD8456037A5C73C2CB: Description / Potential Mitigations; topic=WEAKNESS:CWE-476 — [[EVIDENCE-AA8B7EDD8456037A5C73C2CB\|CWE - CWE-476: NULL Pointer Dereference (5.0)]] |
| [[CLAIM-9067C4BBDEC6054787752E33\|WEAKNESS:CWE-476: defensive_principles]] — "Kiểm tra trả về, lan truyền lỗi và bao phủ trạng thái đối tượng chưa khởi tạo." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AA8B7EDD8456037A5C73C2CB: Description / Potential Mitigations; topic=WEAKNESS:CWE-476 — [[EVIDENCE-AA8B7EDD8456037A5C73C2CB\|CWE - CWE-476: NULL Pointer Dereference (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-1E2175F7CBA0B7C5E6E8CFC9|CVE-2024-35200]], [[EVIDENCE-80DC2AA591D473C96E47B58C|CVE-2026-120993]], [[EVIDENCE-8B4D10F312B6AD83E27780ED|CVE-2024-24989]], [[EVIDENCE-AA8B7EDD8456037A5C73C2CB|CWE - CWE-476: NULL Pointer Dereference (5.0)]], [[EVIDENCE-B70DFB7CE216936748B0CCE6|CVE-2026-27651]], [[EVIDENCE-E080BE810C888D9012E21ECF|CWE - CWE-476: NULL Pointer Dereference (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

