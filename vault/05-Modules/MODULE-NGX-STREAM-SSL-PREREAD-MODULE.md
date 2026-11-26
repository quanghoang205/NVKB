---
entity_type: module
id: MODULE:NGX-STREAM-SSL-PREREAD-MODULE
title: TLS preread — routing metadata và giới hạn tin cậy
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- TLS preread — routing metadata và giới hạn tin cậy
tags:
- nginx
- module
- knowledge
editorial_maturity: AI_REVIEWED
---

# TLS preread — routing metadata và giới hạn tin cậy

Module ssl_preread lấy thông tin từ ClientHello ở preread phase, không cần kết thúc TLS tại proxy; biến thu được có thể phục vụ routing.

## Mục tiêu đo được

- Phân biệt metadata ClientHello với identity đã được xác thực.
- Giải thích yêu cầu nhất quán parser giữa proxy và backend.


Kiến thức tiên quyết: [[PROTOCOL-TLS|TLS 1.3: handshake, identity và protected records]].

Nguồn xác nhận: [[CLAIM-57A4F144F0087F859CE4E2CD|phạm vi tài liệu]].

## Cơ chế và ownership

Preread quan sát phần đầu connection để lấy metadata phục vụ quyết định định tuyến. Proxy chưa kết thúc TLS nên không có cùng chứng cứ với endpoint hoàn tất handshake. Buffer đầu vào, vị trí đã đọc và biến kết quả cần được giữ trong context connection; đọc thiếu dữ liệu phải dẫn đến chờ hoặc lỗi có kiểm soát, không để biến chưa xác định thành quyết định routing.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-E8A2065F039778F6967F868F|Claim của section]].

## Invariant giữa hai bên

Diễn giải: giá trị được proxy sử dụng và ý nghĩa backend gán cho cùng ClientHello phải tương thích trong phạm vi phiên bản giao thức. Metadata không phải chứng thư và không chứng minh quyền vào backend. Routing segmentation không nên dựa vào giả định rằng một biến parser có thể thay thế authentication ở đích.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-6DAAAEF71E240D400456826C|Claim của section]].

## Tradeoff và phòng vệ

Không terminate TLS cho phép backend giữ vai trò bảo mật đầu cuối nhưng làm proxy có ít thông tin đã xác thực hơn. Cần kiểm soát tập backend được định tuyến và policy độc lập tại backend. Giữ version support của backend trong tài liệu thiết kế. Đây là nguyên tắc phòng vệ, không là cấu hình workaround đã được vendor xác nhận cho một CVE.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-1F02C9AA00CB46FE6FCD5A19|Claim của section]].


## Tự đánh giá

Vì sao tên SNI quan sát ở preread không chứng minh client được phép truy cập server đó?

## Đáp án và giải thích

Nó là dữ liệu đề xuất trong handshake, chưa phải kết quả xác thực và authorization của endpoint.

## Liên hệ và bước tiếp theo

[[PROTOCOL-TLS|TLS 1.3: handshake, identity và protected records]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[PROTOCOL-TLS|TLS 1.3: handshake, identity và protected records]] — Mục tiêu 'Phân biệt metadata ClientHello với identity đã được xác thực.' cần mô hình TLS 1.3: handshake, identity và protected records. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-57A4F144F0087F859CE4E2CD\|MODULE:NGX-STREAM-SSL-PREREAD-MODULE: v1.3:knowledge_fact]] — "Module ssl_preread lấy thông tin từ ClientHello ở preread phase, không cần kết thúc TLS tại proxy; biến thu được có thể phục vụ routing." | NGINX / F5 | CURRENT | SUPPORTED / AI_REVIEWED | Introduction; — [[EVIDENCE-4BA76FA5ED0E407DE3B76040\|ngx_stream_ssl_preread_module.html: Introduction;]] |
| [[CLAIM-E8A2065F039778F6967F868F\|MODULE:NGX-STREAM-SSL-PREREAD-MODULE: v1.3:knowledge:Cơ chế và ownership]] — "## Cơ chế và ownership\n\nPreread quan sát phần đầu connection để lấy metadata phục vụ quyết định định tuyến. Proxy chưa kết thúc TLS nên không có cùng chứng cứ với endpoint hoàn … (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-4BA76FA5ED0E407DE3B76040\|ngx_stream_ssl_preread_module.html: Introduction;]] |
| [[CLAIM-6DAAAEF71E240D400456826C\|MODULE:NGX-STREAM-SSL-PREREAD-MODULE: v1.3:knowledge:Invariant giữa hai bên]] — "## Invariant giữa hai bên\n\nDiễn giải: giá trị được proxy sử dụng và ý nghĩa backend gán cho cùng ClientHello phải tương thích trong phạm vi phiên bản giao thức. Metadata không p… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-4BA76FA5ED0E407DE3B76040\|ngx_stream_ssl_preread_module.html: Introduction;]] |
| [[CLAIM-1F02C9AA00CB46FE6FCD5A19\|MODULE:NGX-STREAM-SSL-PREREAD-MODULE: v1.3:knowledge:Tradeoff và phòng vệ]] — "## Tradeoff và phòng vệ\n\nKhông terminate TLS cho phép backend giữ vai trò bảo mật đầu cuối nhưng làm proxy có ít thông tin đã xác thực hơn. Cần kiểm soát tập backend được định t… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-4BA76FA5ED0E407DE3B76040\|ngx_stream_ssl_preread_module.html: Introduction;]] |




## Phạm vi kiểm chứng

[[EVIDENCE-4BA76FA5ED0E407DE3B76040|ngx_stream_ssl_preread_module.html: Introduction;]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

