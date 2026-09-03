# Claude Skills

專為**非程式設計師**設計，旨在學習如何「訓練」AI 成為您的數位分身，實現職場自動化工作流。

---

## 💡 三種擴充功能快速對照

| 類型 | 解決什麼 | 比喻 | 備註 |
|:---|:---|:---|:---|
| **Skills（技能）** | 教 Claude 怎麼把特定任務做好（不連外部服務） | 食譜／SOP | 一個資料夾內含 `SKILL.md` 指引、範本與腳本，符合條件時自動讀取。 |
| **Connectors（連接器）** | 讓 Claude 能存取外部資料或操作其他系統 | 對外的插座、橋樑 | 讀取外部資料請參考 [Connectors](../Connectors/README.md)。 |
| **Plugins（外掛）** | 把多種能力打包成一個可安裝單位 | 整套工具箱 | 打包整套設定請參考 [Plugins](../Plugins/README.md)。 |

---

## 🟢 方案需求與關鍵設定

> **適用方案**：Free / Pro / Max / Team / Enterprise 皆可建立與使用自訂 Skills。

### 🛠️ [Claude Skills 安裝與啟用指南（網頁版上傳 vs. 終端機指令）](./Setup/README.md)

💡 由於網頁/桌面版與 Claude Code 終端機的安裝與啟用方式完全不同，詳細步驟與授課建議請直接點擊上方標題前往指南。

> [!IMPORTANT]
> **使用 Skills 的關鍵前提：啟用「程式碼執行 (Code execution)」功能**
> 
> 在 Claude 中使用或開發 Skills 時，**必須**啟用「**Code execution and file creation**」（程式碼執行與檔案建立）功能。若未開啟，Skills 將無法正常運作。
> 
> ⚙️ **設定路徑**：
> 1. 點擊左下角個人頭像前往 `Settings`（設定）
> 2. 選擇左側選單的 `Capabilities`（能力）
> 3. 將 `Code execution and file creation` 功能切換為**開啟** (On) 狀態
> 
> 💡 *提示：這是因為 Skills 在執行任務時，需要依賴 Claude 在伺服器端執行程式碼以及建立/編輯文件、試算表、簡報等檔案的能力。*

<details>
<summary>⚙️ <b>Settings 設定細節與「找不到 Skills 清單」的常見解惑</b>（點此展開）</summary>
<br>

* **Skills 區段在頁面更下方**：  
  In `Capabilities` 設定頁面中，請繼續**往下方捲動**。經過「Allow network egress」與「Domain allowlist」後，才會看到「**Skills**」區段，那裡才會列出您已安裝的 Skills。

* **內建文件 Skills 自動生效**：  
  `pptx`、`docx`、`xlsx`、`pdf` 這幾個官方文件 Skills **不會**出現在下方的 Skills 清單中。它們是**直接內建**於 `Code execution and file creation` 功能裡的。只要此開關開啟，這幾項文件處理功能（包含簡報、試算表、Word、PDF 等）就已自動生效，無需也無法手動安裝。

* **下方的 Skills 清單會列出**：  
  1. **自訂上傳的 Skills**：例如您上傳的「華梵課程計畫表」、「報價單 (`quotation`)」、「產投課表 (`workforce-training-skill`)」等。
  2. **Anthropic 官方提供的範例 Skills**（若有開放瀏覽與安裝）。
</details>

---

## 📖 相關資源與官方文件

* **官方參考文件**：
  * [A complete guide to building skills for Claude-官方pdf文件](./The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

  * [如何使用 Skills (Use Skills in Claude)](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
  * [如何建立自訂的 Skills (How to create custom Skills)](https://support.claude.com/zh-TW/articles/12512198-%E5%A6%82%E4%BD%95%E5%BB%BA%E7%AB%8B%E8%87%AA%E8%A8%82%E6%8A%80%E8%83%BD)
* **開發者資源**：
  * [skills-claude API Docs](https://platform.claude.com/docs/zh-TW/agents-and-tools/agent-skills/overview)
  * [官方 Skill 範例庫 (Official Skills Repo)](https://github.com/anthropics/skills) *(預設開啟 Code execution and file creation，這些就會自動在雲端掛載)*

---

## 🔰 官方四大類別 Skills 實戰指令包

本節將 Anthropic 官方推出的 17 個 Skills 與實作練習，依據**文件製作、設計、開發、溝通**四大類別劃分。每個類別皆配備專屬的實作指引與直接可複製使用的 RTCCF Prompt 練習：

* **📁 [文件製作類 (Google Workspace) 指令包](./GWorkspace/README.md)**
  * 涵蓋：`pdf`、`docx`、`xlsx`、`pptx` 及 Google Workspace (Docs, Sheets, Slides, Gmail) 應用。
  * 實戰：Google Docs 會議紀錄、Google Sheets 任務追蹤、PowerPoint 簡報生成、Gmail 自動信件草擬等。
* **🎨 [設計與品牌類 (Design & Branding) 指令包](./Design/README.md)**
  * 涵蓋：`brand-guidelines` (品牌識別)、`canvas-design` (2D 畫布排版)、`theme-factory` (配色工廠)、`algorithmic-art` (程序藝術)。
  * 實戰：品牌化規格書、社群貼文畫布佈局、Teal Trust 配色方案展示、p5.js 星軌引力互動藝術。
* **💻 [工程與開發類 (Development & Tech) 指令包](./Development/README.md)**
  * 涵蓋：`claude-api` (API 最佳實踐)、`mcp-builder` (MCP 伺服器建置)、`frontend-design` (現代 UI 設計)、`web-artifacts-builder` (單頁應用)、`webapp-testing` (Playwright 測試)、`skill-creator` (自訂技能引導)。
  * 實戰：互動記帳儀表板 React Artifact、Playwright 端對端測試、Notion 待辦清單 MCP 伺服器設計、自訂合約審查技能。
* **💬 [溝通與內容類 (Communication & Content) 指令包](./Communication/README.md)**
  * 涵蓋：`doc-coauthoring` (個人風潤飾)、`internal-comms` (高效內部公告)、`slack-gif-creator` (動態貼圖生成)。
  * 實戰：保留聲音的數位游牧短文修改、TL;DR 企業 ERP 停機公告、Slack Rocket Welcome 動態貼圖。


---

## 🚀 自訂 Skills 四階演進路徑與建立方式

您可以透過修改或全新建立自訂 Skills 來打造個人的數位分身。以下是**由淺入深**的四個演進階段，每個階段皆提供**「方式 A（使用內建技能建立）」**與**「方式 B（手動建立）」**兩種實作路徑。

### 🟢 第一階：模仿者 (Imitator) —— 單獨建立 `SKILL.md`
* **核心概念**：學會如何撰寫基礎的 `SKILL.md`（定義 `Role`, `Task`, `Constraint`, `Format` 等指引）。
* **適用場景**：純文字的格式處理、語氣修飾、日常事務摘要等。
* **實戰範例**：👉 [**全能郵件修飾專家**](./Examples/Level1_Email_Polisher/README.md)
* **延伸實戰練習（依授課對象選用）**：
  * 🏢 **通用辦公室情境（跨公司 / 公開班學員）**：請參閱底部的 [辦公室實戰工作流地圖](#workflow-map)（範例 1 ~ 2）。
  * 💼 **專業創投情境（企業專班 / 投資機構學員）**：請參閱 [創投 (VC) 專屬 Skill 與 Playwright MCP 自動化實戰](#vc-playwright)。

### 🔵 第二階：創作者 (Creator) —— `SKILL.md` + `references` & `templates`
* **核心概念**：學習掛載外部參考知識（放置於 `references/`）與套用標準文件範本（放置於 `templates/`），使 Claude 產出特定格式的文件。
* **適用場景**：符合公司特定規範的報價單、遵循特定格式的會議紀錄、參考產品手冊進行預檢等。
* **實戰範例**：👉 [**個人化每日報工助手**](./Examples/Level2_Daily_Report/)
* **延伸實戰練習（依授課對象選用）**：
  * 🏢 **通用辦公室情境（跨公司 / 公開班學員）**：請參閱底部的 [辦公室實戰工作流地圖](#workflow-map)（範例 3 ~ 4）。
  * 💼 **專業創投情境（企業專班 / 投資機構學員）**：請參閱 [創投 (VC) 專屬 Skill 實戰（第二階：創作者篇）](#vc-creator)。

### 🟡 第三階：整合者 (Integrator) —— `SKILL.md` + `assets` (Logo與圖片) & 程式碼執行 (Code Execution)
* **核心概念**：運用 Claude 的「**程式碼執行 (Code Execution)**」功能，讓 Skill 會**自動執行指定的 Python 程式碼**！整合 `references/` 規章、`templates/` 報表樣板與 `assets/` 圖片（如公司 Logo），自動進行資料分析、文字稽核與圖表/圖片寫入，產出包含品牌識別與完整格式的實體檔案（如 `.xlsx`）供下載。
* **適用場景**：自動稽核文案並呼叫 Python 寫入帶有 Logo 的 Excel 報告、自動填寫表格樣板並插入企業圖表、生成具備品牌標誌的實體報表等。
* **實戰範例**：👉 [**品牌語氣稽核員**](./Examples/Level3_Brand_Voice/) (自動執行 Python 讀取 Excel 樣板與 `assets/company-logo.jpeg` 圖檔產生稽核報告檔)
* **延伸實戰練習（依授課對象選用）**：
  * 🏢 **通用辦公室情境（跨公司 / 公開班學員）**：請參閱底部的 [辦公室實戰工作流地圖](#workflow-map)（範例 5 ~ 7）。
  * 💼 **專業創投情境（企業專班 / 投資機構學員）**：請參閱 [創投 (VC) 財報數據分析與 Code Execution 自動化實戰](#vc-financial-analyzer)。

### 🔴 第四階：自動化專家 (Automator) —— `SKILL.md` + `scripts` (Python/工具調用)
* **核心概念**：加入 `scripts/` 資料夾放置 Python 腳本或工具宣告定義。結合 Claude 的「程式碼執行 (Code Execution)」，讓 AI 在伺服器端運行腳本，實現資料運算、複雜圖表繪製或自動化處理。
* **適用場景**：自動生成圖表簡報、進行財務數據加總小計、動態更新日程等。
* **實戰範例**：👉 [**智能會議排程秘書**](./Examples/Level4_Meeting_Secretary/)
* **延伸實戰練習（依授課對象選用）**：
  * 🏢 **通用辦公室情境（跨公司 / 公開班學員）**：請參閱底部的 [辦公室實戰工作流地圖](#workflow-map)（範例 8 ~ 10）。
  * 💼 **專業創投情境（企業專班 / 投資機構學員）**：請參閱 [創投 (VC) 財報數據分析與 Code Execution 自動化實戰](#vc-financial-analyzer)（含 Python 精準運算與趨勢圖表生成）。

---



<div id="workflow-map"></div>

## 🧩 10 個辦公室工作流範例規劃：由簡單到複雜

> **設計原則**：每個範例都以「辦公室真實任務」為場景，從單純文字改寫開始，逐步加入表格、檔案、規則、資料查詢、與跨工具協作。
> 下表與上方自訂 Skills 四階演進路徑互相對應：範例 1–2 對應「第一階：模仿者」，範例 3–4 對應「第二階：創作者」，範例 5–7 對應「第三階：整合者」，範例 8–10 對應「第四階：自動化專家」。

| # | 對應演進階段 | Skill 名稱 | 辦公室場景 | 可形成的工作流 |
| :---: | :--- | :--- | :--- | :--- |
| 1 | 🟢 第一階：模仿者 | [社群貼文文案大師](./Examples/Office_Workflow_01_Copywriter.md) | 有簡單的活動想法，需要快速撰寫成社群推廣文案 | 輸入核心概念 → 選擇平台 → 產出吸睛文案、Hashtags 與 Call-to-Action |
| 2 | 🟢 第一階：模仿者 | [主管交辦事項整理員](./Examples/Office_Workflow_02_Task_Extractor.md) | 會議後收到一堆零散訊息，需要整理成待辦清單 | 貼上對話 → 抽取任務 → 標記負責人、期限、優先級 |
| 3 | 🔵 第二階：創作者 | [客戶報價單產生器](./Examples/Office_Workflow_03_Customer_Quotation/) | 有隨興的專案品項、金額與折讓，需要產生正式報價單 | 輸入報價項目與客戶資訊 → 進行折讓計算 → 產出標準格式報價單 |
| 4 | 🔵 第二階：創作者 | [會議紀錄轉行動計畫助手](./Examples/Office_Workflow_04_Meeting_Action_Plan/) | 會議逐字稿太長，主管只想看結論與下一步 | 貼上逐字稿 → 摘要決議 → 產出 Action Items → 寄送前檢查 |
| 5 | 🟡 第三階：整合者 | [請假與代理安排助手](./Examples/Office_Workflow_05_Leave_Handover/) | 員工請假時，需要整理交接事項與通知信 | 輸入請假日期與工作項目 → 產出交接清單、代理通知、主管摘要 |
| 6 | 🟡 第三階：整合者 | [採購申請預檢員](./Examples/Office_Workflow_06_Purchase_Checker.md) | 行政或 IT 採購前，需要確認品項、預算、理由是否完整 | 貼上採購需求 → 檢查缺漏 → 產出補件問題與申請書草稿 |
| 7 | 🟡 第三階：整合者 | [客戶回覆與 CRM 更新助手](./Examples/Office_Workflow_07_Customer_CRM.md) | 業務收到客戶信件後，要回覆並更新客戶狀態 | 貼上客戶信 → 判斷意圖 → 產出回信 → 產生 CRM 更新摘要 |
| 8 | 🔴 第四階：自動化專家 | [週會資料彙整與簡報大綱助手](./Examples/Office_Workflow_08_Weekly_Brief.md) | 部門週會前，需要從多份進度回報整理重點 | 匯入多份回報 → 合併重複項 → 找風險 → 產出簡報大綱 |
| 9 | 🔴 第四階：自動化專家 | [跨部門簽核追蹤秘書](./Examples/Office_Workflow_09_Approval_Tracker.md) | 文件需要法務、財務、主管多方簽核，容易卡關 | 輸入簽核流程 → 查目前狀態 → 找卡點 → 產出催辦訊息 |
| 10 | 🔴 第四階：自動化專家 | [辦公室營運儀表板代理人](./Examples/Office_Workflow_10_Operations_Dashboard.md) | 主管每天想知道會議、待辦、客訴、採購、簽核的整體狀態 | 讀取多來源資料 → 分析異常 → 產出每日營運摘要 → 建議下一步 |

---


<div id="vc-playwright"></div>

* **💼 [創投 (VC) 專屬 Skill 與 Playwright MCP 自動化實戰](./VC_Playwright/README.md)**
  * 涵蓋：Deal Sourcing 標的偵測、Due Diligence 盡職調查、Market Mapping 競品分析、Portfolio 營運健康追蹤。
  * 實戰：Playwright MCP 動態抓取 + VC 分析 SOP 產出 Markdown 投資報告、多 MCP 整合 (FileSystem / Slack / Notion)。
  

<div id="vc-creator"></div>

* **💼 [創投 (VC) 專屬 Skill 實戰（第二階：創作者篇）](./VC_Creator/)**
  * 涵蓋：投資備忘錄 (Investment Memo) 產生器、Term Sheet 條款檢核與風險評級 (Red Flag Alerts)、Pitch Deck 簡報審查與問答生成器。
  * 技巧：結合 `references/`（創投指標規章、條款指南）與 `templates/`（標準 IC 備忘錄與風險報告範本）。

<div id="vc-financial-analyzer"></div>

* **💼 [創投 (VC) 財報數據分析與 Code Execution 自動化實戰](./VC_Financial_Analyzer/)**
  * 涵蓋：Excel 報表上傳自動掃描、互動式分析建議選單、100% 精準 Python 數據運算、動態渲染財務趨勢與 Runway 圖表、標準 IC 財務盡調報告產出。
  * 實戰：結合 **Code Execution (Code Interpreter)** 零數據幻覺運算 + `references/` 創投指標警訊庫 + `templates/` 標準盡調簡報樣板。


---


← [返回 Claude_AI 主講義](../README.md) | 🏠 [返回專案總首頁](../../README.md)

