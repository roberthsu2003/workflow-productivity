# 開放來源 Skills（實用開源工具與技能）

在生成式 AI 與自動化工作流程中，AI 需要具備**讀取、解析、生成與編輯日常辦公文件**的能力。以下整理 GitHub 上最常用且強大的 **4 大類開源文件處理技能與核心工具**：

---

## 1. 📊 open-sheet（試算表 / 表格處理）

專門處理 Excel、Google Sheets 及 CSV 等試算表資料的讀取與自動生成：

* **[benborgers/opensheet](https://github.com/benborgers/opensheet)**
  * **用途**：將公開的 Google Sheets 直接轉換為乾淨的 JSON API，方便 AI Agent 或前端快速讀取試算表資料。
  * **特點**：輕量、免 API 金鑰、零設定，非常適合快速搭建自動化資料讀取工作流。
* **[SheetJS (sheetjs/sheetjs)](https://github.com/SheetJS/sheetjs)**
  * **用途**：JavaScript / TypeScript 與 Node.js 生態系中最通用的 Excel（`.xlsx`、`.xls`、`.csv`）解析與生成工具。
  * **特點**：效能優異，支援廣泛的試算表格式轉換與儲存格樣式處理。

---

## 2. 📽️ open-slide（投影片 / 簡報處理）

用於自動生成簡報投影片與處理高解析度影像：

* **[scanny/python-pptx](https://github.com/scanny/python-pptx)**
  * **用途**：建立、讀取及修改 PowerPoint（`.pptx`）檔案的 Python 函式庫，是絕大多數 AI Slide 生成技能的核心引擎。
  * **特點**：支援版面配置（Layout）、文字樣式、色彩主題、圖形繪製與表格插入。
* **[openslide/openslide](https://github.com/openslide/openslide)**
  * **用途**：高效讀取高解析度全切片影像（Whole Slide Images）的 C 函式庫（具 Python 綁定）。
  * **特點**：適用於醫療影像、病理切片與超大解析度數位掃描檔案的多尺度快速讀取。

---

## 3. 📝 open-docx（Word 文件處理）

負責處理微軟 Word 文件排版、合約審閱與公文報告生成：

* **[python-docx (python-docx/python-docx)](https://github.com/python-docx/python-docx)**
  * **用途**：操作與生成 Microsoft Word（`.docx`）文件的標準 Python 套件。
  * **特點**：支援段落、標題階層、表格、自訂樣式（Styles）與圖片精準嵌入，是產出正式公文與報告的必備工具。
* **[dolanmiu/docx](https://github.com/dolanmiu/docx)**
  * **用途**：JavaScript / TypeScript 生態系中用於生成 `.docx` 的開源工具。
  * **特點**：宣告式 API 設計，支援在 Node.js 與瀏覽器前端直接匯出排版精美的 Word 檔案。

---

## 4. 📄 open-pdf（PDF 解析與處理）

用於合約、論文、發票與掃描文件的文字/表格擷取及合併：

* **[pymupdf/PyMuPDF](https://github.com/pymupdf/PyMuPDF) & [pypdf](https://github.com/py-pdf/pypdf)**
  * **用途**：Python 中最廣泛用於擷取文字、提取表格、分割合併與加註浮水印的核心工具。
  * **特點**：解析速度極快，常作為 LLM / RAG 讀取與理解 PDF 文件的底層解析器。
* **[LibrePDF/OpenPDF](https://github.com/LibrePDF/OpenPDF)**
  * **用途**：基於 iText 4 的 Java 開源 PDF 函式庫（LGPL/MPL 授權）。
  * **特點**：專注於伺服器端高品質 PDF 的程式化生成、編輯與數位簽章操作。

---

## 🔗 相關延伸閱讀

* 📖 **[Claude 官方 Skills 指令包](../Claude_ai/Skills/README.md)**：包含 PPTX、DOCX、XLSX、PDF 的即用指令。
* 🔌 **[連結應用程式](../連結應用程式/README.md)**：Google Workspace、Canva 整合指南。
* 📝 **[儲存與重複使用 AI 提示詞](../儲存與重複使用AI提示詞/README.md)**：自訂提示詞與 AI 助手。
