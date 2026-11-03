# -*- coding: utf-8 -*-
"""各類所得扣繳暨免扣繳憑單申報檔、二代健保補充保險費明細申報檔產生器。
依「綜合所得稅資料電子申報作業要點」（UTF-8 分隔符號格式，副檔名 U8）與健保署補充保險費明細申報檔案格式（CSV）產生，可匯入申報系統。
用法：python tax_export.py --data data --year 2026 --out 輸出資料夾
  --data 為存放「薪資_YYYYMM.xlsx(.enc)」的資料夾；--year 為給付年度（民國年請填西元，例如 2026）。
  依「申報設定」的薪資發放月份判斷給付年度（次月發薪時，12月薪資歸入次年所得）。
本程式涵蓋員工薪資所得（格式50）與其補充保險費；顧問費、執行業務、租金等其他所得請另行申報。
匯入前請先用國稅局申報程式、健保署媒體檢核程式檢核。範例值未改時預設不產檔（--allow-placeholder／--allow-invalid-id 僅供測試）。
"""
import argparse, datetime, os, sys
import hrdata, common as C

CRLF = "\r\n"

def collect(data_dir, year, offset):
    """彙整給付年度內各月資料，回傳 (員編 → 彙總, 各月明細, 最新月份檔路徑)。"""
    months = hrdata.year_files(data_dir, year, offset)
    if not months: sys.exit(f"{data_dir} 內找不到給付年度 {year} 的薪資檔")
    emps, detail = {}, []
    for ym, path in months:
        for eid, rec in hrdata.load_employees(path).items():
            it = hrdata.month_tax_items(rec)
            e = emps.setdefault(eid, dict(name=rec["name"], idno=rec["idno"], zh=rec["zhenghao"], addr=rec["addr"], pay=0, tax=0, vol=0, months=[]))
            e["pay"] += it["薪資所得(應稅)"] + it["其他兼職薪資"]; e["tax"] += it["薪資扣繳"] + it["獎金扣繳"]; e["vol"] += it["勞退自願提繳"]
            if it["薪資所得(應稅)"] + it["其他兼職薪資"] > 0: e["months"].append(ym)
            raw = rec["raw"]
            detail.append(dict(ym=ym, eid=eid, name=rec["name"], idno=rec["idno"], supp=it["補充保費代扣"], perf=hrdata._g(raw, "績效獎金"),
                               pt=hrdata._g(raw, "其他(兼職)"), insured=hrdata._g(raw, "健保薪資")))
    return emps, detail, months[-1][1]

def pay_date(ym, cfg):
    y, m = int(ym[:4]), int(ym[4:]) + int(cfg.get("pay_offset", "0") or 0)
    if m > 12: y, m = y + 1, m - 12
    d = int(cfg.get("pay_day", "0") or 0)
    return C.month_end(y, m) if d == 0 else datetime.date(y, m, min(d, 28))

def income_file(cfg, emps, year, serial_start=1, warnings=None, allow_invalid_id=False):
    w = warnings if warnings is not None else []
    cid, office = cfg["company_id"], cfg["tax_office"]; ry = f"{year - 1911:03d}"; today = datetime.date.today()
    lines, n, tot_pay, tot_tax, tot_vol = [], 0, 0, 0, 0
    first = last = None
    for eid, e in sorted(emps.items()):
        if e["pay"] <= 0: continue
        zh, idno = e["zh"] or "0", e["idno"]
        if zh == "0" and not C.check_person_id(idno):
            w.append(f"{eid} {e['name']}：身分證字號未通過檢查" + ("（已略過檢查）" if allow_invalid_id else "，未入檔"))
            if not allow_invalid_id: continue
        if len(e["name"]) < 2: w.append(f"{eid}：姓名少於2個字"); continue
        if not e["addr"]: w.append(f"{eid} {e['name']}：缺戶籍地址（地址全空白會被剔除）"); continue
        n += 1; serial = f"{serial_start + n - 1:08d}"; first = first or serial; last = serial
        months = sorted(e["months"]); period = f"{int(months[0][:4]) - 1911:03d}{months[0][4:]}{int(months[-1][:4]) - 1911:03d}{months[-1][4:]}"
        gross, tax = int(e["pay"]), int(e["tax"]); net = gross - tax
        f = [office, serial, cid, "", "50", idno, zh, str(gross), str(tax), str(net), eid, "", "", cfg.get("soft_flag", "A"), "", ry,
             C.to_fullwidth(e["name"])[:50], C.to_fullwidth(e["addr"])[:100], period, str(int(e["vol"])), "", "", "", "", "",
             cfg.get("issue_mode", "1"), "", "", "", "", f"{today.month:02d}{today.day:02d}", ""]
        assert len(f) == 32
        lines.append("|".join(f)); tot_pay += gross; tot_tax += tax; tot_vol += int(e["vol"])
    if not n: sys.exit("沒有可入檔的所得資料")
    book = [office, "ZZ000001", cid, "9", "1", "1", "3", "", str(n), str(tot_pay), str(tot_tax), cfg["wh_tax_no"], "", cfg["house_tax_no"], "", ry,
            C.roc_date(today), first, last, "", "", "", str(tot_vol), "", "", "C"]
    assert len(book) == 26
    unit = [office, "", cid, "1", cfg["unit_name"][:50], cfg["unit_addr"][:26], cfg["payer_name"][:20], cfg["contact"][:20], cfg["phone"], cfg["email"],
            cfg["wh_tax_no"], "", "01", "", "N", "", "N"]
    assert len(unit) == 17
    lines += ["|".join(C.to_fullwidth(x) if i in () else x for i, x in enumerate(book)), "|".join(unit)]
    return lines, n, tot_pay, tot_tax

def supp_files(cfg, detail, year, out, warnings, allow_invalid_id=False):
    today = datetime.date.today(); rate, mult = float(cfg.get("supp_rate", "0.0211")), float(cfg.get("bonus_mult", "4"))
    groups = {"62": [], "63": []}; cum = {}
    for d in sorted(detail, key=lambda x: (x["ym"], x["eid"])):
        cum_prev = cum.get(d["eid"], 0); cum[d["eid"]] = cum_prev + d["perf"]
        if d["perf"] > 0:                                   # 獎金：全年累計超過投保金額倍數的部分才計費
            ins = d["insured"] * mult
            expect = round((max(0, cum[d["eid"]] - ins) - max(0, cum_prev - ins)) * rate)
            if abs(expect - d["supp"]) > 1: warnings.append(f"{d['eid']} {d['name']} {d['ym']}：獎金補充保費應為約 {expect}，薪資檔填 {d['supp']}，請核對")
        if d["supp"] <= 0: continue
        cat = "62" if d["perf"] > 0 else ("63" if d["pt"] > 0 else None)
        if not cat: warnings.append(f"{d['eid']} {d['name']} {d['ym']}：有補充保費但沒有獎金或兼職給付，無法歸類，未入檔"); continue
        if not C.check_person_id(d["idno"]) and not allow_invalid_id: warnings.append(f"{d['eid']} {d['name']}：身分證字號未通過檢查，補充保費未入檔"); continue
        groups[cat].append(dict(d, cum=cum[d["eid"]], paid=pay_date(d["ym"], cfg)))
    made = []
    heads = {"62": ("*資料識別碼,處理方式(新增I 覆蓋R),給付日期,所得人身分證號,所得人姓名,單次獎金給付金額,扣繳補充保險費金額,申報編號(詳格式說明),投保單位代號,扣費當月投保金額,同年度累計獎金金額,資料註記"),
             "63": ("*資料識別碼,處理方式(新增I 覆蓋R),給付日期,所得人身分證號,所得人姓名,單次給付金額,扣繳補充保險費金額,申報編號(詳格式說明),信託註記,資料註記")}
    for seq, (cat, items) in enumerate([(c, i) for c, i in groups.items() if i], 1):
        cnt, seen = len(items), {}
        top = ["1", cfg["company_id"], cat, C.roc_ym(items[0]["paid"]), C.roc_ym(items[-1]["paid"]), str(cnt),
               str(sum(x["perf"] if cat == "62" else x["pt"] for x in items)), str(sum(x["supp"] for x in items)),
               C.pad_fullwidth(cfg["unit_name"], 25), cfg["phone"], cfg["email"], C.pad_fullwidth(cfg["contact"], 25)]
        rows = []
        for x in items:
            key = (x["idno"], x["paid"]); seen[key] = seen.get(key, 0) + 1
            base = ["2", "I", C.roc_date(x["paid"]), x["idno"], C.to_fullwidth(x["name"])[:25]]
            if cat == "62": rows.append(base + [str(int(x["perf"])), str(int(x["supp"])), str(seen[key]), cfg["nhi_unit"], str(int(x["insured"])), str(int(x["cum"])), ""])
            else: rows.append(base + [str(int(x["pt"])), str(int(x["supp"])), str(seen[key]), "", ""])
        hdr1 = "*資料識別碼,統一編號,所得類別,給付起始年月,給付結束年月,申報總筆數,所得(收入)給付總額,扣繳補充保險費總額,扣費義務人名稱,聯絡電話,電子郵件信箱,聯絡人姓名"
        text = CRLF.join([hdr1, ",".join(top), heads[cat]] + [",".join(r) for r in rows]) + CRLF
        name = f"DPR{cfg['company_id']}{C.roc_date(today)}{seq:03d}.csv"
        with open(os.path.join(out, name), "wb") as f: f.write(text.encode("cp950", errors="replace"))
        made.append((name, cat, cnt, sum(x["supp"] for x in items)))
    return made

def main():
    ap = argparse.ArgumentParser(description="各類所得與補充保費申報檔產生器")
    ap.add_argument("--data", default="data"); ap.add_argument("--year", type=int, required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--allow-placeholder", action="store_true"); ap.add_argument("--allow-invalid-id", action="store_true")
    a = ap.parse_args()
    months = hrdata.list_months(a.data)
    if not months: sys.exit("data 資料夾內沒有薪資檔")
    cfg = hrdata.load_config(hrdata.month_path(a.data, months[0]))
    need = ["tax_office", "wh_tax_no", "house_tax_no", "nhi_unit", "unit_addr", "payer_name", "contact", "phone", "email"]
    bad = C.config_problems(cfg, need)
    if not C.check_company_id(cfg.get("company_id", "")): sys.exit("申報設定的營利事業統一編號未通過邏輯檢查")
    if bad and not a.allow_placeholder: sys.exit("「申報設定」下列項目仍是空白或範例值，請先填寫：" + "、".join(bad) + "（測試可加 --allow-placeholder）")
    emps, detail, _ = collect(a.data, a.year, int(cfg.get("pay_offset", "0") or 0))
    os.makedirs(a.out, exist_ok=True); warnings = []
    lines, n, gross, tax = income_file(cfg, emps, a.year, warnings=warnings, allow_invalid_id=a.allow_invalid_id)
    p = os.path.join(a.out, f"{cfg['company_id']}.{a.year - 1911:03d}.U8")
    with open(p, "w", encoding="utf-8", newline="") as f: f.write(CRLF.join(lines) + CRLF)
    made = supp_files(cfg, detail, a.year, a.out, warnings, a.allow_invalid_id)
    rep = [f"給付年度：{a.year}（民國 {a.year - 1911} 年）", f"各類所得申報檔：{os.path.basename(p)}（薪資所得 {n} 人，給付總額 {gross:,}，扣繳稅額 {tax:,}）"]
    rep += [f"補充保費申報檔：{m[0]}（類別 {m[1]}，{m[2]} 筆，補充保費 {m[3]:,}）" for m in made] or ["補充保費申報檔：本年度沒有需申報的補充保費"]
    rep += ["", "需處理或確認的事項："] + (["・" + x for x in warnings] or ["・無"])
    rep += ["", "提醒：1. 匯入前請用國稅局申報程式／健保署媒體檢核程式檢核。 2. 所得申報期限原則上為次年1月31日（遇連續3日以上國定假日順延）。",
            "3. 補充保費須於給付日次月底前繳納；年度明細申報與繳款書請依健保署規定辦理。 4. 本檔僅含員工薪資所得，顧問費、執行業務、租金等其他所得需另行申報。"]
    open(os.path.join(a.out, "申報核對報告.txt"), "w", encoding="utf-8").write("\n".join(rep))
    print("\n".join(rep))

if __name__ == "__main__":
    main()
