---
entity_type: weakness
id: WEAKNESS:CWE-835
title: CWE-835 — Infinite Loop
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-835 — Infinite Loop
tags:
- nginx
- weakness
- knowledge
---

# CWE-835 — Infinite Loop

Điều kiện thoát của vòng lặp không thể đạt trong một trạng thái xử lý.

## Mục tiêu đo được

- Giải thích CWE-835 — Infinite Loop bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Điều kiện thoát của vòng lặp không thể đạt trong một trạng thái xử lý.

## Cơ chế hoạt động bình thường

Mỗi vòng phải tạo tiến triển có thể chứng minh hoặc kết thúc có giới hạn.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Mỗi vòng phải tạo tiến triển có thể chứng minh hoặc kết thúc có giới hạn.

## Nhóm lỗi liên quan

Infinite Loop

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Đặt giới hạn công việc, kiểm tra invariant tiến triển và xử lý trạng thái không đổi.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-0FE52C7852A904DDCBD066D4\|WEAKNESS:CWE-835: definition]] — "Điều kiện thoát của vòng lặp không thể đạt trong một trạng thái xử lý." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:0062C4E072953C3410CED3E5: Description / Potential Mitigations; topic=WEAKNESS:CWE-835 — [[EVIDENCE-0062C4E072953C3410CED3E5\|CWE - CWE-835: Loop with Unreachable Exit Condition (5.0)]] |
| [[CLAIM-037D6727EAB6184020C8F238\|WEAKNESS:CWE-835: normal_behavior]] — "Mỗi vòng phải tạo tiến triển có thể chứng minh hoặc kết thúc có giới hạn." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:0062C4E072953C3410CED3E5: Description / Potential Mitigations; topic=WEAKNESS:CWE-835 — [[EVIDENCE-0062C4E072953C3410CED3E5\|CWE - CWE-835: Loop with Unreachable Exit Condition (5.0)]] |
| [[CLAIM-4867AF9D182D90BC010AEF48\|WEAKNESS:CWE-835: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:0062C4E072953C3410CED3E5: Description / Potential Mitigations; topic=WEAKNESS:CWE-835 — [[EVIDENCE-0062C4E072953C3410CED3E5\|CWE - CWE-835: Loop with Unreachable Exit Condition (5.0)]] |
| [[CLAIM-5643513783D41D1136C995A8\|WEAKNESS:CWE-835: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:0062C4E072953C3410CED3E5: Description / Potential Mitigations; topic=WEAKNESS:CWE-835 — [[EVIDENCE-0062C4E072953C3410CED3E5\|CWE - CWE-835: Loop with Unreachable Exit Condition (5.0)]] |
| [[CLAIM-F2AE3460E575E476448E6107\|WEAKNESS:CWE-835: safety_assumptions]] — "Mỗi vòng phải tạo tiến triển có thể chứng minh hoặc kết thúc có giới hạn." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:0062C4E072953C3410CED3E5: Description / Potential Mitigations; topic=WEAKNESS:CWE-835 — [[EVIDENCE-0062C4E072953C3410CED3E5\|CWE - CWE-835: Loop with Unreachable Exit Condition (5.0)]] |
| [[CLAIM-8942A18F94AF6AFDE048F0A1\|WEAKNESS:CWE-835: related_failure_classes]] — "Infinite Loop" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:0062C4E072953C3410CED3E5: Description / Potential Mitigations; topic=WEAKNESS:CWE-835 — [[EVIDENCE-0062C4E072953C3410CED3E5\|CWE - CWE-835: Loop with Unreachable Exit Condition (5.0)]] |
| [[CLAIM-57B62F81B7149288914C8224\|WEAKNESS:CWE-835: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:0062C4E072953C3410CED3E5: Description / Potential Mitigations; topic=WEAKNESS:CWE-835 — [[EVIDENCE-0062C4E072953C3410CED3E5\|CWE - CWE-835: Loop with Unreachable Exit Condition (5.0)]] |
| [[CLAIM-C38A1433A76D377491A9DE58\|WEAKNESS:CWE-835: defensive_principles]] — "Đặt giới hạn công việc, kiểm tra invariant tiến triển và xử lý trạng thái không đổi." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:0062C4E072953C3410CED3E5: Description / Potential Mitigations; topic=WEAKNESS:CWE-835 — [[EVIDENCE-0062C4E072953C3410CED3E5\|CWE - CWE-835: Loop with Unreachable Exit Condition (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-0062C4E072953C3410CED3E5|CWE - CWE-835: Loop with Unreachable Exit Condition (5.0)]], [[EVIDENCE-A0E312C3345B2591EBD6E89B|CVE-2026-132779]], [[EVIDENCE-DE52FE1407841B766BE78251|CVE-2026-118899]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

