# 11-3 生成土地開發戰情 Excel 發布檔提示詞

> 🏆 **本單元核心技術**：**多維度地產戰情活頁簿（Multi-Sheet Real Estate Dashboard Workbook）自動渲染**  
> 告別雜亂簡陋的陽春 Excel，教導學員透過 Python `openpyxl` 將 AI 清洗與特徵衍生後的地政大數據，自動建構成包含「土地開發戰情儀表板、建商大宗獵地清單、容積移轉與公保地清單、實價登錄全量清洗資料」四大工作表的專業級發布檔！

---

## 💡 為什麼高階土地開發分析必須採用「四合一多工作表戰情架構」？

在不動產私募基金、建商土地開發部或估價師事務所中，一份合格的土地市場戰情報告絕不能只有一張塞滿 1,772 筆數字的平鋪表格，必須依循投資委員會高層與第一線土地開發人員的決策路徑進行「分層交付」：
1. **工作表 1【土地開發戰情儀表板】**：高層視角。包含頂部 4 大核心 KPI 統計卡、熱門地段 TOP 10 交易排行榜、土地使用分區總體分佈佔比表，以及土地開發部主管決策備忘錄（Executive Takeaways），3 秒掌握全市熱點。
2. **工作表 2【建商大宗獵地清單】**：投資精準視角。過濾出全筆移轉且實質坪數 ≧ 30 坪的大宗土地指標案（共 56 筆），排除散戶持分雜訊，供獵地團隊鎖定地主。
3. **工作表 3【容積移轉與公保地清單】**：法規籌碼視角。萃取使用分區為道路用地、公園、學校之交易（共 80 筆），提供高層評估爭取最高法定容積獎勵之買賣動向。
4. **工作表 4【實價登錄全量清洗資料】**：數據工程底座。完整收錄 1,772 筆資料與 12 個計算欄位（含持分比例、實質移轉坪數、策略分類標籤），支援後續樞紐分析與稽核查驗。

---

## 💬 一鍵執行 Python 生成 Excel 提示詞（傳送給 AI 執行）

```markdown
請擔任頂級商業儀表板設計美學的 Python 數據工程師，根據已完成清洗的新北市實價登錄 1,772 筆土地交易數據，撰寫並執行 openpyxl 腳本，產出包含四個專屬工作表的高質感發布檔《新北市土地交易實價登錄與開發戰情分析_已完成.xlsx》：

【設計規範】
1. 企業配色規範（大地產商務風）：
   - 主題深海藍：RGB(26, 54, 93) [#1A365D]（儀表板標題與表格首列）
   - 大地琥珀金：RGB(192, 86, 33) [#C05621]（大宗獵地工作表首列與強調框）
   - 翡翠公保綠：RGB(47, 133, 90) [#2F855A]（公保容積工作表首列）
   - KPI 卡片柔和底色：淡天藍 [#EBF8FF]、淡琥珀金 [#FEFCBF]、淡翡翠綠 [#F0FFF4]
   - 斑馬紋交錯底色：極淺灰 [#F7FAFC]
   - 格線：精緻細框線 [#D0D5DD]
2. 數值與儲存格格式化：
   - 面積與坪數統一設定為 `#,##0.00` 數字格式。
   - 百分比設定為 `0.0%`。
   - 所有工作表首列均凍結窗格（Freeze Panes）並啟用自動篩選（AutoFilter）。
   - 字型統一使用「微軟正黑體」或 Arial。

【四個工作表結構】
- Sheet 1【土地開發戰情儀表板】：
  - 頂部大器標題區、4 大 KPI 卡片、TOP 10 熱門地段排行榜、使用分區分佈表、高層決策備忘錄卡片。
- Sheet 2【建商大宗獵地清單】：
  - 篩選全筆移轉 ≧ 30 坪之 56 筆交易，欄位包含：編號、地段、地號、實質移轉坪數、原始面積、使用分區、移轉情形。
- Sheet 3【容積移轉與公保地清單】：
  - 篩選 80 筆道路/公園/機關公保地交易，欄位同上。
- Sheet 4【實價登錄全量清洗資料】：
  - 完整收錄 1,772 筆 12 欄完整數據集。

請直接執行 Python 腳本並產出高品質 `.xlsx` 活頁簿！
```

---

## 🐍 核心 Python 自動生成引擎源碼

以下為完整生產級可執行腳本，使用 `python3` 即可一鍵生成：

```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from collections import defaultdict, Counter

# 1. 讀取素材並執行特徵工程
wb_raw = openpyxl.load_workbook("素材_新北市實價登錄土地交易原始檔.xlsx", data_only=True)
sheet_raw = wb_raw["土地"]
raw_rows = list(sheet_raw.iter_rows(values_only=True))[2:]

cleaned_data = []
total_raw_area = 0.0
total_actual_m2 = 0.0
total_actual_ping = 0.0

sec_stats = defaultdict(lambda: {"count": 0, "m2": 0.0, "ping": 0.0, "zonings": Counter()})
zoning_stats = defaultdict(lambda: {"count": 0, "ping": 0.0})

dev_deals = []
public_facilities = []

for r in raw_rows:
    serial = str(r[0]) if r[0] else ""
    sec = str(r[1]) if r[1] else "未詳"
    raw_m2 = float(r[2]) if r[2] is not None else 0.0
    zoning_raw = str(r[3]) if r[3] is not None else "未知"
    den = float(r[4]) if r[4] not in (None, 0, "") else 1.0
    num = float(r[5]) if r[5] not in (None, "") else 1.0
    transfer_type = str(r[6]) if r[6] is not None else "未詳"
    parcel = str(r[7]) if r[7] is not None else ""
    
    ratio = (num / den) if den > 0 else 1.0
    if ratio > 1.0: 
        ratio = 1.0
    
    actual_m2 = raw_m2 * ratio
    actual_ping = actual_m2 * 0.3025
    
    total_raw_area += raw_m2
    total_actual_m2 += actual_m2
    total_actual_ping += actual_ping
    
    z_clean = zoning_raw.replace("都市：其他:", "").replace("都市：", "").replace("非都市：", "").strip()
    
    # 策略分類
    is_public = any(k in z_clean for k in ["道路", "公園", "機關", "學校", "公共設施"])
    is_large = (transfer_type == "全筆移轉" and actual_ping >= 30.0)
    
    if is_large:
        category = "大宗獵地/開發指標"
        dev_deals.append((serial, sec, parcel, actual_ping, raw_m2, z_clean, transfer_type))
    elif is_public:
        category = "容積移轉/公保地"
        public_facilities.append((serial, sec, parcel, actual_ping, raw_m2, z_clean, transfer_type))
    else:
        category = "一般持分/集合住宅"
        
    cleaned_data.append({
        "serial": serial, "section": sec, "parcel": parcel,
        "raw_m2": raw_m2, "zoning": z_clean,
        "den": den, "num": num, "ratio": ratio,
        "actual_m2": actual_m2, "actual_ping": actual_ping,
        "transfer_type": transfer_type, "category": category
    })
    
    sec_stats[sec]["count"] += 1
    sec_stats[sec]["m2"] += actual_m2
    sec_stats[sec]["ping"] += actual_ping
    sec_stats[sec]["zonings"][z_clean] += 1
    
    # 宏觀分區分類
    if any(k in z_clean for k in ["農業", "保護", "山坡", "農牧"]):
        macro_z = "農業/保護區"
    elif "住宅" in z_clean:
        macro_z = "住宅區"
    elif "商業" in z_clean:
        macro_z = "商業區"
    elif any(k in z_clean for k in ["工業", "產業"]):
        macro_z = "工業/產業專用"
    elif is_public:
        macro_z = "公共設施/道路"
    else:
        macro_z = "其他分區"
        
    zoning_stats[macro_z]["count"] += 1
    zoning_stats[macro_z]["ping"] += actual_ping

# 建立輸出活頁簿
wb_out = openpyxl.Workbook()

# 色彩與樣式定義
NAVY = "1A365D"
AMBER = "C05621"
GREEN = "2F855A"
BORDER_CLR = "D0D5DD"
ZEBRA_CLR = "F7FAFC"

font_title = Font(name="微軟正黑體", size=16, bold=True, color="1A365D")
font_sub = Font(name="微軟正黑體", size=10, color="4A5568")
font_sec_hdr = Font(name="微軟正黑體", size=12, bold=True, color="1A365D")
font_th = Font(name="微軟正黑體", size=10, bold=True, color="FFFFFF")
font_td = Font(name="微軟正黑體", size=10)
font_td_bold = Font(name="微軟正黑體", size=10, bold=True)
font_kpi_num = Font(name="Arial", size=18, bold=True, color="1A365D")
font_kpi_lbl = Font(name="微軟正黑體", size=9, color="4A5568")

fill_navy = PatternFill("solid", fgColor=NAVY)
fill_amber = PatternFill("solid", fgColor=AMBER)
fill_green = PatternFill("solid", fgColor=GREEN)
fill_zebra = PatternFill("solid", fgColor=ZEBRA_CLR)
fill_kpi1 = PatternFill("solid", fgColor="EBF8FF")
fill_kpi2 = PatternFill("solid", fgColor="FEFCBF")
fill_kpi3 = PatternFill("solid", fgColor="FEEBC8")
fill_kpi4 = PatternFill("solid", fgColor="F0FFF4")

thin_side = Side(style="thin", color=BORDER_CLR)
box_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

# ---------------- Sheet 1: 土地開發戰情儀表板 ----------------
ws1 = wb_out.active
ws1.title = "土地開發戰情儀表板"
ws1.views.sheetView[0].showGridLines = True

ws1["A1"] = "新北市不動產實價登錄土地交易戰情分析儀表板"
ws1["A1"].font = font_title
ws1["A2"] = "資料範圍：新北市最新土地交易實價登錄 | 樣本數：1,772 筆 | 分析單位：土地開發投資決策委員會"
ws1["A2"].font = font_sub

# 4 大 KPI 卡片
kpis = [
    ("B4:C6", "總交易件數", f"{len(cleaned_data):,} 筆", "新北全市移轉樣本數", fill_kpi1),
    ("E4:F6", "總實質移轉坪數", f"{total_actual_ping:,.1f} 坪", f"約 {total_actual_m2:,.0f} m²", fill_kpi2),
    ("H4:I6", "大宗獵地指標案", f"{len(dev_deals)} 筆", "全筆移轉 ≧ 30 坪", fill_kpi3),
    ("K4:L6", "公保/容積移轉籌碼", f"{len(public_facilities)} 筆", "道路/公園/機關用地", fill_kpi4),
]

for rng, title, val, sub, fill in kpis:
    start_col, start_row = rng.split(":")[0][0], int(rng.split(":")[0][1:])
    end_col, end_row = rng.split(":")[1][0], int(rng.split(":")[1][1:])
    ws1.merge_cells(rng)
    cell = ws1[f"{start_col}{start_row}"]
    cell.value = f"{title}\n{val}\n{sub}"
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.fill = fill
    for r in range(start_row, end_row + 1):
        for c in range(ord(start_col) - ord("A") + 1, ord(end_col) - ord("A") + 2):
            ws1.cell(r, c).border = box_border

# TOP 10 地段排行
ws1["A8"] = "📊 新北市土地交易熱門地段 TOP 10（依實質移轉坪數排序）"
ws1["A8"].font = font_sec_hdr

headers_top10 = ["排名", "地段名稱", "交易筆數", "實質移轉面積(m²)", "實質移轉坪數(坪)", "全市坪數佔比", "主要土地屬性"]
for col_idx, h in enumerate(headers_top10, start=1):
    c = ws1.cell(9, col_idx, h)
    c.font = font_th
    c.fill = fill_navy
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = box_border

sorted_secs = sorted(sec_stats.items(), key=lambda x: x[1]["ping"], reverse=True)[:10]
for idx, (s_name, s_info) in enumerate(sorted_secs, start=1):
    r_idx = 9 + idx
    top_z = s_info["zonings"].most_common(1)[0][0] if s_info["zonings"] else "其他"
    vals = [
        idx, s_name, s_info["count"], round(s_info["m2"], 2),
        round(s_info["ping"], 2), s_info["ping"] / total_actual_ping, top_z
    ]
    for c_idx, val in enumerate(vals, start=1):
        c = ws1.cell(r_idx, c_idx, val)
        c.font = font_td_bold if c_idx in (2, 5) else font_td
        c.border = box_border
        if c_idx == 1: c.alignment = Alignment(horizontal="center")
        elif c_idx == 3: 
            c.number_format = "#,##0"
            c.alignment = Alignment(horizontal="right")
        elif c_idx in (4, 5): 
            c.number_format = "#,##0.00"
            c.alignment = Alignment(horizontal="right")
        elif c_idx == 6: 
            c.number_format = "0.0%"
            c.alignment = Alignment(horizontal="right")

# 使用分區分佈概況
ws1["H8"] = "🏷️ 土地使用分區總體分佈概況"
ws1["H8"].font = font_sec_hdr

headers_zoning = ["使用分區大類", "交易筆數", "筆數佔比", "實質移轉坪數"]
for col_idx, h in enumerate(headers_zoning, start=8):
    c = ws1.cell(9, col_idx, h)
    c.font = font_th
    c.fill = fill_navy
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = box_border

sorted_zonings = sorted(zoning_stats.items(), key=lambda x: x[1]["ping"], reverse=True)
for idx, (z_name, z_info) in enumerate(sorted_zonings, start=1):
    r_idx = 9 + idx
    vals = [z_name, z_info["count"], z_info["count"] / len(cleaned_data), round(z_info["ping"], 2)]
    for c_idx, val in enumerate(vals, start=8):
        c = ws1.cell(r_idx, c_idx, val)
        c.font = font_td
        c.border = box_border
        if c_idx == 9: 
            c.number_format = "#,##0"
            c.alignment = Alignment(horizontal="right")
        elif c_idx == 10: 
            c.number_format = "0.0%"
            c.alignment = Alignment(horizontal="right")
        elif c_idx == 11: 
            c.number_format = "#,##0.00"
            c.alignment = Alignment(horizontal="right")

# 決策備忘錄卡片
ws1["A21"] = "📌 土地開發與投資決策委員會核心觀點摘要 (Land Banking Executive Takeaways)"
ws1["A21"].font = font_sec_hdr

takeaways = [
    "1. 【外圍大面積農保地為主要坪數支撐】：頂角段倒照湖小段、大坪段、萬西段雖僅數筆交易，但因屬全筆農保地買賣，合計移轉逾 9,400 坪，佔全市實質坪數近半，反映休閒農地或長線資產佈局熱絡。",
    "2. 【市區重劃區以大樓持分分割為主】：江翠段（114筆）、仁愛段（59筆）、五谷王段（53筆）交易最頻繁，平均每筆實質土地持分僅 1~3 坪，代表預售完工交屋潮，地價具高度抗跌指標性。",
    "3. 【容積移轉公保地持續浮現收購訊號】：本期出現 80 筆道路用地與公共設施保留地過戶（中原段、三和段等），顯示建商積極儲備容積移轉籌碼，有利於後續精華區建案爭取頂級容積獎勵。"
]
for idx, text in enumerate(takeaways, start=22):
    ws1.cell(idx, 1, text).font = font_td
    ws1.merge_cells(start_row=idx, start_column=1, end_row=idx, end_column=12)

# ---------------- Sheet 2: 建商大宗獵地清單 ----------------
ws2 = wb_out.create_sheet(title="建商大宗獵地清單")
ws2.views.sheetView[0].showGridLines = True
ws2["A1"] = "建商與投資機構大宗土地買賣指標清單 (全筆移轉 ≧ 30 坪)"
ws2["A1"].font = Font(name="微軟正黑體", size=14, bold=True, color=AMBER)
ws2["A2"] = f"共篩選出 {len(dev_deals)} 筆指標個案，依實質移轉坪數排序"
ws2["A2"].font = font_sub

headers_large = ["編號", "土地位置(地段)", "地號", "實質移轉坪數(坪)", "原始面積(m²)", "土地使用分區", "移轉情形"]
for c_idx, h in enumerate(headers_large, start=1):
    c = ws2.cell(4, c_idx, h)
    c.font = font_th
    c.fill = fill_amber
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = box_border

dev_deals.sort(key=lambda x: x[3], reverse=True)
for r_idx, deal in enumerate(dev_deals, start=5):
    for c_idx, val in enumerate(deal, start=1):
        c = ws2.cell(r_idx, c_idx, val)
        c.font = font_td_bold if c_idx == 4 else font_td
        c.border = box_border
        if r_idx % 2 == 0: c.fill = fill_zebra
        if c_idx in (4, 5): 
            c.number_format = "#,##0.00"
            c.alignment = Alignment(horizontal="right")
        elif c_idx in (1, 3, 7):
            c.alignment = Alignment(horizontal="center")

# ---------------- Sheet 3: 容積移轉與公保地清單 ----------------
ws3 = wb_out.create_sheet(title="容積移轉與公保地清單")
ws3.views.sheetView[0].showGridLines = True
ws3["A1"] = "容積移轉籌碼：公共設施保留地與道路用地清單"
ws3["A1"].font = Font(name="微軟正黑體", size=14, bold=True, color=GREEN)
ws3["A2"] = f"共篩選出 {len(public_facilities)} 筆道路/公保地交易明細"
ws3["A2"].font = font_sub

for c_idx, h in enumerate(headers_large, start=1):
    c = ws3.cell(4, c_idx, h)
    c.font = font_th
    c.fill = fill_green
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = box_border

public_facilities.sort(key=lambda x: x[3], reverse=True)
for r_idx, item in enumerate(public_facilities, start=5):
    for c_idx, val in enumerate(item, start=1):
        c = ws3.cell(r_idx, c_idx, val)
        c.font = font_td
        c.border = box_border
        if r_idx % 2 == 0: c.fill = fill_zebra
        if c_idx in (4, 5): 
            c.number_format = "#,##0.00"
            c.alignment = Alignment(horizontal="right")
        elif c_idx in (1, 3, 7):
            c.alignment = Alignment(horizontal="center")

# ---------------- Sheet 4: 實價登錄全量清洗資料 ----------------
ws4 = wb_out.create_sheet(title="實價登錄全量清洗資料")
ws4.views.sheetView[0].showGridLines = True
ws4["A1"] = f"新北市實價登錄土地交易完整清洗資料表 ({len(cleaned_data):,} 筆全量)"
ws4["A1"].font = Font(name="微軟正黑體", size=14, bold=True, color=NAVY)

headers_all = [
    "交易編號", "地段名稱", "地號", "土地移轉面積(m²)", "使用分區(清洗後)",
    "持分分母", "持分分子", "持分比例", "實質移轉面積(m²)", "實質移轉坪數(坪)",
    "移轉情形", "交易策略分類"
]
for c_idx, h in enumerate(headers_all, start=1):
    c = ws4.cell(3, c_idx, h)
    c.font = font_th
    c.fill = fill_navy
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = box_border

for r_idx, row in enumerate(cleaned_data, start=4):
    row_vals = [
        row["serial"], row["section"], row["parcel"], row["raw_m2"], row["zoning"],
        row["den"], row["num"], row["ratio"], row["actual_m2"], row["actual_ping"],
        row["transfer_type"], row["category"]
    ]
    for c_idx, val in enumerate(row_vals, start=1):
        c = ws4.cell(r_idx, c_idx, val)
        c.font = font_td
        c.border = box_border
        if r_idx % 2 == 1: c.fill = fill_zebra
        if c_idx in (4, 9, 10): 
            c.number_format = "#,##0.00"
            c.alignment = Alignment(horizontal="right")
        elif c_idx in (6, 7): 
            c.number_format = "#,##0"
            c.alignment = Alignment(horizontal="right")
        elif c_idx == 8: 
            c.number_format = "0.0000%"
            c.alignment = Alignment(horizontal="right")
        elif c_idx in (1, 3, 11, 12):
            c.alignment = Alignment(horizontal="center")

# 自動調整欄寬與凍結窗格
for ws in [ws1, ws2, ws3, ws4]:
    for col in ws.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = max(len(str(cell.value or '')) for cell in col)
        ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

ws1.freeze_panes = "A10"
ws2.freeze_panes = "A5"
ws3.freeze_panes = "A5"
ws4.freeze_panes = "A4"

wb_out.save("新北市土地交易實價登錄與開發戰情分析_已完成.xlsx")
print("✅ 出版級 Excel 戰情發布檔生成完成！")
```
