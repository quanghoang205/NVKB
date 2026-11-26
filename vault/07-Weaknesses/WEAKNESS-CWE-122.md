---
entity_type: weakness
id: WEAKNESS:CWE-122
title: CWE-122 — Heap-based Buffer Overflow
verification_status: INFERRED
generated: true
schema_version: 1.2.0
aliases:
- CWE-122 — Heap-based Buffer Overflow
tags:
- nginx
- weakness
- knowledge
---

# CWE-122 — Heap-based Buffer Overflow

Ghi vượt buffer được cấp phát trên heap.

## Mục tiêu đo được

- Giải thích CWE-122 — Heap-based Buffer Overflow bằng cơ chế và ranh giới tin cậy.
- Phân biệt dữ kiện từ nguồn với nhận định suy luận; truy vết bằng evidence.




## Định nghĩa

Ghi vượt buffer được cấp phát trên heap.

## Cơ chế hoạt động bình thường

Allocation phải đủ kích thước; mọi offset ghi nằm trong vùng sở hữu.

## Vị trí trong kiến trúc

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Security boundary

Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy.

## Giả định an toàn

Allocation phải đủ kích thước; mọi offset ghi nằm trong vùng sở hữu.

## Nhóm lỗi liên quan

Heap-based Buffer Overflow

## Tác động khi giả định bị vi phạm

Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố.

## Nguyên tắc phòng vệ

Dùng kiểm tra capacity/length và sanitizer khi phát triển.








## Truy vết nhận định

Mỗi link mở đúng Claim ID và giá trị; nhãn legacy không phải semantic approval.

| Claim / giá trị | Authority | Hiệu lực | Source support / review | Evidence locator |
| --- | --- | --- | --- | --- |
| [[CLAIM-222160EFDF0AF59AB1DCDE1F\|WEAKNESS:CWE-122: definition]] — "Ghi vượt buffer được cấp phát trên heap." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AC77FAA5BCFF7678FAEA0D75: Description / Potential Mitigations; topic=WEAKNESS:CWE-122 — [[EVIDENCE-AC77FAA5BCFF7678FAEA0D75\|CWE - CWE-122: Heap-based Buffer Overflow (5.0)]] |
| [[CLAIM-3E77A277EF6492A446EBE106\|WEAKNESS:CWE-122: normal_behavior]] — "Allocation phải đủ kích thước; mọi offset ghi nằm trong vùng sở hữu." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AC77FAA5BCFF7678FAEA0D75: Description / Potential Mitigations; topic=WEAKNESS:CWE-122 — [[EVIDENCE-AC77FAA5BCFF7678FAEA0D75\|CWE - CWE-122: Heap-based Buffer Overflow (5.0)]] |
| [[CLAIM-94D96CF87D4C0B49E309AFC4\|WEAKNESS:CWE-122: architecture_position]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AC77FAA5BCFF7678FAEA0D75: Description / Potential Mitigations; topic=WEAKNESS:CWE-122 — [[EVIDENCE-AC77FAA5BCFF7678FAEA0D75\|CWE - CWE-122: Heap-based Buffer Overflow (5.0)]] |
| [[CLAIM-61D09701582D517EFF26DFF0\|WEAKNESS:CWE-122: security_boundary]] — "Ranh giới bộ nhớ, trạng thái hoặc quyền của phần mềm xử lý dữ liệu không tin cậy." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AC77FAA5BCFF7678FAEA0D75: Description / Potential Mitigations; topic=WEAKNESS:CWE-122 — [[EVIDENCE-AC77FAA5BCFF7678FAEA0D75\|CWE - CWE-122: Heap-based Buffer Overflow (5.0)]] |
| [[CLAIM-387331078C0E74A1BA190A64\|WEAKNESS:CWE-122: safety_assumptions]] — "Allocation phải đủ kích thước; mọi offset ghi nằm trong vùng sở hữu." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AC77FAA5BCFF7678FAEA0D75: Description / Potential Mitigations; topic=WEAKNESS:CWE-122 — [[EVIDENCE-AC77FAA5BCFF7678FAEA0D75\|CWE - CWE-122: Heap-based Buffer Overflow (5.0)]] |
| [[CLAIM-3AB4936596797A0592AB26F0\|WEAKNESS:CWE-122: related_failure_classes]] — "Heap-based Buffer Overflow" | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AC77FAA5BCFF7678FAEA0D75: Description / Potential Mitigations; topic=WEAKNESS:CWE-122 — [[EVIDENCE-AC77FAA5BCFF7678FAEA0D75\|CWE - CWE-122: Heap-based Buffer Overflow (5.0)]] |
| [[CLAIM-D31D0455F648097AD9EB67C5\|WEAKNESS:CWE-122: failure_impact]] — "Tác động phụ thuộc lớp lỗi và context triển khai; chỉ khẳng định tác động cụ thể khi advisory tương ứng công bố." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AC77FAA5BCFF7678FAEA0D75: Description / Potential Mitigations; topic=WEAKNESS:CWE-122 — [[EVIDENCE-AC77FAA5BCFF7678FAEA0D75\|CWE - CWE-122: Heap-based Buffer Overflow (5.0)]] |
| [[CLAIM-5877AD2A3A0788CBEDF5EAFF\|WEAKNESS:CWE-122: defensive_principles]] — "Dùng kiểm tra capacity/length và sanitizer khi phát triển." | MITRE CWE | CURRENT | NOT_REVIEWED / NOT_REVIEWED | EVIDENCE:AC77FAA5BCFF7678FAEA0D75: Description / Potential Mitigations; topic=WEAKNESS:CWE-122 — [[EVIDENCE-AC77FAA5BCFF7678FAEA0D75\|CWE - CWE-122: Heap-based Buffer Overflow (5.0)]] |




## Phạm vi kiểm chứng

[[EVIDENCE-0CCC16DDE68A1713FAED2329|CVE-2026-15176]], [[EVIDENCE-1F6DBE760A34B37CAD1CF4A7|CVE-2026-42055]], [[EVIDENCE-4DFBBE4B964C3500C9AAFD36|CVE-2026-42533]], [[EVIDENCE-8A5EFD9F2F8B58978470483B|CVE-2026-90439]], [[EVIDENCE-8F5015B6CA57FA297E6319B8|CVE-2026-93479]], [[EVIDENCE-AC77FAA5BCFF7678FAEA0D75|CWE - CWE-122: Heap-based Buffer Overflow (5.0)]], [[EVIDENCE-DC1432949B4CBBFA7575048F|CVE-2026-42945]], [[EVIDENCE-F7F3915BEDFBC5BA090B7D90|CVE-2026-27654]], [[EVIDENCE-F8A106D1BC0974617FFB0815|CVE-2026-9256]]

Bản biên soạn cần semantic review; nhãn legacy không chứng nhận factual accuracy.



[[Learning-Library|Learning Library]] · [[Research-Library|Research Library]]

