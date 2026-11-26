---
entity_type: component
id: COMPONENT:REVERSE-PROXY
title: Reverse proxy
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Reverse proxy
tags:
- nginx
- component
- knowledge
---

# Reverse proxy

Thành phần nhận request client và chuyển tới upstream rồi trả response.

## Mục tiêu đo được

- Giải thích Reverse proxy bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Thành phần nhận request client và chuyển tới upstream rồi trả response.

## Cơ chế hoạt động bình thường

Proxy module tạo request upstream, xử lý kết nối, header và buffering theo cấu hình; upstream là một trust boundary riêng.

## Vị trí trong kiến trúc

Ranh giới client ↔ NGINX ↔ backend.

## Security boundary

Ranh giới client ↔ NGINX ↔ backend.

## Giả định an toàn

Không tin header định danh hay thông tin tuyến do client cung cấp nếu chưa kiểm soát.

## Nhóm lỗi liên quan

Parsing inconsistencies; information disclosure.

## Tác động khi giả định bị vi phạm

Sai định tuyến hoặc lộ dữ liệu theo cách ứng dụng dùng proxy.

## Nguyên tắc phòng vệ

Xác định rõ header tin cậy, timeout, TLS upstream và kích thước buffer.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-D7E315FC1B601C6ACD7642E8\|COMPONENT:REVERSE-PROXY: definition]] — "Thành phần nhận request client và chuyển tới upstream rồi trả response." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1884967DB1FB9643EED0FB13: proxy_pass; topic=COMPONENT:REVERSE-PROXY — [[EVIDENCE-1884967DB1FB9643EED0FB13\|Module ngx_http_proxy_module]] |
| [[CLAIM-C2F5EBF7914F57046D893E56\|COMPONENT:REVERSE-PROXY: normal_behavior]] — "Proxy module tạo request upstream, xử lý kết nối, header và buffering theo cấu hình; upstream là một trust boundary riêng." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1884967DB1FB9643EED0FB13: proxy_pass; topic=COMPONENT:REVERSE-PROXY — [[EVIDENCE-1884967DB1FB9643EED0FB13\|Module ngx_http_proxy_module]] |
| [[CLAIM-4F7DDC25DE51768319C1FD7D\|COMPONENT:REVERSE-PROXY: architecture_position]] — "Ranh giới client ↔ NGINX ↔ backend." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1884967DB1FB9643EED0FB13: proxy_pass; topic=COMPONENT:REVERSE-PROXY — [[EVIDENCE-1884967DB1FB9643EED0FB13\|Module ngx_http_proxy_module]] |
| [[CLAIM-DB636F4B06A5267617D47E9A\|COMPONENT:REVERSE-PROXY: security_boundary]] — "Ranh giới client ↔ NGINX ↔ backend." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1884967DB1FB9643EED0FB13: proxy_pass; topic=COMPONENT:REVERSE-PROXY — [[EVIDENCE-1884967DB1FB9643EED0FB13\|Module ngx_http_proxy_module]] |
| [[CLAIM-F9267C22A88E0E2FA18221C0\|COMPONENT:REVERSE-PROXY: safety_assumptions]] — "Không tin header định danh hay thông tin tuyến do client cung cấp nếu chưa kiểm soát." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1884967DB1FB9643EED0FB13: proxy_pass; topic=COMPONENT:REVERSE-PROXY — [[EVIDENCE-1884967DB1FB9643EED0FB13\|Module ngx_http_proxy_module]] |
| [[CLAIM-4E5783244996F60A83BC6ECD\|COMPONENT:REVERSE-PROXY: related_failure_classes]] — "Parsing inconsistencies; information disclosure." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1884967DB1FB9643EED0FB13: proxy_pass; topic=COMPONENT:REVERSE-PROXY — [[EVIDENCE-1884967DB1FB9643EED0FB13\|Module ngx_http_proxy_module]] |
| [[CLAIM-90174C169A9EF436F00363DD\|COMPONENT:REVERSE-PROXY: failure_impact]] — "Sai định tuyến hoặc lộ dữ liệu theo cách ứng dụng dùng proxy." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1884967DB1FB9643EED0FB13: proxy_pass; topic=COMPONENT:REVERSE-PROXY — [[EVIDENCE-1884967DB1FB9643EED0FB13\|Module ngx_http_proxy_module]] |
| [[CLAIM-691CA68E9900CC86B45FA8ED\|COMPONENT:REVERSE-PROXY: defensive_principles]] — "Xác định rõ header tin cậy, timeout, TLS upstream và kích thước buffer." | NGINX / F5 | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:1884967DB1FB9643EED0FB13: proxy_pass; topic=COMPONENT:REVERSE-PROXY — [[EVIDENCE-1884967DB1FB9643EED0FB13\|Module ngx_http_proxy_module]] |




## Phạm vi kiểm chứng

[[EVIDENCE-1884967DB1FB9643EED0FB13|Module ngx_http_proxy_module]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

