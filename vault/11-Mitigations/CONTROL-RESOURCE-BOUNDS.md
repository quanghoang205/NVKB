---
entity_type: securitycontrol
id: CONTROL:RESOURCE-BOUNDS
title: Giới hạn tài nguyên và tiến độ event loop
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Giới hạn tài nguyên và tiến độ event loop
tags:
- nginx
- securitycontrol
- knowledge
editorial_maturity: AI_REVIEWED
---

# Giới hạn tài nguyên và tiến độ event loop

worker_connections giới hạn số connection của một worker, bao gồm kết nối tới upstream; khả năng mở file descriptor và giới hạn hệ điều hành còn ràng buộc capacity thực tế.

## Mục tiêu đo được

- Tính ngân sách connection theo cả client và upstream.
- Phân biệt giới hạn tài nguyên với tính đúng của đường xử lý lỗi.


Kiến thức tiên quyết: [[COMPONENT-EVENT-DRIVEN|Event loop và non-blocking I/O]], [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]].

Nguồn xác nhận: [[CLAIM-04713563C5E55DDA4423EBD3|phạm vi tài liệu]].

## Cơ chế bình thường

Worker quản lý nhiều connection trong event loop. Một request proxy có thể cần tài nguyên phía client lẫn upstream, cùng buffer, timer và file. Giới hạn connection không phải số request tối đa vì keepalive và multiplexing thay đổi ánh xạ. Giới hạn file descriptor của tiến trình/hệ điều hành có thể khiến capacity thực tế thấp hơn cấu hình dự định.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-E94BEFD17EF78FE8CD62A9DA|Claim của section]].

## Ownership và liveness

Khi cạn tài nguyên, đường cấp phát thất bại vẫn phải giữ state nhất quán và trả quyền điều khiển. Một vòng lặp liên tục retry mà không tạo tiến độ có thể tiêu thụ CPU dù memory còn đủ. Timer không bảo đảm hiệu lực nếu event loop không được chạy timer callback. Liveness vì vậy bao gồm tiến độ công việc, không chỉ process còn tồn tại.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-400BD665D0DD9B68887CD6D5|Claim của section]].

## Tradeoff và phòng vệ

Tăng giới hạn giúp throughput trong một số workload nhưng giữ nhiều state và làm tăng ngân sách memory/file. Giới hạn quá thấp có thể gây từ chối công việc hợp lệ. Cần capacity model theo workload và metric quản trị; đây không là công cụ dò hệ thống bên ngoài. Kiểm đường resource exhaustion, timeout và cancellation ở code review, rồi dùng evidence deployment để kiểm bản sửa đang chạy. Điều chỉnh một knob không thay remediation lỗi UAF hoặc arithmetic.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-2E1993A8EBD3EF9A53757421|Claim của section]].


## Tự đánh giá

Tăng worker_connections có sửa được UAF trên nhánh cấp connection thất bại không?

## Đáp án và giải thích

Không; nó có thể thay thời điểm gặp nhánh lỗi nhưng không sửa contract lifetime của implementation.

## Liên hệ và bước tiếp theo

[[COMPONENT-EVENT-DRIVEN|Event loop và non-blocking I/O]], [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-EVENT-DRIVEN|Event loop và non-blocking I/O]] — Mục tiêu 'Tính ngân sách connection theo cả client và upstream.' cần mô hình Event loop và non-blocking I/O. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]] — Mục tiêu 'Tính ngân sách connection theo cả client và upstream.' cần mô hình Connection và HTTP request: hai vòng đời. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-04713563C5E55DDA4423EBD3\|CONTROL:RESOURCE-BOUNDS: v1.3:knowledge_fact]] — "worker_connections giới hạn số connection của một worker, bao gồm kết nối tới upstream; khả năng mở file descriptor và giới hạn hệ điều hành còn ràng buộc capacity thực tế." | NGINX / F5 | CURRENT | SUPPORTED / AI_REVIEWED | #worker_connections; #worker_rlimit_nofile; #worker_shutdown_timeout — [[EVIDENCE-296B9DBE04BA6F34CC70FCBA\|ngx_core_module.html: #worker_connections; #worker_rlimit_nofile; #worker_shutdown_timeout]] |
| [[CLAIM-E94BEFD17EF78FE8CD62A9DA\|CONTROL:RESOURCE-BOUNDS: v1.3:knowledge:Cơ chế bình thường]] — "## Cơ chế bình thường\n\nWorker quản lý nhiều connection trong event loop. Một request proxy có thể cần tài nguyên phía client lẫn upstream, cùng buffer, timer và file. Giới hạn c… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #worker_connections; #worker_rlimit_nofile; #worker_shutdown_timeout — [[EVIDENCE-296B9DBE04BA6F34CC70FCBA\|ngx_core_module.html: #worker_connections; #worker_rlimit_nofile; #worker_shutdown_timeout]] |
| [[CLAIM-400BD665D0DD9B68887CD6D5\|CONTROL:RESOURCE-BOUNDS: v1.3:knowledge:Ownership và liveness]] — "## Ownership và liveness\n\nKhi cạn tài nguyên, đường cấp phát thất bại vẫn phải giữ state nhất quán và trả quyền điều khiển. Một vòng lặp liên tục retry mà không tạo tiến độ có t… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #worker_connections; #worker_rlimit_nofile; #worker_shutdown_timeout — [[EVIDENCE-296B9DBE04BA6F34CC70FCBA\|ngx_core_module.html: #worker_connections; #worker_rlimit_nofile; #worker_shutdown_timeout]] |
| [[CLAIM-2E1993A8EBD3EF9A53757421\|CONTROL:RESOURCE-BOUNDS: v1.3:knowledge:Tradeoff và phòng vệ]] — "## Tradeoff và phòng vệ\n\nTăng giới hạn giúp throughput trong một số workload nhưng giữ nhiều state và làm tăng ngân sách memory/file. Giới hạn quá thấp có thể gây từ chối công v… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #worker_connections; #worker_rlimit_nofile; #worker_shutdown_timeout — [[EVIDENCE-296B9DBE04BA6F34CC70FCBA\|ngx_core_module.html: #worker_connections; #worker_rlimit_nofile; #worker_shutdown_timeout]] |




## Phạm vi kiểm chứng

[[EVIDENCE-296B9DBE04BA6F34CC70FCBA|ngx_core_module.html: #worker_connections; #worker_rlimit_nofile; #worker_shutdown_timeout]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]
