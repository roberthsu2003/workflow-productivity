# 步驟三：生成施工查驗照片紀錄 Word 發布檔提示詞

> 💡 **教學情境**：在完成結構化 Markdown 審核確認無誤後，進入工程品管文件發布階段。本步驟指導具備 Code Interpreter（進階資料分析）能力的 AI 平台（如 ChatGPT Plus/Team、Claude 或 Antigravity），使用 Python `python-docx` 函式庫，自動生成版型、配色、線條與圖片嵌入 100% 精準對齊公共工程驗收標準的 Word（`.docx`）查驗報告！  
> 🛠️ **適用平台**：ChatGPT（進階資料分析模式）、Claude（支援檔案生成之模式）或支援 Python 代碼執行的 AI 代理。

---

## 🎯 核心轉換工作流

```mermaid
flowchart LR
    A["<b>結構化 Markdown 紀錄</b><br/>施工查驗照片紀錄.md"] --> B["<b>4-3 Word 發布提示詞</b><br/>（樣式規格 ＋ 自動產檔指示）"]
    B --> C["<b>AI 背景執行 Python</b><br/>#274B5F 藍灰表頭 ＋ 斑馬底色 ＋ 固定圖片寬高"]
    C --> D["🏆 <b>驗收級 DOCX 成品</b><br/>施工查驗照片紀錄.docx"]
```

---

## 📋 提示詞複製專區

請將下方內容直接複製貼入剛才完成白板辨識與 Markdown 檢核的 AI 對話框中：

```markdown
## Role

你是一位專精於公共工程品質管制文件與 Word 自動化排版的 Python 資料工程專家，擅長使用 `python-docx` 產出排版專業、字型與版面完全符合政府公共工程驗收標準的專業報告。

## Task

請根據剛才核對確認無誤的「施工查驗照片紀錄.md」內容以及現場提供的 3 張照片：
- `LINE_ALBUM_427前池三頂板下層筋綁紮查驗_260427_1.jpg`
- `LINE_ALBUM_427前池三頂板下層筋綁紮查驗_260427_9.jpg`
- `LINE_ALBUM_427前池三頂板下層筋綁紮查驗_260427_15.jpg`

編寫並執行 Python 程式，直接產出一份可供直接下載的驗收級 Word 文件（檔名：`115.04.27前池第3單元頂版下層筋綁紮查驗_施工查驗照片紀錄.docx`）。

## 排版與樣式規格要求

這份 Word 文件必須嚴格遵循以下規格，以確保格式與業主驗收標準一模一樣：

1. **頁面尺寸與邊距**：
   - 紙張設定為 Letter 直式（寬 612 pt、高 792 pt）。
   - 四周邊界：上邊距 48.95 pt、下邊距 44.65 pt、左邊距 51.85 pt、右邊距 51.85 pt。

2. **標題與段落**：
   - 主標題：「前池第三單元頂板下層筋綁紮施工查驗紀錄」，`Arial Unicode MS`（或標楷體）22 pt 粗體黑色，水平置中。
   - 副標題：「工程施工查驗照片彙整」，10.5 pt 灰色（`#66737A`），水平置中。
   - 內文引言：「本文件彙整本次施工後鋼筋綁紮查驗資料與現場照片，供查驗紀錄及後續檢核使用。」，10.5 pt 黑色。

3. **專業表格設計（基本資料表、查驗資料表）**：
   - 表格整體水平置中，外框與內框格線均為細灰色實線（`#D9D9D9`，sz=6）。
   - 寬度設定：第一欄（標題欄）寬度固定 93.6 pt；第二欄（內容欄）寬度固定 406.8 pt。
   - 儲存格內邊距（Padding）：上下各 110 dxa、左右各 130 dxa，文字垂直置中。
   - 配色規範：
     * 第一欄（標題）：底色深青藍色 `#274B5F`，文字為白色粗體 10 pt。
     * 第二欄（內容）：採交替斑馬紋底色（白色 `#FFFFFF` 與極淺灰 `#F5F7F8`），文字為黑色 10 pt。

4. **照片嵌入與排版規範**：
   - 每一張照片前均需配置「現場照片 X」大標題（15 pt 粗體黑色）與灰色副標題「查驗日期 115.4.27 ｜ 前池（第三單元）頂板（下層）」（9.5 pt 灰色 `#66737A`）。
   - 照片置中嵌入，固定寬度 482.4 pt（約 17.02 cm）、高度 362.0 pt（約 12.77 cm），確保原始比例不拉伸失真，單頁排版完整。
   - 照片下方置中顯示檔案名稱標註（8.5 pt 灰色 `#66737A`）。

請直接執行 Python 程式產出 `.docx` 檔案，並在回覆中提供該檔案的直接下載連結！
```

---

## 💻 附錄：AI 執行之 Python 核心程式碼參考

若需要在本地或伺服器端批次執行，AI 於後台執行的核心生成邏輯如下：

```python
import os
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def build_inspection_docx(output_path, img_dir):
    doc = docx.Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Pt(612.0), Pt(792.0)
    sec.top_margin, sec.bottom_margin = Pt(48.95), Pt(44.65)
    sec.left_margin, sec.right_margin = Pt(51.85), Pt(51.85)

    # 標題
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("前池第三單元頂板下層筋綁紮施工查驗紀錄")
    r_title.font.name = "Arial Unicode MS"
    r_title.font.size = Pt(22.0)
    r_title.font.bold = True

    # 基本資料表與查驗資料表（包含 #274B5F 深藍灰底色與 #D9D9D9 邊框）
    # ...（照片依序以 482.4 pt x 362.0 pt 置中嵌入）
    doc.save(output_path)
```
