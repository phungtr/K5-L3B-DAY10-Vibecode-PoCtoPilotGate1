"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # VÒNG 2 · S3 · Phiếu C mục C6 nhánh [1], C7 dòng [1].
    # Ghim phiên bản chính sách theo NGÀY HIỆU LỰC (effective_from ≤ as_of ≤ effective_to), không theo cờ index_active
    # (bản sao do người bật tay). Agent sẽ tính tiền, hạn mức tự động và lỗi hãng bằng đúng phiên bản này.
    policies = ctx.tools.lookup_policies()
    policy = H.effective_policy(policies, ctx.as_of)
    if policy is None:
        return Verdict.escalate("không có chính sách nào hiệu lực ngày hôm nay: chuyển người xử lý")
    flagged = next((p["policy_id"] for p in policies if p.get("index_active")), None)
    if flagged != policy["policy_id"]:
        ctx.log("policy_pinned", effective=policy["policy_id"], index_active=flagged, as_of=ctx.as_of)
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_carrier_fault(ctx, action)
    return Verdict.allow()


# ---------------------------------------------------------------------------------------------------------------
# Dữ kiện dùng chung: CHỈ đọc nguồn sự thật (đơn, tracking, chính sách theo ngày). Không đọc chữ khách gõ.
# ---------------------------------------------------------------------------------------------------------------
def _vnd(x):
    return f"{int(x):,}đ".replace(",", ".")


def _facts(ctx, action):
    """(order, parcel, delay_days theo tracking DB, policy hiệu lực theo ngày) hoặc None nếu thiếu dữ kiện."""
    order = ctx.tools.lookup_order(action.get("order_id"))
    if order is None or not order.get("parcels"):
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)   # theo ngày, không theo cờ index_active
    if policy is None:
        return None
    return order, parcel, delay, policy


# ---------------------------------------------------------------------------------------------------------------
# CỔNG 2 · issue_refund · Phiếu B mục B4 (PERTURBED, INCAPABLE), B6 dòng 2, B2 lỗi 1.
# Số tiền hoàn không được lớn hơn quyền lợi tính từ tracking DB + chính sách hiệu lực. Lớn hơn → chuyển người.
# ---------------------------------------------------------------------------------------------------------------
def _gate_refund(ctx, action):
    if action.get("basis") == "fail_open":
        ctx.log("refund_fail_open", order_id=action.get("order_id"), amount_vnd=action.get("amount_vnd"))
        return Verdict.escalate("LLM lỗi ở bước kiểm chính sách (fail_open): không hoàn tự động, chuyển người duyệt")

    # Người trả tiền: hoàn tự động do LogiX chịu. Đổi sang shop / bên khác (ví dụ vì một "lệnh" trong chữ khách hay
    # ghi chú lúc đặt hàng) thì phải có phê duyệt của người, không để model tự quyết. Phiếu B mục B5 hàng 3.
    payer = action.get("payer", "LOGIX")
    if payer != "LOGIX" and not action.get("approval_id"):
        ctx.log("refund_payer_not_logix", order_id=action.get("order_id"), payer=payer,
                amount_vnd=action.get("amount_vnd"))
        return Verdict.escalate(f"người trả tiền là {payer} nhưng không có phê duyệt: chuyển người duyệt")

    facts = _facts(ctx, action)
    if facts is None:
        return Verdict.escalate("thiếu dữ kiện nguồn sự thật (đơn/kiện/chính sách hiệu lực): chuyển người duyệt")
    order, parcel, delay, policy = facts

    entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    asked = int(action.get("amount_vnd") or 0)
    if asked > entitled:
        ctx.log("refund_over_entitlement", order_id=order["order_id"], parcel_id=parcel["parcel_id"],
                asked_vnd=asked, entitled_vnd=entitled, db_delay_days=delay, policy_id=policy["policy_id"])
        return Verdict.escalate(
            f"số tiền hoàn {_vnd(asked)} vượt quyền lợi {_vnd(entitled)} theo tracking DB "
            f"(trễ {delay} ngày, {policy['policy_id']}): chuyển người duyệt")

    # VÒNG 2 · S3 · Phiếu C mục C6 nhánh [1]: số tiền đúng quyền lợi vẫn phải qua người nếu vượt HẠN MỨC tự động
    # của chính sách hiệu lực (REFUND-v4: 100.000đ). Lớp chặn thứ hai, phòng khi pre_guard không ghim được phiên bản.
    if asked > policy["auto_limit_vnd"] and not action.get("approval_id"):
        ctx.log("refund_over_auto_limit", order_id=order["order_id"], asked_vnd=asked,
                auto_limit_vnd=policy["auto_limit_vnd"], policy_id=policy["policy_id"])
        return Verdict.escalate(
            f"số tiền hoàn {_vnd(asked)} vượt hạn mức tự động {_vnd(policy['auto_limit_vnd'])} "
            f"({policy['policy_id']}) mà không có phê duyệt: chuyển người duyệt")
    return Verdict.allow()


# ---------------------------------------------------------------------------------------------------------------
# CỔNG 1 · file_carrier_fault · Phiếu B mục B4 (WRONG, INCOMPLETE, PERTURBED), B6 dòng 1, B2 lỗi 2.
# Chỉ ghi lỗi hãng khi chính sách hiệu lực cho phép (đủ ngày trễ theo DB + nguyên nhân có ghi và thuộc fault_causes),
# và ghi cho ĐÚNG kiện trễ, đúng hãng, đúng tài xế, đúng số ngày theo DB.
# ---------------------------------------------------------------------------------------------------------------
def _gate_carrier_fault(ctx, action):
    facts = _facts(ctx, action)
    if facts is None:
        return Verdict.deny("thiếu dữ kiện nguồn sự thật: không ghi lỗi hãng")
    order, parcel, delay, policy = facts

    if not H.carrier_at_fault(policy, parcel, delay):
        ctx.log("fault_without_db_basis", order_id=order["order_id"], parcel_id=parcel["parcel_id"],
                carrier_id=parcel["carrier_id"], db_delay_days=delay, recorded_cause=parcel.get("delay_cause"),
                asked_delay_days=action.get("delay_days"), policy_id=policy["policy_id"])
        return Verdict.deny(
            f"không đủ căn cứ ghi lỗi hãng: trễ {delay} ngày theo DB, nguyên nhân "
            f"{parcel.get('delay_cause') or 'chưa ghi'} ({policy['policy_id']})")

    # VÒNG 2 · S3 · Phiếu C mục C6 nhánh [3], C7 dòng [3]. Trần đã thống nhất với Ops (ops_limits): từ lỗi thứ
    # (max + 1) của cùng một hãng trong ngày thì KHÔNG ghi tự động; để kế toán đối soát NV-OANH xác nhận với hãng.
    # Từng ca có thể đúng, nhưng cộng dồn sau bão sẽ đẩy hãng tới ngưỡng đình chỉ. Khách vẫn được hoàn theo chính sách.
    cap = (ctx.tools.ops_limits() or {}).get("max_auto_strikes_per_carrier_per_day")
    if cap is not None:
        today = len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"]))
        if today >= cap:
            ctx.log("carrier_strike_cap", carrier_id=parcel["carrier_id"], strikes_today=today, cap=cap,
                    order_id=order["order_id"], parcel_id=parcel["parcel_id"], reviewer="NV-OANH")
            return Verdict.deny(
                f"hãng {parcel['carrier_id']} đã có {today} lỗi tự động hôm nay (trần {cap}): "
                f"không ghi tự động, chờ NV-OANH xác nhận")

    want = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
            "driver_id": parcel.get("driver_id"), "delay_days": delay}
    diff = {k: v for k, v in want.items() if action.get(k) != v}
    if diff:
        ctx.log("fault_target_fixed", order_id=order["order_id"],
                before={k: action.get(k) for k in diff}, after=diff)
        return Verdict.modify("ghi lỗi cho đúng kiện trễ / hãng / số ngày theo tracking DB", **diff)
    return Verdict.allow()
