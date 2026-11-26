---
entity_type: component
id: COMPONENT:REWRITE-ENGINE
title: HTTP rewrite — URI, biến và kích thước biểu diễn
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- HTTP rewrite — URI, biến và kích thước biểu diễn
tags:
- nginx
- component
- knowledge
editorial_maturity: AI_REVIEWED
---

# HTTP rewrite — URI, biến và kích thước biểu diễn

Rewrite module thay URI, tạo redirect hoặc chọn cấu hình theo điều kiện; directive xử lý theo thứ tự và có thể dẫn đến chọn lại location.

## Mục tiêu đo được

- Phân biệt URI với đường dẫn filesystem.
- Giải thích tính nhất quán giữa phép tính độ dài và dữ liệu thực sự được tạo.


Kiến thức tiên quyết: [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]].

Nguồn xác nhận: [[CLAIM-BACC9DABCE19D3B649EC4194|phạm vi tài liệu]].

## Cơ chế và lifecycle

Rewrite chạy trên state HTTP request, có thể thay URI và dẫn tới tìm location mới. Tài liệu phân biệt dừng bộ directive hiện tại và bắt đầu tìm lại location. Một URI của request, đối số URI, đường dẫn file và văn bản redirect là các biểu diễn khác nhau. Chúng có quy tắc xử lý độ dài và ký tự riêng; không thể dùng độ dài của biểu diễn này thay biểu diễn khác.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-140443274DFD77FA2EF7AC4F|Claim của section]].

## Ownership và biến

Biến, capture và output trung gian phải thuộc đúng trạng thái request tại lúc dùng. Một giá trị có thể được đánh giá khi được tham chiếu; không giả định mọi biến là hằng kể từ parsing. Mô hình review là lấy giá trị, tính dung lượng, tạo output và sử dụng trong cùng context hợp lệ. Nếu dữ liệu thay giữa hai bước, dung lượng tính trước có thể không còn đúng. Đây là invariant thiết kế, không tự khẳng định mọi CVE rewrite có cùng root cause.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-96D5CED18E608BDF687DE94B|Claim của section]].

## Ranh giới và tradeoff

Sự linh hoạt của rewrite cho phép biểu diễn policy routing gọn, nhưng tăng tương tác giữa location, URI và filesystem. Capture mang dữ liệu, không mang quyền vượt ranh giới document root. Các nhánh lỗi, redirect và internal redirect đều phải giữ giới hạn buffer và trạng thái biến. Kiểm cấu hình giúp nhận diện tính năng cần quản trị; không thay cập nhật implementation khi vendor công bố lỗi memory.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-ED9FF733B90C3CB64934CC56|Claim của section]].

## Nguyên tắc phòng vệ

Review phép tính kích thước và phép ghi cùng nhau; kiểm overflow trước khi cấp phát và kiểm mỗi bước encode. Phân biệt source-confirmed applicability với mô hình lỗi suy luận. Các CVE alias, map và rewrite có phạm vi phiên bản khác nhau dù cùng liên quan chuỗi; không sao chép điều kiện hay fix từ một bài sang bài khác.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-2000F4BB608580ED74CDF25B|Claim của section]].


## Tự đánh giá

Một chuỗi có độ dài hợp lệ trước encode có bảo đảm buffer sau encode đủ không?

## Đáp án và giải thích

Không; cần tính theo biểu diễn đích và bảo đảm giá trị được tính cũng là giá trị được ghi.

## Liên hệ và bước tiếp theo

[[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]] — Mục tiêu 'Phân biệt URI với đường dẫn filesystem.' cần mô hình Connection và HTTP request: hai vòng đời. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-BACC9DABCE19D3B649EC4194\|COMPONENT:REWRITE-ENGINE: v1.3:knowledge_fact]] — "Rewrite module thay URI, tạo redirect hoặc chọn cấu hình theo điều kiện; directive xử lý theo thứ tự và có thể dẫn đến chọn lại location." | NGINX / F5 | CURRENT | SUPPORTED / AI_REVIEWED | Introduction; — [[EVIDENCE-55E423A56D64C254EE0D8DDE\|ngx_http_rewrite_module.html: Introduction;]] |
| [[CLAIM-140443274DFD77FA2EF7AC4F\|COMPONENT:REWRITE-ENGINE: v1.3:knowledge:Cơ chế và lifecycle]] — "## Cơ chế và lifecycle\n\nRewrite chạy trên state HTTP request, có thể thay URI và dẫn tới tìm location mới. Tài liệu phân biệt dừng bộ directive hiện tại và bắt đầu tìm lại locat… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-55E423A56D64C254EE0D8DDE\|ngx_http_rewrite_module.html: Introduction;]] |
| [[CLAIM-96D5CED18E608BDF687DE94B\|COMPONENT:REWRITE-ENGINE: v1.3:knowledge:Ownership và biến]] — "## Ownership và biến\n\nBiến, capture và output trung gian phải thuộc đúng trạng thái request tại lúc dùng. Một giá trị có thể được đánh giá khi được tham chiếu; không giả định mọ… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-55E423A56D64C254EE0D8DDE\|ngx_http_rewrite_module.html: Introduction;]] |
| [[CLAIM-ED9FF733B90C3CB64934CC56\|COMPONENT:REWRITE-ENGINE: v1.3:knowledge:Ranh giới và tradeoff]] — "## Ranh giới và tradeoff\n\nSự linh hoạt của rewrite cho phép biểu diễn policy routing gọn, nhưng tăng tương tác giữa location, URI và filesystem. Capture mang dữ liệu, không mang… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-55E423A56D64C254EE0D8DDE\|ngx_http_rewrite_module.html: Introduction;]] |
| [[CLAIM-2000F4BB608580ED74CDF25B\|COMPONENT:REWRITE-ENGINE: v1.3:knowledge:Nguyên tắc phòng vệ]] — "## Nguyên tắc phòng vệ\n\nReview phép tính kích thước và phép ghi cùng nhau; kiểm overflow trước khi cấp phát và kiểm mỗi bước encode. Phân biệt source-confirmed applicability với… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-55E423A56D64C254EE0D8DDE\|ngx_http_rewrite_module.html: Introduction;]] |




## Phạm vi kiểm chứng

[[EVIDENCE-55E423A56D64C254EE0D8DDE|ngx_http_rewrite_module.html: Introduction;]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

