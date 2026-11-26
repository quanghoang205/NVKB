---
entity_type: component
id: COMPONENT:VIRTUAL-HOSTS
title: Virtual hosts
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Virtual hosts
tags:
- nginx
- component
- knowledge
---

# Virtual hosts

Nhiều cấu hình server chia sẻ hạ tầng lắng nghe.

## Mục tiêu đo được

- Giải thích Virtual hosts bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Nhiều cấu hình server chia sẻ hạ tầng lắng nghe.

## Cơ chế hoạt động bình thường

NGINX chọn nhóm listen theo địa chỉ/cổng và đối chiếu tên server; default server thuộc socket listen. TLS có bước chọn theo SNI.

## Vị trí trong kiến trúc

Ranh giới chính sách giữa các tên miền dùng chung listener.

## Security boundary

Ranh giới chính sách giữa các tên miền dùng chung listener.

## Giả định an toàn

Các quyết định xác thực và cấu hình phải gắn đúng server được chọn.

## Nhóm lỗi liên quan

Authentication policy violation.

## Tác động khi giả định bị vi phạm

Áp dụng nhầm chính sách truy cập giữa virtual hosts.

## Nguyên tắc phòng vệ

Rà soát default server, server_name và chính sách TLS/mTLS nhất quán.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-F5C1AE804BFBEFE7DEBDE444\|COMPONENT:VIRTUAL-HOSTS: definition]] — "Nhiều cấu hình server chia sẻ hạ tầng lắng nghe." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:FDB9B691A2BFB99A8CC78B34: Name-based virtual servers; topic=COMPONENT:VIRTUAL-HOSTS — [[EVIDENCE-FDB9B691A2BFB99A8CC78B34\|How nginx processes a request]] |
| [[CLAIM-3CA083E16D8B951F2A41FEBE\|COMPONENT:VIRTUAL-HOSTS: normal_behavior]] — "NGINX chọn nhóm listen theo địa chỉ/cổng và đối chiếu tên server; default server thuộc socket listen. TLS có bước chọn theo SNI." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:FDB9B691A2BFB99A8CC78B34: Name-based virtual servers; topic=COMPONENT:VIRTUAL-HOSTS — [[EVIDENCE-FDB9B691A2BFB99A8CC78B34\|How nginx processes a request]] |
| [[CLAIM-674A213ECD087ACB9A9C4B06\|COMPONENT:VIRTUAL-HOSTS: architecture_position]] — "Ranh giới chính sách giữa các tên miền dùng chung listener." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:FDB9B691A2BFB99A8CC78B34: Name-based virtual servers; topic=COMPONENT:VIRTUAL-HOSTS — [[EVIDENCE-FDB9B691A2BFB99A8CC78B34\|How nginx processes a request]] |
| [[CLAIM-8170B13890370AC7598F1654\|COMPONENT:VIRTUAL-HOSTS: security_boundary]] — "Ranh giới chính sách giữa các tên miền dùng chung listener." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:FDB9B691A2BFB99A8CC78B34: Name-based virtual servers; topic=COMPONENT:VIRTUAL-HOSTS — [[EVIDENCE-FDB9B691A2BFB99A8CC78B34\|How nginx processes a request]] |
| [[CLAIM-75A873D0753332149298F64F\|COMPONENT:VIRTUAL-HOSTS: safety_assumptions]] — "Các quyết định xác thực và cấu hình phải gắn đúng server được chọn." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:FDB9B691A2BFB99A8CC78B34: Name-based virtual servers; topic=COMPONENT:VIRTUAL-HOSTS — [[EVIDENCE-FDB9B691A2BFB99A8CC78B34\|How nginx processes a request]] |
| [[CLAIM-E47FF0583740A6A43ACCA512\|COMPONENT:VIRTUAL-HOSTS: related_failure_classes]] — "Authentication policy violation." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:FDB9B691A2BFB99A8CC78B34: Name-based virtual servers; topic=COMPONENT:VIRTUAL-HOSTS — [[EVIDENCE-FDB9B691A2BFB99A8CC78B34\|How nginx processes a request]] |
| [[CLAIM-8D79898B17BC949F399E1A9E\|COMPONENT:VIRTUAL-HOSTS: failure_impact]] — "Áp dụng nhầm chính sách truy cập giữa virtual hosts." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:FDB9B691A2BFB99A8CC78B34: Name-based virtual servers; topic=COMPONENT:VIRTUAL-HOSTS — [[EVIDENCE-FDB9B691A2BFB99A8CC78B34\|How nginx processes a request]] |
| [[CLAIM-5CCEA1CFA7801DF687A9236E\|COMPONENT:VIRTUAL-HOSTS: defensive_principles]] — "Rà soát default server, server_name và chính sách TLS/mTLS nhất quán." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:FDB9B691A2BFB99A8CC78B34: Name-based virtual servers; topic=COMPONENT:VIRTUAL-HOSTS — [[EVIDENCE-FDB9B691A2BFB99A8CC78B34\|How nginx processes a request]] |




## Phạm vi kiểm chứng

[[EVIDENCE-FDB9B691A2BFB99A8CC78B34|How nginx processes a request]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

