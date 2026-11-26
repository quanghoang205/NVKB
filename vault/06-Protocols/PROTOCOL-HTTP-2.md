---
entity_type: protocol
id: PROTOCOL:HTTP-2
title: HTTP/2 — multiplexing, cửa sổ và tài nguyên worker
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- HTTP/2 — multiplexing, cửa sổ và tài nguyên worker
tags:
- nginx
- protocol
- knowledge
editorial_maturity: AI_REVIEWED
---

# HTTP/2 — multiplexing, cửa sổ và tài nguyên worker

RFC 9113 quy định flow control ở cả stream và connection; cửa sổ thuộc từng hướng nhận trên một hop, không biểu diễn bộ nhớ tự do của toàn server.

## Mục tiêu đo được

- Phân biệt connection window với stream window.
- Giải thích vì sao giới hạn stream và worker_connections là hai loại tài nguyên.


Kiến thức tiên quyết: [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]], [[COMPONENT-EVENT-DRIVEN|Event loop và non-blocking I/O]].

Nguồn xác nhận: [[CLAIM-BDEE33EA299A2D92E02FE9BB|phạm vi tài liệu]].

## Hoạt động bình thường

HTTP/2 ghép nhiều stream trên một TCP connection. Mỗi stream có trạng thái và message riêng, còn connection giữ các giới hạn dùng chung. Flow control theo RFC là credit do bên nhận cấp; bên gửi tuân giới hạn ở cả hai cấp. Credit này có hướng, và chỉ thuộc hop đang trao đổi. Proxy kết thúc hop client và khởi tạo hop upstream không thể sao chép mọi trạng thái vận chuyển như một message bất biến.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-8789F163D1C5F5F13D93B107|Claim của section]].

## Ownership và lifecycle

Stream HTTP có thể hoàn tất trước connection. Một request proxy còn liên quan upstream connection và output đang chờ. Khi không cấp thêm được connection hoặc tài nguyên, nhánh lỗi phải giải phóng đúng những phần đã được tạo mà không để callback cũ dùng state đã hủy. Đây là mô hình review ownership; RFC không mô tả allocator nội bộ của NGINX.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-4C8B83FAE2534CDCC0DB1BA0|Claim của section]].

## Invariant và tradeoff

Cửa sổ là số có giới hạn và phải cập nhật bằng phép toán giữ miền hợp lệ. Nới credit giúp throughput trên đường truyền có độ trễ nhưng tăng dữ liệu đang bay và ngân sách nhận. worker_connections là giới hạn đối tượng connection của worker, không phải credit HTTP/2 và không phải số request HTTP tối đa. Đổi một giá trị không sửa được phép toán hoặc lifetime bug ở giá trị kia.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-A77B6FBC0734E5721355F7E1|Claim của section]].

## Nguyên tắc phòng vệ

Review các đường cập nhật window, cấp tài nguyên thất bại và cleanup. Giới hạn tài nguyên phải làm request thất bại có kiểm soát, không phá invariant bộ nhớ. Các counter protocol, buffer capacity và lifecycle là ba nghĩa vụ riêng. Bài CVE-2026-123007 bàn về window; CVE-2026-123633 bàn về use-after-free khi tài nguyên connection hạn chế. Không dùng hai mô tả làm hướng dẫn tạo traffic.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-301E88CB6426F5D394CA62B5|Claim của section]].


## Tự đánh giá

Có thể khẳng định tăng worker_connections sẽ vá lỗi flow control không?

## Đáp án và giải thích

Không. Một bên là giới hạn tài nguyên worker, bên kia là state/counter giao thức; remediation phải dựa release chứa bản sửa.

## Liên hệ và bước tiếp theo

[[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]], [[COMPONENT-EVENT-DRIVEN|Event loop và non-blocking I/O]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-EVENT-DRIVEN|Event loop và non-blocking I/O]] — Mục tiêu 'Phân biệt connection window với stream window.' cần mô hình Event loop và non-blocking I/O. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]] — Mục tiêu 'Phân biệt connection window với stream window.' cần mô hình Connection và HTTP request: hai vòng đời. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-BDEE33EA299A2D92E02FE9BB\|PROTOCOL:HTTP-2: v1.3:knowledge_fact]] — "RFC 9113 quy định flow control ở cả stream và connection; cửa sổ thuộc từng hướng nhận trên một hop, không biểu diễn bộ nhớ tự do của toàn server." | IETF / RFC Editor | CURRENT | SUPPORTED / AI_REVIEWED | §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE — [[EVIDENCE-2CF57B908B8E8450F39E5F7F\|rfc9113.html: §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE]] |
| [[CLAIM-8789F163D1C5F5F13D93B107\|PROTOCOL:HTTP-2: v1.3:knowledge:Hoạt động bình thường]] — "## Hoạt động bình thường\n\nHTTP/2 ghép nhiều stream trên một TCP connection. Mỗi stream có trạng thái và message riêng, còn connection giữ các giới hạn dùng chung. Flow control t… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE — [[EVIDENCE-2CF57B908B8E8450F39E5F7F\|rfc9113.html: §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE]] |
| [[CLAIM-4C8B83FAE2534CDCC0DB1BA0\|PROTOCOL:HTTP-2: v1.3:knowledge:Ownership và lifecycle]] — "## Ownership và lifecycle\n\nStream HTTP có thể hoàn tất trước connection. Một request proxy còn liên quan upstream connection và output đang chờ. Khi không cấp thêm được connecti… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE — [[EVIDENCE-2CF57B908B8E8450F39E5F7F\|rfc9113.html: §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE]] |
| [[CLAIM-A77B6FBC0734E5721355F7E1\|PROTOCOL:HTTP-2: v1.3:knowledge:Invariant và tradeoff]] — "## Invariant và tradeoff\n\nCửa sổ là số có giới hạn và phải cập nhật bằng phép toán giữ miền hợp lệ. Nới credit giúp throughput trên đường truyền có độ trễ nhưng tăng dữ liệu đan… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE — [[EVIDENCE-2CF57B908B8E8450F39E5F7F\|rfc9113.html: §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE]] |
| [[CLAIM-301E88CB6426F5D394CA62B5\|PROTOCOL:HTTP-2: v1.3:knowledge:Nguyên tắc phòng vệ]] — "## Nguyên tắc phòng vệ\n\nReview các đường cập nhật window, cấp tài nguyên thất bại và cleanup. Giới hạn tài nguyên phải làm request thất bại có kiểm soát, không phá invariant bộ … (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE — [[EVIDENCE-2CF57B908B8E8450F39E5F7F\|rfc9113.html: §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE]] |




## Phạm vi kiểm chứng

[[EVIDENCE-2CF57B908B8E8450F39E5F7F|rfc9113.html: §5.1 Stream States; §5.2 Flow Control; §6.9 WINDOW_UPDATE]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

