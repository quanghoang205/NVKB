---
entity_type: module
id: MODULE:NGX-HTTP-SSI-MODULE
title: SSI và subrequest — công việc con, output và cleanup
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- SSI và subrequest — công việc con, output và cleanup
tags:
- nginx
- module
- knowledge
editorial_maturity: AI_REVIEWED
---

# SSI và subrequest — công việc con, output và cleanup

SSI module xử lý lệnh trong response và có thể đưa nội dung khác vào qua include; việc này khác với gửi response nguyên trạng.

## Mục tiêu đo được

- Phân biệt subrequest với client connection mới.
- Nêu nghĩa vụ giữ output sống đến khi consumer kết thúc.


Kiến thức tiên quyết: [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]], [[COMPONENT-MEMORY-POOL|Memory pool: ownership, lifetime và cleanup]].

Nguồn xác nhận: [[CLAIM-C459FCC770E3F0CDA9B25D22|phạm vi tài liệu]].

## Cơ chế bình thường

SSI là filter có thể tạo công việc bổ sung để lấy nội dung và ghép vào response. Công việc con tham gia lifecycle của request nhưng không đồng nhất với một client connection mới. Một phần output có thể đã sẵn sàng trong khi phần khác còn chờ; mô hình dữ liệu cần biểu diễn thứ tự và điểm hoàn tất rõ ràng.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-E1147B065A605EEF9000EB6F|Claim của section]].

## Ownership và invariant

Diễn giải thiết kế: main request, subrequest, buffer và thao tác I/O có thể hoàn thành khác thời điểm. Callback hoàn tất phải được ràng buộc với owner còn sống; hủy main request không cho phép callback muộn tiếp tục dùng bộ nhớ cũ. Bộ lọc giữ con trỏ input phải biết khi nào upstream hoặc pool được quyền tái dùng vùng đó. Việc chuyển sang đường AIO còn thêm một mốc hoàn tất ngoài lần gọi hiện tại.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-C49DD0691E11CE3BE7D1D540|Claim của section]].

## Tradeoff và phòng vệ

Ghép nội dung tăng khả năng tái sử dụng nhưng tăng số tác vụ và tài nguyên đồng thời. Buffering giảm lệ thuộc tốc độ bên nhận nhưng cần thêm bộ nhớ/đĩa; tắt buffering không loại bỏ lifetime requirement. Review cancellation, timeout và thứ tự cleanup; dùng bản sửa khi advisory chỉ ra UAF. SSI, slice và mirror đều có thể liên hệ subrequest nhưng không được coi cùng implementation hay cùng lỗi.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-6FE3B4622D0220E05DB45343|Claim của section]].


## Tự đánh giá

Handler tạo subrequest đã trả về có nghĩa mọi output của nó đã được giải phóng được chưa?

## Đáp án và giải thích

Chưa; cần biết consumer, buffered output và callback còn chờ trước khi kết luận lifetime đã kết thúc.

## Liên hệ và bước tiếp theo

[[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]], [[COMPONENT-MEMORY-POOL|Memory pool: ownership, lifetime và cleanup]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-MEMORY-POOL|Memory pool: ownership, lifetime và cleanup]] — Mục tiêu 'Phân biệt subrequest với client connection mới.' cần mô hình Memory pool: ownership, lifetime và cleanup. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]] — Mục tiêu 'Phân biệt subrequest với client connection mới.' cần mô hình Connection và HTTP request: hai vòng đời. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-C459FCC770E3F0CDA9B25D22\|MODULE:NGX-HTTP-SSI-MODULE: v1.3:knowledge_fact]] — "SSI module xử lý lệnh trong response và có thể đưa nội dung khác vào qua include; việc này khác với gửi response nguyên trạng." | NGINX / F5 | CURRENT | SUPPORTED / AI_REVIEWED | Introduction; — [[EVIDENCE-E407E38B58D01A696505E388\|ngx_http_ssi_module.html: Introduction;]] |
| [[CLAIM-E1147B065A605EEF9000EB6F\|MODULE:NGX-HTTP-SSI-MODULE: v1.3:knowledge:Cơ chế bình thường]] — "## Cơ chế bình thường\n\nSSI là filter có thể tạo công việc bổ sung để lấy nội dung và ghép vào response. Công việc con tham gia lifecycle của request nhưng không đồng nhất với mộ… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-E407E38B58D01A696505E388\|ngx_http_ssi_module.html: Introduction;]] |
| [[CLAIM-C49DD0691E11CE3BE7D1D540\|MODULE:NGX-HTTP-SSI-MODULE: v1.3:knowledge:Ownership và invariant]] — "## Ownership và invariant\n\nDiễn giải thiết kế: main request, subrequest, buffer và thao tác I/O có thể hoàn thành khác thời điểm. Callback hoàn tất phải được ràng buộc với owner… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-E407E38B58D01A696505E388\|ngx_http_ssi_module.html: Introduction;]] |
| [[CLAIM-6FE3B4622D0220E05DB45343\|MODULE:NGX-HTTP-SSI-MODULE: v1.3:knowledge:Tradeoff và phòng vệ]] — "## Tradeoff và phòng vệ\n\nGhép nội dung tăng khả năng tái sử dụng nhưng tăng số tác vụ và tài nguyên đồng thời. Buffering giảm lệ thuộc tốc độ bên nhận nhưng cần thêm bộ nhớ/đĩa;… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Introduction; — [[EVIDENCE-E407E38B58D01A696505E388\|ngx_http_ssi_module.html: Introduction;]] |




## Phạm vi kiểm chứng

[[EVIDENCE-E407E38B58D01A696505E388|ngx_http_ssi_module.html: Introduction;]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

