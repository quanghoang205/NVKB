---
entity_type: module
id: MODULE:NGX-HTTP-MP4-MODULE
title: MP4 pseudo-streaming và ranh giới metadata
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- MP4 pseudo-streaming và ranh giới metadata
tags:
- nginx
- module
- knowledge
editorial_maturity: AI_REVIEWED
---

# MP4 pseudo-streaming và ranh giới metadata

Module MP4 thực hiện pseudo-streaming; việc xử lý metadata có chi phí CPU, bộ nhớ và I/O. Tài liệu phân biệt xử lý media với gửi file tĩnh và quy định giới hạn buffer metadata.

## Mục tiêu đo được

- Phân biệt gửi file MP4 tĩnh với việc phân tích và tái sắp metadata.
- Giải thích vì sao kích thước buffer và tính hợp lệ của index là hai nghĩa vụ riêng.


Kiến thức tiên quyết: [[COMPONENT-MEMORY-POOL|Memory pool: ownership, lifetime và cleanup]], [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]].

Nguồn xác nhận: [[CLAIM-51861748B86419308252ADB7|phạm vi tài liệu]].

## Cơ chế bình thường và ownership

Module không phải bộ giải mã video tổng quát. Nó đọc cấu trúc mô tả media để tạo một đoạn có thời gian bắt đầu/kết thúc phù hợp với trình phát. Metadata moov chứa thông tin index. Khi metadata nằm cuối file, server phải chuẩn bị thứ tự đầu ra thích hợp trước khi phát dữ liệu; việc chuẩn bị file ngay ở bước xuất bản có thể giảm công việc lặp tại worker. Request không có yêu cầu xử lý đoạn có thể đi theo đường gửi tài nguyên tĩnh được tài liệu mô tả.

Tách ba loại tài nguyên khi thiết kế: file nguồn do hệ thống lưu trữ quản lý, buffer metadata phục vụ xử lý, và các buffer đầu ra có thể chưa gửi hết. Việc đã đọc xong metadata không có nghĩa output đã hoàn thành. Đây là mô hình ownership để review, không xác nhận chính xác cấu trúc C của từng bản NGINX. Khi request kết thúc hoặc bị hủy, không được còn callback dùng bộ nhớ thuộc request đã giải phóng.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-9C74AC1FAF0F8E17A8524E3B|Claim của section]].

## Invariant về cấu trúc và kích thước

Diễn giải phòng vệ: offset phải nằm trong vùng file tương ứng, số phần tử phải phù hợp độ dài bảng, và phép nhân/cộng để tính kích thước phải biểu diễn được trong kiểu đích trước cấp phát. Kiểm giới hạn một buffer không thay thế kiểm quan hệ giữa các bảng. Máy 32-bit có miền biểu diễn khác 64-bit; điều này giúp hiểu vì sao applicability có thể giới hạn kiến trúc, nhưng không tự chứng minh CVE nào là integer overflow.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-E7B7C6539590D6C0BDC27746|Claim của section]].

## Tradeoff và kiểm soát

Giới hạn metadata tránh một request chiếm bộ nhớ không giới hạn; tăng giới hạn để nhận file lớn cũng tăng ngân sách tài nguyên cần dự phòng. Tài liệu cho biết vượt mp4_max_buffer_size dẫn đến lỗi xử lý; đó không phải bằng chứng rằng mọi lỗi parser đều được chặn. Chuẩn hóa media trong quy trình xuất bản và hạn chế ai được đưa file vào vùng phục vụ giúp quản trị đầu vào, còn bản vá vẫn cần thiết cho lỗi implementation.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-527D9D77AD2987253AAB97A2|Claim của section]].

## Liên hệ nghiên cứu

CVE-2024-7347 mô tả over-read và kết thúc worker; CVE-2026-27784 giới hạn 32-bit; CVE-2026-32647 có khả năng thực thi mã được CNA nêu như tác động có thể xảy ra. Đọc từng note để lấy evidence và giới hạn; cùng module không có nghĩa cùng lỗi hay cùng hậu quả. Không sử dụng tên CWE để suy vị trí atom hoặc hàm lỗi.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-8C2EAF607EF92AA4FEA3A49E|Claim của section]].


## Tự đánh giá

Tại sao một file phát được bằng trình phát không đủ chứng minh đường xử lý metadata trên server an toàn? Vì sao không chuyển điều kiện 32-bit của 27784 sang 32647?

## Đáp án và giải thích

Hai phần mềm có parser, phép tính và lifecycle riêng. Điều kiện kiến trúc là dữ kiện của từng advisory; chỉ nguồn của đúng CVE mới hỗ trợ việc thu hẹp phạm vi đó.

## Liên hệ và bước tiếp theo

[[COMPONENT-MEMORY-POOL|Memory pool: ownership, lifetime và cleanup]], [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]]

## Quan hệ có định kiểu

- `CONTEXTUAL_ASSOCIATION` → [[WEAKNESS-CWE-125|CWE-125 — Out-of-bounds read]] — Nguồn 7347 nêu worker kết thúc; không mở rộng thành host/root compromise. Kiến trúc cung cấp context học lớp lỗi; không xác nhận mọi instance có lỗi. **INTERPRETATION / PARTIAL**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-MEMORY-POOL|Memory pool: ownership, lifetime và cleanup]] — Mục tiêu 'Phân biệt gửi file MP4 tĩnh với việc phân tích và tái sắp metadata.' cần mô hình Memory pool: ownership, lifetime và cleanup. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]] — Mục tiêu 'Phân biệt gửi file MP4 tĩnh với việc phân tích và tái sắp metadata.' cần mô hình Connection và HTTP request: hai vòng đời. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-51861748B86419308252ADB7\|MODULE:NGX-HTTP-MP4-MODULE: v1.3:knowledge_fact]] — "Module MP4 thực hiện pseudo-streaming; việc xử lý metadata có chi phí CPU, bộ nhớ và I/O. Tài liệu phân biệt xử lý media với gửi file tĩnh và quy định giới hạn buffer metadata." | NGINX / F5 | CURRENT | SUPPORTED / AI_REVIEWED | Introduction; — [[EVIDENCE-F28678BADEAF73E031E9FFF2\|ngx_http_mp4_module.html: Introduction;]] |
| [[CLAIM-9C74AC1FAF0F8E17A8524E3B\|MODULE:NGX-HTTP-MP4-MODULE: v1.3:knowledge:Cơ chế bình thường và ownership]] — "## Cơ chế bình thường và ownership\n\nModule không phải bộ giải mã video tổng quát. Nó đọc cấu trúc mô tả media để tạo một đoạn có thời gian bắt đầu/kết thúc phù hợp với trình phá… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-F28678BADEAF73E031E9FFF2\|ngx_http_mp4_module.html: Introduction;]] |
| [[CLAIM-E7B7C6539590D6C0BDC27746\|MODULE:NGX-HTTP-MP4-MODULE: v1.3:knowledge:Invariant về cấu trúc và kích thước]] — "## Invariant về cấu trúc và kích thước\n\nDiễn giải phòng vệ: offset phải nằm trong vùng file tương ứng, số phần tử phải phù hợp độ dài bảng, và phép nhân/cộng để tính kích thước … (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-F28678BADEAF73E031E9FFF2\|ngx_http_mp4_module.html: Introduction;]] |
| [[CLAIM-527D9D77AD2987253AAB97A2\|MODULE:NGX-HTTP-MP4-MODULE: v1.3:knowledge:Tradeoff và kiểm soát]] — "## Tradeoff và kiểm soát\n\nGiới hạn metadata tránh một request chiếm bộ nhớ không giới hạn; tăng giới hạn để nhận file lớn cũng tăng ngân sách tài nguyên cần dự phòng. Tài liệu c… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-F28678BADEAF73E031E9FFF2\|ngx_http_mp4_module.html: Introduction;]] |
| [[CLAIM-8C2EAF607EF92AA4FEA3A49E\|MODULE:NGX-HTTP-MP4-MODULE: v1.3:knowledge:Liên hệ nghiên cứu]] — "## Liên hệ nghiên cứu\n\nCVE-2024-7347 mô tả over-read và kết thúc worker; CVE-2026-27784 giới hạn 32-bit; CVE-2026-32647 có khả năng thực thi mã được CNA nêu như tác động có thể … (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-F28678BADEAF73E031E9FFF2\|ngx_http_mp4_module.html: Introduction;]] |




## Phạm vi kiểm chứng

[[EVIDENCE-F28678BADEAF73E031E9FFF2|ngx_http_mp4_module.html: Introduction;]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

