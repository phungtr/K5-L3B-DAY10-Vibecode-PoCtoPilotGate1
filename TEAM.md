# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Vibecode`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Vibecode-PoCtoPilotGate1` (https://github.com/phungtr/K5-L3B-DAY10-Vibecode-PoCtoPilotGate1)
- Thẻ sự cố đã bốc (S1–S8): `S3`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phùng Quang Trà | 2A202604094 | Kỹ sư cổng |      x      |
|   2 | Nguyễn Quốc Toàn | 2A202604098 | Kỹ sư cổng |             |
|   3 | Nguyễn Bảo Trung | 2A202604013 | Sản phẩm và kinh doanh |             |
|   4 | Lại Trọng Đức | 2A202604019 | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

---

## NguyenBaoTrung-2A202604013

### Phần việc phụ trách

- **Vai:** Sản phẩm và kinh doanh (`Nguyễn Bảo Trung` · `2A202604013`).
- **Tài liệu & config chính:** `config/acceptance_criteria.json`; `config/operating_gates.json` (mục `business`); Phiếu A (`A1` Câu 1.1, `A3` Câu 1.5, `A4` Câu 1.6); Phiếu B (`B3` Câu 2.3, `B7.4` Câu 2.9, `B8` cột `v1`); Phiếu C (`C5` Câu 3.2, `C12` cột `v2` & ba dòng bắt buộc).

### Đóng góp cụ thể

- **Khối 1 (Phiếu A & Tiêu chí):** Viết mục tiêu cấp hệ thống (Câu 1.1), giải thích khoảng tin cậy 95% (Câu 1.5), hoàn thiện câu tiêu chí kèm hành động, 4 câu soát, ranh giới đầu ra (Câu 1.6) và khóa ngưỡng trong `config/acceptance_criteria.json` (`pass_rate ≥ 0,99`, `pass_k ≥ 0,95`, 3 chỉ số an toàn `= 0`, `escalation_rate ≤ 0,35`, `cost_per_ticket ≤ 8.000đ`, `roi ≥ 0,25`, `queue_stuck = 0`) trước khi đánh giá.
- **Khối 2 (Phiếu B & Gate v1):** Hoàn thiện bản đồ dữ liệu + ví dụ concept drift `REFUND-v4` ngày `2026-12-01` (`B3`); đặt cổng `business` (`daily_refund_cap_vnd = 1.500.000`, `cost_budget_per_ticket_vnd = 1.000`, `pilot_scope` 4 kho bán lẻ `HN, HCM, DN, CT` giữ `HCM-B2B` làm tay, `roi_min = 0,25`) khớp `ops_limits`/`ops_facts` (`B7.4`); đọc report vòng 1 và chốt `v1 = Tiếp tục` (`B8`).
- **Khối 3 (Phiếu C · Thẻ `S3`):** Chạy tự kiểm tra mốc `prepared` trên `S3` (`FAIL`: `ROI -2,4`, hoàn sai `900.000đ`, `15` lỗi oan `MKD`/`VNX`); viết specification kiểm được cho `S3` ở `C5` Câu 3.2 (bắt buộc ghim `policy_id` theo `as_of` ở `pre_guard` và chuyển người khi vượt `auto_limit_vnd` thiếu duyệt); điền sẵn phần nền/nhận xét `prepared` của `C12` (*chờ bản sửa `after` để chốt `v2`*).

### Bằng chứng

- **Commit:** `c90eb45` (Câu 1.1), `27b2937` & `fc2f6b3` (Câu 1.6 + `acceptance_criteria.json`), `0b64495` (ký tiêu chí trước khi đo), `5470448` (`B7.4` + `config/operating_gates.json` mục `business`), `c0089d2` (`B8` quyết định `v1`), `ffdc43b` (`C5` Câu 3.2).
- **Mã lần chạy:** `R-base-before-20261119-163318-b45eeb`, `R-base-prepared-20261119-165623-e9a32d`, `R-base-prepared-20261119-165911-e9a32d` (`9/9 ĐẠT`, `ROI 1,22`, `4.510đ/ticket`); `R-S3-grade-20261119-170244-e9a32d` (`base`/`prepared` trên `S3`).
- **Dòng trong phiếu:** `templates/form-a-criteria.md` (`A1`, `A3`, `A4`); `templates/form-b-evaluation-gates.md` (`B3`, `B7.4`, `B8`); `templates/form-c-incident.md` (`C5` Câu 3.2, `C12`).

### Exit ticket

- **Một điều học được:** Khóa tiêu chí *"nếu trượt → làm gì"* trước khi thấy số và gắn cổng tiền/phạm vi/ROI vào vận hành mới chặn được tâm lý "châm chước 1 ca lẻ" làm hại bên thứ ba.
- **Một điều còn chưa chắc:** Trên dữ liệu pilot thật (khác mock), tỉ lệ thiếu/sai `delay_cause` từ hãng và áp lực hàng chờ khi bão kéo dài nhiều ngày có đẩy chi phí/ticket vượt `8.000đ` hoặc kéo `ROI` xuống dưới `0,25` hay không *(cần đo trực tiếp trước Gate 2)*.

---

## LaiTrongDuc-2A202604019

### Phần việc phụ trách

- **Vai:** Vận hành và pháp lý (`Lại Trọng Đức` · `2A202604019`).
- **Tài liệu & config chính:** `config/operating_gates.json` (mục `operations` và `legal` vòng 1 & vòng 2); Phiếu A (`A1` Câu 1.2, `A2` Câu 1.4); Phiếu B (`B7.5` Runbook 1–3, `B7.6` Giờ cao điểm — Câu 2.10; đứng tên PIC nhóm 5, 7, 8 ở `B5`); Phiếu C (`C1` mốc prepared & đối chiếu pre-mortem, `C3.5` mở lại bản đồ dữ liệu thẻ `S3`, `C5` Câu 3.3, `C9–C11` Câu 3.7); gom và kiểm tra bài nộp (`submission/submission.json`, `lab10.check_submission --collect`).

### Đóng góp cụ thể

- **Khối 1 (Phiếu A):** Viết mục tiêu từ góc nhìn chị Oanh (`NV-OANH`, kế toán đối soát) và chị Hạnh (`NV-HANH`, trưởng ca CSKH) ở Câu 1.2; thiết kế Telemetry production không cần nhãn cho `file_carrier_fault` (đo tỉ lệ lỗi không có căn cứ tracking theo ca và cộng dồn 7 ngày so với `suspend_after_strikes_7d`, ngưỡng Vàng/Đỏ và 4 điểm mù) ở Câu 1.4.
- **Khối 2 (Phiếu B & Cổng vòng 1):** Thiết lập cổng `operations` (`NV-TUNG`, `NV-HANH`, 1 người trực / 6 ca/giờ, SLA 60 phút, `decision_note = true`, `review_sampling_pct = 10%`, `stop_conditions`, `#logix-refund-pilot-alerts`) và `legal` (`pii_fields_blocked_to_third_party = ["recipient_contact", "customer_note"]`, `carrier_fault_requires_recorded_cause = true`) trong `config/operating_gates.json`; viết Runbook 1–3 (`B7.5`) và phương án Giờ cao điểm (`B7.6`). Cổng vòng 1 đã đỡ trực tiếp 20/35 lỗi hãng oan và giữ `pii_leaks = 0` khi nhận thẻ `S3`.
- **Khối 3 (Phiếu C · Thẻ `S3`) & Nộp bài:** Chạy mốc `prepared` trên `S3` và đối chiếu pre-mortem (`C1`), mở lại bản đồ dữ liệu cho `policies` / `delay_cause` / trần lỗi ngày (`C3.5`), viết giả định môi trường (`C5` Câu 3.3); cập nhật `operations.stop_conditions` vòng 2 cho `policy_pinned` & trần lỗi hãng ngày; hoàn thiện Fault tree sau sửa (`C9`), Risk register (`C10`), cập nhật checklist 9 nhóm và Runbook 4–5 (`C11`); chuẩn bị `submission/submission.json`.
- **Ghi chú sử dụng AI:** Có dùng trợ lý AI để tra cứu cấu trúc codebase (`ops.py`, `agent.py`, `world.json`), đối chiếu số liệu report và rà soát câu chữ; tự kiểm chứng toàn bộ ngưỡng vận hành, pháp lý và nội dung runbook trước khi commit.

### Bằng chứng

- **Commit:** `8a26246` & `3bc0712` (Phiếu A Câu 1.2 & 1.4), `c47e489` (Câu 2.10 `operating_gates.json` + Runbook 1–3 & Giờ cao điểm), `c917d3a` (Phiếu C `C1`, `C3.5`, `C5` Câu 3.3), và commit hoàn thiện `C9–C11` + `submission.json` + `TEAM.md`.
- **Mã lần chạy:** `R-S3-grade-20261119-170052-e9a32d` (mốc `prepared` trên `S3`: giảm lỗi oan `35 → 15`), `R-S3-grade-20261119-172404-418fc9` (mốc `after` trên `S3`: `pass_rate = 1,0`, `0` lỗi oan, `0` PII, `0` ca ùn, `ROI = 1,27`).
- **Dòng trong phiếu:** `templates/form-a-criteria.md` (`A1` Câu 1.2, `A2` Câu 1.4); `templates/form-b-evaluation-gates.md` (`B7.5`, `B7.6`); `templates/form-c-incident.md` (`C1`, `C3.5`, `C5` Câu 3.3, `C9–C11`); `config/operating_gates.json` (`operations`, `legal`).

### Exit ticket

- **Một điều học được:** Cổng bằng config và quy trình vận hành (`carrier_fault_requires_recorded_cause`, chặn PII, `decision_note`, kiểm mẫu 10% và giới hạn thời gian dừng 15 phút) giải quyết được nhiều rủi ro mà không cần đụng vào model, nhưng vẫn phải đi kèm phát hiện sớm cho phần con người dễ quên (như đồng bộ cờ chính sách).
- **Một điều còn chưa chắc:** Khi bão kéo dài nhiều ngày ngoài thực tế, tần suất điều phối nhập bù hoặc sửa muộn `delay_cause` sau khi đã gửi thông báo cho hãng có đủ cao để buộc phải tạm hoãn ghi lỗi tự động 48 giờ ở tuyến thiên tai hay không.
