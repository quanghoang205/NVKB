---
entity_type: protocol
id: PROTOCOL:DNS
title: DNS resolver — cache, công việc chờ và quyền sở hữu
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- DNS resolver — cache, công việc chờ và quyền sở hữu
tags:
- nginx
- protocol
- knowledge
editorial_maturity: AI_REVIEWED
---

# DNS resolver — cache, công việc chờ và quyền sở hữu

Directive resolver chỉ định name servers để phân giải tên upstream; tài liệu mô tả TTL/cache, phạm vi truy vấn và timeout. Resolver context không phải identity đã được TLS xác thực.

## Mục tiêu đo được

- Phân biệt cached DNS result với context chờ của request.
- Giải thích vì sao timeout và cancellation cần ownership riêng.


Kiến thức tiên quyết: [[COMPONENT-EVENT-DRIVEN|Event loop và non-blocking I/O]], [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]].

Nguồn xác nhận: [[CLAIM-D4BF028B5E46E158B345BE41|phạm vi tài liệu]].

## Cơ chế bình thường

Khi cần địa chỉ từ một tên upstream, resolver gửi truy vấn đến name server cấu hình và nhận kết quả để kết nối. Tài liệu NGINX mô tả cache theo TTL và khả năng cấu hình thời gian hiệu lực. Timeout chờ truy vấn không cùng ý nghĩa với thời hạn cache: hết thời gian chờ của một request không buộc mọi kết quả cache phải biến mất.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-8BE294EE9896545CFC3EC6C9|Claim của section]].

## Ownership và lifecycle

Mô hình thiết kế gồm yêu cầu phân giải, state truy vấn và những công việc ứng dụng đang chờ. Nhiều request hoặc subrequest có thể cần cùng tên nhưng có thời gian kết thúc khác nhau. Chia sẻ kết quả tiết kiệm truy vấn; nó không có nghĩa mọi người chờ chung một lifetime. Khi client hủy request hoặc tác vụ OCSP kết thúc, callback chưa chạy phải không còn quyền dùng context đã giải phóng.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-78E124EF6650F5ED2AAFBA8D|Claim của section]].

## Invariant và trust boundary

Diễn giải: mỗi callback trả lời phải tìm được một owner còn hợp lệ, và chỉ tác động đúng tác vụ đang chờ. Trả lời DNS là dữ liệu, không phải chứng cứ peer được phép phục vụ ứng dụng. TLS identity verification và authorization vẫn là nghĩa vụ riêng sau khi đã có địa chỉ. Giới hạn phạm vi resolver có ích cho vận hành nhưng không sửa UAF trong quản lý callback.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-5207086B18714E0BBD06C4A3|Claim của section]].

## Tradeoff và kiểm soát

Cache lâu giảm latency và lưu lượng truy vấn nhưng trì hoãn phản ánh thay đổi; nhiều truy vấn đồng thời tăng state chờ. Giới hạn timeout giảm thời gian giữ tài nguyên, đồng thời tạo thêm nhánh cleanup phải đúng. Đọc riêng CVE OCSP và CVE subrequest: chúng cùng dùng resolver nhưng không chứng minh cùng đường lỗi. Tài liệu directive không cho đủ cấu trúc dữ liệu nội bộ để xác định fault location bằng từ khóa.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-B94FC2AAA573561E1A8231A1|Claim của section]].


## Tự đánh giá

Subrequest bị hủy có cho phép giải phóng mọi state DNS của tên mà nó dùng không?

## Đáp án và giải thích

Không thể kết luận vậy; có thể có các owner khác còn chờ hoặc cache còn hiệu lực. Cần contract chia sẻ và lifetime thực tế.

## Liên hệ và bước tiếp theo

[[COMPONENT-EVENT-DRIVEN|Event loop và non-blocking I/O]], [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]] — Mục tiêu 'Phân biệt cached DNS result với context chờ của request.' cần mô hình Connection và HTTP request: hai vòng đời. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-EVENT-DRIVEN|Event loop và non-blocking I/O]] — Mục tiêu 'Phân biệt cached DNS result với context chờ của request.' cần mô hình Event loop và non-blocking I/O. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-D4BF028B5E46E158B345BE41\|PROTOCOL:DNS: v1.3:knowledge_fact]] — "Directive resolver chỉ định name servers để phân giải tên upstream; tài liệu mô tả TTL/cache, phạm vi truy vấn và timeout. Resolver context không phải identity đã được TLS xác thự… (mở Claim để đọc đủ) | NGINX / F5 | CURRENT | SUPPORTED / AI_REVIEWED | #resolver; #resolver_timeout — [[EVIDENCE-4FF4160FB0B56E492E1FCF7C\|ngx_http_core_module.html: #resolver; #resolver_timeout]] |
| [[CLAIM-8BE294EE9896545CFC3EC6C9\|PROTOCOL:DNS: v1.3:knowledge:Cơ chế bình thường]] — "## Cơ chế bình thường\n\nKhi cần địa chỉ từ một tên upstream, resolver gửi truy vấn đến name server cấu hình và nhận kết quả để kết nối. Tài liệu NGINX mô tả cache theo TTL và khả… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #resolver; #resolver_timeout — [[EVIDENCE-4FF4160FB0B56E492E1FCF7C\|ngx_http_core_module.html: #resolver; #resolver_timeout]] |
| [[CLAIM-78E124EF6650F5ED2AAFBA8D\|PROTOCOL:DNS: v1.3:knowledge:Ownership và lifecycle]] — "## Ownership và lifecycle\n\nMô hình thiết kế gồm yêu cầu phân giải, state truy vấn và những công việc ứng dụng đang chờ. Nhiều request hoặc subrequest có thể cần cùng tên nhưng c… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #resolver; #resolver_timeout — [[EVIDENCE-4FF4160FB0B56E492E1FCF7C\|ngx_http_core_module.html: #resolver; #resolver_timeout]] |
| [[CLAIM-5207086B18714E0BBD06C4A3\|PROTOCOL:DNS: v1.3:knowledge:Invariant và trust boundary]] — "## Invariant và trust boundary\n\nDiễn giải: mỗi callback trả lời phải tìm được một owner còn hợp lệ, và chỉ tác động đúng tác vụ đang chờ. Trả lời DNS là dữ liệu, không phải chứn… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #resolver; #resolver_timeout — [[EVIDENCE-4FF4160FB0B56E492E1FCF7C\|ngx_http_core_module.html: #resolver; #resolver_timeout]] |
| [[CLAIM-B94FC2AAA573561E1A8231A1\|PROTOCOL:DNS: v1.3:knowledge:Tradeoff và kiểm soát]] — "## Tradeoff và kiểm soát\n\nCache lâu giảm latency và lưu lượng truy vấn nhưng trì hoãn phản ánh thay đổi; nhiều truy vấn đồng thời tăng state chờ. Giới hạn timeout giảm thời gian… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #resolver; #resolver_timeout — [[EVIDENCE-4FF4160FB0B56E492E1FCF7C\|ngx_http_core_module.html: #resolver; #resolver_timeout]] |




## Phạm vi kiểm chứng

[[EVIDENCE-4FF4160FB0B56E492E1FCF7C|ngx_http_core_module.html: #resolver; #resolver_timeout]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

