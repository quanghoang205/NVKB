---
entity_type: component
id: COMPONENT:LOCATION-MATCHING
title: Location matching
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Location matching
tags:
- nginx
- component
- knowledge
---

# Location matching

Chọn cấu hình xử lý theo URI.

## Mục tiêu đo được

- Giải thích Location matching bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Chọn cấu hình xử lý theo URI.

## Cơ chế hoạt động bình thường

NGINX xử lý location có exact match, prefix và regular expression theo quy tắc của core module; internal redirect có thể chọn lại location.

## Vị trí trong kiến trúc

Ranh giới URI, đường dẫn tài nguyên và cấu hình kiểm soát truy cập.

## Security boundary

Ranh giới URI, đường dẫn tài nguyên và cấu hình kiểm soát truy cập.

## Giả định an toàn

Không giả định thứ tự dòng trong tệp luôn là thứ tự ưu tiên match.

## Nhóm lỗi liên quan

Configuration policy bypass; path mapping error.

## Tác động khi giả định bị vi phạm

Request đi vào handler hoặc tài nguyên ngoài dự kiến.

## Nguyên tắc phòng vệ

Kiểm thử các trường hợp URI đại diện và kiểm tra sự tương tác giữa location, alias và rewrite.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-AE057ACAFC9FFB528A7D574C\|COMPONENT:LOCATION-MATCHING: definition]] — "Chọn cấu hình xử lý theo URI." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:CC0FC3E5BE9713A5AEAA31DE: location; topic=COMPONENT:LOCATION-MATCHING — [[EVIDENCE-CC0FC3E5BE9713A5AEAA31DE\|Module ngx_http_core_module]] |
| [[CLAIM-E0BC4A13084A68DA98FCB032\|COMPONENT:LOCATION-MATCHING: normal_behavior]] — "NGINX xử lý location có exact match, prefix và regular expression theo quy tắc của core module; internal redirect có thể chọn lại location." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:CC0FC3E5BE9713A5AEAA31DE: location; topic=COMPONENT:LOCATION-MATCHING — [[EVIDENCE-CC0FC3E5BE9713A5AEAA31DE\|Module ngx_http_core_module]] |
| [[CLAIM-5EB38E2D40AEA5F24C327E6A\|COMPONENT:LOCATION-MATCHING: architecture_position]] — "Ranh giới URI, đường dẫn tài nguyên và cấu hình kiểm soát truy cập." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:CC0FC3E5BE9713A5AEAA31DE: location; topic=COMPONENT:LOCATION-MATCHING — [[EVIDENCE-CC0FC3E5BE9713A5AEAA31DE\|Module ngx_http_core_module]] |
| [[CLAIM-EC01726CE2124848044175D9\|COMPONENT:LOCATION-MATCHING: security_boundary]] — "Ranh giới URI, đường dẫn tài nguyên và cấu hình kiểm soát truy cập." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:CC0FC3E5BE9713A5AEAA31DE: location; topic=COMPONENT:LOCATION-MATCHING — [[EVIDENCE-CC0FC3E5BE9713A5AEAA31DE\|Module ngx_http_core_module]] |
| [[CLAIM-802A6D924145DF87D4AB73D8\|COMPONENT:LOCATION-MATCHING: safety_assumptions]] — "Không giả định thứ tự dòng trong tệp luôn là thứ tự ưu tiên match." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:CC0FC3E5BE9713A5AEAA31DE: location; topic=COMPONENT:LOCATION-MATCHING — [[EVIDENCE-CC0FC3E5BE9713A5AEAA31DE\|Module ngx_http_core_module]] |
| [[CLAIM-DFF4F7BA19FF06A0D5762B7C\|COMPONENT:LOCATION-MATCHING: related_failure_classes]] — "Configuration policy bypass; path mapping error." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:CC0FC3E5BE9713A5AEAA31DE: location; topic=COMPONENT:LOCATION-MATCHING — [[EVIDENCE-CC0FC3E5BE9713A5AEAA31DE\|Module ngx_http_core_module]] |
| [[CLAIM-06A33ED70E5C61BC479B90D5\|COMPONENT:LOCATION-MATCHING: failure_impact]] — "Request đi vào handler hoặc tài nguyên ngoài dự kiến." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:CC0FC3E5BE9713A5AEAA31DE: location; topic=COMPONENT:LOCATION-MATCHING — [[EVIDENCE-CC0FC3E5BE9713A5AEAA31DE\|Module ngx_http_core_module]] |
| [[CLAIM-F596CCF8EB3AF1896A75CA37\|COMPONENT:LOCATION-MATCHING: defensive_principles]] — "Kiểm thử các trường hợp URI đại diện và kiểm tra sự tương tác giữa location, alias và rewrite." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:CC0FC3E5BE9713A5AEAA31DE: location; topic=COMPONENT:LOCATION-MATCHING — [[EVIDENCE-CC0FC3E5BE9713A5AEAA31DE\|Module ngx_http_core_module]] |




## Phạm vi kiểm chứng

[[EVIDENCE-CC0FC3E5BE9713A5AEAA31DE|Module ngx_http_core_module]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

