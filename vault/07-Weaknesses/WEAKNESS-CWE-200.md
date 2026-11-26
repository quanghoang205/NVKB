---
entity_type: weakness
id: WEAKNESS:CWE-200
title: CWE-200 — Information disclosure
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-200 — Information disclosure
tags:
- nginx
- weakness
- knowledge
---

# CWE-200 — Information disclosure

Thông tin được cung cấp cho chủ thể không được phép.

## Mục tiêu đo được

- Giải thích CWE-200 — Information disclosure bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Thông tin được cung cấp cho chủ thể không được phép.

## Cơ chế hoạt động bình thường

Chỉ dữ liệu nằm trong phạm vi quyền của request mới được trả về hoặc ghi vào kênh có thể đọc.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Buffer, cache key, log và response không lẫn dữ liệu khác context.

## Nhóm lỗi liên quan

Information disclosure

## Tác động khi giả định bị vi phạm

Lộ dữ liệu theo loại và mức độ được nguồn xác nhận.

## Nguyên tắc phòng vệ

Giảm dữ liệu nhạy cảm, kiểm soát cache/log và kiểm tra ranh giới response.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-1072AC253B1BAB6A306DC6AD\|WEAKNESS:CWE-200: definition]] — "Thông tin được cung cấp cho chủ thể không được phép." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:43C837E961E377425755DEC0: Description / Potential Mitigations; topic=WEAKNESS:CWE-200 — [[EVIDENCE-43C837E961E377425755DEC0\|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]] |
| [[CLAIM-F91C64E742516882290F14B1\|WEAKNESS:CWE-200: normal_behavior]] — "Chỉ dữ liệu nằm trong phạm vi quyền của request mới được trả về hoặc ghi vào kênh có thể đọc." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:43C837E961E377425755DEC0: Description / Potential Mitigations; topic=WEAKNESS:CWE-200 — [[EVIDENCE-43C837E961E377425755DEC0\|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]] |
| [[CLAIM-0DE2156C53DF5975DE8D8733\|WEAKNESS:CWE-200: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:43C837E961E377425755DEC0: Description / Potential Mitigations; topic=WEAKNESS:CWE-200 — [[EVIDENCE-43C837E961E377425755DEC0\|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]] |
| [[CLAIM-4102960DFB16183DD0F1E54E\|WEAKNESS:CWE-200: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:43C837E961E377425755DEC0: Description / Potential Mitigations; topic=WEAKNESS:CWE-200 — [[EVIDENCE-43C837E961E377425755DEC0\|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]] |
| [[CLAIM-31CDF49D3C651ADDF5C99E75\|WEAKNESS:CWE-200: safety_assumptions]] — "Buffer, cache key, log và response không lẫn dữ liệu khác context." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:43C837E961E377425755DEC0: Description / Potential Mitigations; topic=WEAKNESS:CWE-200 — [[EVIDENCE-43C837E961E377425755DEC0\|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]] |
| [[CLAIM-95B310C4DF064ED4C1BF12B7\|WEAKNESS:CWE-200: related_failure_classes]] — "Information disclosure" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:43C837E961E377425755DEC0: Description / Potential Mitigations; topic=WEAKNESS:CWE-200 — [[EVIDENCE-43C837E961E377425755DEC0\|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]] |
| [[CLAIM-6640A93A0085DEE1EE1366C2\|WEAKNESS:CWE-200: failure_impact]] — "Lộ dữ liệu theo loại và mức độ được nguồn xác nhận." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:43C837E961E377425755DEC0: Description / Potential Mitigations; topic=WEAKNESS:CWE-200 — [[EVIDENCE-43C837E961E377425755DEC0\|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]] |
| [[CLAIM-51FDCB65AB1E29DDAAA5FA62\|WEAKNESS:CWE-200: defensive_principles]] — "Giảm dữ liệu nhạy cảm, kiểm soát cache/log và kiểm tra ranh giới response." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:43C837E961E377425755DEC0: Description / Potential Mitigations; topic=WEAKNESS:CWE-200 — [[EVIDENCE-43C837E961E377425755DEC0\|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-298DD279D3CE2B051D376EFD|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]], [[EVIDENCE-43C837E961E377425755DEC0|CWE - CWE-200: Exposure of Sensitive Information to an Unauthorized Actor (5.0)]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

