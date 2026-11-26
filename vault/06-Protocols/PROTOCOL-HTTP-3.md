---
entity_type: protocol
id: PROTOCOL:HTTP-3
title: HTTP/3 — message framing và stream chuyên biệt
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- HTTP/3 — message framing và stream chuyên biệt
tags:
- nginx
- protocol
- knowledge
editorial_maturity: AI_REVIEWED
---

# HTTP/3 — message framing và stream chuyên biệt

RFC 9114 ánh xạ mỗi request lên một client-initiated bidirectional QUIC stream; HEADERS và DATA có thứ tự hợp lệ, còn control stream có vai trò riêng.

## Mục tiêu đo được

- Vẽ ranh giới HTTP message và QUIC stream.
- Phân biệt state request với state điều khiển dùng chung.


Kiến thức tiên quyết: [[PROTOCOL-QUIC|QUIC — stream, connection và kiểm chứng địa chỉ]].

Nguồn xác nhận: [[CLAIM-42775420035E17A7D510E87D|phạm vi tài liệu]].

## Cơ chế và phân lớp

HTTP/3 sử dụng QUIC stream để mang HTTP message. HEADERS biểu diễn phần trường, DATA mang nội dung; trailer nếu có đánh dấu một phần khác của message. Parser cần giữ trạng thái để chấp nhận đúng thứ tự và xử lý việc dữ liệu đến từng phần. Ranh giới một gói UDP, một lần callback và một HTTP message không trùng nhau.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-BC3410121C90BD66DAED1491|Claim của section]].

## Ownership và state dùng chung

Request stream thuộc một công việc HTTP, trong khi control stream và cơ chế nén trường có trạng thái phục vụ nhiều trao đổi. Việc đóng request không cho phép tùy tiện hủy state connection mà request khác còn dùng. Ngược lại, giữ connection sống không cho phép tái sử dụng con trỏ request đã kết thúc. Mô hình này giải thích nhu cầu đọc bài memory pool trước khi phân tích use-after-free.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-9640066C7549A0BF372E0CBD|Claim của section]].

## Invariant và tradeoff

Diễn giải: mọi byte được bàn giao cho upstream phải thuộc đúng body của request đang xét; trạng thái parser phải xác định liệu vùng buffer chứa message data hay control data. Buffering giúp tách tốc độ client và upstream nhưng đòi hỏi ghi nhận độ dài, ownership và điểm kết thúc chính xác. Không dùng việc message đi qua TLS để bỏ qua kiểm cấu trúc sau giải mã.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-42C5E6F73FECDA959A42709F|Claim của section]].

## Nguyên tắc review

So sánh lifetime request, control stream và buffer khi đọc advisory. Với lỗi ở nén trường, tên encoder không tự chỉ ra hàm hay thuật toán cụ thể; nguồn chuẩn chỉ dạy cơ chế bình thường. Với lỗi address spoofing, đọc QUIC address validation và policy ứng dụng; với lỗi body injection, đọc ranh giới message/upstream. Các bài CVE không cung cấp traffic hay quy trình tái hiện.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-D1351840EFFC441E740C62F5|Claim của section]].


## Tự đánh giá

Tại sao xác thực tính toàn vẹn của một kết nối vẫn chưa chứng minh các byte được gán đúng request?

## Đáp án và giải thích

Bảo vệ vận chuyển và parsing ứng dụng là hai lớp; parser vẫn phải xác định đúng ownership, framing và trạng thái của message đã nhận.

## Liên hệ và bước tiếp theo

[[PROTOCOL-QUIC|QUIC — stream, connection và kiểm chứng địa chỉ]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[PROTOCOL-QUIC|QUIC — stream, connection và kiểm chứng địa chỉ]] — Mục tiêu 'Vẽ ranh giới HTTP message và QUIC stream.' cần mô hình QUIC — stream, connection và kiểm chứng địa chỉ. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-42775420035E17A7D510E87D\|PROTOCOL:HTTP-3: v1.3:knowledge_fact]] — "RFC 9114 ánh xạ mỗi request lên một client-initiated bidirectional QUIC stream; HEADERS và DATA có thứ tự hợp lệ, còn control stream có vai trò riêng." | IETF / RFC Editor | CURRENT | SUPPORTED / AI_REVIEWED | §4.1 HTTP Message Framing; §6 Stream Mapping and Usage — [[EVIDENCE-8D04B81E8C20010F84D4889B\|rfc9114.html: §4.1 HTTP Message Framing; §6 Stream Mapping and Usage]] |
| [[CLAIM-BC3410121C90BD66DAED1491\|PROTOCOL:HTTP-3: v1.3:knowledge:Cơ chế và phân lớp]] — "## Cơ chế và phân lớp\n\nHTTP/3 sử dụng QUIC stream để mang HTTP message. HEADERS biểu diễn phần trường, DATA mang nội dung; trailer nếu có đánh dấu một phần khác của message. Par… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | §4.1 HTTP Message Framing; §6 Stream Mapping and Usage — [[EVIDENCE-8D04B81E8C20010F84D4889B\|rfc9114.html: §4.1 HTTP Message Framing; §6 Stream Mapping and Usage]] |
| [[CLAIM-9640066C7549A0BF372E0CBD\|PROTOCOL:HTTP-3: v1.3:knowledge:Ownership và state dùng chung]] — "## Ownership và state dùng chung\n\nRequest stream thuộc một công việc HTTP, trong khi control stream và cơ chế nén trường có trạng thái phục vụ nhiều trao đổi. Việc đóng request … (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | §4.1 HTTP Message Framing; §6 Stream Mapping and Usage — [[EVIDENCE-8D04B81E8C20010F84D4889B\|rfc9114.html: §4.1 HTTP Message Framing; §6 Stream Mapping and Usage]] |
| [[CLAIM-42C5E6F73FECDA959A42709F\|PROTOCOL:HTTP-3: v1.3:knowledge:Invariant và tradeoff]] — "## Invariant và tradeoff\n\nDiễn giải: mọi byte được bàn giao cho upstream phải thuộc đúng body của request đang xét; trạng thái parser phải xác định liệu vùng buffer chứa message… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | §4.1 HTTP Message Framing; §6 Stream Mapping and Usage — [[EVIDENCE-8D04B81E8C20010F84D4889B\|rfc9114.html: §4.1 HTTP Message Framing; §6 Stream Mapping and Usage]] |
| [[CLAIM-D1351840EFFC441E740C62F5\|PROTOCOL:HTTP-3: v1.3:knowledge:Nguyên tắc review]] — "## Nguyên tắc review\n\nSo sánh lifetime request, control stream và buffer khi đọc advisory. Với lỗi ở nén trường, tên encoder không tự chỉ ra hàm hay thuật toán cụ thể; nguồn chu… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | §4.1 HTTP Message Framing; §6 Stream Mapping and Usage — [[EVIDENCE-8D04B81E8C20010F84D4889B\|rfc9114.html: §4.1 HTTP Message Framing; §6 Stream Mapping and Usage]] |




## Phạm vi kiểm chứng

[[EVIDENCE-8D04B81E8C20010F84D4889B|rfc9114.html: §4.1 HTTP Message Framing; §6 Stream Mapping and Usage]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

