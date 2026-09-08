#!/usr/bin/env python3
"""產生 chatGPT_codex 講義用的 Office 格式示範檔（xlsx / pptx / docx / png）。

需要在有 openpyxl / python-pptx / python-docx / pillow 的環境執行：
    python3 -m venv .venv && .venv/bin/pip install openpyxl python-pptx python-docx pillow
    .venv/bin/python tools/generate_office_files.py

與 generate_sample_data.py 一樣，刻意植入教學用的資料問題。
"""
from pathlib import Path
import csv, random

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from docx import Document
from docx.shared import Pt as DocPt
from PIL import Image, ImageDraw

random.seed(20260908)
BASE = Path(__file__).resolve().parent.parent

HEAD_FILL = PatternFill("solid", fgColor="4A3428")
HEAD_FONT = Font(color="FFFFFF", bold=True)
WARN_FILL = PatternFill("solid", fgColor="FFF3CD")


def autosize(ws):
    for col in ws.columns:
        w = max((len(str(c.value)) for c in col if c.value is not None), default=8)
        ws.column_dimensions[get_column_letter(col[0].column)].width = min(w + 4, 42)


def style_header(ws):
    for c in ws[1]:
        c.fill, c.font = HEAD_FILL, HEAD_FONT
        c.alignment = Alignment(horizontal="center", vertical="center")
    ws.freeze_panes = "A2"


# ── 1. 任務追蹤表（Sheets skill 練習：刻意髒資料）──────────────────
def task_tracker():
    p = BASE / "Skills/GWorkspace/01_Sheets_Task_Tracker/sample_files"
    p.mkdir(parents=True, exist_ok=True)
    wb = Workbook(); ws = wb.active; ws.title = "原始待辦清單"
    ws.append(["編號", "部門", "任務", "負責人", "期限", "狀態", "優先度", "備註"])
    rows = [
        [1, "營運處", "東區颱風應變 SOP 修訂", "鄭以樂", "2026/09/14", "進行中", "高", ""],
        [2, "營運處", "花蓮中繼站選址評估", "鄭以樂", "2026-09-30", "未開始", "High", "需搭配站長行程"],
        [3, "資訊處", "WMS 移轉補正", "吳課長", "已完成", "完成", "高", "9/2 完成"],
        [4, "客服中心", "鼎和貿易賠償案", "周慧玲", "盡快", "進行中", "非常高", "已逾期兩週"],
        [5, "業務處", "麥禾冷藏合約確認", "林維倫", "2026/9/11", "待確認", "中", "待法務回覆"],
        [6, "營運處", "冷鏈車輛採購", "吳建志", "", "未開始", "", "數量未定"],
        [7, "客服中心", "8月客訴分析報告", "周慧玲", "2026-09-10", "已完成", "中", ""],
        [8, "資訊處", "Node.js 22 升級", "王冠廷", "2026-09-20", "進行中", "低", ""],
        [9, "營運處", "南區雙11彈性人力", "蔡文豪", "2026/10/15", "未開始", "高", ""],
        [10, "業務處", "元昇食品冷鏈報價", "林維倫", "2026-09-08", "逾期", "中", "客戶已催兩次"],
        [11, "營運處", "月檢討會簡報", "陳柏宇", "2026-09-08", "進行中", "高", ""],
        [12, "資訊處", "配送查詢API效能", "林思妤", "2026-09-15", "已完成", "高", "P95 3.2s→0.48s"],
    ]
    for r in rows:
        ws.append(r)
    for i in (4, 7):  # 期限格式異常的列
        for c in ws[i + 1]:
            c.fill = WARN_FILL
    style_header(ws); autosize(ws)

    ws2 = wb.create_sheet("欄位說明")
    ws2.append(["欄位", "應有格式", "本表的實際狀況"])
    for r in [
        ["期限", "YYYY-MM-DD", "混用 YYYY/MM/DD、YYYY-MM-DD，另有「已完成」「盡快」「空白」"],
        ["優先度", "高／中／低", "混入英文 High、以及「非常高」這個未定義值"],
        ["狀態", "未開始／進行中／已完成", "另出現「待確認」「逾期」兩個未定義值"],
    ]:
        ws2.append(r)
    style_header(ws2); autosize(ws2)
    f = p / "2026年度各部門待辦事項原始清單.xlsx"
    wb.save(f); print(f"  {f.relative_to(BASE)}")


# ── 2. 業務成果簡報（Presentations skill 練習）─────────────────────
def report_pptx():
    p = BASE / "Skills/GWorkspace/02_Presentations_Report/sample_files"
    p.mkdir(parents=True, exist_ok=True)
    prs = Presentation()
    BROWN, GOLD = RGBColor(0x4A, 0x34, 0x28), RGBColor(0xC8, 0x91, 0x2F)

    s = prs.slides.add_slide(prs.slide_layouts[0])
    s.shapes.title.text = "潮汐物流 2026 上半年營運回顧"
    s.placeholders[1].text = "營運處｜2026-09-08｜內部使用"
    s.shapes.title.text_frame.paragraphs[0].runs[0].font.color.rgb = BROWN

    slides = [
        ("整體表現", ["全公司準時率 96.4%（目標 95.0%）",
                      "配送單量 92.1 萬件，達成年度目標 49.8%",
                      "平均配送時數 29.6 小時（目標 ≤30.0）",
                      "客訴率 0.31%（目標 ≤0.35%）"]),
        ("各區狀況", ["北區：準時率 97.6%，穩定，維持現況",
                      "中區：準時率 96.3%（僅 5 個月資料，6 月缺漏）",
                      "南區：準時率 96.5%，檔期彈性人力已備妥",
                      "東區：準時率 94.1%，未達 92% 以外之常態目標"]),
        ("待處理事項", ["東區颱風應變 SOP 尚未修訂完成",
                        "冷鏈車輛量能不足，影響麥禾與元昇兩案",
                        "鼎和貿易賠償案逾期兩週未結"]),
        ("下半年重點", ["東進計畫：花蓮中繼站選址",
                        "冷鏈 2.0：車輛採購與合約確認",
                        "雙 11 檔期人力調度（10/15 前定案）"]),
    ]
    for title, bullets in slides:
        sl = prs.slides.add_slide(prs.slide_layouts[1])
        sl.shapes.title.text = title
        sl.shapes.title.text_frame.paragraphs[0].runs[0].font.color.rgb = BROWN
        tf = sl.placeholders[1].text_frame
        tf.text = bullets[0]
        for b in bullets[1:]:
            tf.add_paragraph().text = b
        for para in tf.paragraphs:
            for run in para.runs:
                run.font.size = Pt(18)

    sl = prs.slides.add_slide(prs.slide_layouts[5])
    sl.shapes.title.text = "資料說明"
    tb = sl.shapes.add_textbox(Inches(0.8), Inches(2), Inches(8.4), Inches(3)).text_frame
    tb.text = "⚠ 中區 2026-06 資料缺漏（WMS 系統移轉期間未落帳）"
    for line in ["中區各項平均值以 5 個月為計算基礎，非 6 個月。",
                 "缺漏資料未以 0 或推估值填補。",
                 "跨區比較時請注意計算基礎不同。"]:
        tb.add_paragraph().text = line
    for para in tb.paragraphs:
        for run in para.runs:
            run.font.size = Pt(16); run.font.color.rgb = GOLD
    f = p / "2026_上半年營運回顧_示範簡報.pptx"
    prs.save(f); print(f"  {f.relative_to(BASE)}")


# ── 3. 會議手記 docx（Docs skill 練習）─────────────────────────────
def meeting_docx():
    p = BASE / "Skills/GWorkspace/03_Docs_Meeting_Notes/sample_files"
    p.mkdir(parents=True, exist_ok=True)
    d = Document()
    d.add_heading("2026 Q3 營運檢討會 會議手記", 0)
    d.add_paragraph("時間：2026-09-08（二）09:30–11:00　地點：會議室 A")
    d.add_paragraph("※ 這是與會者現場手寫的凌亂筆記，未整理。")
    d.add_heading("現場筆記", level=1)
    for t in [
        "上半年準時率 96.4 達標了 但東區還是拖後腿 94.1",
        "東區以樂說颱風那次影響很大 扣掉的話有 96 左右 → 這個數字要再確認",
        "中區六月沒資料 雅琪說是 WMS 移轉 吳課長確認補不回來",
        "→ 決議：報表一律標資料缺漏 不填 0 （營運長拍板）",
        "冷鏈車不夠 建志提的 六台 麥禾+元昇會爆",
        "維倫說採購在跑 但沒給時間 → 這個沒結論",
        "營運長問十月五號來不來得及 維倫說應該可以 → 柏宇當場說要講清楚",
        "→ 柏宇：北中區確定 南區禮拜四回覆",
        "鼎和賠償案 慧玲說法務還在看 已經逾期兩週了",
        "營運長臉色不好看 說這個要優先處理",
        "→ 決議：慧玲本週五前給結案時程（營運長）",
        "雙11 文豪說十月十五前定案彈性人力 沒問題",
        "下次會議 10/13 同時間",
    ]:
        d.add_paragraph(t, style="List Bullet")
    d.add_heading("待整理", level=1)
    d.add_paragraph("※ 以下是我沒聽清楚或不確定的部分：")
    for t in ["東區扣除颱風後的準時率到底是多少？要跟以樂確認",
              "冷鏈車採購的預算金額好像有提到但我沒記到",
              "營運長對鼎和案講的那句「不要再有下次」是指什麼？"]:
        d.add_paragraph(t, style="List Bullet")
    for para in d.paragraphs:
        for run in para.runs:
            if run.font.size is None:
                run.font.size = DocPt(11)
    f = p / "2026_Q3營運檢討會_會議手記.docx"
    d.save(f); print(f"  {f.relative_to(BASE)}")


# ── 4. 採購核准單 docx + 料件明細 csv（Gmail skill 練習）───────────
def purchase_docs():
    p = BASE / "Skills/GWorkspace/04_Gmail_Draft_Dispatch/sample_files"
    p.mkdir(parents=True, exist_ok=True)
    d = Document()
    d.add_heading("潮汐物流股份有限公司　採購核准單", 0)
    d.add_paragraph("單號：PO-2026-0915　　申請日期：2026-09-05")
    t = d.add_table(rows=0, cols=2); t.style = "Table Grid"
    for k, v in [("申請單位", "營運處 車隊管理部"), ("申請人", "吳建志"),
                 ("採購項目", "冷鏈配送耗材（詳見料件明細表）"),
                 ("預估金額", "新臺幣 486,300 元整"),
                 ("需求日期", "2026-09-30 前到貨"),
                 ("供應商", "冷研設備股份有限公司"),
                 ("採購事由", "因應麥禾烘焙與元昇食品冷鏈配送案，現有耗材庫存不足")]:
        row = t.add_row().cells
        row[0].text = k; row[1].text = v
    d.add_paragraph()
    d.add_heading("簽核", level=1)
    st = d.add_table(rows=2, cols=4); st.style = "Table Grid"
    for i, h in enumerate(["申請人", "部門主管", "營運長", "總經理"]):
        st.rows[0].cells[i].text = h
        st.rows[1].cells[i].text = "（已簽）" if i < 3 else "（已簽）2026-09-08"
    d.add_paragraph()
    d.add_paragraph("※ 本單已完成三級簽核，請採購承辦依料件明細表向供應商下單。")
    f = p / "採購核准單_PO-2026-0915.docx"
    d.save(f); print(f"  {f.relative_to(BASE)}")

    fc = p / "採購料件明細表_PO-2026-0915.csv"
    with fc.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["項次", "料號", "品名", "規格", "數量", "單位", "單價", "小計", "備註"])
        items = [
            [1, "BX-1003", "冷鏈保溫箱", "60L 雙層真空", 200, "個", 1250, 250000, "急件"],
            [2, "CL-4001", "乾冰", "食品級", 800, "kg", 85, 68000, "分批交貨"],
            [3, "TP-2002", "易碎品標籤", "防水 100張/捲", 400, "捲", 145, 58000, ""],
            [4, "TH-6001", "溫度記錄器", "藍牙回傳", 60, "台", 1580, 94800, "客戶要求溫控報告"],
            [5, "BG-5001", "防撞氣泡袋", "大號 50入/包", 300, "包", 51, 15300, ""],
        ]
        for it in items:
            w.writerow(it)
        w.writerow(["", "", "", "", "", "", "合計", sum(i[7] for i in items), ""])
    print(f"  {fc.relative_to(BASE)}")


# ── 5. 業務增長趨勢圖 png（圖片輸入練習）──────────────────────────
def trend_png():
    p = BASE / "Skills/GWorkspace/02_Presentations_Report/sample_files"
    p.mkdir(parents=True, exist_ok=True)
    W, H, M = 1200, 640, 90
    img = Image.new("RGB", (W, H), (247, 241, 230))
    dr = ImageDraw.Draw(img)
    dr.text((M, 30), "TideFlow Logistics - Monthly Volume 2026 H1 (thousand parcels)",
            fill=(74, 52, 40))
    data = [148, 152, 161, 158, 166, 172]
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    lo, hi = 130, 185
    pw, ph = W - 2 * M, H - 2 * M - 40
    dr.line([(M, H - M), (W - M, H - M)], fill=(74, 52, 40), width=2)
    dr.line([(M, M + 40), (M, H - M)], fill=(74, 52, 40), width=2)
    for g in range(130, 190, 10):
        y = H - M - (g - lo) / (hi - lo) * ph
        dr.line([(M - 5, y), (W - M, y)], fill=(232, 226, 214), width=1)
        dr.text((M - 45, y - 6), str(g), fill=(74, 52, 40))
    pts = []
    for i, v in enumerate(data):
        x = M + pw * (i + 0.5) / len(data)
        y = H - M - (v - lo) / (hi - lo) * ph
        pts.append((x, y))
        dr.text((x - 12, H - M + 12), labels[i], fill=(74, 52, 40))
        dr.text((x - 14, y - 24), str(v), fill=(200, 145, 47))
    dr.line(pts, fill=(200, 145, 47), width=4)
    for x, y in pts:
        dr.ellipse([x - 6, y - 6, x + 6, y + 6], fill=(200, 145, 47))
    dr.text((M, H - 40), "Source: TideFlow WMS. Note: figures are fictional teaching data.",
            fill=(120, 110, 100))
    f = p / "2026_上半年單量趨勢圖.png"
    img.save(f); print(f"  {f.relative_to(BASE)}")


# ── 6. 創投財務模型 xlsx（Investing 練習：刻意含問題）───────────────
def startup_financials():
    p = BASE / "Skills/Investing/02_Investment_Banking_DD/sample_files"
    p.mkdir(parents=True, exist_ok=True)
    wb = Workbook(); ws = wb.active; ws.title = "損益表"
    ws.append(["項目（新臺幣千元）", "2023", "2024", "2025", "2026預估"])
    for r in [
        ["營業收入", 42800, 98500, 186200, 420000],
        ["營業成本", 38500, 84300, 152400, 310000],
        ["毛利", 4300, 14200, 33800, 110000],
        ["研發費用", 18600, 32400, 48900, 62000],
        ["行銷費用", 22400, 51800, 96300, 118000],
        ["管理費用", 8900, 14600, 22100, 28000],
        ["營業利益", -45600, -84600, -133500, -98000],
        ["業外收支", 320, 850, 1200, 1500],
        ["稅前淨利", -45280, -83750, -132300, -96500],
    ]:
        ws.append(r)
    style_header(ws); autosize(ws)

    ws2 = wb.create_sheet("關鍵指標")
    ws2.append(["指標", "2023", "2024", "2025", "2026預估"])
    for r in [
        ["營收成長率", "", "130.1%", "89.0%", "125.6%"],
        ["毛利率", "10.0%", "14.4%", "18.2%", "26.2%"],
        ["行銷費用佔營收", "52.3%", "52.6%", "51.7%", "28.1%"],
        ["月燒錢率（千元）", 3773, 6979, 11025, 8042],
        ["帳上現金（期末）", 68000, 142000, 96000, ""],
        ["現金可用月數", 18.0, 20.3, 8.7, ""],
        ["客戶數", 1240, 3180, 6420, 15000],
        ["單客獲取成本 CAC", 18.1, 16.3, 15.0, 9.2],
        ["單客年貢獻 ARPU", 34.5, 31.0, 29.0, 28.0],
    ]:
        ws2.append(r)
    for i in (2, 4, 9):
        for c in ws2[i + 1]:
            c.fill = WARN_FILL
    style_header(ws2); autosize(ws2)

    ws3 = wb.create_sheet("假設說明")
    ws3.append(["項目", "管理層說法"])
    for r in [
        ["2026 營收成長", "新增三個通路夥伴，預估帶來 40% 增量"],
        ["2026 毛利率提升", "規模效應與供應商議價"],
        ["2026 行銷費用下降", "口碑成長，降低付費獲客依賴"],
        ["2026 CAC 下降", "同上"],
        ["現金", "2026 Q1 完成 B 輪募資（進行中）"],
    ]:
        ws3.append(r)
    style_header(ws3); autosize(ws3)
    f = p / "受評標的_財務摘要_2023-2026E.xlsx"
    wb.save(f); print(f"  {f.relative_to(BASE)}")


if __name__ == "__main__":
    print("產生 Office 格式示範檔：")
    task_tracker(); report_pptx(); trend_png()
    meeting_docx(); purchase_docs(); startup_financials()
    print("\n完成。")
