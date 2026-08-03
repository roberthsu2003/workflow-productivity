# 創新工業技術移轉股份有限公司 (ITIC)
## 🚀 Claude AI 與 Skills 工作流程自動化實作

> **專案簡介**：本課程專為 ITIC 團隊量身打造，旨在建立一套自動化「資料與數據收集 → 重點摘要與分析 → 彙整交付」的數位工作助理流程。

---

## 📌 課程概覽

| 項目 | 說明 |
| :--- | :--- |
| **總時數** | 12 小時（共 3 天，每天 4 小時模組化設計） |
| **授課形式** | 實體工作坊（觀念解說 + 實務上機操作） |
| **適合對象** | ITIC 投資研究、營運管理及業務相關人員（無需程式背景） |
| **課程特色** | 結合 ITIC 投資標的與營運資料實例、零代碼/低維護原生架構、文字與數據雙軌並重 |

### 🎯 課程三大核心目標
1. **自動化工作流**：獨立設計 Claude Skill，自動完成日常情報與數據分析。
2. **團隊知識庫**：建立與維護 Projects 知識庫，轉化團隊經驗為專屬 AI 助理。
3. **擴充與維護**：掌握可持續擴充架構，輕鬆維護市場監控與營運報表系統。

### 💡 預期效益
- ⏱️ **效率大幅提升**：每日新聞與 Excel 數據判讀時間縮短，聚焦策略分析與決策。
- 📊 **產出標準化**：產出統一格式的分析報告與簡報，提升團隊溝通效率。
- 🔧 **靈活可擴充**：學員課後可自行新增投資標的與維護分析規則。

---

## 📚 課程大綱與教材導覽

### 🔹 第一章：Claude 核心操作、Projects 知識庫與關注清單 Skill

#### 📖 參考教材與延伸連結
- [**生成式 AI 模型基本概念**](../../生成式AI模型基本概念/README.md)：解析 LLM 底層能力與上層應用（檔案讀取、搜尋、API 串接）的演進與職場應用觀念。
- [**Prompt 撰寫技巧（實作）**](../../prompt/README.md)：掌握自然語言/YAML/Markdown 內容格式、System Prompt 角色設定與提示詞工程。
- [**Claude 官方 Skill 介紹**](https://github.com/anthropics/skills)：Anthropic 官方開放的 Skills 範例庫，提供標準化 Skill 設計規範與範例。
    - [**使用Anthropic PPTX Skill製作簡報(實作)**](../../Claude_ai/Skills/GWorkspace/README.md)-->**請使用練習C1**
- [**Artifacts 互動內容生成（實作）**](../../Claude_ai/Artifacts/README.md)：透過獨立預覽視窗生成長文案、數據圖表與互動原型，實現即時渲染與版本控制。
- [**Connectors 連結技巧(實作)**](../../Claude_ai/Connectors/README.md)：設定 Connectors 串接 Google Workspace（Drive、Gmail、Calendar、Sheets），讓 Claude 直接存取與整合雲端資料。

#### 🛠️ 課程內容與實作綱要
- **AI 核心與 Prompt 基礎**：熟悉 RTCCF 框架與 System Prompt 角色規則。
- **Projects 知識庫建立**：上傳 ITIC 投資標的清單與關注領域資料，打造專屬雲端知識沙盒。
- **內建 Skill 與 Connectors 實做**：設定 Google Workspace 等連結，實現免複製貼上的資料存取。

---

### 🔹 第二章：自動化新聞與產業情報蒐集、重點摘要 Skill

<details>
<summary>💡 課堂練習／實作驗證：使用 RTCCF,Connectors和pptx的skill</summary>

以下示範搭配 **Google Calendar Connector** 讀取行事曆時，如何撰寫標準 RTCCF Prompt：

#### 範例 1：基礎版 — 本週行程時間軸整理
```markdown
## Role
你是一位個人行程管理助理，擅長精準整理日程與時間規劃。

## Task
請讀取我在 Google Calendar 上的行程，整理出「本週（週一至週五）」的時間軸行程清單。

## Context
- 我已開啟 Google Calendar Connector 連結。
- 本週日期為本工作週（週一至週五）。

## Constraint
- 僅讀取本週一至週五的公開與個人行程。
- 依時間先後順序排列，標註開始與結束時間、會議名稱及地點/會議連結。
- 若當天無行程，請註明「當天無排定行程」。
- 嚴格依據日曆實際資料，不可捏造行程。

## Format
- 以 Markdown 日期標題分段（例如：`### 8/3 (週一)`）。
- 每個行程使用格式：`[時間範圍] 會議名稱 | 地點/連結 | 與會人員`。
```

---

#### 範例 2：進階版 — 創投投資主題簡報製作（使用 Anthropic PPTX Skill）
```markdown
## Role
你是一位創投（Venture Capital）簡報設計助手，擅長將投資主題與摘要轉化為結構清晰的簡報大綱，並運用 Anthropic PPTX Skill 製作專業 PowerPoint 簡報。

## Task
請依我提供的創投主題與要點，先規劃一份簡報大綱與投影片結構，與我討論確認後，再使用 PPTX Skill 製作成 PowerPoint 簡報檔案 (.pptx) 供我下載。

## Context
- 簡報主題：2026 半導體與 AI 創投投資趨勢與評估
- 報告對象：投資審查委員會
- 主要要點：
  1. 關注領域：半導體先進封裝（CoWoS/FOPLP）、矽光子（CPO）與 AI 伺服器供應鏈。
  2. 投資策略：聚焦具技術壁壘的早期與成長期新創。
  3. 風控原則：著重團隊技術專利與客戶驗證進度。

## Constraint
- 語言：繁體中文
- 簡報設計配色：指定使用「Midnight Executive」配色方案（深藍 `1E2761` / 冰藍 `CADCFC` / 白 `FFFFFF`），展現專業嚴謹風格。
- 固定 5 頁簡報結構：封面 → 投資趨勢總覽 → 重點關注領域 → 投資評估標準 → 結語與建議
- 每頁重點條目不超過 4 條。
- **工作流程限制**：
  1. **第一步（討論階段）**：請先使用 Claude Artifacts 功能，呈現每頁投影片的標題與內容大綱草稿。
  2. **第二步（討論階段）**：詢問我是否需要修改，在此時**不要**呼叫 PPTX 產生工具。
  3. **第三步（製作階段）**：待我確認大綱「可以製作」後，呼叫內建 PPTX Skill 將此大綱內容製作成實體 .pptx 簡報檔案。

## Format
- 使用內建 Anthropic PPTX Skill 建立並套用指定配色，匯出 PowerPoint 簡報檔案 (.pptx)。
- 完成後提供簡報檔案下載連結，並列出每頁的標題與大綱摘要。
```

---

#### 範例 3：完整版 — 近 7 天 Email 檢查與重要性分類（配合 Gmail Connector）
```markdown
## Role
你是一位行政與郵件管理助理，擅長資訊過濾、優先級排序與郵件分類整理。

## Task
請檢查我近 7 天（最近一週）在 Gmail 上的收件匣郵件，依據重要性與類別進行整理，並產出高優先待處理事項與郵件分類報告。

## Context
- 我已開啟 Gmail Connector 連結。
- 近期郵件較多，需要快速掌握近 7 天累積的重要資訊與待辦事項。

## Constraint
- 僅讀取最近 7 天內的信件。
- 依照重要性標示等級：`🔴 高優先`（需立即處理/回覆）、`🟡 中優先`（本週內處理）、`🟢 低優先`（僅供參考/例行通知）。
- 郵件類別須歸類為：`[創投/案源]`、`[內部簽核/通知]`、`[外部廠商/合作]`、`[電子報/訂閱]`。
- 若信件包含附件（如：NDA、BP、簡報、財報、合約），請特別標註 `📎 含附件`。
- 嚴格基於郵件實際內容整理，不可捏造；無相關信件時註明「無相關郵件」。

## Format
1. **近 7 天郵件總覽摘要**（總信件數、高優先待辦數）。
2. **🔴 高優先緊急待辦區**（列表包含：`寄件者` | `郵件主旨` | `日期` | `建議行動` | `建議回覆期限`）。
3. **郵件分類總覽表**（Markdown 表格：`重要性` | `類別` | `寄件者` | `主旨` | `日期` | `重點摘要與附件`）。
```

</details>

#### 📖 參考教材與延伸連結
- [**Claude in Chrome 擴充功能**](../../Claude_ai/claude_in_chrome/README.md)：Anthropic 官方 Chrome 擴充功能，可在已登入環境中執行頁面操作與資料讀取，適合 Gmail、內部系統等需登入網頁。
  <details>
  <summary>💡 <b>點擊展開：學員實作驗證（在 Claude Desktop 中使用 Prompt 控制 Chrome）</b></summary>
  <br>

  > 💡 **實作背景**：學員已於本機 Chrome 瀏覽器登入個人/公司帳號（如 Gmail、Google Workspace 或創投內部系統），並於 **Claude Desktop** 設定中啟用「Enable Claude in Chrome」。本驗證旨在確認學員已掌握**在 Claude Desktop 視窗直接輸入 Prompt，遠端驅動 Chrome 讀取與分析已登入網頁**的能力。

  ---

  **📝 實作驗證任務：在 Claude Desktop 輸入 Prompt 進行即時查詢**

  請開啟 **Claude Desktop** 應用程式對話視窗，複製以下任一創投實務 Prompt 貼入並發送測試：

  * **🔹 任務選項 A：已登入 Gmail 郵件檢查與摘要（使用 Claude Desktop）**
    在 Claude Desktop 中輸入 Prompt：
    ```text
    請使用 claude in chrome 開啟我的 Gmail（https://mail.google.com），檢查我最近的信件，幫我整理出：
    1. 寄件者與郵件主旨
    2. 核心訴求 / 創投案源簡述
    3. 需要執行的優先待辦事項與建議行動
    ```

  * **🔹 任務選項 B：產業新聞與標的網站動態擷取（使用 Claude Desktop）**
    在 Claude Desktop 中輸入 Prompt：
    ```text
    請使用 claude in chrome 開啟科技新報（https://technews.tw）或經濟日報，搜尋關於『半導體先進封裝』或『AI伺服器』的最新新聞：
    1. 擷取新聞標題、發布時間與關鍵公司
    2. 為 ITIC 投資評估濃縮 3 大重點摘要與潛在市場影響
    ```

  ---

  **✅ 實作驗證清單（Checklist）**

  - [ ] **連線設定確認**：Claude Desktop 的「Enable Claude in Chrome」已勾選啟用且連線正常。
  - [ ] **Desktop 下指令連動**：在 Claude Desktop 輸入 Prompt 後，能成功喚起並驅動 Chrome 進行分頁切換與內容讀取。
  - [ ] **已登入權限沿用**：無需手動輸入帳密，Claude Desktop 能直接讀取 Chrome 已登入帳號的內容（如 Gmail/內部系統）。
  - [ ] **結果回傳 Desktop**：頁面讀取與分析結果能自動回傳並結構化呈現於 Claude Desktop 對話視窗中。

  </details>
- [**Playwright 本地爬蟲技巧**](../../Claude_ai/Local_MCP/README.md)：透過本機真實瀏覽器支援動態 JS 渲染與頁面互動，適合存取內網與無 API 的公開網站。
  <details>
  <summary>💡 <b>點擊展開：學員實作驗證（Playwright MCP 本地自動化爬蟲操作）</b></summary>
  <br>

  > 💡 **實作背景**：學員電腦已於 Claude Desktop 設定中配置好 `playwright` Local MCP Server。本驗證旨在確認學員掌握**使用 Playwright 本地爬蟲突破雲端白名單限制、動態渲染 JS 網頁並擷取創投資訊**的能力。

  ---

  **📝 實作驗證任務：在 Claude Desktop 使用 Playwright MCP 下指令爬取資訊**

  請開啟 **Claude Desktop** 應用程式對話視窗，複製以下任一創投實務 Prompt 貼入並發送測試：

  * **🔹 任務選項 A：動態網站資料爬取與重點整理（公開資訊/產業新聞）**
    在 Claude Desktop 中輸入 Prompt：
    ```text
    請使用 Playwright MCP 幫我開啟科技新報（https://technews.tw）或公開新聞網頁：
    1. 搜尋過去一週關於『半導體封裝』或『CPO 矽光子』的新聞報導
    2. 擷取前 3 筆資料的『標題』、『發布日期』與『摘要重點』
    3. 將結果整理成 Markdown 表格輸出
    ```

  * **🔹 任務選項 B：新創標的網站動態網頁截圖與產品分析**
    在 Claude Desktop 中輸入 Prompt：
    ```text
    請使用 Playwright MCP 開啟指定的新創公司官網（或科技新聞頁面）：
    1. 開啟網頁並滾動頁面確保動態 JS 內容完全載入
    2. 讀取頁面文字並對首頁重要區塊進行截圖保存
    3. 提煉出該公司的『核心產品/技術』、『應用市場』與『團隊優勢』
    ```

  ---

  **✅ 實作驗證清單（Checklist）**

  - [ ] **MCP 服務連線正常**：在 Claude Desktop 設定中確認 `playwright` Local MCP Server 已正確連線。
  - [ ] **本機瀏覽器自動喚起**：發送指令後，Claude Desktop 能自動驅動本機 Playwright 瀏覽器執行頁面瀏覽與互動。
  - [ ] **突破雲端白名單限制**：成功存取與解析動態渲染（JavaScript）的公開網站頁面。
  - [ ] **結構化表格與摘要產出**：成功將爬取到的文字與數據彙整成 Markdown 表格或簡報要點輸出。

  </details>
- [**Claude Skills 建立指南**](../../Claude_ai/Skills/README.md)：自訂 Skill 四階演進路徑（模仿者 → 創作者 → 整合者 → 自動化專家），用於設計「新聞蒐集」與「重點摘要」兩支專屬 Skill。
- [**Projects 雲端知識沙盒(實作)**](../../Claude_ai/Projects/README.md)：延續第一章建立的關注清單知識庫，將每日蒐集到的新聞與 Excel 歷史資料持續累積在同一個 Project 中，讓 Skill 執行時能參照過往紀錄比對趨勢與異常。
- [**每日產業新聞/情報蒐集實戰指南**](./每日產業新聞情報蒐集實戰.md)：比較泛用搜尋與定點爬蟲差異，含關鍵字組合、Playwright Python 程式範例與 ITIC 專屬情報 Prompt。


#### 🛠️ 課程內容與實作綱要

- **每日產業新聞/情報蒐集 Skill**：採用**混合策略** — 以 Web Search 設計關鍵字組合與時間驗證機制負責廣度，再以 Claude in Chrome／Playwright 定點爬取 3-5 個權威來源負責精準度；讀取第一章建立的關注清單並輸出結構化結果。
- **新聞與情報重點摘要 Skill**：設計摘要 Prompt 技巧（濃縮 2-3 句重點），依「利多/利空/中性」及產業影響度進行分類。

> 📌 **銜接第三章的關鍵提醒**：三種蒐集方式的「可排程性」不同 —— Web Search 可雲端自動執行、Claude in Chrome 需本機瀏覽器、Playwright 本地爬蟲**無法**用 Claude 原生排程觸發。詳見 [實戰指南的排程限制章節](./每日產業新聞情報蒐集實戰.md#-重要限制哪一種做法可以排程自動執行)，務必在本章先建立正確預期。

---

### 🔹 第三章：Excel 數據分析、每日彙整簡報產出、排程自動化與交付實作

#### 📖 參考教材與延伸連結
- [**資料分析與報告撰寫實作**](../../實作任務/資料分析與報告/README.md)：AI 負責的 80% 工作（統計計算、趨勢視覺化建議、異常偵測）與人負責的 20%（數據來源、目標定義、結果驗證），適合套用到 ITIC Excel 業績與營運資料判讀。<br>⚠️ **本教材僅取用「80/20 人機分工框架」觀念**；其中示範的 Google Sheets／ChatGPT／Gemini／Canva 等工具操作不在本課程範圍內，實際操作一律以「上傳 Excel 至 Claude 解析」為準。
- [**討論方式的內容生成**](../../討論方式的內容生成/README.md)：以 Artifact 模式與 Claude 反覆討論、逐步優化內容，並產出 docx、pdf 等格式，適合彙整每日情報與數據分析成正式報告。
- [**簡報的生成**](../../簡報和資訊圖表/簡報的生成.md)：簡報大綱設計、風格與配色建議，以及 NotebookLM／PPT 模板產出流程，供彙整簡報參考。
- [**Scheduled 排程任務**](../../Claude_ai/Scheduled/README.md)：Claude 原生排程功能的建立與管理方式，可設定固定時間自動觸發第一、二章的蒐集與摘要工作流。<br>🔵 **需 Pro / Max / Team / Enterprise 付費方案**，且排程任務於**雲端遠端執行**，無法呼叫本機檔案與應用程式。
- [**Connectors 連結技巧**](../../Claude_ai/Connectors/README.md)：（延續第一章）交付階段需透過 Connectors 串接 Gmail 與 Google Drive，才能把成品自動送達內部信箱或共用雲端資料夾。

#### 🛠️ 課程內容與實作綱要
- **Excel 業績與營運數據分析**：上傳 Excel 業績與營運資料，解析結構化表格，進行趨勢判讀、異常提醒與重點摘要報表整理；實作 AI 負責的 80%（統計計算、異常偵測、段落撰寫）與人負責的 20%（數據來源確認、指標定義、結果驗證）。
- **每日彙整簡報產出 Skill**：串接文件產出能力（Word/PDF），將第二章的文字情報摘要與 Excel 數據分析整合為主管導向的正式簡報與報告。
- **排程自動化（雲端版工作流）**：採用 Claude 原生排程功能，設定固定時間自動觸發第一、二章的完整工作流。<br>⚠️ **可排程的版本以 Web Search ＋ Connectors 為主**；第二章的 Playwright 本地爬蟲**無法**由雲端排程觸發，若需自動化須改由本機作業系統排程器（macOS `launchd` / Windows 工作排程器）呼叫 Claude Code 執行，本章會示範兩者的取捨與設定方式。
- **例外處理與交付對接**：規劃自動化流程例外提醒（如來源無資料、網站改版、排程執行失敗），並透過 Connectors 對接內部交付管道（如 Email、共用雲端資料夾）。
- **綜合演練與成果發表**：完整跑通「蒐集 → 摘要/分析 → 彙整 → 交付」全流程，進行成果展示與後續維護建議。

---

## 📝 課前準備與學習建議

> [!IMPORTANT]
> **帳號方案確認（影響第三章能否實作）**
> 1. **付費方案**：Claude 原生排程（Scheduled）需 **Pro / Max / Team / Enterprise** 付費方案，免費方案無法使用。
> 2. **功能開通狀態**：Scheduled 目前於 Claude Cowork 中提供，**優先開放 Max 方案**，其餘方案陸續開放中。請課前先登入確認左側欄是否已出現「Scheduled」項目。
> 3. **若尚未開通**：第三章的排程段落將改以「手動觸發完整工作流 ＋ 本機作業系統排程器」的替代方案進行，請課前告知，以便講師調整教材配置。

> [!TIP]
> 1. **實務情境對接**：建議課程練習皆使用 ITIC 實際投資組合公司與營運資料作為範例，上完課後即可直接複製套用到日常工作中。
> 2. **交付管道確認**：建議課前先確認 ITIC 現有的資料交付管道（如內部信箱、共用雲端硬碟），以便第三章能無縫對接實際情境；並確認 Google Workspace 的 Connectors 授權是否可由 IT 政策允許。
> 3. **本機環境準備**：若要實作第二章的 Playwright 定點爬蟲，請課前於個人電腦安裝 Python 與 Playwright；**無程式背景的學員不需自行撰寫程式**，課堂上將以「向 Claude 描述需求 → 產生程式碼 → 執行驗證」的方式進行。
