📍 [常見的 AI 應用](../../README.md) › [辦公室全能應用](../README.md) › **Word 與 PDF**

# Word (.docx) 與 PDF (.pdf) 文件生成模組
## 🚀 AI Agent 公文、企劃與報告實戰

> 長篇文件與法規條款無法只靠大綱確認，所以 Word / PDF 比 Excel、簡報多一關：**`RTCCF.md` 確認後，AI 先交付完整內文 `.md` 給你逐段審核，定稿後才轉成 `.docx` / `.pdf`。**

---

## 🧭 人機協作標準工作流（Human-in-the-Loop）

![Word與PDF人機協作工作流](./images/Word與PDF人機協作工作流.svg)

---

## 📚 次資料夾實戰範例導覽

本模組收錄兩個實戰範例，建議依序閱讀：

1. [**範例 01：專案企劃書與推動計畫**](./01_專案企劃書與推動計畫/README.md)：零門檻口語發想，產出 1,500 字「2026 年度辦公室 AI 賦能推動計畫書」。
2. [**範例 02：企業差旅規章萃取員工指南**](./02_企業差旅規章萃取員工指南/README.md)：上傳 3 頁差旅規章 PDF，零幻覺萃取報銷標準與加班換休權益指南。

---

## 📥 AI Agent 匯出 Word (.docx) 與 PDF (.pdf) 指南

各 AI 平台的匯出方式：
- **Gemini**：右下角「**分享與匯出**」➔「**匯出至 Google 文件**」➔ 檔案 ➔ 下載為 `.docx` 或 `.pdf`。
- **Claude.ai**：Artifacts 富文本複製貼入 Word，或另存為 PDF。
- **ChatGPT**：Canvas 畫布檢視 ➔ 點選下載，或以列印另存為 PDF。
- **Google Antigravity（Coding Agent）**：直接依定稿 `.md` 檔案編譯輸出標準 `.docx` / `.pdf`。

### 🔤 `.md` 定稿轉 `.docx` / `.pdf` 跨平台統一字型轉換 Prompt（繁體中文 `zh-TW` ／ Mac & Windows 通用）

因為 Word 與 PDF 是**先產出完整 `.md` 內文並由人類審核定稿後，才進行格式轉換**，因此不需要把轉檔字型塞進內文草稿，只需在「最後放行轉檔」時貼上下方對應的轉換說明 Prompt，即可同時防止「中文退回新細明體」與「雲端轉 PDF 抓到簡體 (`SC`)／日文 (`JP`) 筆畫」兩大問題：

- **① 同時轉換為 Word (`.docx`) ＋ PDF (`.pdf`) 萬用 Prompt（最常用）**：
  ```text
  Markdown 內文審核通過！請依定稿後的 .md 檔案轉換為 Word (.docx) 與 PDF (.pdf)，並嚴格套用以下台灣繁體中文 (zh-TW) 跨平台統一字型規範：
  1. PDF (.pdf)：HTML 底層必須宣告 lang="zh-TW" 繁體中文（台灣）語系，並優先呼叫 "Noto Sans CJK TC" 與 "Noto Sans TC"（CSS 字型堆疊："Noto Sans CJK TC", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif）且內嵌字型，嚴禁映射到簡體 (SC) 或日文 (JP) 字庫；內文字級 11pt、行高 1.6 倍、標題加粗。
  2. Word (.docx)：全篇所有標題、內文段落與表格儲存格，語系設為繁體中文 (zh-TW)，中文字型統一設定為「微軟正黑體 (Microsoft JhengHei)」（或「思源黑體 (Noto Sans TC)」），英數字型統一為「Arial」，且底層 OpenXML 必須同時綁定西文字型 (w:ascii / w:hAnsi) 與東亞中文字型 (w:eastAsia)，避免中文退回新細明體。
  ```

- **② 單獨轉換為 Word (`.docx`) 專用 Prompt**：
  ```text
  Markdown 內文審核通過！請依定稿後的 .md 檔案轉換為 Word (.docx)。
  字型請嚴格遵守台灣繁體中文 (zh-TW) 跨平台規範：全篇（含標題、內文、條列與表格內文字）語系設為繁體中文 (zh-TW)，中文字型統一為「微軟正黑體 (Microsoft JhengHei)」（若雙平台皆已安裝台灣版思源黑體可改用 "Noto Sans TC"），英文與數字統一為「Arial」，並確保在底層 XML 同時設定 w:ascii、w:hAnsi 與東亞字型 w:eastAsia，不可只改英數字型而讓中文退回系統預設字體。
  ```

- **③ 單獨轉換為 PDF (`.pdf`) 專用 Prompt**：
  ```text
  Markdown 內文審核通過！請依定稿後的 .md 檔案轉換為 PDF (.pdf)。
  請使用支援中文字體內嵌（Font Embedding）的轉檔引擎，HTML 底層必須宣告 lang="zh-TW" 繁體中文（台灣）語系，並優先呼叫 "Noto Sans CJK TC" 與 "Noto Sans TC"（CSS 字型堆疊："Noto Sans CJK TC", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif），嚴禁映射到簡體 (SC) 或日文 (JP) 字庫；內文字級 11pt、行高 1.6 倍、標題加粗、表格框線清晰且避免跨頁斷頭。
  ```

### 💡 追求 100% 台灣正統繁體字形的終極絕招（`.docx` ➔ 本機另存 `.pdf`）

在雲端轉檔環境（Linux）執行 HTML 轉 PDF 時，即使設定了黑體，有時仍會因伺服器字庫限制而出現「申、請、補、準」等筆畫偏向**簡體字庫 (`Noto Sans CJK SC`)** 或 **日文字庫 (`Noto Sans CJK JP`)** 的情況。

如果你需要 **100% 台灣設計師等級、毫無簡體筆畫的正統繁體字型**，最一勞永逸的實務做法是：
1. 先用上方 **Prompt ②** 產出已鎖定字型與 `zh-TW` 語系的 **`.docx` (Word) 檔案**（或於對話介面匯出至 **Google Docs**）。
2. 下載回你自己的電腦（Mac / Windows），直接用電腦裡的 **Microsoft Word** 或 **Google Docs**「另存為 PDF」，即可直接調用本機完整且純正的台灣繁體字庫（微軟正黑體、蘋方-繁或思源黑體台灣版）！

---

🧭 [⬆ 回到：辦公室全能應用](../README.md) ｜ [下一頁：Excel 試算表 ➡](../Excel試算表的生成/README.md)
