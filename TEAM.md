# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Vibecode`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Vibecode-PoCtoPilotGate1` (https://github.com/phungtr/K5-L3B-DAY10-Vibecode-PoCtoPilotGate1)
- Thẻ sự cố đã bốc (S1–S8):

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
