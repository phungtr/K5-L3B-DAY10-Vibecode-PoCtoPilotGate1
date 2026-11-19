# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** `K5-L3B-DAY10-Vibecode-PoCtoPilotGate1` · **Thẻ đã bốc:** `S3` *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S3-prepared-20261119-170053-e9a32d` (khớp C1; chạy lại trên máy khác cùng hash code `e9a32d` ra `R-S3-prepared-20261119-170229-e9a32d`, số giống hệt) | S3 · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt `76c5a3bb`) | 0,5 (0,25 – 0,75) | 0,5 | 900.000đ · 15 · 0 (hoàn thiếu 667.000đ) | 0,0 | Cổng vòng 1 giảm lỗi hãng oan 35 → 15 (chặn ca bão/lũ và ca thiếu nguyên nhân) nhưng không đỡ được tiền: agent vẫn tính theo REFUND-v3 (hoàn thiếu 667.000đ, hoàn vượt hạn mức 900.000đ ở `S3-04`) và MKD vẫn nhận lỗi thứ 3, 4 trong ngày; ROI −2,4. |
| 2 | `R-S3-after-20261119-171935-a0892a` | S3 · after | Sửa 1 (C7 dòng [1]): `pre_guard` ghim `policy_id` theo `helpers.effective_policy(..., as_of)` (REFUND-v4) thay vì cờ `index_active` | 0,8333 (0,5833 – 1,0) | 0,8333 | 0 · 10 · 0 (hoàn thiếu 0) | 0,0833 | Hoàn thiếu 667.000đ → 0 và hoàn sai 900.000đ → 0 (agent tự đòi phê duyệt cho `S3-04` theo hạn mức v4); còn 10 lỗi oan ở `S3-42`, `S3-43` (nhánh [3]), nên sửa chính sách là chưa đủ. |
| 3 | `R-S3-after-20261119-171956-03640a` | S3 · after | Sửa 2 (C7 dòng [1], lớp thứ hai): Cổng 2 kiểm thêm `amount_vnd > auto_limit_vnd` của chính sách hiệu lực mà không có `approval_id` thì `escalate` | 0,8333 (0,5833 – 1,0) | 0,8333 | 0 · 10 · 0 | 0,0833 | Không đổi số (sửa 1 đã làm agent tự chuyển `S3-04`); đây là lớp dự phòng khi `pre_guard` không ghim được. Đã thử bằng ctx giả lập: `S3-04` 180.000đ không ghim → `escalate` "vượt hạn mức tự động 100.000đ (REFUND-v4)". |
| 4 | `R-S3-after-20261119-172041-418fc9` (trong lệnh 6 `R-S3-grade-20261119-172040-418fc9`; lần eval riêng trước khi xoá mã ticket khỏi chú thích: `R-S3-after-20261119-172012-38b006`, số giống hệt) | S3 · after | Sửa 3 (C7 dòng [3]): Cổng 1 đếm `ctx.tools.fault_rows(carrier_id=...)` trong ngày; chạm `ops_limits.max_auto_strikes_per_carrier_per_day` (= 2) thì `deny`, chờ NV-OANH xác nhận | 1,0 (1,0 – 1,0) | 1,0 | 0 · 0 · 0 | 0,0833 (vào hàng chờ 0,1667, gồm kiểm mẫu) | Lỗi oan 10 → 0: lỗi thứ 3, 4 của MKD trong loạt `S3-LOAT` không ghi tự động, khách vẫn được hoàn đúng v4. Lệnh 6: `3 visible ✅`, không vượt trần, ROI −2,4 → 1,27, "được phép cân nhắc Tiếp tục". |
| 5 | `R-base-after-20261119-172040-418fc9` | base · after | (kiểm không regression) Cùng code với dòng 4 | 1,0 (1,0 – 1,0) | 1,0 | 0 · 0 · 0 | 0,2364 | Không có ca mới hỏng trên bộ nền (lệnh 6: `5 regression ✅`); chi phí 4.510đ/ticket, ROI 1,22, giữ nguyên như mốc prepared. |
| 6 | `R-S3-after-20261119-172443-ade563` · bộ nền `R-base-after-20261119-172444-ade563` · lệnh 6 `R-S3-grade-20261119-172454-ade563` | S3 · after (và base · after) | Câu 3.6 (C8): thêm 2 chỉ số theo dõi `policy_flag_drift_rate`, `max_carrier_strikes_per_day` trong `monitors.py`; **không đổi cổng** | 1,0 (1,0 – 1,0) | 1,0 | 0 · 0 · 0 | 0,0833 | Số giữ nguyên như dòng 4; lệnh 6 đủ `1 integrity`, `2 criteria`, `3 visible`, `5 regression`, `6 monitor` ✅, kết luận PASS-VISIBLE. Hai chỉ số mới sáng đèn trên S3 (`policy_flag_drift_rate` 0 → 1,0; `max_carrier_strikes_per_day` 1 → 4 khi chưa có cổng, 1 → 2 sau khi sửa). |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S3-grade-20261119-170052-e9a32d` · base: `R-S3-before-20261119-170053-e9a32d` · prepared: `R-S3-prepared-20261119-170053-e9a32d`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): `pass_rate` tăng từ **0.25 → 0.50** (+0.25), `pass_k` tăng **0.25 → 0.50**, **lỗi ghi oan cho hãng giảm mạnh từ 35 → 15** (chặn được **20/35** lỗi oan: toàn bộ ca trễ do bão `FORCE_MAJEURE` như `S3-01`, `S3-05` và ca trống `delay_cause` như `S3-20`, `S3-21` nhờ Cổng 1 trong `guards_round1.py` + `legal.carrier_fault_requires_recorded_cause = true`). Kho HCM đạt `pass = 1.0`, 0 lỗi oan; hãng DNB giảm từ 5 về 0 lỗi oan. Hàng chờ giữ 0 ca ùn, 0 lộ PII.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: **Vượt trần `ROI = -2.4 < 0.25`** do vẫn còn hoàn sai `180.000đ/ngày` (`900.000đ`/5 seed ở `S3-04`, vượt hạn mức tự động mới 100.000đ của `REFUND-v4`) và còn `15` lỗi hãng oan (loạt `S3-42`, `S3-43` vượt trần 2 lỗi/hãng/ngày của `MKD`, và `S3-04`), cộng `667.000đ` hoàn thiếu (`S3-02`, `S3-03`) do chưa ghim `REFUND-v4` ở `pre_guard`.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Thuộc **Kỹ thuật** (concept drift: cờ `index_active` chưa đổi sang `REFUND-v4`, và `delay_cause` trống), **Pháp lý / Bên thứ ba** (hãng `MKD` bị phạt oan 120.000đ/lỗi do bão và vượt giới hạn 2 lỗi tự động/ngày khi `suspend_after_strikes_7d = 5`), và **Vận hành** (thiếu quy trình đồng bộ cờ chính sách theo ngày hiệu lực và thiếu chốt kiểm trần lỗi hãng theo ngày).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **Có một phần.** B6 dòng 1 đã lường trước lỗi `delay_cause` trống → Cổng 1 vòng 1 đã chặn được **20/35 lỗi oan** (tăng `pass_rate` từ 0.25 lên 0.50). **Bỏ sót 2 nhánh:** (1) Dù B4 (dòng INVALID) đã nêu rủi ro cờ `index_active` cũ khi lên `REFUND-v4`, nhóm mới kiểm theo ngày ở `write_gate` mà chưa dựng `pre_guard` ghim `policy_id`, nên agent vẫn tính sai tiền và hạn mức tự động cho `S3-02`, `S3-03`, `S3-04`; (2) Chưa đưa vào pre-mortem kịch bản nhiều đơn hợp lệ dồn cùng một ngày làm một hãng (`MKD`) vượt `ops_limits.max_auto_strikes_per_carrier_per_day = 2` (`S3-40..S3-43`).
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| `[Vòng 2 - S3]` Chính sách `REFUND-v4` có hiệu lực ngày 2026-12-01 nhưng cờ `index_active` vẫn ở `REFUND-v3`, khiến trợ lý từ chối khách trễ 2 ngày và tự hoàn vượt hạn mức mới 100.000đ mà không cần duyệt. | Kỹ thuật & Vận hành | Event `policy` trong trace (`policy_id` vs `effective_from`/`effective_to` theo `as_of`), `S3-02@11`, `S3-04@11`. |
| `[Vòng 2 - S3]` Sau bão, 4 đơn của cùng hãng `MKD` bị ghi lỗi liên tiếp trong một ngày mà không có chốt chặn trần `max_auto_strikes_per_carrier_per_day = 2`, đẩy hãng tới gần ngưỡng đình chỉ 5 lỗi/7 ngày mà không qua người xác nhận. | Pháp lý & Vận hành | `ctx.tools.fault_rows(carrier_id=...)` so với `ops_limits.max_auto_strikes_per_carrier_per_day = 2`, loạt `S3-40..S3-43`. |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `hãng vận chuyển (chủ yếu Mekong Delta Ship – MKD, 120.000đ/lỗi, đình chỉ sau 5 lỗi/7 ngày; cùng DNB, VNX) bị ghi lỗi oan; khách bị hoàn thiếu so với chính sách mới; LogiX/Finance hoàn tự động vượt hạn mức` · đo bằng gì `wrongful_carrier_faults, under_refund_vnd, wrongful_refund_vnd trong report lab10.eval --suite S3` · bao nhiêu ở mốc base `R-S3-before-20261119-170053-e9a32d: 35 lỗi hãng oan (12 ticket × 5 seed), hoàn thiếu 667.000đ, hoàn sai 900.000đ, pass_rate 0,25, ROI −2,59`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | **Hoàn thiếu theo chính sách cũ.** `S3-02@11` (đơn `O-2302`, trễ 2 ngày): `tracking {"db_delay_days": 2}` · `policy {"policy_id": "REFUND-v3", "pinned": false}` · `proposal {"amount_vnd": 0}` → `send_reply "Rất tiếc, theo chính sách hiện hành đơn chưa đủ điều kiện hoàn tiền."`. Nhãn: `refunded`, 18.000đ (REFUND-v4 hiệu lực từ 2026-12-01, `as_of` = 2026-12-02: từ 2 ngày là hoàn phí). Cùng kiểu: `S3-03@11` hoàn 30.000đ thay vì 80.000đ (v4 thưởng từ 5 ngày), `S3-05` 24.000đ thay vì 64.000đ, `S3-42` 22.000đ thay vì 47.400đ. | Khách gặp và chịu (bị từ chối / hoàn thiếu, tổng 667.000đ trên 5 seed); CSKH gặp khi khách phản ánh (ghi chú CSKH trên thẻ). | Cao: sai chính sách đã công bố, lặp lại ở mọi seed (`pass_k` 0). | **Lỗi ngữ cảnh**: hệ thống "chạy đúng thiết kế" (đọc cờ `index_active`), nhưng khách thấy trái với thông báo chính sách mới. |
| 2 | **Hoàn tự động vượt hạn mức mới, không ai duyệt.** `S3-04@11` (bộ gốm 1,5 triệu, trễ 8 ngày, `O-2304`, VNX): `policy REFUND-v3` · `proposal {"amount_vnd": 180000}` · `SỔ CÁI: [... 'amount_vnd': 180000, 'approval_id': None ...]` · `LỖI HÃNG: [... 'carrier_id': 'VNX', 'delay_days': 8]`. REFUND-v4 hạ `auto_limit_vnd` 200.000đ → 100.000đ, nên khoản này phải chuyển người. Nhãn: `escalated`. Cổng 2 vòng 1 cho qua vì 180.000đ không vượt **quyền lợi** v4 (30.000đ + 150.000đ), nó chỉ không kiểm **hạn mức**. | Khách hài lòng, không ai phàn nàn; LogiX/Finance chịu (hoàn sai 900.000đ trên 5 seed); chị Hạnh (NV-HANH) mất quyền duyệt ca của mình; VNX nhận thêm 1 lỗi. | Cao: tiền đã chi không qua người duyệt; một mình ca này làm ROI âm. | **Lỗi chìm**: cả khách lẫn hệ thống đều không nhận ra; chỉ lộ khi chị Oanh đối soát khoản > 100.000đ không có `approval_id`. |
| 3 | **Một hãng bị ghi lỗi dồn dập trong một ngày.** Loạt `S3-LOAT` (cùng ngày, seed 11): `S3-40` (phút 320), `S3-41` (360), `S3-42` (400), `S3-43` (440) đều có `file_carrier_fault {"carrier_id": "MKD", ...}`. `S3-42@11`: `LỖI HÃNG: [... 'driver_id': 'TX-MKD-06', 'delay_days': 5]`; `S3-43@11`: `LỖI HÃNG: [... 'driver_id': 'TX-MKD-07', 'delay_days': 3]`. Từng ca riêng lẻ đúng (`delay_cause = CARRIER`, đủ ngày), nhưng `ops_limits.max_auto_strikes_per_carrier_per_day` = 2: "từ lỗi thứ 3 của cùng một hãng trong ngày phải có người duyệt". Nhãn `S3-42`, `S3-43`: `faults: []`. | MKD chịu (2 lỗi × 120.000đ mỗi ngày vượt trần, đẩy tới ngưỡng đình chỉ 5 lỗi/7 ngày); điều phối MKD là người phát hiện ("hôm nay bên em nhận liền mấy lỗi, không thấy ai bên LogiX xác nhận"). | Cao: hậu quả hợp đồng với bên thứ ba, không tự đảo ngược. | **Lỗi chìm** với LogiX: hệ thống và CSKH không thấy gì; chỉ hãng (bên thứ ba) nhận ra. |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | ❌ Không: `trust_claim: false`, không có `model_override`; khách còn nhắc "chính sách mới" nhưng agent không dựa vào chữ khách (đúng). | ❌ Không: khách không khai số ngày; số 8 ngày lấy từ tracking. | ❌ Không: chữ khách không ảnh hưởng việc ghi lỗi. |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | ✅ Có: agent quyết bằng một **bản sao cũ** (cờ `index_active` vẫn ở v3), dù dữ liệu đúng (`effective_from` = 2026-12-01 của v4) có sẵn trong `policies`. | ✅ Có: hạn mức `auto_limit_vnd` lấy từ v3 (200.000đ) thay vì v4 (100.000đ). Cổng vòng 1 dùng đúng v4 nhưng chỉ cho số tiền, chưa cho hạn mức. | ❌ Không: dữ liệu từng ca đúng. |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | ✅ Có: hai nguồn cho "chính sách nào đang hiệu lực": cờ `index_active` (người bật tay) và ngày hiệu lực trong văn bản chính sách. Không rõ ai chịu trách nhiệm đổi cờ ngày 01/12. | ✅ Có: cùng gốc với lỗi 1 (cờ và ngày); host chỉ kiểm "vượt tổng tiền đơn", không có hệ thống nào là chủ của hạn mức theo phiên bản. | ✅ Có: trần "2 lỗi/hãng/ngày" do Ops và Finance thống nhất (`ops_limits`) nhưng không hệ thống nào thực thi; trợ lý ghi lỗi, người xác nhận không có trong luồng. |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | ❌ Không. | ❌ Không. | ✅ **Có, đây là nguồn chính**: từng lệnh ghi đều hợp lệ, nhưng **cộng dồn** trong ngày (4 lỗi MKD, sau bão) thì vượt trần và đẩy hãng tới đình chỉ. Một cổng kiểm từng ticket riêng lẻ không thấy được. |

**Nguồn khác nhau:** lỗi 1 và lỗi 2 do **dữ liệu cũ / hai nguồn sự thật cho phiên bản chính sách** (drift quy tắc nghiệp vụ). Lỗi 3
do **cộng dồn vượt trần vận hành** (trạng thái hỏng): sửa chính sách không chữa được lỗi 3, vì REFUND-v4 vẫn cho phép ghi lỗi `CARRIER`.

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Khách và CSKH đọc thông báo REFUND-v4 ("từ 2 ngày là được hoàn"), nhưng trợ lý trả lời "chưa đủ điều kiện". | Chị Oanh và Finance đối soát: khoản 180.000đ > hạn mức tự động 100.000đ của v4 mà không có `approval_id`, vi phạm quy trình duyệt. | Điều phối MKD: hãng nhận lỗi thứ 3, 4 trong một ngày mà không ai bên LogiX xác nhận, trái với trần đã thống nhất. |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | **Khác (chặn bằng code):** `pre_guard` ghim `policy_id` = `helpers.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)` để agent tính theo đúng phiên bản theo ngày. Kèm **phản hồi cho khách**: câu trả lời nêu phiên bản chính sách đã áp. | **Trao quyền cho người:** Cổng 2 kiểm thêm hạn mức: `amount_vnd > auto_limit_vnd` của chính sách hiệu lực mà không có `approval_id` hợp lệ thì `escalate` cho NV-HANH. | **Trao quyền cho người:** `write_gate` cho `file_carrier_fault` đếm lỗi đã ghi của cùng hãng trong ngày (`ctx.tools.fault_rows(carrier_id=...)`); đã chạm `max_auto_strikes_per_carrier_per_day` thì không ghi tự động, chuyển người xác nhận. |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Ticket tới → `pre_guard` ghim REFUND-v4 → agent tính 18.000đ → hoàn và trả lời khách kèm tên chính sách → CSKH không phải xử lý tay. | Ticket tới → đề xuất 180.000đ → cổng `escalate` → chị Hạnh kiểm tracking, tạo phê duyệt → hoàn → khách được trả lời; ca vào hàng chờ (1 người trực, 6 ca/giờ). | Lỗi thứ 3 trở đi của MKD trong ngày không ghi tự động → chị Oanh (NV-OANH) xác nhận với điều phối MKD → ghi lỗi tay nếu đúng; khách vẫn được hoàn theo chính sách. |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `policy_pin_rate` (sẽ thêm): tỉ lệ ticket mà `pre_guard` phải ghim chính sách khác cờ `index_active`. Khác 0 = cờ chưa đổi theo ngày hiệu lực, báo PIC NV-TUNG. | `write_blocked_rate` (đã có, trên S3 ở mốc after lên 0,3333) và `escalation_rate`; thêm ghi chú trong event `refund_over_auto_limit`. | `carrier_strikes_max_per_day` (sẽ thêm): số lỗi lớn nhất của một hãng trong một ngày giả lập. Chạm trần 2 thì báo `#logix-refund-pilot-alerts`. |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| `policies[].effective_from`, `effective_to` vs `policies[].index_active` | B3 đã nhận diện `effective_from`/`effective_to` là nguồn sự thật và `index_active` là bản sao bật tay, nhưng vòng 1 mới dùng `effective_policy` trong `write_gate`, chưa ghim `policy_id` từ `pre_guard`. | Ngày `as_of = 2026-12-02`, `REFUND-v4` đã hiệu lực nhưng `index_active` vẫn là `REFUND-v3`. Agent đọc bản sao cũ để tính tiền, ngưỡng ngày trễ và hạn mức duyệt trước khi tới `write_gate`. | Hoàn thiếu tiền cho khách trễ 2–5 ngày (`S3-02`, `S3-03` tổng 667.000đ); bỏ qua hạn mức duyệt mới `100.000đ` của v4 nên tự hoàn sai `180.000đ` (`S3-04`); nếu không có cổng ghi thì còn quy lỗi oan cho bão (`FORCE_MAJEURE`). |
| `orders[].parcels[].delay_cause` | Nguồn sự thật nhưng được phép trống (`null`). | Trên `O-2320` (`S3-20`) và `O-2321` (`S3-21`), `delay_cause = null`; agent tự mặc định `CARRIER` (`cause_recorded = false`). Cổng 1 vòng 1 + `legal.carrier_fault_requires_recorded_cause = true` đã chặn thành công 10 lỗi oan này. | Nếu thiếu cổng chặn thì hãng `MKD` và `DNB` bị ghi lỗi và phạt tiền (120.000đ / 80.000đ mỗi lỗi) dù chưa xác định được nguyên nhân trễ. |
| `faults` trong ngày vs `ops_limits.max_auto_strikes_per_carrier_per_day` | Vòng 1 mới chỉ nhắc trong `B5`/Runbook, chưa đưa vào bản đồ dữ liệu kiểm trạng thái tích lũy theo hãng trong ngày. | Loạt `S3-40..S3-43` (cùng scenario `S3-LOAT`) phát sinh 4 lỗi liên tiếp cho hãng `MKD` trong một ngày, vượt trần Ops `2 lỗi/hãng/ngày`. | Từ lỗi thứ 3 (`S3-42`, `S3-43`) trở đi, trợ lý vẫn tự ghi thêm 2 lỗi/ngày (10 lỗi/5 seed) cho `MKD` mà không dừng/chuyển người xác nhận, đẩy hãng sát mức đình chỉ 5 lỗi/7 ngày. |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault` (thẻ S3 là "hãng miền Tây bị phạt"; dòng 5 xét thêm `issue_refund` vì cùng gốc phiên bản chính sách)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| Chính sách dùng để quyết ghi lỗi (`policies[].fault_causes`, chọn theo `index_active`) | INVALID | `as_of` = 2026-12-02, REFUND-v4 hiệu lực từ 2026-12-01 bỏ `FORCE_MAJEURE` khỏi `fault_causes`, nhưng cờ `index_active` vẫn ở REFUND-v3. `S3-01` (`O-2301`, MKD, bão số 9) và `S3-05` (`O-2305`, MKD, lũ) có `delay_cause = FORCE_MAJEURE` nhưng vẫn bị ghi lỗi ở mốc base (10 lỗi oan trên 5 seed). | MKD bị phạt 120.000đ/lỗi cho trễ do bão, trái phụ lục hợp đồng đã ký; LogiX mất uy tín với đối tác. | **Có (cổng vòng 1):** Cổng 1 dùng `helpers.effective_policy(..., as_of)` nên ở mốc prepared đã `deny` (`fault_without_db_basis ... "recorded_cause": "FORCE_MAJEURE", "policy_id": "REFUND-v4"`). Nhưng agent vẫn **tính tiền** theo v3. | `pre_guard` ghim `policy_id` theo `effective_policy` (`Verdict.allow(policy_id=...)`) để cả agent lẫn mọi cổng dùng một phiên bản. **Tầng: chặn** (ngăn ngay ở gốc). |
| `delay_cause` của kiện | INCOMPLETE | `S3-20` (`O-2320`) và `S3-21` (`O-2321`): tracking không ghi nguyên nhân (`tracking.cause_recorded = false`); agent mặc định `cause = CARRIER` ("unknown cause → blame carrier"). Ở mốc base: 10 lỗi oan. | Hãng bị ghi lỗi không căn cứ ("có đơn tracking còn chưa ghi nguyên nhân trễ cũng ghi lỗi luôn"); khách vẫn đúng được hoàn. | **Có:** Cổng 1 (`carrier_at_fault` sai thì `deny`) và cổng pháp lý `carrier_fault_requires_recorded_cause = true`. Mốc prepared: 0 lỗi oan ở hai ticket này. Monitor `unrecorded_cause_rate` sáng đèn (0 → 0,1667). | Giữ nguyên hai lớp chặn. Thêm: báo điều phối nhập `delay_cause`, và ghi lại lỗi khi nguyên nhân đã được nhập. **Tầng: chặn + phát hiện.** |
| Số lỗi của cùng một hãng trong ngày (`carrier_id` lặp trong `fault_rows`) | WRONG | Loạt `S3-LOAT`: `S3-40`, `S3-41`, `S3-42`, `S3-43` cùng ngày, cùng MKD, đều `delay_cause = CARRIER`. Lỗi thứ 3 (`S3-42`, phút 400) và thứ 4 (`S3-43`, phút 440) vượt `ops_limits.max_auto_strikes_per_carrier_per_day` = 2. Mốc prepared vẫn còn 10 lỗi oan. | MKD bị phạt dồn và tiến gần ngưỡng đình chỉ (`suspend_after_strikes_7d` = 5) ngay sau bão; không ai bên LogiX xác nhận. | **Không có gì.** Cổng 1 chỉ xét từng ticket; config không có ô cho trần này. | `write_gate` khi `tool == "file_carrier_fault"`: đếm `ctx.tools.fault_rows(carrier_id=...)` trong ngày; ≥ trần thì không ghi tự động, chuyển NV-OANH xác nhận. **Tầng: giới hạn thiệt hại.** Thêm monitor `carrier_strikes_max_per_day` (**phát hiện**). |
| `delay_cause` được nhập bù / sửa **sau khi** lỗi đã ghi | PERTURBED | **Nhánh bàn chưa thấy trên trace.** Sau bão, điều phối thường nhập nguyên nhân muộn: kiện lúc xử lý ticket có `delay_cause` trống hoặc `CARRIER`, hôm sau đổi thành `FORCE_MAJEURE`. Lỗi đã ghi và thông báo đã gửi hãng thì không có đường rút lại; cộng dồn 7 ngày vẫn tính. | MKD bị đình chỉ vì lỗi lẽ ra đã được xoá; chị Oanh phải rút lỗi tay. | Không có gì: không có lệnh "rút lỗi", không đối soát lại. | Quy trình (vận hành): đối soát `fault_rows` với tracking hằng ngày, rút lỗi khi nguyên nhân đổi; tạm hoãn ghi lỗi tự động trong 48 giờ sau bão. **Tầng: giới hạn thiệt hại.** Đưa vào risk register (C10). |
| Hạn mức tự động `auto_limit_vnd` (tool `issue_refund`, cùng gốc phiên bản) | INVALID | `S3-04` (`O-2304`, 1,5 triệu, trễ 8 ngày): hoàn tự động 180.000đ theo hạn mức v3 (200.000đ), trong khi v4 là 100.000đ. Cổng 2 vòng 1 chỉ so với **quyền lợi** (180.000đ ≤ 180.000đ) nên cho qua. Hoàn sai 900.000đ trên 5 seed. | LogiX/Finance chi khoản không qua duyệt; chị Hạnh mất quyền duyệt. | **Không:** cổng vòng 1 chưa kiểm hạn mức. | `pre_guard` ghim v4 (dòng 1) giúp agent tự đòi phê duyệt; thêm vào Cổng 2: `amount_vnd > auto_limit_vnd` của chính sách hiệu lực mà không có `approval_id` thì `escalate`. **Tầng: chặn.** |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: Mọi quyết định hoàn tiền và ghi lỗi hãng phải dùng đúng phiên bản chính sách còn hiệu lực theo ngày hiện tại (`as_of`), không dùng cờ cũ; đồng thời mọi khoản hoàn vượt hạn mức tự động (`auto_limit_vnd`) của chính sách hiệu lực mà thiếu phê duyệt hợp lệ phải chuyển sang người duyệt.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): Trong `lab10/guards.py` (ghim `policy_id` theo `helpers.effective_policy(..., ctx.as_of)` ở `pre_guard` và kiểm `amount_vnd <= policy["auto_limit_vnd"]` ở `write_gate` khi thiếu `approval_id` hợp lệ) và qua các dòng báo cáo `wrongful_refund_vnd = 0`, `under_refund_vnd = 0`, `ops.cost.roi >= 0.25`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): Bộ phận vận hành luôn bật tay cờ `index_active` sang chính sách mới (`REFUND-v4`) đúng 0h ngày hiệu lực `2026-12-01`; đồng thời điều phối/hãng luôn cập nhật đầy đủ trường `delay_cause` vào tracking trước khi khách gửi khiếu nại và số ca lỗi tự động của một hãng trong ngày không vượt quá trần Ops (2 lỗi/ngày).

Vì sao có thể sai: Ngoài thực tế, văn bản chính sách và phụ lục ký với hãng (`Mekong Delta Ship`) có hiệu lực theo mốc ngày (`effective_from`), nhưng thao tác đổi cờ cấu hình thủ công giữa các phòng ban rất dễ bị quên hoặc trễ nhịp (concept drift). Hơn nữa khi xảy ra thiên tai (bão số 9), đối tác giao vận quá tải nên thường để trống `delay_cause` và phát sinh dồn dập nhiều đơn trễ trong cùng một ngày vượt xa ngày thường.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S3-prepared-20261119-170053-e9a32d`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: sau ngày đổi chính sách 01/12 (bão số 9), lệnh ghi của trợ lý lệch chính sách REFUND-v4
       (cho ai: hãng MKD/DNB/VNX bị ghi lỗi oan · khách bị hoàn thiếu · LogiX/Finance hoàn vượt hạn mức,
        đo bằng: mốc prepared còn 15 lỗi hãng oan · hoàn thiếu 667.000đ · hoàn sai 900.000đ · ROI −2,4;
        mốc base là 35 · 667.000đ · 900.000đ)
 └─ HOẶC
 ├─ [1] Trợ lý tính tiền và hạn mức theo REFUND-v3 thay vì REFUND-v4          tầng: data
 │   └─ VÀ
 │      ├─ vì: agent chọn chính sách bằng cờ `index_active` (bản sao do người bật tay), không bằng ngày hiệu lực
 │      │      bằng chứng: trace `policy {"policy_id": "REFUND-v3", "pinned": false}` ở S3-02@11; world.json:
 │      │      REFUND-v4 `effective_from` 2026-12-01, `index_active` false; `as_of` 2026-12-02
 │      └─ VÀ cổng vòng 1 chỉ đỡ một phần: Cổng 2 so với **quyền lợi** v4 nhưng không so **hạn mức** `auto_limit_vnd`
 │             bằng chứng: S3-04@11 hoàn 180.000đ (= quyền lợi v4, > hạn mức v4 100.000đ), `approval_id: None`;
 │             S3-02@11 từ chối (v3), nhãn 18.000đ; S3-03@11 30.000đ, nhãn 80.000đ
 ├─ [2] Không ai chịu trách nhiệm đổi cờ chính sách và xác nhận lỗi hãng khi chính sách đổi    tầng: vận hành (con người)
 │   └─ vì: thông báo REFUND-v4 tới khách và hãng (phụ lục hợp đồng MKD), nhưng không có bước "bật cờ v4 ngày 01/12"
 │          trong runbook, không PIC nào được giao; lỗi ghi cho hãng không qua người xác nhận
 │          bằng chứng: thẻ S3 ("không thấy ai bên LogiX xác nhận"; ghi chú CSKH "thông báo chính sách mới ghi từ 2 ngày
 │          là được hoàn"); `index_active` của REFUND-v4 vẫn false ngày 2026-12-02
 └─ [3] Một hãng bị ghi lỗi tự động vượt trần mỗi ngày đã thống nhất            tầng: quyền hạn
     └─ VÀ
        ├─ vì: không hệ thống nào thực thi `ops_limits.max_auto_strikes_per_carrier_per_day` = 2; Cổng 1 xét từng
        │      ticket riêng lẻ, config không có ô cho trần này
        └─ VÀ sau bão, nhiều đơn cùng một hãng miền Tây trễ trong cùng ngày (cộng dồn)
               bằng chứng: loạt `S3-LOAT` seed 11: S3-40 (phút 320), S3-41 (360), S3-42 (400), S3-43 (440) đều
               `file_carrier_fault` cho MKD; S3-42@11, S3-43@11 là lỗi thứ 3 và thứ 4, nhãn `faults: []`
```

Hai nhánh mà cổng vòng 1 **đã cắt** (để đọc cây cho đủ, không tính là nhánh còn hở): ca bão/lũ `FORCE_MAJEURE` bị ghi lỗi
(S3-01, S3-05) và ca tracking không ghi nguyên nhân (S3-20, S3-21). Ở mốc base, hai nhánh này gây 20/35 lỗi oan; mốc prepared
còn 0, vì Cổng 1 dùng `effective_policy` theo ngày, cộng cổng pháp lý `carrier_fault_requires_recorded_cause`.

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Phiên bản chính sách dùng để tính tiền, hạn mức tự động và lỗi hãng phải là phiên bản có `effective_from ≤ as_of ≤ effective_to`; mọi khoản `amount_vnd > auto_limit_vnd` của phiên bản đó phải có `approval_id` hợp lệ. Kiểm được: event `policy.policy_id` = `effective_policy(as_of)`; `wrongful_refund_vnd` = 0, `under_refund_vnd` = 0 trên report. | "Cờ `index_active` luôn được bật đúng ngày chính sách mới có hiệu lực." Thực tế cờ do người bật tay, và ngày 02/12 vẫn chưa ai bật. |
| [2] | Khi một phiên bản chính sách đổi, hệ thống phải báo PIC (NV-TUNG) và không tự động ghi lỗi hãng khi trạng thái chính sách chưa khớp ngày. Kiểm được: monitor đếm ticket phải ghim chính sách khác cờ (`policy_pin_rate` > 0 thì báo `alert_channel`). | "Đổi chính sách là việc của văn bản, hệ thống tự đi theo"; "hãng sẽ phản hồi qua kênh chính thức trước khi thiệt hại lớn". Thực tế hãng chỉ phát hiện sau khi đã bị phạt nhiều lỗi. |
| [3] | Không ghi quá `max_auto_strikes_per_carrier_per_day` (= 2) lỗi tự động cho cùng một hãng trong một ngày; từ lỗi thứ 3 phải có người xác nhận. Kiểm được: số dòng `fault_rows` theo hãng/ngày ≤ 2 khi không có người duyệt; monitor `carrier_strikes_max_per_day` ≤ 2. | "Lỗi của hãng là sự kiện độc lập, rải đều theo ngày." Thực tế bão, lũ làm nhiều đơn cùng tuyến, cùng hãng trễ dồn trong một ngày. |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Agent chọn chính sách theo cờ `index_active` (REFUND-v3) chứ không theo ngày hiệu lực, nên tính sai tiền và hạn mức (`S3-02@11`, `S3-03@11`, `S3-04@11`). | **Sửa 1:** `pre_guard`: `Verdict.allow(policy_id=H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)["policy_id"])`, ghi event `policy_pinned` khi khác cờ. **Sửa 2:** `write_gate` → `_gate_refund`: `amount_vnd > auto_limit_vnd` của chính sách hiệu lực mà không có `approval_id` thì `escalate` (event `refund_over_auto_limit`). | Chặn | **NGĂN hẳn** nhánh này ở tầng code: phiên bản chính sách giờ lấy từ nguồn sự thật (ngày hiệu lực), không còn phụ thuộc người bật cờ. Sửa 2 biến nhánh thành **VÀ**: hoàn vượt hạn mức chỉ còn xảy ra khi cả `pre_guard` lẫn Cổng 2 cùng hỏng. Còn hở nếu chính `effective_from` trong bảng `policies` nhập sai. | `R-S3-after-20261119-171935-a0892a` (sửa 1) · `R-S3-after-20261119-171956-03640a` (sửa 2) |
| [2] | Không ai được giao đổi cờ chính sách ngày 01/12 và xác nhận lỗi hãng khi chính sách đổi (con người, vận hành). | **Phần code (Kỹ sư cổng):** event `policy_pinned` trong `pre_guard` cho thấy cờ lệch ngày hiệu lực; dùng làm tín hiệu báo PIC (monitor ở C8). Lỗi thứ 3 trở đi của một hãng trong ngày được chuyển NV-OANH (sửa 3). **Phần quy trình (Vận hành và pháp lý, Đức bổ sung):** `operations.stop_conditions` và Runbook 4–5: PIC NV-TUNG đổi cờ đúng ngày hiệu lực, báo `#logix-refund-pilot-alerts` khi có `policy_pinned`. | Phát hiện + vận hành | **GIẢM khả năng**: nhờ sửa 1, cờ sai không còn gây thiệt hại trực tiếp, nhưng việc con người quên đổi cờ vẫn xảy ra được; ta chỉ phát hiện sớm. Gốc con người không ngăn được bằng code. | `R-S3-after-20261119-172041-418fc9` |
| [3] | Không hệ thống nào thực thi trần `max_auto_strikes_per_carrier_per_day` = 2; sau bão, MKD bị ghi lỗi thứ 3 và thứ 4 trong cùng ngày (`S3-42@11`, `S3-43@11`, loạt `S3-LOAT`). | **Sửa 3:** `write_gate` → `_gate_carrier_fault`: đếm `ctx.tools.fault_rows(carrier_id=...)` của ngày; `>= ctx.tools.ops_limits()["max_auto_strikes_per_carrier_per_day"]` thì `deny` (event `carrier_strike_cap`, người xác nhận NV-OANH). Khách vẫn được hoàn theo chính sách. | Giới hạn thiệt hại | **NGĂN hẳn** việc ghi tự động vượt trần mỗi ngày, nhưng chỉ **GIẢM** tác hại tổng: 2 lỗi đầu mỗi ngày vẫn ghi tự động, và trần 7 ngày (`suspend_after_strikes_7d`) chưa được đếm, vì sổ lỗi mỗi ngày giả lập là mới. Ghi vào risk register (C10). | `R-S3-after-20261119-172041-418fc9` (lệnh 6 `R-S3-grade-20261119-172040-418fc9`) |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `policy_flag_drift_rate` (chính) · kèm `max_carrier_strikes_per_day` (phụ, xem dưới bảng) |
| **Bước / hành vi được đo** | Bước **chọn chính sách** (C6 nhánh [1] và [2]): cờ `index_active` trong bảng `policies`, một bản sao do người bật tay, có còn khớp chính sách có hiệu lực theo ngày (`effective_from` ≤ `as_of` ≤ `effective_to`) hay không. |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ ticket (%) mà cờ `index_active` chỉ sang một phiên bản chính sách khác phiên bản có hiệu lực theo ngày. |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `events` của từng trial: event `guard` có `kind = "policy_pinned"`, do `pre_guard` vòng 2 ghi khi cờ lệch, kèm `effective`, `index_active`, `as_of`. Không đọc nhãn, không đọc chữ khách gõ. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số trial có ít nhất một event `policy_pinned` ÷ tổng số trial được đưa cho trợ lý (mẫu số gồm cả ca chuyển người). Ca `pre_guard` không tìm được chính sách hiệu lực thì đã `escalate` và không ghi event: không tính vào tử số, nhưng vẫn nằm trong mẫu số. |
| **Khung thời gian / ngưỡng báo động** | Tính mỗi ca trực (480 phút). **VÀNG:** > 0 trong ca, tức cờ lệch nhưng `pre_guard` đã ghim đúng phiên bản → PIC NV-TUNG đổi cờ trong 60 phút, báo `#logix-refund-pilot-alerts`. **ĐỎ:** > 0 kéo dài sang ca thứ hai, hoặc xuất hiện vào ngày có chính sách mới hiệu lực → kiểm lại các khoản hoàn và lỗi hãng của ngày đó (Runbook 4). |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | (1) Chỉ sáng khi `pre_guard` vòng 2 chạy: ở mốc base và prepared luôn bằng 0. (2) Không thấy trường hợp chính `effective_from` / `effective_to` nhập sai: cờ và ngày cùng sai thì vẫn báo 0. (3) Không thấy hậu quả cộng dồn cho hãng; phần đó do chỉ số phụ `max_carrier_strikes_per_day` đo. |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | Mốc after: bộ nền **0** · S3 **1,0** (lệnh 6 `R-S3-grade-20261119-172454-ade563`, `6 monitor ✅`). |

**Chỉ số phụ `max_carrier_strikes_per_day`** (C6 nhánh [3]; cùng ý với telemetry ở Phiếu A câu 1.4): số lỗi hãng ghi tự động
**nhiều nhất** mà một hãng nhận trong một ngày giả lập. Dữ liệu là `faults` của các trial cùng `day` và cùng `seed`, không cần nhãn.
Cách tính: đếm số dòng `faults` theo (ngày, seed, hãng), lấy giá trị lớn nhất. Ngưỡng: **> 2** (`ops_limits.max_auto_strikes_per_carrier_per_day`)
là ĐỎ, tắt `file_carrier_fault` và báo NV-OANH xác nhận với hãng. Chỉ số này sáng cả khi chưa có cổng: mốc base, bộ nền **1** · S3
**4** (MKD nhận 4 lỗi trong loạt `S3-LOAT`); mốc after, bộ nền **1** · S3 **2** (cổng sửa 3 giữ đúng trần). Điểm mù: không cộng dồn
7 ngày (`suspend_after_strikes_7d`), vì mỗi ngày giả lập là một sổ lỗi mới.

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `__________`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] ______________________________
 └─ HOẶC
 ├─ [1] ______________ VÀ [gate ______ hỏng]
 ├─ [2] ______________ VÀ [gate ______ hỏng]
 └─ [3] ______________ (còn hở?)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| | | | |
| | | | |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp ___ lần trong một giờ thì: …
2. Nếu nhà cung cấp LLM lỗi quá ___ phút thì: …
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: …

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `0b64495` (giống v1) |
| Hash chốt cổng vòng 1 | `76c5a3bb` (giống v1) |
| Mã lần chạy dùng làm bằng chứng | thẻ `S3`, mốc base: `R-S3-before-20261119-170053-e9a32d` · prepared: `R-S3-prepared-20261119-170053-e9a32d` · after: `[Chờ lần grade cuối sau sửa S3]` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | `[Chờ bản chạy after sau sửa S3]` |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | `[Chờ bản chạy after sau sửa S3]` |
| Quyết định (khoanh một) | `[Chờ bản chạy after sau sửa S3]` *(chọn 1: Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng)* |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `[Chờ bản chạy after sau sửa S3]` |
| Bằng chứng 2 | `[Chờ bản chạy after sau sửa S3]` |
| Bằng chứng 3 | `[Chờ bản chạy after sau sửa S3]` |
| Khớp dòng nào trong `decision_rule` đã ký? | `[Chờ bản chạy after sau sửa S3]` |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | `[Điền theo quyết định v2]` |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | `[Điền theo quyết định v2]` |
| Nếu Dừng: bài học ghi lại | `[Điền theo quyết định v2]` |
| Ngày quyết định lại (trừ khi Dừng) | `2026-11-26` *(nếu không chọn Dừng, khớp A4 & B8)* |
| PIC ký | `Nguyễn Bảo Trung (Sản phẩm và kinh doanh)` |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: `[Chờ bản chạy after sau sửa S3]`
- Report tự kiểm tra: mã lần chạy `[Chờ bản chạy after sau sửa S3]` · ô nào còn đỏ (nguyên nhân × tầng): `[Chờ bản chạy after sau sửa S3]`
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: **Đỡ được:** chặn **20/35** lỗi oan cho hãng (giảm `35 → 15`, `pass_rate` `0,25 → 0,50`, `pass_k` `0,25 → 0,50`; sạch hoàn toàn `S3-01`, `S3-05` trễ do bão `FORCE_MAJEURE`, `S3-20..21` trống `delay_cause`, `DNB` `5 → 0`, kho `HCM` đạt `1,0`, giữ `pii_leaks = 0`, `queue_stuck = 0`). **Bỏ sót:** chưa ghim `policy_id` theo `as_of` ở `pre_guard` và chưa kiểm `auto_limit_vnd` của `REFUND-v4` (`100.000đ`), nên hoàn thiếu `667.000đ` (`S3-02..03`), hoàn sai `900.000đ` / 5 seed (`S3-04`) kéo `ROI` xuống `-2,4`, và chưa chặn trần `2 lỗi/hãng/ngày` nên còn `15` lỗi oan (`MKD` loạt `S3-42..43` và `S3-04`).
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: `[Chờ bản chạy after sau sửa S3]`
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Bộ thử mock chưa đo được độ trễ/sai sót nhập `delay_cause` và cập nhật chính sách ngoài thực tế, tải hàng chờ khi bão kéo dài nhiều ngày, cũng như **bài test ẩn (`hidden`)** (đơn, khách, cách viết, ngày khác); vì vậy dù đạt test thấy được vẫn phải giữ kiểm mẫu 10% và điều kiện dừng cứng khi ra pilot.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Thiết kế giả định trường `delay_cause` và ngày giao trong tracking DB do điểm phát/hãng nhập đúng sự thật và phụ lục chính sách mới được cập nhật lên hệ thống đúng trước ngày hiệu lực `as_of`, trong khi thực tế bão lũ hoặc quá tải dễ gây bỏ trống, nhập sai hoặc trễ đồng bộ.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: `[Chờ hoàn tất sửa guards.py / operating_gates.json vòng 2 để kết luận chính xác nhánh nào ngăn hẳn và nhánh nào chỉ giảm]`
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Đo lại độ chính xác và tỉ lệ thiếu `delay_cause` qua đối soát tuần với hãng/shop, tỉ lệ chuyển người cùng thời gian chờ thực tế giờ cao điểm sau bão, và chi phí mỗi ticket kèm ROI thực tế theo từng kho so với ngưỡng `8.000đ` / `0,25`.
