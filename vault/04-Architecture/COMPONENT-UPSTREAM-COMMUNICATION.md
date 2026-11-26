---
entity_type: component
id: COMPONENT:UPSTREAM-COMMUNICATION
title: Upstream communication — hai hop và ownership của response
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Upstream communication — hai hop và ownership của response
tags:
- nginx
- component
- knowledge
editorial_maturity: AI_REVIEWED
---

# Upstream communication — hai hop và ownership của response

Proxy module quản lý request/response tới upstream, chế độ buffering và TLS verification riêng; connection tới client và upstream là hai context khác nhau.

## Mục tiêu đo được

- Vẽ hai trust boundary client/proxy và proxy/upstream.
- Phân biệt response buffering với request buffering.


Kiến thức tiên quyết: [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]], [[PROTOCOL-TLS|TLS 1.3: handshake, identity và protected records]].

Nguồn xác nhận: [[CLAIM-4F35ED7ED48D829CB9467480|phạm vi tài liệu]].

## Cơ chế bình thường

Reverse proxy nhận message ở một hop và tạo trao đổi khác với upstream. Transport, TLS identity và protocol version của hai hop có thể khác nhau. Được xác thực trên hop client không tự chứng minh upstream đã được xác thực; có TLS ở upstream cũng cần policy verification đúng tên và trust source. Tài liệu có directive riêng cho TLS name/verification và phiên bản HTTP upstream.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-9B8164D27E42E49384968F91|Claim của section]].

## Buffering và lifecycle

Response buffering cho phép đọc upstream và lưu dữ liệu trước khi client nhận hết; phần vượt bộ nhớ có thể tới temporary file. Khi tắt buffering, nhịp chuyển dữ liệu gắn chặt hơn với bên nhận, nhưng buffer vẫn tồn tại. Request buffering lại thuộc chiều client tới upstream. Hai công tắc không đồng nghĩa và không thay cho kiểm framing.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-82A002DFC36D6EDC7D156637|Claim của section]].

## Invariant ranh giới

Diễn giải: mỗi byte được chuyển phải thuộc đúng message và được đọc từ một nguồn hợp lệ trong state hiện hành. Response upstream là dữ liệu cần parse, không là chỉ thị tự do cho state của worker. Việc chuyển giữa HTTP/2 và representation nội bộ vẫn phải giữ ranh giới headers/body, độ dài và capacity. Khi upstream đóng sớm hoặc timeout, request không được coi là thành công chỉ vì trước đó đã có kết nối.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-B2B453778A6430D8BF5934F0|Claim của section]].

## Tradeoff và phòng vệ

Buffering tách tốc độ hai bên nhưng tiêu thụ tài nguyên; streaming giảm chờ nhưng kéo dài sự phụ thuộc lifecycle. TLS bảo vệ đường truyền trong phạm vi identity và state được triển khai đúng; nó không loại bỏ lỗi xử lý dữ liệu đã giải mã. Quản trị nguồn upstream, chứng thư, timeout và package update là các lớp riêng. Không áp dụng cùng cấu hình mitigation cho HTTP proxy, gRPC, SCGI và uwsgi chỉ vì tất cả đều có upstream.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-427B93525744D03B18CE4AAA|Claim của section]].


## Tự đánh giá

Một deployment dùng HTTPS tới upstream có bảo đảm mọi byte đưa vào response đều thuộc phiên được xác thực không?

## Đáp án và giải thích

Cần implementation đúng state và verification policy; nhãn HTTPS không thay chứng cứ contract và bản sửa cho lỗi implementation.

## Liên hệ và bước tiếp theo

[[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]], [[PROTOCOL-TLS|TLS 1.3: handshake, identity và protected records]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[PROTOCOL-TLS|TLS 1.3: handshake, identity và protected records]] — Mục tiêu 'Vẽ hai trust boundary client/proxy và proxy/upstream.' cần mô hình TLS 1.3: handshake, identity và protected records. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]] — Mục tiêu 'Vẽ hai trust boundary client/proxy và proxy/upstream.' cần mô hình Connection và HTTP request: hai vòng đời. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.
- `CONTEXTUAL_ASSOCIATION` → [[WEAKNESS-CWE-172|CWE-172 — Encoding Error]] — Nguồn 42926 nêu upstream request injection; không suy hậu quả ứng dụng tiếp theo. Kiến trúc cung cấp context học lớp lỗi; không xác nhận mọi instance có lỗi. **INTERPRETATION / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-4F35ED7ED48D829CB9467480\|COMPONENT:UPSTREAM-COMMUNICATION: v1.3:knowledge_fact]] — "Proxy module quản lý request/response tới upstream, chế độ buffering và TLS verification riêng; connection tới client và upstream là hai context khác nhau." | NGINX / F5 | CURRENT | SUPPORTED / AI_REVIEWED | #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name — [[EVIDENCE-866DA2E2D0C2FB0A535A8A90\|ngx_http_proxy_module.html: #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name]] |
| [[CLAIM-9B8164D27E42E49384968F91\|COMPONENT:UPSTREAM-COMMUNICATION: v1.3:knowledge:Cơ chế bình thường]] — "## Cơ chế bình thường\n\nReverse proxy nhận message ở một hop và tạo trao đổi khác với upstream. Transport, TLS identity và protocol version của hai hop có thể khác nhau. Được xác… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name — [[EVIDENCE-866DA2E2D0C2FB0A535A8A90\|ngx_http_proxy_module.html: #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name]] |
| [[CLAIM-82A002DFC36D6EDC7D156637\|COMPONENT:UPSTREAM-COMMUNICATION: v1.3:knowledge:Buffering và lifecycle]] — "## Buffering và lifecycle\n\nResponse buffering cho phép đọc upstream và lưu dữ liệu trước khi client nhận hết; phần vượt bộ nhớ có thể tới temporary file. Khi tắt buffering, nhịp… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name — [[EVIDENCE-866DA2E2D0C2FB0A535A8A90\|ngx_http_proxy_module.html: #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name]] |
| [[CLAIM-B2B453778A6430D8BF5934F0\|COMPONENT:UPSTREAM-COMMUNICATION: v1.3:knowledge:Invariant ranh giới]] — "## Invariant ranh giới\n\nDiễn giải: mỗi byte được chuyển phải thuộc đúng message và được đọc từ một nguồn hợp lệ trong state hiện hành. Response upstream là dữ liệu cần parse, kh… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name — [[EVIDENCE-866DA2E2D0C2FB0A535A8A90\|ngx_http_proxy_module.html: #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name]] |
| [[CLAIM-427B93525744D03B18CE4AAA\|COMPONENT:UPSTREAM-COMMUNICATION: v1.3:knowledge:Tradeoff và phòng vệ]] — "## Tradeoff và phòng vệ\n\nBuffering tách tốc độ hai bên nhưng tiêu thụ tài nguyên; streaming giảm chờ nhưng kéo dài sự phụ thuộc lifecycle. TLS bảo vệ đường truyền trong phạm vi … (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name — [[EVIDENCE-866DA2E2D0C2FB0A535A8A90\|ngx_http_proxy_module.html: #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name]] |




## Phạm vi kiểm chứng

[[EVIDENCE-866DA2E2D0C2FB0A535A8A90|ngx_http_proxy_module.html: #proxy_buffering; #proxy_request_buffering; #proxy_http_version; #proxy_ssl_verify; #proxy_ssl_name]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

