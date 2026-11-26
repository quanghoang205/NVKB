---
entity_type: weakness
id: WEAKNESS:CWE-908
title: CWE-908 — Uninitialized Resource
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-908 — Uninitialized Resource
tags:
- nginx
- weakness
- knowledge
---

# CWE-908 — Uninitialized Resource

Sử dụng tài nguyên hoặc trường dữ liệu trước khi khởi tạo đầy đủ.

## Mục tiêu đo được

- Giải thích CWE-908 — Uninitialized Resource bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Sử dụng tài nguyên hoặc trường dữ liệu trước khi khởi tạo đầy đủ.

## Cơ chế hoạt động bình thường

Các trường bắt buộc được khởi tạo trước khi đối tượng được công bố cho callback.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Các trường bắt buộc được khởi tạo trước khi đối tượng được công bố cho callback.

## Nhóm lỗi liên quan

Uninitialized Resource

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Khởi tạo rõ ràng, kiểm tra state transition và bao phủ nhánh lỗi.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-43B1C8B8C138B98F706BDBC2\|WEAKNESS:CWE-908: definition]] — "Sử dụng tài nguyên hoặc trường dữ liệu trước khi khởi tạo đầy đủ." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:7D3E5C22A48FCE4BA1BEFF87: Description / Potential Mitigations; topic=WEAKNESS:CWE-908 — [[EVIDENCE-7D3E5C22A48FCE4BA1BEFF87\|CWE - CWE-908: Use of Uninitialized Resource (5.0)]] |
| [[CLAIM-C240CD8C3EC10AC6B1ECFB97\|WEAKNESS:CWE-908: normal_behavior]] — "Các trường bắt buộc được khởi tạo trước khi đối tượng được công bố cho callback." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:7D3E5C22A48FCE4BA1BEFF87: Description / Potential Mitigations; topic=WEAKNESS:CWE-908 — [[EVIDENCE-7D3E5C22A48FCE4BA1BEFF87\|CWE - CWE-908: Use of Uninitialized Resource (5.0)]] |
| [[CLAIM-02CA8AA4501CFE35889EE093\|WEAKNESS:CWE-908: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:7D3E5C22A48FCE4BA1BEFF87: Description / Potential Mitigations; topic=WEAKNESS:CWE-908 — [[EVIDENCE-7D3E5C22A48FCE4BA1BEFF87\|CWE - CWE-908: Use of Uninitialized Resource (5.0)]] |
| [[CLAIM-4816DA2C8D7CAEBFF31F2F65\|WEAKNESS:CWE-908: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:7D3E5C22A48FCE4BA1BEFF87: Description / Potential Mitigations; topic=WEAKNESS:CWE-908 — [[EVIDENCE-7D3E5C22A48FCE4BA1BEFF87\|CWE - CWE-908: Use of Uninitialized Resource (5.0)]] |
| [[CLAIM-340BA06E27E6CA6AFDF3493B\|WEAKNESS:CWE-908: safety_assumptions]] — "Các trường bắt buộc được khởi tạo trước khi đối tượng được công bố cho callback." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:7D3E5C22A48FCE4BA1BEFF87: Description / Potential Mitigations; topic=WEAKNESS:CWE-908 — [[EVIDENCE-7D3E5C22A48FCE4BA1BEFF87\|CWE - CWE-908: Use of Uninitialized Resource (5.0)]] |
| [[CLAIM-71FE1ABFD105E92AF0EF2F6E\|WEAKNESS:CWE-908: related_failure_classes]] — "Uninitialized Resource" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:7D3E5C22A48FCE4BA1BEFF87: Description / Potential Mitigations; topic=WEAKNESS:CWE-908 — [[EVIDENCE-7D3E5C22A48FCE4BA1BEFF87\|CWE - CWE-908: Use of Uninitialized Resource (5.0)]] |
| [[CLAIM-3D6B836B3563F61EC22C8452\|WEAKNESS:CWE-908: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:7D3E5C22A48FCE4BA1BEFF87: Description / Potential Mitigations; topic=WEAKNESS:CWE-908 — [[EVIDENCE-7D3E5C22A48FCE4BA1BEFF87\|CWE - CWE-908: Use of Uninitialized Resource (5.0)]] |
| [[CLAIM-5A6E292A87679BCCAB55E62F\|WEAKNESS:CWE-908: defensive_principles]] — "Khởi tạo rõ ràng, kiểm tra state transition và bao phủ nhánh lỗi." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:7D3E5C22A48FCE4BA1BEFF87: Description / Potential Mitigations; topic=WEAKNESS:CWE-908 — [[EVIDENCE-7D3E5C22A48FCE4BA1BEFF87\|CWE - CWE-908: Use of Uninitialized Resource (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-7D3E5C22A48FCE4BA1BEFF87|CWE - CWE-908: Use of Uninitialized Resource (5.0)]], [[EVIDENCE-B76F07A8D7C0CE6F98B12DF7|CVE-2026-97629]], [[EVIDENCE-E249E8C616C63CD9A664D9E4|CVE-2026-60005]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

