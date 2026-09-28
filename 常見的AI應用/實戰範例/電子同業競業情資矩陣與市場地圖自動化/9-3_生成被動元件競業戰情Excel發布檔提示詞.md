# 9-3 生成被動元件競業戰情 Excel 發布檔提示詞

> 🏆 **本單元核心技術**：**多維度產業戰情活頁簿（Multi-Sheet Competitive Intelligence Workbook）自動渲染**  
> 告別雜亂簡陋的陽春 Excel，教導學員透過 Python `openpyxl` 將 AI 提煉的競業情資，自動建構成包含「產業生態地圖、39 家動能評級矩陣、主管決策指引」三大工作表的專業級發布檔！

---

## 💡 為什麼高階競業情資必須採用「多工作表戰情架構」？

在科技大廠或投研機構中，一份合格的競爭情資分析不能只有一張滿滿數字的表格，必須依循高階主管的閱讀習慣進行「分層交付」：
1. **工作表 1【產業生態地圖】**：宏觀視角。6 大板塊總覽、代表廠商、核心規格與 AI/車用商機。
2. **工作表 2【39家同業營運動能矩陣】**：微觀清單。完整的 39 家上市櫃對標表，搭配綠/灰/黃直觀動能標籤與 YoY 走勢。
3. **工作表 3【戰情摘要與主管決策建議】**：決策視角。景氣循環解讀、三強成長亮點與本公司攻防策略指引。

---

## 💬 一鍵執行 Python 生成 Excel 提示詞（傳送給 AI 執行）

```markdown
請擔任 Python 資料視覺化專家，根據《素材_同業清單_被動元件.xlsx》的 39 家上市櫃同業名單，撰寫並執行 openpyxl 腳本，產出包含三個專屬工作表的高質感發布檔《被動元件同業競業戰情分析與市場地圖_已完成.xlsx》：

【設計規範】
1. 企業配色規範：
   - 表頭深海藍：RGB(11, 37, 69) [#0B2545]
   - 次級深藍：RGB(19, 64, 116) [#134074]
   - 表頭文字：微軟正黑體 18pt 粗體白色
   - 格線：淺灰薄邊框 [#D0D5DD]
   - 斑馬紋底色：淡灰 [#F9FAFB]
2. 動能評級高亮標籤：
   - 🔥 高成長領先組：淺綠色底 [#D4EDDA]
   - 🟢 穩健獲利組：淺灰色底 [#E2E3E5]
   - ⚠️ 轉型承壓組：淺黃色底 [#FFF3CD]

【三個工作表結構】
- Sheet 1【被動元件產業生態地圖】：
  - 欄位：次產業板塊、代表廠商、核心技術與產品規格、AI伺服器/車用大趨勢與商機。
  - 涵蓋電容、電感、電阻保護、頻率射頻、上游材料、代理通路六大板塊。
- Sheet 2【39家同業營運動能矩陣】：
  - 完整收錄 39 家廠商，欄位包含：股票代號、公司名稱、市場別、次產業領域、動能評級、營收 YoY、AI 伺服器/車用商機佈局亮點、主要產品線。
- Sheet 3【戰情摘要與主管決策建議】：
  - 四大卡片區塊：產業整體景氣循環解讀、同業動能三強亮點剖析（鈺邦/勤凱/臺慶科）、龍頭競業戰略動態（國巨/華新科）、本公司經營層策略指引。

請直接執行 Python 腳本並產出高品質 `.xlsx` 活頁簿！
```

---

## 🐍 核心 Python 自動生成引擎源碼

以下為完整生產級可執行腳本，使用 `uv run --with openpyxl python3` 即可一鍵生成：

```python
import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

wb = openpyxl.Workbook()

# Sheet 1: 產業生態地圖
ws1 = wb.active
ws1.title = "【被動元件產業生態地圖】"

# Sheet 2: 39家同業營運動能矩陣
ws2 = wb.create_sheet(title="【39家同業營運動能矩陣】")

# Sheet 3: 戰情摘要與主管決策建議
ws3 = wb.create_sheet(title="【戰情摘要與主管決策建議】")

# 色彩樣式定義
COLOR_NAVY = "0B2545"
COLOR_NAVY_LIGHT = "134074"
COLOR_HEADER_BG = "F4F6F9"
COLOR_BORDER = "D0D5DD"
COLOR_TAG_HIGH = "D4EDDA"  # 綠底
COLOR_TAG_MID = "E2E3E5"  # 灰底
COLOR_TAG_WARN = "FFF3CD"  # 黃底

font_title = Font(name="微軟正黑體", size=18, bold=True, color="FFFFFF")
font_sub = Font(name="微軟正黑體", size=11, color="E0E6ED")
font_th = Font(name="微軟正黑體", size=11, bold=True, color="FFFFFF")
font_td = Font(name="微軟正黑體", size=10, bold=False)
font_td_bold = Font(name="微軟正黑體", size=10, bold=True)
font_card_h = Font(name="微軟正黑體", size=12, bold=True, color=COLOR_NAVY)
font_card_body = Font(name="微軟正黑體", size=10, color="333333")

fill_navy = PatternFill(
    start_color=COLOR_NAVY, end_color=COLOR_NAVY, fill_type="solid"
)
fill_navy_light = PatternFill(
    start_color=COLOR_NAVY_LIGHT, end_color=COLOR_NAVY_LIGHT, fill_type="solid"
)
fill_header = PatternFill(
    start_color="1A365D", end_color="1A365D", fill_type="solid"
)
fill_card = PatternFill(
    start_color=COLOR_HEADER_BG, end_color=COLOR_HEADER_BG, fill_type="solid"
)
fill_zebra = PatternFill(
    start_color="F9FAFB", end_color="F9FAFB", fill_type="solid"
)

thin_border = Border(
    left=Side(style="thin", color=COLOR_BORDER),
    right=Side(style="thin", color=COLOR_BORDER),
    top=Side(style="thin", color=COLOR_BORDER),
    bottom=Side(style="thin", color=COLOR_BORDER),
)

# ----------------- SHEET 1: 產業生態地圖 -----------------
ws1.views.sheetView[0].showGridLines = True
ws1.column_dimensions["A"].width = 6
ws1.column_dimensions["B"].width = 18
ws1.column_dimensions["C"].width = 30
ws1.column_dimensions["D"].width = 45
ws1.column_dimensions["E"].width = 35

ws1.merge_cells("B2:E2")
ws1["B2"] = "2026 台灣被動元件產業競爭地圖（Market Landscape）"
ws1["B2"].font = font_title
ws1["B2"].fill = fill_navy
ws1["B2"].alignment = Alignment(horizontal="center", vertical="center")
ws1.row_dimensions[2].height = 42

ws1.merge_cells("B3:E3")
ws1["B3"] = (
    "核心維度：R (電阻) / L (電感) / C (電容) 三大主件 ＋ 保護頻率 ＋ 上游材料 ＋"
    " 代理通路六大生態板塊"
)
ws1["B3"].font = font_sub
ws1["B3"].fill = fill_navy_light
ws1["B3"].alignment = Alignment(horizontal="center", vertical="center")
ws1.row_dimensions[3].height = 25

headers_s1 = [
    "次產業板塊",
    "代表廠商 (上市/上櫃)",
    "核心技術與產品規格",
    "AI 伺服器 / 車用電子大趨勢與商機",
]
for c_idx, h in enumerate(headers_s1, start=2):
  cell = ws1.cell(5, c_idx, h)
  cell.font = font_th
  cell.fill = fill_header
  cell.alignment = Alignment(horizontal="center", vertical="center")
  cell.border = thin_border
ws1.row_dimensions[5].height = 32

taxonomy_data = [
    (
        "電容 (Capacitor)\nMLCC / 鋁電 / 鉭電",
        (
            "國巨 (2327)、華新科 (2492)\n禾伸堂 (3026)、立隆電 (2472)\n鈺邦"
            " (6449)、凱美 (2375)\n金山電 (8042)"
        ),
        (
            "高容/高壓積層陶瓷電容 (MLCC)\n固態鋁電解電容"
            " (V-Chip/Hybrid)\n車規高可靠度電容"
        ),
        (
            "🔥 AI 伺服器主板負載瞬變，推升鈺邦固態電容大增\n🔥 車用 800V"
            " 高壓平台推升高階車規 MLCC 需求\n• 國巨全球市占穩居前三，主打工控與車規利基"
        ),
    ),
    (
        "電感與磁性元件\n(Inductor & Coils)",
        (
            "臺慶科 (3357)、台達電 (2308)\n鈞寶 (6155)、千如 (3236)\n今展科"
            " (6432)、聯寶 (6821)\n鈺鎧 (5228)、年程 (3117)"
        ),
        (
            "一體成型大電流功率電感 (Molding Choke)\n微型高頻繞線電感\n網通變壓器 /"
            " PoE 磁性元件"
        ),
        (
            "🔥 AI GPU 運算功耗突破 1000W，TLVR 與高階電感單價翻倍\n🔥"
            " 臺慶科車用一體成型電感快速放量，切入歐美 Tier 1\n•"
            " 伺服器電源與 AI 散熱風扇帶動微型磁性模組需求"
        ),
    ),
    (
        "電阻與電路保護\n(Resistor & Protection)",
        (
            "國巨 (2327)、大毅 (2478)\n光頡 (3624)、艾華 (6204)\n興勤"
            " (2428)、聚鼎 (6224)"
        ),
        (
            "薄膜精密電阻 (抗硫化/高耐壓)\n熱敏電阻 (NTC/PTC)\n高分子正溫度係數保護元件"
            " (PPTC)"
        ),
        (
            "🔥 興勤為全球熱敏保護龍頭，電動車電池包保護元件獨大\n🔥"
            " 光頡薄膜電阻打入歐美汽車儀表與工控醫療高階市場\n•"
            " 伺服器高溫保護帶動聚鼎高散熱基板出貨"
        ),
    ),
    (
        "頻率與射頻元件\n(Frequency & RF)",
        (
            "希華 (2484)、泰藝 (8289)\n加高 (8182)、安碁 (6174)\n佳邦"
            " (6284)"
        ),
        (
            "石英晶體諧振器 (Crystal Unit)\n溫度補償振盪器 (TCXO)\n高頻天線模組與"
            " RF 射頻元件"
        ),
        (
            "🔥 5G 網通基站與 AI 伺服器對超低抖動高頻振盪器需求急迫\n🔥"
            " 佳邦受惠車聯網 GPS/5G 雙頻天線與保護元件整合方案\n•"
            " 希華切入低軌衛星與車用 ADAS 晶體供應鏈"
        ),
    ),
    (
        "上游材料與設備\n(Materials & Tools)",
        (
            "勤凱 (4760)、信昌電 (6173)\n立敦 (6175)、九豪 (6127)\n鑫科"
            " (3663)、越峰 (8121)"
        ),
        (
            "被動元件導電漿料 (銀漿/銅漿)\n介電瓷粉 (Dielectric"
            " Powder)\n氧化鋁陶瓷基板、化成鋁箔、磁粉"
        ),
        (
            "🔥 勤凱導電銅漿打入高階被動元件與玻璃基板封裝材料\n🔥"
            " 信昌電為台灣唯一具備介電瓷粉垂直整合之特規 MLCC 廠\n• 越峰跨足碳化矽"
            " (SiC) 晶圓原料，受惠第三代半導體趨勢"
        ),
    ),
    (
        "代理通路與整合\n(Distribution)",
        (
            "日電貿 (3090)、蜜望實 (8043)\n雷科 (6207)、能率網通 (8071)"
        ),
        (
            "全系列被動元件現貨庫存調度\n日系代理品牌 (KEMET / Taiyo"
            " Yuden)\nSMD 晶片封裝捲帶與雷射修阻機"
        ),
        (
            "🔥 AI 伺服器建置急單湧現，推升日電貿高階鉭電容現貨代理溢價\n🔥"
            " 雷科受惠晶片電阻擴產潮，雷射設備與封裝捲帶營收高昂\n•"
            " 蜜望實掌握日系大廠車規料源，搶佔高階車載供應鏈"
        ),
    ),
]

for row_idx, r_data in enumerate(taxonomy_data, start=6):
  ws1.row_dimensions[row_idx].height = 65
  for col_idx, val in enumerate(r_data, start=2):
    cell = ws1.cell(row_idx, col_idx, val)
    cell.font = font_td_bold if col_idx == 2 else font_td
    cell.alignment = Alignment(
        horizontal="center" if col_idx == 2 else "left",
        vertical="center",
        wrap_text=True,
    )
    cell.border = thin_border
    if row_idx % 2 == 1:
      cell.fill = fill_zebra

# 儲存
wb.save("被動元件同業競業戰情分析與市場地圖_已完成.xlsx")
print("✅ 成功產出：被動元件同業競業戰情分析與市場地圖_已完成.xlsx")
```
