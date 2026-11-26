---
entity_type: component
id: COMPONENT:HTTP-CACHING
title: HTTP caching
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- HTTP caching
tags:
- nginx
- component
- knowledge
---

# HTTP caching

Tái sử dụng response upstream theo cache key và chính sách cache.

## Mục tiêu đo được

- Giải thích HTTP caching bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Tái sử dụng response upstream theo cache key và chính sách cache.

## Cơ chế hoạt động bình thường

NGINX tra cache theo key, thời gian hiệu lực và chỉ thị cache; các điều kiện bypass/no-cache quyết định việc đọc hoặc lưu response.

## Vị trí trong kiến trúc

Ranh giới dữ liệu dùng chung trong cache và dữ liệu gắn người dùng/tenant.

## Security boundary

Ranh giới dữ liệu dùng chung trong cache và dữ liệu gắn người dùng/tenant.

## Giả định an toàn

Cache key phải phân biệt các context trả về nội dung khác nhau.

## Nhóm lỗi liên quan

Information disclosure; cache key inconsistency.

## Tác động khi giả định bị vi phạm

Nội dung bị chia sẻ sai phạm vi hoặc lỗi thời.

## Nguyên tắc phòng vệ

Rà soát cache key, Authorization/Cookie, Vary và điều kiện bypass cho dữ liệu riêng tư.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-D88643D7B9E62BB145440943\|COMPONENT:HTTP-CACHING: definition]] — "Tái sử dụng response upstream theo cache key và chính sách cache." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:EB05C6F9389F40F1937A4BF0: proxy_cache; topic=COMPONENT:HTTP-CACHING — [[EVIDENCE-EB05C6F9389F40F1937A4BF0\|Module ngx_http_proxy_module]] |
| [[CLAIM-3F1C7CD058DCD18BB8F77BA2\|COMPONENT:HTTP-CACHING: normal_behavior]] — "NGINX tra cache theo key, thời gian hiệu lực và chỉ thị cache; các điều kiện bypass/no-cache quyết định việc đọc hoặc lưu response." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:EB05C6F9389F40F1937A4BF0: proxy_cache; topic=COMPONENT:HTTP-CACHING — [[EVIDENCE-EB05C6F9389F40F1937A4BF0\|Module ngx_http_proxy_module]] |
| [[CLAIM-27779A2F94251DF49AB5DCC0\|COMPONENT:HTTP-CACHING: architecture_position]] — "Ranh giới dữ liệu dùng chung trong cache và dữ liệu gắn người dùng/tenant." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:EB05C6F9389F40F1937A4BF0: proxy_cache; topic=COMPONENT:HTTP-CACHING — [[EVIDENCE-EB05C6F9389F40F1937A4BF0\|Module ngx_http_proxy_module]] |
| [[CLAIM-1C1BADCFFFB9F93E7B4D26B4\|COMPONENT:HTTP-CACHING: security_boundary]] — "Ranh giới dữ liệu dùng chung trong cache và dữ liệu gắn người dùng/tenant." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:EB05C6F9389F40F1937A4BF0: proxy_cache; topic=COMPONENT:HTTP-CACHING — [[EVIDENCE-EB05C6F9389F40F1937A4BF0\|Module ngx_http_proxy_module]] |
| [[CLAIM-EB316330BB3C2182E278B82A\|COMPONENT:HTTP-CACHING: safety_assumptions]] — "Cache key phải phân biệt các context trả về nội dung khác nhau." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:EB05C6F9389F40F1937A4BF0: proxy_cache; topic=COMPONENT:HTTP-CACHING — [[EVIDENCE-EB05C6F9389F40F1937A4BF0\|Module ngx_http_proxy_module]] |
| [[CLAIM-40E315740A38DC39C7512E59\|COMPONENT:HTTP-CACHING: related_failure_classes]] — "Information disclosure; cache key inconsistency." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:EB05C6F9389F40F1937A4BF0: proxy_cache; topic=COMPONENT:HTTP-CACHING — [[EVIDENCE-EB05C6F9389F40F1937A4BF0\|Module ngx_http_proxy_module]] |
| [[CLAIM-1B8B469AC7C40B3B30EA29F9\|COMPONENT:HTTP-CACHING: failure_impact]] — "Nội dung bị chia sẻ sai phạm vi hoặc lỗi thời." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:EB05C6F9389F40F1937A4BF0: proxy_cache; topic=COMPONENT:HTTP-CACHING — [[EVIDENCE-EB05C6F9389F40F1937A4BF0\|Module ngx_http_proxy_module]] |
| [[CLAIM-C5CC886B05343FEA8F6C2729\|COMPONENT:HTTP-CACHING: defensive_principles]] — "Rà soát cache key, Authorization/Cookie, Vary và điều kiện bypass cho dữ liệu riêng tư." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:EB05C6F9389F40F1937A4BF0: proxy_cache; topic=COMPONENT:HTTP-CACHING — [[EVIDENCE-EB05C6F9389F40F1937A4BF0\|Module ngx_http_proxy_module]] |




## Phạm vi kiểm chứng

[[EVIDENCE-EB05C6F9389F40F1937A4BF0|Module ngx_http_proxy_module]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

