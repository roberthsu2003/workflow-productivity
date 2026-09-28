# 8-3 生成星嵐月報 PPT 發布檔提示詞

> 🏆 **本單元核心技術**：**`python-pptx` 16:9 品牌級商業資訊圖表自動排版**  
> 徹底擺脫「每個月初手動從 Excel 截圖、貼到 PPT、手拉表格大小、對齊文字」的低效痛苦，由 AI 直接驅動 Python 一鍵生成高階經營簡報發布檔！
> 
> *註：本案例示範採用虛擬企業名稱「**星嵐大飯店（StarShore Hotel）**」進行去識別化呈現。*

---

## 💡 為什麼自動化月報一定要學「python-pptx 商業圖表排版」？

在企業總經理室或營運幕僚的日常工作中，每個月向董事會或高階長官呈報的簡報有以下三大特點：
1. **版面高度標準化**：固定的 16:9 比例、品牌母片、色彩規範、頁首頁尾。
2. **圖表要求極高質感**：不能是 Excel 預設的陽春配色，必須具備大卡片（Card）、圓角矩形、品牌對比色與雙軸排版。
3. **數據每月更新、格式永遠不變**：如果每個月都手動複製貼上，不僅耗費整整兩天，還極容易貼錯月份或看漏數字。
👉 **解法**：讓 AI 撰寫 `python-pptx` 腳本，直接將 Excel 統計結果、原生圖表（Chart）、統計表格（Table）與商業洞見文字，一次性自動繪製成可編輯的 `.pptx` 簡報！

---

## 💬 一鍵執行 Python-pptx 套表提示詞（傳送給 AI 執行）

```markdown
請擔任資深 Python 商業視覺化專家，根據《2026 黑卡透過LINE客服訂房紀錄(樞紐分析).xlsx》與《2026 黑卡透過LINE客服訂房每月紀錄.xlsx》的核算數據，使用 python-pptx 撰寫並執行自動化腳本，產出 16:9 比例的正式商業月報簡報《星嵐大飯店_2026年1-8月黑卡訂房成效月報_已完成.pptx》：

【簡報全域設計規範】
1. 投影片比例：寬 13.333 英吋，高 7.5 英吋（標準 16:9 寬螢幕）。
2. 品牌標準色系：
   - 頂部與主標題深海藍：RGB(11, 37, 69) [#0B2545]
   - 品牌強調香檳金：RGB(197, 168, 128) [#C5A880]
   - 次級裝飾藍：RGB(19, 64, 116) [#134074]
   - 卡片背景底色：RGB(245, 247, 250) [#F5F7FA]
   - 警示與成長珊瑚紅：RGB(238, 108, 77) [#EE6C4D]
3. 頁首與頁尾：
   - 每頁頂部具備深海藍 Header 橫幅，左側標註「STARSHORE HOTEL 星嵐大飯店」，中央為簡報標題與副標，右側為品牌標語「More Than A Stay」。
   - 每頁底部具備深藍 Footer，標註「STARSHORE HOTEL 星嵐大飯店 | 美好，從星嵐開始」。

【三頁投影片內容架構】
- 第一頁【會員與館別偏好榜】：
  - 雙欄對比卡片：左欄「福福黑卡」、右欄「波波黑卡」。
  - 各欄上方具備「總訂房次數」、「總房晚數」、「總間數」三大白色 KPI 指標方塊。
  - 下方分別以金牌/銀牌/銅牌繪製「訂房次數 TOP 3」與「房晚數 TOP 3」之長條統計圖。
- 第二頁【量價趨勢與 YoY 成長雙軸看板】：
  - 圖表 1：2026 1-8月 Actual(A) 走勢折線圖（訂房間數 vs 營收萬元）。
  - 圖表 2：2025 vs 2026 累計訂房表現 YoY 比較長條圖（間數 +50.5%，營收 +56.7%）。
  - 底部具備 3 個指標卡片（累計間數 1,562 間、累計營收 890 萬、核心成長結論）。
- 第三頁【ADR 達成率與商業洞察】：
  - 圖表 1：2026 各月目標 ADR 達成率柱狀圖（整體 109%）。
  - 圖表 2：2026 vs 2025 各月 ADR 差異長條圖。
  - 底部左側：1~8月及平均值之完整數據對照表格（共 10 列 6 欄）。
  - 底部右側：香檳金外框之「💡 重點摘要與商業洞察 (Key Takeaways)」卡片，條列 4 點高階決策分析。

請直接執行 Python 腳本並產出高品質 `.pptx` 簡報檔案！
```

---

## 🐍 核心 Python-pptx 自動排版引擎源碼

以下為完整生產級可執行腳本，使用 `uv run --with python-pptx python3` 即可一鍵生成：

```python
import os
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

# 1. 初始化 16:9 簡報
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# 品牌色票 (星嵐大飯店 StarShore Hotel)
COLOR_NAVY_DARK = RGBColor(11, 37, 69)  # #0B2545 深海藍
COLOR_NAVY_LIGHT = RGBColor(19, 64, 116)  # #134074 次級藍
COLOR_GOLD = RGBColor(197, 168, 128)  # #C5A880 香檳金
COLOR_BG_CARD = RGBColor(245, 247, 250)  # #F5F7FA 淺灰底
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_CORAL = RGBColor(238, 108, 77)  # #EE6C4D 珊瑚粉紅
COLOR_TEXT_MAIN = RGBColor(29, 45, 68)  # #1D2D44 深灰黑
COLOR_MUTED = RGBColor(120, 130, 140)


def add_header(slide, title_text, subtitle_text='By Book Day (Actual A)'):
  # 頂部導航橫幅
  header_box = slide.shapes.add_shape(
      MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.1)
  )
  header_box.fill.solid()
  header_box.fill.fore_color.rgb = COLOR_NAVY_DARK
  header_box.line.color.rgb = COLOR_NAVY_DARK

  # 品牌名稱
  tx_brand = slide.shapes.add_textbox(
      Inches(0.5), Inches(0.15), Inches(2.5), Inches(0.8)
  )
  tf_brand = tx_brand.text_frame
  p0 = tf_brand.paragraphs[0]
  p0.text = 'STARSHORE HOTEL'
  p0.font.name = 'Arial'
  p0.font.size = Pt(11)
  p0.font.bold = True
  p0.font.color.rgb = COLOR_GOLD
  p1 = tf_brand.add_paragraph()
  p1.text = '星嵐大飯店'
  p1.font.name = '微軟正黑體'
  p1.font.size = Pt(13)
  p1.font.bold = True
  p1.font.color.rgb = COLOR_WHITE

  # 看板標題
  tx_title = slide.shapes.add_textbox(
      Inches(3.2), Inches(0.12), Inches(7.5), Inches(0.85)
  )
  tf_title = tx_title.text_frame
  p_t = tf_title.paragraphs[0]
  p_t.text = title_text
  p_t.font.name = '微軟正黑體'
  p_t.font.size = Pt(20)
  p_t.font.bold = True
  p_t.font.color.rgb = COLOR_WHITE
  if subtitle_text:
    p_sub = tf_title.add_paragraph()
    p_sub.text = subtitle_text
    p_sub.font.name = 'Arial'
    p_sub.font.size = Pt(12)
    p_sub.font.color.rgb = COLOR_GOLD

  # 右側 Slogan
  tx_slogan = slide.shapes.add_textbox(
      Inches(11.0), Inches(0.2), Inches(2.0), Inches(0.6)
  )
  p_s = tx_slogan.text_frame.paragraphs[0]
  p_s.text = 'More Than A Stay'
  p_s.font.name = 'Georgia'
  p_s.font.italic = True
  p_s.font.size = Pt(12)
  p_s.font.color.rgb = COLOR_GOLD
  p_s.alignment = PP_ALIGN.RIGHT


def add_footer(slide):
  footer_box = slide.shapes.add_shape(
      MSO_SHAPE.RECTANGLE,
      Inches(0),
      Inches(7.05),
      Inches(13.333),
      Inches(0.45),
  )
  footer_box.fill.solid()
  footer_box.fill.fore_color.rgb = COLOR_NAVY_DARK
  footer_box.line.color.rgb = COLOR_NAVY_DARK

  tx = slide.shapes.add_textbox(
      Inches(0.5), Inches(7.08), Inches(12.333), Inches(0.35)
  )
  p = tx.text_frame.paragraphs[0]
  p.text = 'STARSHORE HOTEL 星嵐大飯店  |  美好，從星嵐開始'
  p.font.name = '微軟正黑體'
  p.font.size = Pt(10)
  p.font.color.rgb = COLOR_WHITE


# ==================== SLIDE 1：會員與館別偏好榜 ====================
slide1 = prs.slides.add_slide(blank_layout)
add_header(
    slide1,
    '福福卡與波波卡 1-8月 各館訂房房晚數前三名',
    'VIP 會員偏好據點與累計訂房指標',
)
add_footer(slide1)

# 左卡：福福卡
bg_c1 = slide1.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6),
    Inches(1.35),
    Inches(5.8),
    Inches(5.4),
)
bg_c1.fill.solid()
bg_c1.fill.fore_color.rgb = COLOR_BG_CARD
bg_c1.line.color.rgb = RGBColor(220, 225, 230)

header_c1 = slide1.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.6),
    Inches(1.35),
    Inches(5.8),
    Inches(0.65),
)
header_c1.fill.solid()
header_c1.fill.fore_color.rgb = COLOR_NAVY_LIGHT
tx_c1 = slide1.shapes.add_textbox(
    Inches(0.8), Inches(1.4), Inches(5.4), Inches(0.5)
)
tx_c1.text_frame.paragraphs[0].text = '福福卡 1-8月 各館訂房房晚數前三名'
tx_c1.text_frame.paragraphs[0].font.name = '微軟正黑體'
tx_c1.text_frame.paragraphs[0].font.size = Pt(15)
tx_c1.text_frame.paragraphs[0].font.bold = True
tx_c1.text_frame.paragraphs[0].font.color.rgb = COLOR_WHITE

# KPI 指標區
badge_y = Inches(2.15)
badges1 = [('總訂房次數', '11 次'), ('總房晚數', '13 晚'), ('總間數', '12 間')]
for i, (label, val) in enumerate(badges1):
  bx = Inches(0.8 + i * 1.85)
  b_box = slide1.shapes.add_shape(
      MSO_SHAPE.ROUNDED_RECTANGLE, bx, badge_y, Inches(1.7), Inches(0.8)
  )
  b_box.fill.solid()
  b_box.fill.fore_color.rgb = COLOR_WHITE
  b_box.line.color.rgb = RGBColor(220, 225, 230)
  tx_b = slide1.shapes.add_textbox(
      bx, badge_y + Inches(0.05), Inches(1.7), Inches(0.7)
  )
  tf_b = tx_b.text_frame
  p0 = tf_b.paragraphs[0]
  p0.text = label
  p0.font.name = '微軟正黑體'
  p0.font.size = Pt(9.5)
  p0.font.color.rgb = COLOR_MUTED
  p0.alignment = PP_ALIGN.CENTER
  p1 = tf_b.add_paragraph()
  p1.text = val
  p1.font.name = 'Arial'
  p1.font.size = Pt(15)
  p1.font.bold = True
  p1.font.color.rgb = COLOR_NAVY_DARK
  p1.alignment = PP_ALIGN.CENTER

# 福福卡 TOP 3 排行
t_label1 = slide1.shapes.add_textbox(
    Inches(0.8), Inches(3.1), Inches(4.0), Inches(0.35)
)
t_label1.text_frame.paragraphs[0].text = '訂房次數 TOP 3 (單位: 次)'
t_label1.text_frame.paragraphs[0].font.name = '微軟正黑體'
t_label1.text_frame.paragraphs[0].font.size = Pt(12)
t_label1.text_frame.paragraphs[0].font.bold = True
t_label1.text_frame.paragraphs[0].font.color.rgb = COLOR_NAVY_DARK

top_rows1 = [
    ('🥇 1. HB 新竹湖濱館', 3),
    ('🥈 2. SA 蘇澳四季館', 3),
    ('🥉 3. HL 花蓮館', 2),
]
for idx, (hotel, count) in enumerate(top_rows1):
  ry = Inches(3.5 + idx * 0.45)
  tx_r = slide1.shapes.add_textbox(Inches(0.8), ry, Inches(2.6), Inches(0.35))
  tx_r.text_frame.paragraphs[0].text = hotel
  tx_r.text_frame.paragraphs[0].font.name = '微軟正黑體'
  tx_r.text_frame.paragraphs[0].font.size = Pt(11)
  tx_r.text_frame.paragraphs[0].font.bold = True
  bar_w = Inches(count * 0.6)
  bar = slide1.shapes.add_shape(
      MSO_SHAPE.RECTANGLE, Inches(3.4), ry + Inches(0.05), bar_w, Inches(0.28)
  )
  bar.fill.solid()
  bar.fill.fore_color.rgb = COLOR_NAVY_LIGHT
  tx_v = slide1.shapes.add_textbox(
      Inches(3.4) + bar_w + Inches(0.1), ry, Inches(0.8), Inches(0.35)
  )
  tx_v.text_frame.paragraphs[0].text = str(count)
  tx_v.text_frame.paragraphs[0].font.name = 'Arial'
  tx_v.text_frame.paragraphs[0].font.size = Pt(11)
  tx_v.text_frame.paragraphs[0].font.bold = True

# 右卡：波波卡
bg_c2 = slide1.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(6.8),
    Inches(1.35),
    Inches(5.8),
    Inches(5.4),
)
bg_c2.fill.solid()
bg_c2.fill.fore_color.rgb = COLOR_BG_CARD
bg_c2.line.color.rgb = RGBColor(220, 225, 230)

header_c2 = slide1.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(6.8),
    Inches(1.35),
    Inches(5.8),
    Inches(0.65),
)
header_c2.fill.solid()
header_c2.fill.fore_color.rgb = COLOR_NAVY_DARK
tx_c2 = slide1.shapes.add_textbox(
    Inches(7.0), Inches(1.4), Inches(5.4), Inches(0.5)
)
tx_c2.text_frame.paragraphs[0].text = '波波卡 1-8月 各館訂房房晚數前三名'
tx_c2.text_frame.paragraphs[0].font.name = '微軟正黑體'
tx_c2.text_frame.paragraphs[0].font.size = Pt(15)
tx_c2.text_frame.paragraphs[0].font.bold = True
tx_c2.text_frame.paragraphs[0].font.color.rgb = COLOR_WHITE

badges2 = [
    ('總訂房次數', '948 次'),
    ('總房晚數', '1,815 晚'),
    ('總間數', '1,156 間'),
]
for i, (label, val) in enumerate(badges2):
  bx = Inches(7.0 + i * 1.85)
  b_box = slide1.shapes.add_shape(
      MSO_SHAPE.ROUNDED_RECTANGLE, bx, badge_y, Inches(1.7), Inches(0.8)
  )
  b_box.fill.solid()
  b_box.fill.fore_color.rgb = COLOR_WHITE
  b_box.line.color.rgb = RGBColor(220, 225, 230)
  tx_b = slide1.shapes.add_textbox(
      bx, badge_y + Inches(0.05), Inches(1.7), Inches(0.7)
  )
  tf_b = tx_b.text_frame
  p0 = tf_b.paragraphs[0]
  p0.text = label
  p0.font.name = '微軟正黑體'
  p0.font.size = Pt(9.5)
  p0.font.color.rgb = COLOR_MUTED
  p0.alignment = PP_ALIGN.CENTER
  p1 = tf_b.add_paragraph()
  p1.text = val
  p1.font.name = 'Arial'
  p1.font.size = Pt(15)
  p1.font.bold = True
  p1.font.color.rgb = COLOR_NAVY_DARK
  p1.alignment = PP_ALIGN.CENTER

# 波波卡 TOP 3 排行
top_rows3 = [
    ('🥇 1. TN 台南館', 278),
    ('🥈 2. SA 蘇澳四季館', 177),
    ('🥉 3. HB 新竹湖濱館', 152),
]
for idx, (hotel, count) in enumerate(top_rows3):
  ry = Inches(3.5 + idx * 0.45)
  tx_r = slide1.shapes.add_textbox(Inches(7.0), ry, Inches(2.6), Inches(0.35))
  tx_r.text_frame.paragraphs[0].text = hotel
  tx_r.text_frame.paragraphs[0].font.name = '微軟正黑體'
  tx_r.text_frame.paragraphs[0].font.size = Pt(11)
  tx_r.text_frame.paragraphs[0].font.bold = True
  bar_w = Inches((count / 300) * 1.8)
  bar = slide1.shapes.add_shape(
      MSO_SHAPE.RECTANGLE, Inches(9.6), ry + Inches(0.05), bar_w, Inches(0.28)
  )
  bar.fill.solid()
  bar.fill.fore_color.rgb = COLOR_NAVY_LIGHT
  tx_v = slide1.shapes.add_textbox(
      Inches(9.6) + bar_w + Inches(0.1), ry, Inches(0.8), Inches(0.35)
  )
  tx_v.text_frame.paragraphs[0].text = str(count)
  tx_v.text_frame.paragraphs[0].font.name = 'Arial'
  tx_v.text_frame.paragraphs[0].font.size = Pt(11)
  tx_v.text_frame.paragraphs[0].font.bold = True

# ==================== SLIDE 2：量價雙軸走勢與 YoY ====================
slide2 = prs.slides.add_slide(blank_layout)
add_header(
    slide2,
    '2026年 1-8月 訂房成效分析 By Book Day (Actual A)',
    '間數走勢與營業收入雙軸成長指標',
)
add_footer(slide2)

# 圖表 1：雙軸折線圖
chart_data_1 = CategoryChartData()
chart_data_1.categories = [
    '1月',
    '2月',
    '3月',
    '4月',
    '5月',
    '6月',
    '7月',
    '8月',
]
chart_data_1.add_series(
    '訂房間數 (間)', (256, 184, 212, 144, 127, 121, 240, 278)
)
chart_data_1.add_series(
    '營業收入 (萬元)', (150, 91, 125, 85, 75, 70, 140, 163)
)
chart_1 = slide2.shapes.add_chart(
    XL_CHART_TYPE.LINE_MARKERS,
    Inches(0.8),
    Inches(1.9),
    Inches(6.1),
    Inches(3.5),
    chart_data_1,
).chart
chart_1.has_legend = True
chart_1.legend.position = XL_LEGEND_POSITION.TOP

# 圖表 2：YoY 比較圖
chart_data_2 = CategoryChartData()
chart_data_2.categories = ['訂房間數 (間)', '營業收入 (萬元)']
chart_data_2.add_series('2025年', (1038, 568))
chart_data_2.add_series('2026年', (1562, 890))
chart_2 = slide2.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED,
    Inches(7.5),
    Inches(1.9),
    Inches(5.0),
    Inches(3.5),
    chart_data_2,
).chart
chart_2.has_legend = True
chart_2.legend.position = XL_LEGEND_POSITION.TOP

# 底部 3 個 KPI 卡片
kpis = [
    ('1-8月 累計訂房間數', '1,562 間', '年增 +50.5% (1,038 ➔ 1,562)'),
    ('1-8月 累計營業收入', 'NT$ 890 萬', '年增 +56.7% (568萬 ➔ 890萬)'),
    ('營運趨勢核心結論', '量價齊揚 成長強勁', '暑假 7~8 月達最高峰，營收突破 303 萬元'),
]
for i, (title, main_val, sub) in enumerate(kpis):
  kx = Inches(0.6 + i * 4.1)
  k_box = slide2.shapes.add_shape(
      MSO_SHAPE.ROUNDED_RECTANGLE,
      kx,
      Inches(5.8),
      Inches(3.9),
      Inches(1.05),
  )
  k_box.fill.solid()
  k_box.fill.fore_color.rgb = COLOR_BG_CARD
  k_box.line.color.rgb = RGBColor(220, 225, 230)
  tx_k = slide2.shapes.add_textbox(
      kx + Inches(0.15), Inches(5.85), Inches(3.6), Inches(0.95)
  )
  tf_k = tx_k.text_frame
  p0 = tf_k.paragraphs[0]
  p0.text = title
  p0.font.name = '微軟正黑體'
  p0.font.size = Pt(11)
  p0.font.color.rgb = COLOR_MUTED
  p1 = tf_k.add_paragraph()
  p1.text = main_val
  p1.font.name = 'Arial'
  p1.font.size = Pt(17)
  p1.font.bold = True
  p1.font.color.rgb = COLOR_CORAL if i == 1 else COLOR_NAVY_DARK
  p2 = tf_k.add_paragraph()
  p2.text = sub
  p2.font.name = '微軟正黑體'
  p2.font.size = Pt(9.5)
  p2.font.color.rgb = COLOR_NAVY_LIGHT

# ==================== SLIDE 3：ADR 達成與商業洞察 ====================
slide3 = prs.slides.add_slide(blank_layout)
add_header(
    slide3,
    '2026 目標 ADR 達成率與 2025 ADR 差異分析',
    'By Book Day (1-8月平均房價定價策略效益評估)',
)
add_footer(slide3)

# 表格與 Key Takeaways
table_shape = slide3.shapes.add_table(
    10, 6, Inches(0.6), Inches(4.2), Inches(6.0), Inches(2.65)
)
table = table_shape.table
table_headers = ['月份', '2026目標', '2026實際', '達成率', '2025實際', 'YoY差異%']
table_data = [
    ['1月', '5,395', '5,862', '109%', '5,388', '+8.8%'],
    ['2月', '5,235', '4,954', '95%', '4,930', '+0.5%'],
    ['3月', '5,153', '5,890', '114%', '6,428', '-8.4%'],
    ['4月', '5,809', '5,901', '102%', '4,970', '+18.7%'],
    ['5月', '5,222', '5,894', '113%', '4,710', '+25.1%'],
    ['6月', '5,192', '5,780', '111%', '6,273', '-7.9%'],
    ['7月', '5,383', '5,845', '109%', '5,472', '+6.8%'],
    ['8月', '5,384', '5,860', '109%', '5,395', '+8.6%'],
    ['平均', '5,347', '5,836', '109%', '5,570', '+4.8%'],
]
for col_idx, h in enumerate(table_headers):
  cell = table.cell(0, col_idx)
  cell.text = h
  cell.fill.solid()
  cell.fill.fore_color.rgb = COLOR_NAVY_DARK
  p = cell.text_frame.paragraphs[0]
  p.font.name = '微軟正黑體'
  p.font.size = Pt(9.5)
  p.font.bold = True
  p.font.color.rgb = COLOR_WHITE
  p.alignment = PP_ALIGN.CENTER

for r_idx, row in enumerate(table_data):
  for c_idx, val in enumerate(row):
    cell = table.cell(r_idx + 1, c_idx)
    cell.text = val
    cell.fill.solid()
    cell.fill.fore_color.rgb = (
        RGBColor(230, 235, 245)
        if r_idx == 8
        else (RGBColor(248, 249, 250) if r_idx % 2 == 1 else COLOR_WHITE)
    )
    p = cell.text_frame.paragraphs[0]
    p.font.name = 'Arial' if c_idx > 0 else '微軟正黑體'
    p.font.size = Pt(9)
    p.font.bold = r_idx == 8 or c_idx == 3
    p.alignment = PP_ALIGN.CENTER

# Key Takeaways Card
card_tk = slide3.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(6.8),
    Inches(4.2),
    Inches(5.9),
    Inches(2.65),
)
card_tk.fill.solid()
card_tk.fill.fore_color.rgb = RGBColor(254, 250, 246)
card_tk.line.color.rgb = COLOR_GOLD

tx_tk_h = slide3.shapes.add_textbox(
    Inches(7.0), Inches(4.3), Inches(5.5), Inches(0.35)
)
tx_tk_h.text_frame.paragraphs[0].text = (
    '💡 重點摘要與商業洞察 (Key Takeaways)'
)
tx_tk_h.text_frame.paragraphs[0].font.name = '微軟正黑體'
tx_tk_h.text_frame.paragraphs[0].font.size = Pt(13)
tx_tk_h.text_frame.paragraphs[0].font.bold = True
tx_tk_h.text_frame.paragraphs[0].font.color.rgb = COLOR_NAVY_DARK

insights = [
    (
        '• 2026 年 1-8 月整體目標 ADR 達成率為 109%，8'
        ' 個月份中有 7 個月份超越預算目標。'
    ),
    (
        '• 與 2025 年相比，平均 ADR 成長 4.8%（+266 元），呈現「量增價揚」的正向定價走勢。'
    ),
    (
        '• 以月份成長動能來看，5 月成長幅度最高（+25.1%），4'
        ' 月次之（+18.7%），顯示春季專案奏效。'
    ),
    (
        '• 3 月與 6 月較 2025 年呈現微幅負成長（-8.4% 及'
        ' -7.9%），主要受去年同期高基期影響，非需求減退。'
    ),
]
tx_tk_body = slide3.shapes.add_textbox(
    Inches(7.0), Inches(4.9), Inches(5.5), Inches(1.85)
)
tf_body = tx_tk_body.text_frame
tf_body.word_wrap = True
for idx, ins in enumerate(insights):
  p = tf_body.paragraphs[0] if idx == 0 else tf_body.add_paragraph()
  p.text = ins
  p.font.name = '微軟正黑體'
  p.font.size = Pt(9.5)
  p.font.color.rgb = COLOR_TEXT_MAIN

# 儲存投影片
out_path = '星嵐大飯店_2026年1-8月黑卡訂房成效月報_已完成.pptx'
prs.save(out_path)
print(f'✅ 成功產出 16:9 商業簡報發布檔：{out_path}')
```
