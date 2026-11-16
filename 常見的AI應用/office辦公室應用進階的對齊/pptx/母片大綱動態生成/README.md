# 🏢 主軸二：企業母片（Slide Master）＋ 簡報大綱動態生成 `.pptx`

> 💡 **與「主軸一（固定月報 `{{佔位符}}`）」有什麼不同？**  
> 當每次簡報**主題不同、頁數不固定、且需要混用多種版型**（例如：封面＋章節頁＋單欄重點＋左右雙欄對比）時，不需要在投影片上寫死 `{{佔位符}}`。  
> 我們直接把**公司的 `.pptx` 母片（Slide Master）** 當作樣版，讓 AI 根據你提供的**大綱**自動決定分頁與版型配對，再由 Python 動態新增投影片並保留企業品牌樣式！

---

## 📦 本模組實作檔案

| 檔案類型 | 檔案名稱 | 說明 |
| :--- | :--- | :--- |
| 公司母片範本 | [企業母片範本.pptx](./企業母片範本.pptx) | 16:9 企業母片，內建頁首 Logo 與頁尾橫幅圖片，以及 8 種標準 Layout（封面、單欄、章節、雙欄、對比、結尾致謝、左重點右說明、左圖右文） |
| 簡報大綱範例 | [sample_outline.md](./sample_outline.md) | 提案簡報大綱（純 Markdown 文字，無須管排版座標） |
| 步驟 1 腳本 | [inspect_master.py](./inspect_master.py) | **母片體檢工具**：掃描公司 `.pptx` 母片，輸出所有 Layout 與原生 `placeholder.idx` |
| AI 規劃規格 | [slide_plan.json](./slide_plan.json) | AI 閱讀大綱與母片目錄後，產出的分頁與版型配對 JSON |
| 步驟 3 腳本 | [build_from_outline.py](./build_from_outline.py) | **動態生成引擎**：依 JSON 動態 `add_slide`，填入文字/圖片、防溢出並清除未用空框 |
| 示範成果 | [簡報_母片動態生成示範.pptx](./簡報_母片動態生成示範.pptx) | 執行 `build_from_outline.py` 產出的 8 頁完整企業簡報 |

---

## 🛠️ 三步驟實戰流程

### 步驟 1：掃描公司母片，產出「版型目錄」
先用 Python 讀取公司給的 `.pptx` 母片，列出每個版面配置（Slide Layout）的編號、名稱與可用的原生佔位符（`idx`）：

```bash
uv run --with python-pptx python3 inspect_master.py 企業母片範本.pptx
```

這會輸出一段結構化 JSON（例如 `layout_index: 4` 是 `05_雙欄對比含小標`，裡面有 `0: 標題`、`1: 左小標`、`2: 左內文`、`3: 右小標`、`4: 右內文`）。這份清單只要掃描一次，就能當作 AI 的排版說明書。

---

### 步驟 2：提供「大綱＋版型目錄」，讓 AI 規劃分頁 JSON

把你的簡報大綱（例如 [sample_outline.md](./sample_outline.md)）連同步驟 1 掃描出的版型目錄交給 AI：

<details>
<summary>📋 點此展開「大綱轉 slide_plan.json 參考 Prompt」</summary>

```text
請根據以下「公司母片版型目錄」與「簡報大綱」，幫我規劃每一頁最適合的版型，輸出為標準 JSON（格式需符合 `slide_plan.json` 規範）：
1. 依大綱語意自動挑選最適合的 `layout_index`（例如：對比內容選 `05_雙欄對比含小標`、雙項目並陳選 `04_左右雙欄內容`、單純重點選 `02_單欄標題與條列`）。
2. 每頁條列盡量控制在 3～5 點內、每點精簡扼要，避免單頁文字過多。
3. 條列支援 `{"text": "...", "level": 0}` 或 `level: 1` 子項目格式。
4. 嚴格只使用該 `layout_index` 確實擁有的 `placeholder.idx`。
```

</details>

---

### 步驟 3：Python 動態增頁與防溢出生成

執行生成腳本，Python 會以公司母片為基底，逐頁新增投影片並套用對應版型：

```bash
uv run --with python-pptx python3 build_from_outline.py
```

#### 💻 核心實作關鍵（`build_from_outline.py` 三大保護）
1. **清空範本舊頁、保留母片（`clear_existing_slides`）**：許多公司提供的 `.pptx` 內含範例頁，腳本會先清空主投影片區，只留乾淨的 Slide Master 與 Layouts。
2. **強制 `word_wrap = True` 與長文字自動縮字**：當單一佔位符總字數超過安全上限（預設 `160` 字）時，自動將字體微調縮小，避免文字爆出框架。
3. **自動移除未使用的佔位符（`remove_unused_placeholders`）**：若某個 Layout 有預留副標或頁尾佔位符但該頁沒填內容，腳本會直接從 XML 移除空框，確保簡報乾淨無「按一下以新增文字」提示。

---

## 💡 實務提醒：如果公司的公版 `.pptx` 沒有做好「母片 Layout」怎麼辦？
有些公司的公版簡報是把色塊和 Logo 直接貼在一般投影片上，而不是做在 PowerPoint 的「投影片母片（Slide Master）」裡：
- **標準做法（建議）**：請設計或用 PowerPoint「檢視 → 投影片母片」把常用版型存成 Layout，即可直接套用本模組。
- **替代做法**：若只有一般投影片範本頁，可改用「複製指定範例頁（Clone Slide）＋ 主軸一的 `{{佔位符}}` 替換」來達成動態頁數。

---

[← 返回 PowerPoint (.pptx) 進階對齊兩大主軸總覽](../README.md)
