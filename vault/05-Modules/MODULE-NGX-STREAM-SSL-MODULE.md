---
entity_type: module
id: MODULE:NGX-STREAM-SSL-MODULE
title: Stream TLS — chứng thư, policy và trạng thái OCSP
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- Stream TLS — chứng thư, policy và trạng thái OCSP
tags:
- nginx
- module
- knowledge
editorial_maturity: AI_REVIEWED
---

# Stream TLS — chứng thư, policy và trạng thái OCSP

Module stream SSL có các directive riêng để xác minh client certificate và OCSP; ssl_ocsp yêu cầu policy xác minh chứng thư thích hợp và resolver cho tên OCSP responder.

## Mục tiêu đo được

- Phân biệt chứng thư hợp chuỗi với chứng thư còn được chấp nhận theo revocation policy.
- Xác định context virtual server của quyết định xác thực.


Kiến thức tiên quyết: [[PROTOCOL-TLS|TLS 1.3: handshake, identity và protected records]], [[COMPONENT-TLS-SESSION-LIFECYCLE|TLS resumption: state, ticket và policy hiện hành]].

Nguồn xác nhận: [[CLAIM-D06893BC40E7F96FFDB00FBD|phạm vi tài liệu]].

## Cơ chế bình thường

TLS trong stream xử lý bảo vệ và xác thực kết nối trước khi proxy dữ liệu ứng dụng. Certificate chain, kết quả revocation và policy yêu cầu chứng thư là những dữ kiện khác nhau. Tài liệu phân biệt xác minh chứng thư được yêu cầu, tùy chọn, và OCSP validation. Một kết quả OCSP đã trả về không tự thực thi policy; đường hoàn tất handshake phải sử dụng kết quả đó đúng cách.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-39D1855A0C973C0B12414028|Claim của section]].

## Ownership và lifecycle

State handshake thuộc connection, trong khi cấu hình trust và policy thuộc virtual server/cấu hình đang sử dụng. Resolver hoặc OCSP có thể cần chờ ngoài một lần callback; request kiểm tra có owner và điểm hoàn tất riêng. Diễn giải phòng vệ là quyết định chấp nhận không được xảy ra trước kết quả bắt buộc, và callback muộn không được dùng context đã hủy. Session resumption lại mang state từ kết nối trước sang quyết định mới, nên không được coi socket mới đã thừa hưởng mọi quyền cũ.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-BA964F6D3A07E0E9C9ABFA96|Claim của section]].

## Invariant và tradeoff

Chính sách của server được chọn phải chi phối client-auth decision, kể cả server không phải mặc định và handshake rút gọn. Cache làm giảm độ trễ nhưng kéo dài thời gian state tồn tại; cần scope, timeout và quy tắc đổi khóa rõ ràng. OCSP bổ sung trạng thái thu hồi nhưng tạo phụ thuộc vào resolver, responder và timeout; chính sách lỗi phải được thiết kế rõ thay vì suy từ việc đã bật TLS.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-B4661F8BE2B935AF748D532C|Claim của section]].

## Phòng vệ và giới hạn

Review identity context qua virtual-server selection, handshake và resume. Ghi nguồn trust, revocation policy và thế hệ cấu hình trong chứng cứ triển khai. Các directive của stream không được mặc nhiên đồng nhất với HTTP SSL. Bài này mô tả contract cần có; các CVE riêng mới xác định thời điểm và phạm vi implementation vi phạm contract.

_Diễn giải tác giả; PARTIAL_: [[CLAIM-A035D49584A80D6E66BE7373|Claim của section]].


## Tự đánh giá

OCSP trả revoked nhưng handshake thành công có thể được coi là client đã hợp lệ vì chain đúng không?

## Đáp án và giải thích

Không khi policy bắt buộc revocation validation; chain và revocation kiểm tra các điều kiện khác nhau và đều phải chi phối quyết định cuối.

## Liên hệ và bước tiếp theo

[[PROTOCOL-TLS|TLS 1.3: handshake, identity và protected records]], [[COMPONENT-TLS-SESSION-LIFECYCLE|TLS resumption: state, ticket và policy hiện hành]]

## Quan hệ có định kiểu

- `REQUIRES_KNOWLEDGE_OF` → [[PROTOCOL-TLS|TLS 1.3: handshake, identity và protected records]] — Mục tiêu 'Phân biệt chứng thư hợp chuỗi với chứng thư còn được chấp nhận theo revocation policy.' cần mô hình TLS 1.3: handshake, identity và protected records. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.
- `REQUIRES_KNOWLEDGE_OF` → [[COMPONENT-TLS-SESSION-LIFECYCLE|TLS resumption: state, ticket và policy hiện hành]] — Mục tiêu 'Phân biệt chứng thư hợp chuỗi với chứng thư còn được chấp nhận theo revocation policy.' cần mô hình TLS resumption: state, ticket và policy hiện hành. Quyết định sư phạm, không là fault location. **PEDAGOGICAL / PARTIAL**.



## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-D06893BC40E7F96FFDB00FBD\|MODULE:NGX-STREAM-SSL-MODULE: v1.3:knowledge_fact]] — "Module stream SSL có các directive riêng để xác minh client certificate và OCSP; ssl_ocsp yêu cầu policy xác minh chứng thư thích hợp và resolver cho tên OCSP responder." | NGINX / F5 | CURRENT | SUPPORTED / AI_REVIEWED | #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache — [[EVIDENCE-3A43D6C5BBCD84195240076C\|ngx_stream_ssl_module.html: #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache]] |
| [[CLAIM-39D1855A0C973C0B12414028\|MODULE:NGX-STREAM-SSL-MODULE: v1.3:knowledge:Cơ chế bình thường]] — "## Cơ chế bình thường\n\nTLS trong stream xử lý bảo vệ và xác thực kết nối trước khi proxy dữ liệu ứng dụng. Certificate chain, kết quả revocation và policy yêu cầu chứng thư là n… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache — [[EVIDENCE-3A43D6C5BBCD84195240076C\|ngx_stream_ssl_module.html: #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache]] |
| [[CLAIM-BA964F6D3A07E0E9C9ABFA96\|MODULE:NGX-STREAM-SSL-MODULE: v1.3:knowledge:Ownership và lifecycle]] — "## Ownership và lifecycle\n\nState handshake thuộc connection, trong khi cấu hình trust và policy thuộc virtual server/cấu hình đang sử dụng. Resolver hoặc OCSP có thể cần chờ ngo… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache — [[EVIDENCE-3A43D6C5BBCD84195240076C\|ngx_stream_ssl_module.html: #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache]] |
| [[CLAIM-B4661F8BE2B935AF748D532C\|MODULE:NGX-STREAM-SSL-MODULE: v1.3:knowledge:Invariant và tradeoff]] — "## Invariant và tradeoff\n\nChính sách của server được chọn phải chi phối client-auth decision, kể cả server không phải mặc định và handshake rút gọn. Cache làm giảm độ trễ nhưng … (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache — [[EVIDENCE-3A43D6C5BBCD84195240076C\|ngx_stream_ssl_module.html: #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache]] |
| [[CLAIM-A035D49584A80D6E66BE7373\|MODULE:NGX-STREAM-SSL-MODULE: v1.3:knowledge:Phòng vệ và giới hạn]] — "## Phòng vệ và giới hạn\n\nReview identity context qua virtual-server selection, handshake và resume. Ghi nguồn trust, revocation policy và thế hệ cấu hình trong chứng cứ triển kh… (mở Claim để đọc đủ) | NVKB AI curation | CURRENT | PARTIAL / AI_REVIEWED | #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache — [[EVIDENCE-3A43D6C5BBCD84195240076C\|ngx_stream_ssl_module.html: #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache]] |




## Phạm vi kiểm chứng

[[EVIDENCE-3A43D6C5BBCD84195240076C|ngx_stream_ssl_module.html: #ssl_verify_client; #ssl_ocsp; #ssl_certificate; #ssl_session_cache]]

Per-section interpretations remain PARTIAL; not a source-code audit or human approval.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

