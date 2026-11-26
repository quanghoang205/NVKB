---
entity_type: weakness
id: WEAKNESS:CWE-290
title: CWE-290 — Authentication Bypass by Spoofing
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-290 — Authentication Bypass by Spoofing
tags:
- nginx
- weakness
- knowledge
---

# CWE-290 — Authentication Bypass by Spoofing

Tin vào thông tin định danh có thể bị giả mạo trong quá trình authentication.

## Mục tiêu đo được

- Giải thích CWE-290 — Authentication Bypass by Spoofing bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Tin vào thông tin định danh có thể bị giả mạo trong quá trình authentication.

## Cơ chế hoạt động bình thường

Định danh phải được chứng minh bằng cơ chế xác thực phù hợp, không chỉ bằng metadata.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Định danh phải được chứng minh bằng cơ chế xác thực phù hợp, không chỉ bằng metadata.

## Nhóm lỗi liên quan

Authentication Bypass by Spoofing

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Liên kết identity với bằng chứng mật mã/chính sách và kiểm tra trust boundary.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-90FE6627899214D62F8B91C7\|WEAKNESS:CWE-290: definition]] — "Tin vào thông tin định danh có thể bị giả mạo trong quá trình authentication." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DE7D1D7AF92C028CF23ED19B: Description / Potential Mitigations; topic=WEAKNESS:CWE-290 — [[EVIDENCE-DE7D1D7AF92C028CF23ED19B\|CWE - CWE-290: Authentication Bypass by Spoofing (5.0)]] |
| [[CLAIM-281282F2DE66B61FA890ED32\|WEAKNESS:CWE-290: normal_behavior]] — "Định danh phải được chứng minh bằng cơ chế xác thực phù hợp, không chỉ bằng metadata." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DE7D1D7AF92C028CF23ED19B: Description / Potential Mitigations; topic=WEAKNESS:CWE-290 — [[EVIDENCE-DE7D1D7AF92C028CF23ED19B\|CWE - CWE-290: Authentication Bypass by Spoofing (5.0)]] |
| [[CLAIM-18DCC2E78E9FCB79A48B8A22\|WEAKNESS:CWE-290: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DE7D1D7AF92C028CF23ED19B: Description / Potential Mitigations; topic=WEAKNESS:CWE-290 — [[EVIDENCE-DE7D1D7AF92C028CF23ED19B\|CWE - CWE-290: Authentication Bypass by Spoofing (5.0)]] |
| [[CLAIM-5C4267AF8C399E503095A0E7\|WEAKNESS:CWE-290: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DE7D1D7AF92C028CF23ED19B: Description / Potential Mitigations; topic=WEAKNESS:CWE-290 — [[EVIDENCE-DE7D1D7AF92C028CF23ED19B\|CWE - CWE-290: Authentication Bypass by Spoofing (5.0)]] |
| [[CLAIM-FA781CE3D8529A7293A88A9D\|WEAKNESS:CWE-290: safety_assumptions]] — "Định danh phải được chứng minh bằng cơ chế xác thực phù hợp, không chỉ bằng metadata." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DE7D1D7AF92C028CF23ED19B: Description / Potential Mitigations; topic=WEAKNESS:CWE-290 — [[EVIDENCE-DE7D1D7AF92C028CF23ED19B\|CWE - CWE-290: Authentication Bypass by Spoofing (5.0)]] |
| [[CLAIM-8A09943FB14BF11F9B20BF44\|WEAKNESS:CWE-290: related_failure_classes]] — "Authentication Bypass by Spoofing" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DE7D1D7AF92C028CF23ED19B: Description / Potential Mitigations; topic=WEAKNESS:CWE-290 — [[EVIDENCE-DE7D1D7AF92C028CF23ED19B\|CWE - CWE-290: Authentication Bypass by Spoofing (5.0)]] |
| [[CLAIM-8BCF7D43FB057853F9C464B1\|WEAKNESS:CWE-290: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DE7D1D7AF92C028CF23ED19B: Description / Potential Mitigations; topic=WEAKNESS:CWE-290 — [[EVIDENCE-DE7D1D7AF92C028CF23ED19B\|CWE - CWE-290: Authentication Bypass by Spoofing (5.0)]] |
| [[CLAIM-BE57064B7403B7017CBD5E71\|WEAKNESS:CWE-290: defensive_principles]] — "Liên kết identity với bằng chứng mật mã/chính sách và kiểm tra trust boundary." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DE7D1D7AF92C028CF23ED19B: Description / Potential Mitigations; topic=WEAKNESS:CWE-290 — [[EVIDENCE-DE7D1D7AF92C028CF23ED19B\|CWE - CWE-290: Authentication Bypass by Spoofing (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-DE7D1D7AF92C028CF23ED19B|CWE - CWE-290: Authentication Bypass by Spoofing (5.0)]], [[EVIDENCE-E27A471AEA52899E1C3CDC79|CVE-2026-40460]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

