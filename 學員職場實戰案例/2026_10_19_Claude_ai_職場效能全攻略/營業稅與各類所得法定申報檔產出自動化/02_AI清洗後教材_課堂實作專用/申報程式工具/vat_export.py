# -*- coding: utf-8 -*-
"""營業稅進銷項資料檔產生器。
依「營業稅電子資料申報繳稅作業要點」附件五格式（每筆81字元，檔名＝統一編號.TXT）產生，並同時輸出進項明細表、銷項明細表 Excel。
資料來源：素材總表的「流程2_報銷申請」（進項）與「營業稅_銷項登記」（銷項），公司資料來自「申報設定」。
用法：python vat_export.py --xlsx 無紙化流程_素材總表.xlsx --from 2026-11-01 --to 2026-12-31 --out 輸出資料夾
匯入前請先用財政部「營業稅網路申報程式」的前端審核功能檢核；若審核通過再上傳。範例值未改時預設不產檔（--allow-placeholder 可略過，僅供測試）。
"""
import argparse, os, re, sys, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import hrdata, common as C

IN_FMT = {"電子發票": "25", "統一發票(三聯式)": "21", "二聯式收銀機發票": "22"}
TAXCODE = {"應稅": "1", "零稅率": "2", "免稅": "3", "作廢": "F"}
F = "Microsoft JhengHei"

def _table(ws, row0):
    hdr = {}
    for c in range(1, ws.max_column + 1):
        v = ws.cell(row0, c).value
        if v: hdr[v] = c
    return hdr

def read_purchases(wb, d_from, d_to, include_nondeductible, notes):
    ws = wb["流程2_報銷申請"]; h = _table(ws, 4); out = []
    for r in range(5, ws.max_row + 1):
        no = ws.cell(r, h["申請編號"]).value
        if not no: continue
        g = lambda k: ws.cell(r, h[k]).value
        kind, d = g("憑證種類"), C.to_date(g("憑證日期"))
        if g("營業稅申報狀態") == "已申報" or not kind: continue
        if kind not in IN_FMT:
            notes.append((no, "進項", f"憑證種類「{kind}」不屬營業稅進項申報範圍，未入檔")); continue
        if not d or not (d_from <= d <= d_to):
            if d and d < d_from: notes.append((no, "進項", f"憑證日期 {d} 早於申報期間，未入檔"))
            continue
        track = (g("發票字軌號碼") or "").strip().upper(); seller = str(g("統一編號") or "").strip()
        base, tax = int(g("未稅金額") or 0), int(g("稅額") or 0)
        ded = g("進項稅額檢核") or ""; typ = g("扣抵類別") or "進貨及費用"
        problems = []
        if g("買受人為本公司統編") != "是": problems.append("買受人統編不是本公司，不得扣抵")
        if not re.fullmatch(r"[A-Z]{2}\d{8}", track): problems.append("發票字軌號碼須為2位英文加8位數字")
        if not C.check_company_id(seller): problems.append(f"賣方統一編號「{seller}」未通過邏輯檢查")
        if problems:
            notes.append((no, "進項", "；".join(problems) + "，未入檔")); continue
        if "不得扣抵" in ded:
            if not include_nondeductible:
                notes.append((no, "進項", "不得扣抵，未入檔（併入申報書進項總金額）")); continue
            code = "3" if typ == "進貨及費用" else "4"
        else:
            code = "1" if typ == "進貨及費用" else "2"
        fmt = IN_FMT[kind]
        amount, vat = (base + tax, 0) if fmt == "22" else (base, tax)      # 二聯式：銷售額內含稅額，稅額填0
        out.append(dict(kind="進項", no=no, date=d, fmt=fmt, buyer=None, seller=seller, track=track, amount=amount, tax=vat,
                        taxcode=TAXCODE.get(g("課稅別") or "應稅", "1"), deduct=code, customs="", cert=kind))
    return out

def read_sales(wb, d_from, d_to, notes):
    if "營業稅_銷項登記" not in wb.sheetnames: return []
    ws = wb["營業稅_銷項登記"]; h = _table(ws, 4); out = []
    for r in range(5, ws.max_row + 1):
        track = ws.cell(r, h["發票字軌號碼"]).value
        if not track: continue
        g = lambda k: ws.cell(r, h[k]).value
        d = C.to_date(g("發票開立日期"))
        if g("營業稅申報狀態") == "已申報": continue
        if not d or not (d_from <= d <= d_to): continue
        track = str(track).strip().upper(); buyer = str(g("買受人統編") or "").strip()
        fmt = str(g("格式代號") or "")[:2]; tcode = TAXCODE.get(g("課稅別") or "應稅", "1")
        problems = []
        if not re.fullmatch(r"[A-Z]{2}\d{8}", track): problems.append("發票字軌號碼須為2位英文加8位數字")
        if buyer and not C.check_company_id(buyer): problems.append(f"買受人統編「{buyer}」未通過邏輯檢查")
        if fmt not in ("31", "32", "35"): problems.append("格式代號須為31、32或35")
        if problems:
            notes.append((track, "銷項", "；".join(problems) + "，未入檔")); continue
        void = tcode == "F"
        out.append(dict(kind="銷項", no=track, date=d, fmt=fmt, buyer=buyer, seller=None, track=track, name=g("買受人名稱") or "",
                        amount=0 if void else int(g("銷售額(未稅)") or 0), tax=0 if void else int(g("營業稅額") or 0), taxcode=tcode,
                        deduct="", customs="" if void else str(g("通關方式註記") or "")[:1]))
    return out

def build_record(x, company, vat_tax_no, serial):
    void = x["taxcode"] == "F"
    buyer = (company if x["kind"] == "進項" else (x.get("buyer") or "")).ljust(8)
    seller = (x["seller"] if x["kind"] == "進項" else company).ljust(8)
    if void: buyer = " " * 8
    rec = (x["fmt"] + vat_tax_no + f"{serial:07d}" + C.roc_ym(x["date"]) + buyer + seller + x["track"][:2] + x["track"][2:]
           + ("0" * 12 if void else f"{x['amount']:012d}") + x["taxcode"] + ("0" * 10 if void else f"{x['tax']:010d}")
           + (x["deduct"] or " ") + " " * 5 + " " + " " + (x["customs"] or " "))
    assert len(rec) == 81, (len(rec), rec)
    return rec

def write_report(path, rows, notes, d_from, d_to):
    wb = Workbook(); hd = PatternFill("solid", fgColor="1F4E79"); th = Side(style="thin", color="BFBFBF"); bd = Border(left=th, right=th, top=th, bottom=th)
    def sheet(ws, title, cols, data):
        ws.title = title
        for i, c in enumerate(cols, 1):
            x = ws.cell(1, i, c); x.font = Font(name=F, bold=True, color="FFFFFF"); x.fill = hd; x.border = bd; x.alignment = Alignment(horizontal="center", wrap_text=True)
        for r, row in enumerate(data, 2):
            for i, v in enumerate(row, 1):
                x = ws.cell(r, i, v); x.font = Font(name=F, size=10); x.border = bd
                if isinstance(v, (int, float)): x.number_format = "#,##0"
        for i in range(1, len(cols) + 1): ws.column_dimensions[ws.cell(1, i).column_letter].width = 16
        return len(data)
    pur = [x for x in rows if x["kind"] == "進項"]; sal = [x for x in rows if x["kind"] == "銷項"]
    n1 = sheet(wb.active, "進項明細表", ["申請編號", "格式代號", "憑證種類", "憑證日期", "銷售人統編", "發票字軌號碼", "銷售額", "營業稅額", "課稅別", "扣抵代號"],
               [[x["no"], x["fmt"], x["cert"], x["date"].isoformat(), x["seller"], x["track"], x["amount"], x["tax"], x["taxcode"], x["deduct"]] for x in pur])
    wb.active.cell(n1 + 2, 1, "合計").font = Font(name=F, bold=True)
    wb.active.cell(n1 + 2, 7, sum(x["amount"] for x in pur)); wb.active.cell(n1 + 2, 8, sum(x["tax"] for x in pur))
    ws2 = wb.create_sheet(); n2 = sheet(ws2, "銷項明細表", ["發票字軌號碼", "格式代號", "開立日期", "買受人統編", "買受人名稱", "銷售額", "營業稅額", "課稅別"],
               [[x["track"], x["fmt"], x["date"].isoformat(), x["buyer"], x["name"], x["amount"], x["tax"], x["taxcode"]] for x in sal])
    ws2.cell(n2 + 2, 1, "合計").font = Font(name=F, bold=True); ws2.cell(n2 + 2, 6, sum(x["amount"] for x in sal)); ws2.cell(n2 + 2, 7, sum(x["tax"] for x in sal))
    ws3 = wb.create_sheet(); sheet(ws3, "未入檔與提醒", ["編號", "類別", "原因"], [list(n) for n in notes])
    ws4 = wb.create_sheet("摘要")
    lines = [f"申報期間：{d_from} 至 {d_to}", f"進項筆數：{len(pur)}　銷售額合計：{sum(x['amount'] for x in pur):,}　稅額合計：{sum(x['tax'] for x in pur):,}",
             f"銷項筆數：{len(sal)}　銷售額合計：{sum(x['amount'] for x in sal):,}　稅額合計：{sum(x['tax'] for x in sal):,}",
             "進銷項檔格式：營業稅電子資料申報繳稅作業要點附件五（每筆81字元）；匯入前請先以官方申報程式前端審核。"]
    for i, t in enumerate(lines, 1): ws4.cell(i, 1, t).font = Font(name=F, size=11)
    ws4.column_dimensions["A"].width = 110
    wb.save(path)

def main():
    ap = argparse.ArgumentParser(description="營業稅進銷項資料檔產生器")
    ap.add_argument("--xlsx", required=True); ap.add_argument("--from", dest="d_from", required=True); ap.add_argument("--to", dest="d_to", required=True)
    ap.add_argument("--out", required=True); ap.add_argument("--include-nondeductible", action="store_true"); ap.add_argument("--allow-placeholder", action="store_true")
    a = ap.parse_args()
    d_from, d_to = C.to_date(a.d_from), C.to_date(a.d_to)
    cfg = hrdata.load_config(a.xlsx); wb = hrdata.load_workbook(a.xlsx, data_only=True)
    bad = C.config_problems(cfg, ["vat_tax_no"])
    if not C.check_company_id(cfg.get("company_id", "")): sys.exit("申報設定的營利事業統一編號未通過邏輯檢查")
    if bad and not a.allow_placeholder: sys.exit("「申報設定」的營業人稅籍編號仍是空白或範例值，請先填寫（測試可加 --allow-placeholder）")
    if not re.fullmatch(r"\d{9}", cfg["vat_tax_no"]): sys.exit("營業人稅籍編號須為9碼數字")
    notes = []
    rows = read_purchases(wb, d_from, d_to, a.include_nondeductible, notes) + read_sales(wb, d_from, d_to, notes)
    if not rows: sys.exit("申報期間內沒有可入檔的進銷項資料")
    os.makedirs(a.out, exist_ok=True); company = cfg["company_id"]
    rows.sort(key=lambda x: (0 if x["kind"] == "進項" else 1, x["date"], x["no"]))
    txt = os.path.join(a.out, f"{company}.TXT")
    with open(txt, "w", encoding="ascii", newline="") as f:
        for i, x in enumerate(rows, 1): f.write(build_record(x, company, cfg["vat_tax_no"], i) + "\r\n")
    rep = os.path.join(a.out, f"營業稅進銷項明細_{d_from:%Y%m}-{d_to:%Y%m}.xlsx")
    write_report(rep, rows, notes, d_from, d_to)
    print(f"完成：{txt}（{len(rows)} 筆）\n明細表：{rep}")
    for n in notes: print("提醒：", *n)

if __name__ == "__main__":
    main()
