# 📊 PowerPoint (`.pptx`) 進階對齊：16:9 簡報母片佔位符注入與防溢出

> 📖 **課前原理導讀（附講解圖）**：不清楚什麼是簡報佔位符樣版、Run 層級替換或不知道要裝哪些套件？  
> 👉 **[請先看這裡：佔位符樣版與核心 Python 套件介紹](./00_佔位符樣版與核心套件介紹.md)**

鎖定 16:9 投影片色塊與卡片邊界，利用 `python-pptx` 在 **Run 層級**精準替換 `{{佔位符}}`，同時處理長文字自動折行（`word_wrap`）與動態縮字防溢出。

---

## 📦 下載本單元實作檔案

| 檔案類型 | 檔案名稱 | 說明 |
| :--- | :--- | :--- |
| **一鍵打包** | **[📥 pptx_PowerPoint進階對齊實作包.zip](./pptx_PowerPoint進階對齊實作包.zip)** | 包含下列所有原始範本、資料檔與示範成果 |
| 原始檔案 | [簡報範本_原始檔.pptx](./簡報範本_原始檔.pptx) | 含真實範例文字的 16:9 專案週報簡報 |
| 佔位符樣版 | [簡報範本_佔位符樣版.pptx](./簡報範本_佔位符樣版.pptx) | 已預留 `{{專案名稱}}`、`{{KPI1_數字}}` 等 13 個佔位符 |
| 測試資料 | [presentation_data.md](./presentation_data.md) | 含「標準版」與「長文字壓力測試」兩組結構化資料 |
| 示範成果 1 | [簡報_示範成果_1_智慧客服專案.pptx](./簡報_示範成果_1_智慧客服專案.pptx) | 標準資料套用結果（KPI 置中、字型色彩完全保留） |
| 示範成果 2 | [簡報_示範成果_2_ERP升級(長文字防溢出測試).pptx](./簡報_示範成果_2_ERP升級(長文字防溢出測試).pptx) | 長標題與長條列自動縮字折行，不爆出卡片框 |

---

## 🛠️ 實戰兩階段：先做佔位符樣版，再寫對齊腳本

### 階段 0：將原始簡報轉為「佔位符樣版」（若你只有舊簡報）

> 💡 **先別急著複製！請先學會提示詞裡的 4 個「關鍵字」**  
> 學員在請 AI 幫忙製作 `.pptx` 樣版時，必須看懂這 4 個核心要求，未來換任何簡報才不會改壞版面：
> 1. **「保留原 Shape 座標、字型與對齊（Run 層級替換）」**：不能直接改寫 `shape.text`，要在 `paragraph.runs` 裡修改文字，才能保住原本的粗體、色彩與 `PP_ALIGN.CENTER` 置中對齊。
> 2. **「統一定義 `{{欄位名稱}}` 佔位符」**：把會變動的標題、KPI 數字、摘要條列換成雙大括號標記，固定不動的標籤（如「📌 本期重點摘要」）維持原樣。
> 3. **「強制開啟 `word_wrap = True`」**：確保任何文字框都不會因為內容變長而橫向衝出卡片邊界。
> 4. **「產出欄位對照清單（Mapping Table）」**：要求 AI 在改完樣版後，順便列出所有 `{{佔位符}}` 名稱與建議字數上限，方便下一階段寫腳本。

📋 **Prompt 0（複製使用）**：
```text
請幫我把這份 `簡報範本_原始檔.pptx` 改造成可重複套用的佔位符樣版 `簡報範本_佔位符樣版.pptx`：
1. 絕對保留原本 16:9 的所有色塊、卡片座標、字型、色彩與段落對齊設定（請在 Run 層級替換文字，不要直接覆寫 shape.text）。
2. 將會變動的專案名稱、報告期間、單位、簡報者、日期、3 組 KPI 標題與數字、重點摘要與下週待辦，替換為 `{{欄位名稱}}` 格式的佔位符。
3. 確認所有內文文字框皆開啟 `word_wrap = True`。
4. 最後請列出你建立的所有 `{{佔位符}}` 清單與每個欄位的對齊方式，方便我準備資料檔。
```

---

### 階段 1：批次注入資料並執行「長文字防溢出」對齊

📋 **Prompt 1（複製使用）**：
```text
請閱讀 `簡報範本_佔位符樣版.pptx` 與 `presentation_data.md` 中的兩組資料，幫我寫一支使用 `python-pptx` 的 Python 腳本，分別產出兩份簡報並確保以下對齊規則：
1. 在 `paragraph.runs` 層級進行 `{{佔位符}}` 替換（並處理佔位符被 PowerPoint 拆成多個 Run 的情況），保留原有的字體顏色、粗體與置中/靠左對齊。
2. 強制設定文字框 `word_wrap = True`，防止文字橫向溢出卡片框。
3. 針對「標題」與「重點摘要／下週待辦」加入防溢出縮字保護：當文字超過安全長度時，自動等比例縮小字體（例如內文從 13pt 降至 10.5pt），確保 Case 2 的長文字完整顯示在卡片範圍內。
```

#### 💻 核心 Python 實作範例（`python-pptx` 防溢出精華）
```python
from pptx import Presentation
from pptx.util import Pt

def replace_in_paragraph(para, mapping, max_chars=None, shrink_pt=None):
    full_text = "".join(run.text for run in para.runs)
    for key, val in mapping.items():
        if key in full_text:
            full_text = full_text.replace(key, str(val))
    if para.runs and full_text != "".join(r.text for r in para.runs):
        para.runs[0].text = full_text          # 保留第一個 Run 的字型、色彩與對齊
        for r in para.runs[1:]:
            r.text = ""
        if max_chars and shrink_pt and len(full_text) > max_chars:
            para.runs[0].font.size = Pt(shrink_pt)  # 長文字自動縮字防溢出
```

---

## ✅ 成果驗收自我檢查表（Checklist）
- [ ] 開啟兩份示範簡報，封面與內頁的 16:9 標題列、KPI 卡片位置完全一致。
- [ ] KPI 數字仍維持大字體、粗體、藍色與**置中對齊**（沒有被洗成預設黑字靠左）。
- [ ] Case 2（ERP 升級）的長標題與長條列內容皆自動折行且縮小字體，**沒有任何文字溢出卡片邊框**。

---

[← 返回現代職場 AI 應用全指南](../../README.md)
