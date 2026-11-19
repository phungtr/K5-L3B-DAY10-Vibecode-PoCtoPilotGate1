"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


# ---------------------------------------------------------------------------------------------------------------
# Chỉ số của bàn (Kỹ sư cổng). Chỉ đọc events trong trace, không dùng nhãn. Mỗi hàm trả về tỉ lệ trên số trial.
# ---------------------------------------------------------------------------------------------------------------
def _rate(trials, hit):
    return sum(1 for t in trials if any(hit(e) for e in t["events"])) / max(1, len(trials))


def claim_db_mismatch_rate(trials):
    """Kỹ thuật · Phiếu B mục B2 lỗi 1, B4 dòng PERTURBED.
    Tỉ lệ ticket có event `model_override`: số ngày khách tự khai đè lên số ngày theo tracking DB.
    Đọc từ event của agent nên sáng đèn cả khi chưa có cổng. Tăng đột ngột = khách đang truyền nhau cách viết."""
    return _rate(trials, lambda e: e.get("type") == "model_override")


def unrecorded_cause_rate(trials):
    """Dữ liệu · Phiếu B mục B4 dòng INCOMPLETE.
    Tỉ lệ ticket mà tracking không ghi nguyên nhân trễ (`tracking.cause_recorded == false`), tức agent tự suy là CARRIER.
    Tăng = hãng / điều phối nhập thiếu `delay_cause`, nguy cơ ghi oan lỗi hãng."""
    return _rate(trials, lambda e: e.get("type") == "tracking" and e.get("cause_recorded") is False)


def fail_open_rate(trials):
    """Hạ tầng · Phiếu B mục B4 dòng INCAPABLE.
    Tỉ lệ ticket mà LLM lỗi ở bước kiểm chính sách và agent rơi vào `fail_open` (hoàn nguyên phí ship, ghi lỗi hãng).
    Khác 0 = giờ cao điểm / LLM 429; theo dõi cùng hàng chờ người duyệt."""
    return _rate(trials, lambda e: e.get("type") == "llm_fallback" and e.get("mode") == "fail_open")


def write_blocked_rate(trials):
    """Cổng · Phiếu B mục B2 phần 3 (`fault_without_db_basis`) và Cổng 1, Cổng 2 trong guards.py.
    Tỉ lệ ticket có ít nhất một lệnh ghi bị cổng chặn hoặc sửa (event `gate` deny/escalate/modify của guards.py, cổng
    kinh doanh của host, hoặc cổng pháp lý chặn ghi lỗi hãng). KHÔNG đếm việc bỏ trường PII khỏi thông báo gửi hãng,
    vì việc đó xảy ra với mọi thông báo, không phải dấu hiệu sự cố. Ở mốc base luôn 0; sau khi có cổng, tăng = có thêm
    ca agent định ghi sai mà cổng đỡ được."""
    def hit(e):
        if e.get("type") in ("gate", "business_gate"):
            return True
        return e.get("type") == "legal_gate" and e.get("gate") == "carrier_fault_requires_recorded_cause"
    return _rate(trials, hit)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "claim_db_mismatch_rate": claim_db_mismatch_rate,
    "unrecorded_cause_rate": unrecorded_cause_rate,
    "fail_open_rate": fail_open_rate,
    "write_blocked_rate": write_blocked_rate,
}
STARTER_MONITORS = ("escalation_rate",)
