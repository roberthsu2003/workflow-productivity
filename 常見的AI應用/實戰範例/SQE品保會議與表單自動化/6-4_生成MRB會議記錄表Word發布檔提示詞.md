# 步驟 4：生成 FR-MR09 會議記錄表 Word 發布檔提示詞（Python 自動化排版）

> 🛠️ **執行方式**：  
> 當人類 SQE 完成「步驟 3」審批並回覆「`確認無誤，繼續生成 Word 表單`」後，將本指令交付給具備代碼執行能力之 AI（如 ChatGPT Advanced Data Analysis、Claude Artifacts 或本機 Python 環境），即可一鍵產出 100% 吻合製造業驗收標準的 Word 表單！

---

## 📋 交付給 AI 之發布生成提示詞

```markdown
請根據人類剛剛審批通過之「MRB 品質決策核對卡片」資料，使用 Python `python-docx` 套件，自動生成一份高水準、符合製造業標準之《FR-MR09 會議記錄表.docx》檔案。

【版面與排版嚴格規範】：
1. 頁面邊界：標準邊界（上下左右各 2.54 cm / 1 吋）。
2. 表頭基本資訊：
   - 文件大標題：「會議記錄表」（置中、粗體、18pt、深藍色 #1A365D）。
   - 會議基本欄位：日期（2026年08月13日）、會議主旨（M260802 藍機右殼 黏結凸輪 黏結下齒板會議討論）、時間、主持人、地點、記錄人。
   - 跨部門會簽簽名欄：包含技術長、行銷處、業務課、品保處、生產處、製造課、生管課、資材處、總經理、標準課、倉管課之網格會簽簽核框。
3. 議題內容區塊（結構化條列）：
   - 每個議題需包含清晰的小節標題與縮排內文：
     - 議題 1：藍機右殼 L93XXAR1 外觀泛黃問題（現況、主要問題、處置結論）
     - 議題 2：黏結凸輪 92XX079 角度公差及組裝功能（現況、品質風險、判斷依據、對照驗證方案表格、處置結論）
     - 議題 3：黏結下齒板(加工) 93XXAO2 需 80pcs 試作及熱處理/噴砂製程驗證（現況、重要品質要求、處置結論）
4. 待辦事項追蹤表（Action Items）：
   - 建立高質感三欄/四欄表格（序號、任務內容、負責人/單位、預計完成時間）。
   - 表頭以深藍底色（#2B4C7E）搭配白色粗體字，數據列加入斑馬紋底色（#F7FAFC）。
5. 表尾：
   - 標記公司名稱「台積電股份有限公司 PANTECH INTERNATIONAL INC.」（或去識別化名稱）。
   - 表單編號：「FR-MR09 v.01」。
```

---

## 🐍 核心自動產檔 Python 腳本（免安裝環境直接可跑）

```python
import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_mrb_docx(output_path="FR-MR09_會議記錄表_已完成.docx"):
    doc = Document()
    
    # 邊界設定
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # 標題
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run("會 議 記 錄 表")
    title_run.font.name = "微軟正黑體"
    title_run.font.size = Pt(20)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    # 基本資訊表
    info_table = doc.add_table(rows=3, cols=4)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        [("會議日期", "2026年08月13日"), ("會議主旨", "藍機右殼/黏結凸輪/下齒板異常審查 (M260802)")],
        [("開會時間", "15:30 ~ 16:06"), ("開會地點", "泛源會議室")],
        [("會 主 持", "謝華賢 (技術長)"), ("記    錄", "楊子賢 (資材處SQE)")]
    ]
    for r_idx, row in enumerate(info_data):
        for c_pair_idx, (k, v) in enumerate(row):
            c1 = info_table.cell(r_idx, c_pair_idx*2)
            c2 = info_table.cell(r_idx, c_pair_idx*2 + 1)
            c1.text = k
            c2.text = v
            set_cell_background(c1, "EDF2F7")
            c1.paragraphs[0].runs[0].font.bold = True
            c1.paragraphs[0].runs[0].font.name = "微軟正黑體"
            c2.paragraphs[0].runs[0].font.name = "微軟正黑體"
            set_cell_margins(c1, top=80, bottom=80, left=100, right=100)
            set_cell_margins(c2, top=80, bottom=80, left=100, right=100)

    doc.add_paragraph() # 空行

    # 會簽欄
    sign_table = doc.add_table(rows=2, cols=11)
    sign_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    dept_names = ["總經理", "技術長", "品保處", "資材處", "生產處", "製造課", "生管課", "業務課", "行銷處", "標準課", "倉管課"]
    for i, name in enumerate(dept_names):
        hdr_cell = sign_table.cell(0, i)
        hdr_cell.text = name
        set_cell_background(hdr_cell, "E2E8F0")
        p = hdr_cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if p.runs:
            p.runs[0].font.size = Pt(8.5)
            p.runs[0].font.bold = True
        body_cell = sign_table.cell(1, i)
        body_cell.text = "\n\n" # 簽核留白

    doc.add_paragraph()

    # 議題標題函式
    def add_topic(num, title, items):
        h = doc.add_paragraph()
        r = h.add_run(f"議題 {num}：{title}")
        r.font.name = "微軟正黑體"
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x2B, 0x4C, 0x7E)
        
        for subtitle, text in items:
            p = doc.add_paragraph()
            sub_r = p.add_run(f"【{subtitle}】\n")
            sub_r.font.name = "微軟正黑體"
            sub_r.font.bold = True
            sub_r.font.size = Pt(10.5)
            sub_r.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
            
            txt_r = p.add_run(text)
            txt_r.font.name = "微軟正黑體"
            txt_r.font.size = Pt(10)
            p.paragraph_format.left_indent = Inches(0.2)

    # 議題 1
    add_topic(1, "藍機右殼 L93XXAR1 外觀泛黃問題討論", [
        ("現況描述", "部分庫存零件存在外觀顏色差異與長期存放狀況。其中約 3pcs 貼面板結構外觀泛黃；部分零件外觀白色斑點符合客戶既有同意接收標準。確認不能使用之 13pcs 藍機右殼先行管制。"),
        ("品質與營運影響", "不良品扣除後將直接影響原承諾之成套配套物料，若後續維修備品需求增加，恐引發庫存缺料風險。"),
        ("MRB 處置結論", "已確認泛黃之 13pcs 即刻實施隔離管制，全數納入保留倉；其餘合規庫存加速出貨，並持續監控庫存存放狀況。")
    ])

    # 議題 2
    add_topic(2, "黏結凸輪 92XX079 角度公差放寬之組裝功能風險", [
        ("主要問題與風險", "原公差為 19° ±0.5°，加工廠商申請放寬至 ±1°。品保評估目前在 ±0.5° 下組裝已有調整困難，若放寬將直接改變開關啟動行程、大幅增加組裝工時，甚至造成售後更換困難。"),
        ("驗證方案與對照條件", "暫不直接放寬公差！技術長核定先以 19.5°~20° 角度製作 5pcs 試作件進行對照驗證，比較組裝時間、調整次數、啟動行程與不良率。"),
        ("MRB 處置結論", "小批量對照組裝若無顯著差異再評估放寬；若仍影響功能則維持原規格並責令供應商（承化）自費改善；改善未果即啟動備援供應商（竹翔）開模。")
    ])

    # 議題 3
    add_topic(3, "黏結下齒板(加工) 93XXAO2 需 80pcs 試作及全製程驗證", [
        ("現況與製程轉移", "前期 3pcs 樣品已於鑫將驗證初步合格。原熱處理廠（國泰）有黑痕缺陷，現將熱處理製程轉由鑫將執行。"),
        ("關鍵品質要求", "熱處理對齒板尺寸形狀影響甚鉅，不可單看熱處理外觀，必須完整走過「加工 ➔ 熱處理 ➔ 噴砂 ➔ 電鍍 ➔ 最終尺寸與功能檢驗」全製程。"),
        ("MRB 處置結論", "核定 80pcs 試作案繼續執行。3pcs 僅為初步驗證，待 80pcs 全製程驗證確認穩定合格後，方能正式作為量產製程依據。")
    ])

    doc.add_page_break()

    # 待辦事項表格
    ai_h = doc.add_paragraph()
    ai_r = ai_h.add_run("三、 待辦追蹤事項清單 (Action Items)")
    ai_r.font.name = "微軟正黑體"
    ai_r.font.size = Pt(13)
    ai_r.font.bold = True
    ai_r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    ai_table = doc.add_table(rows=7, cols=4)
    ai_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["序號", "任務內容說明", "負責單位／人員", "預計完成時間"]
    for i, h in enumerate(headers):
        c = ai_table.cell(0, i)
        c.text = h
        set_cell_background(c, "2B4C7E")
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.runs[0]
        run.font.name = "微軟正黑體"
        run.font.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    actions = [
        ("1", "確認長期庫存零件是否有變色、老化或其他品質風險", "品保處／倉庫", "2026 年底前"),
        ("2", "完成 80pcs 下齒板試作，並完整走完全製程", "資材處／供應商／二廠加工組", "依專案排程"),
        ("3", "完成 80pcs 熱處理、噴砂後之尺寸及外觀檢驗報告", "品保處", "80pcs 完成後"),
        ("4", "針對凸輪 19.5°-20° 角度條件進行 5pcs 小批量對照組裝", "承化／資材處／品保處", "儘速安排"),
        ("5", "量測角度變化對開關啟動行程之實際影響數據", "生產處／品保處／研發處", "小批量試驗後"),
        ("6", "若承化改善仍無法達標，啟動第二供應商（竹翔）開模方案", "資材處／研發處", "第一階段評估後")
    ]

    for row_idx, data in enumerate(actions, start=1):
        bg = "F7FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(data):
            c = ai_table.cell(row_idx, col_idx)
            c.text = text
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            p = c.paragraphs[0]
            if col_idx in (0, 2, 3):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if p.runs:
                p.runs[0].font.name = "微軟正黑體"
                p.runs[0].font.size = Pt(9.5)

    # 頁尾資訊
    footer_p = doc.add_paragraph()
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    f_run = footer_p.add_run("\n\n台積電股份有限公司 PANTECH INTERNATIONAL INC.   |   表單編號：FR-MR09 v.01")
    f_run.font.name = "微軟正黑體"
    f_run.font.size = Pt(8.5)
    f_run.font.color.rgb = RGBColor(0x71, 0x80, 0x96)

    doc.save(output_path)
    print(f"✅ 成功產出：{output_path}")

if __name__ == "__main__":
    create_mrb_docx()
```
