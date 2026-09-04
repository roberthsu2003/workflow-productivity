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
- [**ITIC 專屬學員講義（12小時精華完整版）**](./ITIC_學員講義.md)：涵蓋三章節之觀念建立、操作筆記、Prompt 範本與實務踩雷提醒。
- [**每日產業新聞情報蒐集實戰（ITIC 專案指南）**](./每日產業新聞情報蒐集實戰.md)：深度解析「泛用搜尋 vs 定點爬蟲」之策略選型、發布時間檢驗與自動化情報蒐集 Prompt。
- [**AI Agent 基本概念**](../../AI_Agent基本概念/README.md)：解析從語言模型到多功能 AI Agent（思考大腦、規劃、工具調用、記憶與感知）的演進與職場應用觀念。
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
- [**Claude Skills 建立指南**](../../Claude_ai/Skills/README.md)：自訂 Skill 前兩階演進（第一階：模仿者 ➔ 第二階：創作者），學習建立基礎自訂 Skill 與結構化樣板（Templates）對接。
  <details>
  <summary>💡 <b>點擊展開：學員實作驗證（基礎 Skill 建立與樣板對接）</b></summary>
  <br>

  > 💡 **實作背景**：驗證學員是否能自行建立 `Email Expert`（模仿者）或 `Daily Report`（創作者樣板對接）Skill。

  ---

  **📝 實作驗證任務：手動建立與測試自訂 Skill**

  1. 開啟新對話，輸入指令：「`請幫我建立一個名為『郵件修飾專家』的 Skill，角色是專業文案，任務是修飾生硬郵件成禮貌商務信件，請使用 /skill-creator 自動產出。`」
  2. 下載產出的 ZIP 檔並解壓至 **Customize ➔ Skills** 完成安裝。
  3. 開啟全新對話，輸入一段生硬口吻的測試訊息，確認 Claude 是否自動啟用該 Skill 並輸出包含主旨、稱謂與禮貌正文的郵件。

  ---

  **✅ 實作驗證清單（Checklist）**

  - [ ] **Skill 安裝確認**：在 Customize ➔ Skills 清單中能看見新增的 Skill。
  - [ ] **自動識別啟用**：貼入生硬短訊時，Claude 能自動調用該 Skill 進行處理。
  - [ ] **結構符合規範**：產出的郵件符合主旨、稱謂、正文、祝禱與簽名檔完整結構。

  </details>


---

### 🔹 第三章：Excel 數據分析、Skill 整合者實作、排程自動化與交付實作

- [**Projects 雲端知識沙盒(實作)**](../../Claude_ai/Projects/README.md)：延續第一章建立的關注清單知識庫，將每日蒐集到的新聞與 Excel 歷史資料持續累積在同一個 Project 中，讓 Skill 執行時能參照過往紀錄比對趨勢與異常。
  <details>
  <summary>💡 <b>點擊展開：學員實作驗證（Projects 雲端知識庫上傳與檢索）</b></summary>
  <br>

  > 💡 **實作背景**：學員已在 Projects 中建立專屬的「ITIC 投資組合與關注清單」知識庫。本驗證旨在確認學員掌握上傳關注檔案並在對話中呼叫知識庫內容進行比對的能力。

  ---

  **📝 實作驗證任務：在 Project 中上傳資料並進行跨檔案詢問**

  1. 前往 **Projects** 頁面，開啟專屬的投資關注 Project。
  2. 在 **Project Knowledge** 上傳關注產業清單文件（如：`itic_watchlist.pdf` 或 `.txt`）。
  3. 在 Project 對話框中輸入 Prompt：「`請參考 Project 知識庫中的關注清單，比對我今天開啟的新聞標的，說明該標的是否屬於我們的重點關注領域？`」

  ---

  **✅ 實作驗證清單（Checklist）**

  - [ ] **檔案成功上傳**：能在 Project Knowledge 中看見已上傳的關注清單檔案。
  - [ ] **知識庫引述檢索**：Claude 回答時能精確引述 Project 中的檔案內容進行比對。
  - [ ] **專案隔離保護**：切換至其他 Project 時，資料獨立不互相混淆。

  </details>

- [**Claude Skills 建立指南**](../../Claude_ai/Skills/README.md)：自訂 Skill 第三階演進（第三階：整合者），學習運用 Code Execution 讓 Skill 自動執行指定程式碼，整合樣板與視覺資產檔（assets），實現高階工作流自動化。
  - [**每日產業新聞與情報自動化蒐集(模仿者 (Imitator))**](../../Claude_ai/Skills/VC_Playwright/README.md)
  - [**創投 (VC) 專屬 Skill 實戰（第二階：創作者篇）**](../../Claude_ai/Skills/VC_Creator/README.md)
  - [**品牌語氣稽核員（第三階：整合者code execution）**](../../Claude_ai/Skills/Examples/Level3_Brand_Voice/SKILL.md)
  - [**資料分析與報告撰寫實作（第三階：整合者code execution）**](../../Claude_ai/Skills/VC_Financial_Analyzer/README.md)
  
  <details>
  <summary>💡 <b>點擊展開：學員實作驗證（第三階：整合者 Skill 實作）</b></summary>
  <br>

  > 💡 **實作背景**：驗證學員能否不靠寫程式，整合 Projects 知識庫、規範與範例檔打造高階分析 Skill。

  ---

  **📝 實作驗證任務：建立整合型 Skill**

  1. 建立一個名為 `ITIC Report Integrator` 的 Skill。
  2. 在 Instructions 中定義：同時引用 Project 知識庫的關注標準、結合樣板檔格式，自動產出含分析與建議的投資摘要報告。
  3. 在新對話中輸入測試資訊，驗證 Skill 是否能同時讀取 Project 並套用樣板輸出。

  ---

  **✅ 實作驗證清單（Checklist）**

  - [ ] **免寫程式整合**：無需 Python 程式即可透過 Markdown 設定完成多資源整合。
  - [ ] **多來源參照**：回應結果能同時整合 Project 知識與樣板規範。

  </details>
- [**Claude Cowork 協作工作空間**](../../Claude_ai/cowork/README.md)：Anthropic 全新 AI 獨立工作空間，支援自主多步驟任務執行、整合 Connectors 與 Skills，適合無程式背景者進行進階自動化。<br>🔵 **需 Pro / Max / Team / Enterprise 付費方案**，且排程任務於**雲端遠端執行**，無法呼叫本機檔案與應用程式。
  <details>
  <summary>💡 <b>點擊展開：學員實作驗證（Claude Cowork 獨立工作空間）</b></summary>
  <br>

  > 💡 **實作背景**：驗證學員在 Claude Cowork 空間中發起自主任務的能力。

  ---

  **📝 實作驗證任務：在 Cowork 建立自主工作流程**

  1. 從左側選單切換至 **Cowork** 工作空間，建立一個新的 Cowork 任務 Session。
  2. 輸入 Prompt：「`請幫我執行週報彙整任務：讀取目前關聯的 Google Drive 與 Gmail，整理出本週 3 大重點進度與待辦事項。`」
  3. 觀察 Claude 在 Cowork 視窗中自主拆解步驟、調用工具並交付成果。

  ---

  **✅ 實作驗證清單（Checklist）**

  - [ ] **Cowork 空間開啟**：成功進入 Cowork 視窗發起任務。
  - [ ] **多步驟自主執行**：Claude 能連續呼叫工具並完成複雜流程。

  </details>

  
- [**Scheduled 排程任務**](../../Claude_ai/Scheduled/README.md)：Claude 原生排程功能的建立與管理方式，可設定固定時間自動觸發第一、二章的蒐集與摘要工作流。<br>🔵 **需 Pro / Max / Team / Enterprise 付費方案**，且排程任務於**雲端遠端執行**，無法呼叫本機檔案與應用程式。
  <details>
  <summary>💡 <b>點擊展開：學員實作驗證（Scheduled 雲端定時排程）</b></summary>
  <br>

  > 💡 **實作背景**：驗證學員建立 Scheduled 定時排程任務的能力。

  ---

  **📝 實作驗證任務：建立每日定時排程**

  1. 前往 **Scheduled** 頁面，點選 **New task**。
  2. 設定執行頻率（例如：每工作日 早上 9:00）。
  3. 填入任務 Prompt：「`自動讀取 Google Workspace Connectors，彙整每日最新郵件與行程摘要。`」
  4. 儲存排程，在 Scheduled 列表確認任務已排入待執行佇列。

  ---

  **✅ 實作驗證清單（Checklist）**

  - [ ] **排程設定成功**：任務出現在 Scheduled 清單中且時間頻率正確。
  - [ ] **雲端獨立運行**：確認任務說明符合雲端遠端執行規範。

  </details>

---


