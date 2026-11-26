---
entity_type: component
id: COMPONENT:PROCESS-PRIVILEGES
title: Process privileges
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Process privileges
tags:
- nginx
- component
- knowledge
---

# Process privileges

Tách quyền của tiến trình điều phối và tiến trình xử lý request.

## Mục tiêu đo được

- Giải thích Process privileges bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Tách quyền của tiến trình điều phối và tiến trình xử lý request.

## Cơ chế hoạt động bình thường

Master có thể cần quyền tạo tài nguyên; worker sử dụng user/group cấu hình. Quyền thực tế phụ thuộc cách vận hành dịch vụ.

## Vị trí trong kiến trúc

Ranh giới hệ điều hành giữa quyền quản trị, tệp hệ thống và dữ liệu request.

## Security boundary

Ranh giới hệ điều hành giữa quyền quản trị, tệp hệ thống và dữ liệu request.

## Giả định an toàn

Không suy ra worker chạy root chỉ từ việc master có quyền cao.

## Nhóm lỗi liên quan

Privilege misconfiguration.

## Tác động khi giả định bị vi phạm

Phạm vi tác động có thể lớn hơn khi quyền worker vượt nhu cầu.

## Nguyên tắc phòng vệ

Áp dụng least privilege và đối chiếu service unit, user directive cùng quyền tệp.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-8D31F5CF6CCFCE4E54508B39\|COMPONENT:PROCESS-PRIVILEGES: definition]] — "Tách quyền của tiến trình điều phối và tiến trình xử lý request." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DEAA4C59D9EB3708DB5D7CA6: Processes; topic=COMPONENT:PROCESS-PRIVILEGES — [[EVIDENCE-DEAA4C59D9EB3708DB5D7CA6\|Development guide]] |
| [[CLAIM-CCF7BB5E5C9D7652506FF72A\|COMPONENT:PROCESS-PRIVILEGES: normal_behavior]] — "Master có thể cần quyền tạo tài nguyên; worker sử dụng user/group cấu hình. Quyền thực tế phụ thuộc cách vận hành dịch vụ." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DEAA4C59D9EB3708DB5D7CA6: Processes; topic=COMPONENT:PROCESS-PRIVILEGES — [[EVIDENCE-DEAA4C59D9EB3708DB5D7CA6\|Development guide]] |
| [[CLAIM-4A51BA6BA0DEC432E31BF856\|COMPONENT:PROCESS-PRIVILEGES: architecture_position]] — "Ranh giới hệ điều hành giữa quyền quản trị, tệp hệ thống và dữ liệu request." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DEAA4C59D9EB3708DB5D7CA6: Processes; topic=COMPONENT:PROCESS-PRIVILEGES — [[EVIDENCE-DEAA4C59D9EB3708DB5D7CA6\|Development guide]] |
| [[CLAIM-93119D93AFEB48B0FAAAC842\|COMPONENT:PROCESS-PRIVILEGES: security_boundary]] — "Ranh giới hệ điều hành giữa quyền quản trị, tệp hệ thống và dữ liệu request." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DEAA4C59D9EB3708DB5D7CA6: Processes; topic=COMPONENT:PROCESS-PRIVILEGES — [[EVIDENCE-DEAA4C59D9EB3708DB5D7CA6\|Development guide]] |
| [[CLAIM-8DBD3FC8006A9B1C480811E4\|COMPONENT:PROCESS-PRIVILEGES: safety_assumptions]] — "Không suy ra worker chạy root chỉ từ việc master có quyền cao." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DEAA4C59D9EB3708DB5D7CA6: Processes; topic=COMPONENT:PROCESS-PRIVILEGES — [[EVIDENCE-DEAA4C59D9EB3708DB5D7CA6\|Development guide]] |
| [[CLAIM-51184D27F430B3B6DB406310\|COMPONENT:PROCESS-PRIVILEGES: related_failure_classes]] — "Privilege misconfiguration." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DEAA4C59D9EB3708DB5D7CA6: Processes; topic=COMPONENT:PROCESS-PRIVILEGES — [[EVIDENCE-DEAA4C59D9EB3708DB5D7CA6\|Development guide]] |
| [[CLAIM-5AC620E0D0AB23D5D83B5715\|COMPONENT:PROCESS-PRIVILEGES: failure_impact]] — "Phạm vi tác động có thể lớn hơn khi quyền worker vượt nhu cầu." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DEAA4C59D9EB3708DB5D7CA6: Processes; topic=COMPONENT:PROCESS-PRIVILEGES — [[EVIDENCE-DEAA4C59D9EB3708DB5D7CA6\|Development guide]] |
| [[CLAIM-2043F40A58798EA0B70E2F4B\|COMPONENT:PROCESS-PRIVILEGES: defensive_principles]] — "Áp dụng least privilege và đối chiếu service unit, user directive cùng quyền tệp." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:DEAA4C59D9EB3708DB5D7CA6: Processes; topic=COMPONENT:PROCESS-PRIVILEGES — [[EVIDENCE-DEAA4C59D9EB3708DB5D7CA6\|Development guide]] |




## Phạm vi kiểm chứng

[[EVIDENCE-DEAA4C59D9EB3708DB5D7CA6|Development guide]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

