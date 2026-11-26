---
entity_type: weakness
id: WEAKNESS:CWE-787
title: Out-of-bounds Write — biên bộ nhớ và giới hạn tác động
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Out-of-bounds Write — biên bộ nhớ và giới hạn tác động
tags:
- nginx
- weakness
- knowledge
editorial_maturity: AI_REVIEWED
---

# Out-of-bounds Write — biên bộ nhớ và giới hạn tác động

CWE-787 mô tả ghi ngoài biên buffer dự định; các hậu quả và biện pháp giảm thiểu được taxonomy nêu không chứng minh tất cả cùng xảy ra ở một CVE cụ thể.

## Mục tiêu đo được

- Phân biệt spatial safety
- temporal safety và initialization.
- Tách lớp lỗi memory khỏi hậu quả cụ thể được chứng minh.


Kiến thức tiên quyết: [[COMPONENT-MEMORY-POOL|Memory pool: ownership, lifetime và cleanup]], [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]].

Nguồn xác nhận: [[CLAIM-9152EC0FFF2E4DF223C54BA7|phạm vi tài liệu]].

## Ba câu hỏi về bộ nhớ

Một lần truy cập cần trả lời ba câu riêng: địa chỉ có nằm trong vùng hợp lệ không, allocation có còn sống không, và dữ liệu đã được khởi tạo cho mục đích hiện tại chưa? CWE-787 tập trung ghi ngoài biên buffer. Dùng taxonomy chi tiết ở bài CVE để phân biệt over-read, overwrite, use-after-free hay uninitialized access; không gộp tất cả thành một root cause. Các phần lifetime và initialization dưới đây là so sánh sư phạm, không mở rộng định nghĩa CWE-787.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-FAD86353F9C9DA531271C500|Claim của section]].

## Ownership và lifecycle

Allocation tạo capacity; owner xác định ai chịu trách nhiệm kết thúc lifetime; consumer chỉ được dùng trong contract đó. Pool giải phóng tài nguyên theo nhóm giúp quản lý hiệu quả nhưng không tự theo dõi mọi con trỏ mà module khác giữ. Một callback còn chờ hoặc subrequest còn chạy làm việc xác định lifetime khó hơn. Spatial safety không sửa temporal safety và ngược lại.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-B660A7FCCC621BB9AFBA7475|Claim của section]].

## Invariant và tradeoff

Diễn giải: kiểm kích thước trước chuyển kiểu/cấp phát, giữ con trỏ/độ dài đồng bộ, và bảo đảm mọi đường cleanup thống nhất. Ownership rõ có thể làm thiết kế dài hơn nhưng giảm phụ thuộc ngầm; sao chép dữ liệu giảm chia sẻ lifetime nhưng tốn memory và CPU. Chia sẻ buffer giúp throughput nhưng cần protocol trả ownership hoặc reference management rõ ràng.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-31D00EBDEFF632BD91B7F270|Claim của section]].

## Hậu quả và kiểm soát

Over-read không tự chứng minh dữ liệu đã được gửi ra ngoài; overwrite không tự chứng minh code execution; worker crash không tự chứng minh toàn host ngừng hoạt động. Đọc source impact của từng CVE trước khi kết luận. Hardening có thể giảm khả năng hoặc hậu quả của một số lớp lỗi nhưng không làm phép truy cập sai trở thành đúng. Giữ quyền worker thấp, kiểm chứng bản vá và review các đường lỗi là các lớp bổ sung, không phải phép đo miễn nhiễm.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-986BA3F6AA09638B5F978268|Claim của section]].


## Tự đánh giá

Một lỗi thuộc CWE memory có đủ để gắn confirmed RCE không?

## Đáp án và giải thích

Không. CWE phân loại weakness; cần evidence riêng cho hậu quả và điều kiện được nguồn công bố.

## Liên hệ và bước tiếp theo

[[COMPONENT-MEMORY-POOL|Memory pool: ownership, lifetime và cleanup]], [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-CONNECTION-LIFECYCLE|Connection và HTTP request: hai vòng đời]] — Mục tiêu 'Phân biệt spatial safety' cần mô hình Connection và HTTP request: hai vòng đời. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-MEMORY-POOL|Memory pool: ownership, lifetime và cleanup]] — Mục tiêu 'Phân biệt spatial safety' cần mô hình Memory pool: ownership, lifetime và cleanup. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-9152EC0FFF2E4DF223C54BA7\|WEAKNESS:CWE-787: v1.3:knowledge_fact]] — "CWE-787 mô tả ghi ngoài biên buffer dự định; các hậu quả và biện pháp giảm thiểu được taxonomy nêu không chứng minh tất cả cùng xảy ra ở một CVE cụ thể." | MITRE CWE | CURRENT | SUPPORTED / AI_REVIEWED | Description; Common Consequences; Potential Mitigations — [[EVIDENCE-2EA269027FEA7940F910D54E\|787.html: Description; Common Consequences; Potential Mitigations]] |
| [[CLAIM-FAD86353F9C9DA531271C500\|WEAKNESS:CWE-787: v1.3:knowledge:Ba câu hỏi về bộ nhớ]] — "## Ba câu hỏi về bộ nhớ\n\nMột lần truy cập cần trả lời ba câu riêng: địa chỉ có nằm trong vùng hợp lệ không, allocation có còn sống không, và dữ liệu đã được khởi tạo cho mục đíc… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Description; Common Consequences; Potential Mitigations — [[EVIDENCE-2EA269027FEA7940F910D54E\|787.html: Description; Common Consequences; Potential Mitigations]] |
| [[CLAIM-B660A7FCCC621BB9AFBA7475\|WEAKNESS:CWE-787: v1.3:knowledge:Ownership và lifecycle]] — "## Ownership và lifecycle\n\nAllocation tạo capacity; owner xác định ai chịu trách nhiệm kết thúc lifetime; consumer chỉ được dùng trong contract đó. Pool giải phóng tài nguyên th… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Description; Common Consequences; Potential Mitigations — [[EVIDENCE-2EA269027FEA7940F910D54E\|787.html: Description; Common Consequences; Potential Mitigations]] |
| [[CLAIM-31D00EBDEFF632BD91B7F270\|WEAKNESS:CWE-787: v1.3:knowledge:Invariant và tradeoff]] — "## Invariant và tradeoff\n\nDiễn giải: kiểm kích thước trước chuyển kiểu/cấp phát, giữ con trỏ/độ dài đồng bộ, và bảo đảm mọi đường cleanup thống nhất. Ownership rõ có thể làm thi… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Description; Common Consequences; Potential Mitigations — [[EVIDENCE-2EA269027FEA7940F910D54E\|787.html: Description; Common Consequences; Potential Mitigations]] |
| [[CLAIM-986BA3F6AA09638B5F978268\|WEAKNESS:CWE-787: v1.3:knowledge:Hậu quả và kiểm soát]] — "## Hậu quả và kiểm soát\n\nOver-read không tự chứng minh dữ liệu đã được gửi ra ngoài; overwrite không tự chứng minh code execution; worker crash không tự chứng minh toàn host ngừ… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | Description; Common Consequences; Potential Mitigations — [[EVIDENCE-2EA269027FEA7940F910D54E\|787.html: Description; Common Consequences; Potential Mitigations]] |




## Phạm vi kiểm chứng

[[EVIDENCE-0C6A671431F2CA2EA43D9D2E|CVE-2024-32760]], [[EVIDENCE-2EA269027FEA7940F910D54E|787.html: Description; Common Consequences; Potential Mitigations]], [[EVIDENCE-93E077BF039FAE4289B5A57E|CWE - CWE-787: Out-of-bounds Write (5.0)]], [[EVIDENCE-A4EEA6D224631DCC0EB9BC48|CWE - CWE-787: Out-of-bounds Write (5.0)]], [[EVIDENCE-F03600C558EF2F690E6E4A14|CVE-2026-123007]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

