# Claude_AI 教學講義（Free 方案為主）

這份講義以 **Claude Free 方案**為主軸，分為「基礎核心單元」與「進階與代理功能」兩大部分，各單元皆清楚標示適用於 Free 還是 Pro 方案，方便對照使用。

> **官方來源**：[Claude Pricing](https://claude.com/pricing) · [What is the Pro plan?](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan) · [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

---

## 🎯 方案速覽：Free vs Pro

| 能力 | 🟢 Free | 🔵 Pro（$20/月） |
| :--- | :---: | :---: |
| 基本對話（Chats）/ Web 搜尋 / Memory | ✓ | ✓ |
| Artifacts：Docs / Slides / Design 範本、互動成品、連結分享 | ✓ | ✓ |
| Artifacts：Data 儀表板 / Sheets / Whiteboards、儲存資料、連接 App | ✗ | ✓ |
| 程式碼執行 / 產出 Word・Excel・PPT・PDF | ✓ | ✓ |
| Connectors（Slack / Google Workspace / Remote MCP） | ✓（有用量限制） | ✓ |
| Skills（含自訂 SKILL.md） | ✓ | ✓ |
| Desktop Extensions（本地 MCP） | ✓ | ✓ |
| Extended Thinking | ✓ | ✓ |
| **Projects**（雲端知識沙盒） | ✓（限 5 個） | ✓ |
| **Model selector**（Opus 等） | ✗ | ✓ |
| **Research Mode** | ✗ | ✓ |
| **代理任務**（在對話中交辦多步驟任務，自動執行） | ✗ | ✓ |
| **Scheduled**（排程任務） | ✗ | ✓ |
| **內建瀏覽器**（Built-in Browser，需 Claude Desktop） | ✗ | ✓ |
| **Computer Use**（Beta，需 Claude Desktop；Team / Enterprise 暫不支援） | ✗ | ✓ |
| **Claude Code**（終端機開發工具） | ✗ | ✓ |
| **Plugins**（外掛安裝與瀏覽） | ✓ | ✓ |
| **Plugins**（於代理任務及 Claude Code 內使用） | ✗ | ✓ |
| 使用量上限 | 較低 | 至少 5 倍 |

> 💡 **教學提醒**：用 Free 方案就能跑完「基礎核心單元」全部範例，以及 Projects（限 5 個）。若課堂上要示範 Plugins、Claude Code、代理任務、內建瀏覽器、Computer Use 等 Pro 專屬功能，建議講師端使用 Pro 帳號展示，學生用 Free 帳號完成大部分練習。

---

## 📚 核心單元

### ⚙️ Settings（環境準備）— **Free**
> **📂 [進入主題筆記：Settings](./Settings/README.md)**  
> 上課第一步：開啟必要功能（Artifacts、Analysis Tool、快捷鍵）。Free 可用大部分基本設定。

### 🟢 Chats（對話）— **Free（核心必學）**
> **📂 [進入主題筆記：Chats](./Chats/README.md)**  
> 學會 **RTCCF 框架**（Role/Task/Context/Constraint/Format）撰寫高品質 Prompt，並透過自然指令產出 Markdown / Word / Excel / PowerPoint / PDF。  
> 內含五個產出範例（.md / .docx / .xlsx / .pptx / .pdf），全部 Free 可用。

### 🟢 Artifacts（成品）— **Free 可用 Docs / Slides / Design；Data / Sheets / 儲存資料需 Pro**
> **📂 [進入主題筆記：Artifacts](./Artifacts/README.md)**  
> 2026/9/16 全面改版：所有作品都集中在左側欄 **Artifacts** 分頁，新增 Docs、Slides、Design（Free）與 Data、Sheets、Whiteboards（Pro）、Motion（Team）範本。成品預設私人，可設定檢視／留言／編輯權限，並可匯出 Word / PowerPoint / PDF。  
> 內含 10 個可直接複製 Prompt 的實作範例（範例 1～6 Free 即可完成）。

### 🟢 討論方式的內容生成（人機協作 Human in the Loop 實戰）— **Free（核心工作流）**
> **📂 [進入主題筆記：討論方式的內容生成](./討論方式的內容生成/README.md)**  
> **告別單向盲猜與洗版噩夢！** 揭密人機協作 (Human-in-the-Loop) 最關鍵鐵律：**「只有儲存成為 Markdown（.md）格式的檔案，才可以人機協作！」** 二進位檔案（Word/Excel/PPT/PDF）為不可協作的單向編譯產物；所有推敲、局部修訂與版本回溯皆必須在 `.md` 檔案上完成，定稿後再一鍵導出成品，極致省 Token 且精準交付。  
> 內含四大實戰實例與真實檔案下載區（含真實生成之 .docx / .xlsx / .pptx / .pdf）：
> - 📄 [01. Word 商業企劃書與 SOP 矩陣](./討論方式的內容生成/Examples/01_Docx_Product_Launch_Plan/README.md)：解決直出 Word 格式死板問題，打磨時程與突發 SOP 後一鍵編譯排版級 DOCX。
> - 📊 [02. Excel 動態損益與跨表預算模型](./討論方式的內容生成/Examples/02_Xlsx_Financial_Budget_Model/README.md)：解決公式錯誤痛點，校對 Markdown 欄位後一鍵編譯 4 工作表、自帶連鎖公式 (=SUM) 的真實 XLSX。
> - 📽️ [03. PowerPoint 商業融資簡報分鏡](./討論方式的內容生成/Examples/03_Pptx_Pitch_Deck_Master/README.md)：解決滿版小字問題，打磨 One Message per Slide 與演講備忘稿，一鍵產出 16:9 暗黑科技風 PPTX。
> - 📜 [04. PDF 永續查驗報告暨高階簽核公文](./討論方式的內容生成/Examples/04_Pdf_ESG_Audit_Report/README.md)：解決跑版缺字痛點，對齊 ISO 14064-1 條文與數據，一鍵編譯雙色防偽、帶用印簽章的正式 PDF。  
> 深度閱讀：[01. HITL 核心心法](./討論方式的內容生成/Guide/01_HITL_Human_In_The_Loop_Core.md) · [02. 標題座標法工藝](./討論方式的內容生成/Guide/02_Coordinate_Method_and_Artifacts.md) · [03. 四大格式導出工程學](./討論方式的內容生成/Guide/03_Multi_Format_Export_Engineering.md)

### 🟢 Projects（雲端知識沙盒）— **Free（限 5 個）／Pro（無限制）**
> **📂 [進入主題筆記：Projects](./Projects/README.md)**  
> 為每個任務建立獨立的雲端知識空間，可上傳專屬檔案、設定 Custom Instructions、勾選專屬 Connectors，實現「跨對話」記憶共享與專案隔離。Free 方案最多可建立 5 個 Project；Pro 方案無數量限制。

### 🟢 Connectors（連接器）— **Free（用量限制）**
> **📂 [進入主題筆記：Connectors](./Connectors/README.md)**  
> 透過 OAuth 2.0 與 Remote MCP 安全直連外部雲端服務，告別手動複製貼上與檔案搬運。  
> 內含三大實戰次章節與完整配套偽檔案（可直接下載上傳/匯入測試）：
> - 📂 [01. Google Workspace 實戰](./Connectors/01_Google_Workspace/README.md)：Drive 跨檔分析、Gmail 摘要與日曆衝突調配（附營運數據 CSV、策略備忘錄 MD、模擬郵件）。
> - 🎨 [02. Canva 設計自動化](./Connectors/02_Canva/README.md)：文案一鍵匹配商務簡報範本、社群貼文 Brand Kit 色彩審查（附行銷企劃 MD、色票規範 JSON、排版文案）。
> - 📝 [03. Notion 知識庫實戰](./Connectors/03_Notion/README.md)：跨資料庫自然語言搜尋、Sprint 看板健康度與 Blocker 挖掘（附 PRD CSV、Sprint Tasks CSV、協作手冊 MD）。  
> 進階閱讀：[OAuth 2.0 與雲端隱私安全深度指南](./Connectors/Guide/01_OAuth_and_Security.md)

### 🟢 Skills（技能）— **Free**
> **📂 [進入主題筆記：Skills](./Skills/README.md)**  
> 自訂 `SKILL.md` 讓 Claude 變成你的數位分身。Free 帳號即可建立、測試與使用自訂 Skill（需開啟 code execution）。  
> 內含四階範例：模仿者 → 創作者 → 整合者 → 自動化專家。  


### 🟡 Plugins（外掛打包）— **Free 可安裝；代理任務 / Code 需 Pro**
> **📂 [進入主題筆記：Plugins](./Plugins/README.md)**  
> 將 Connectors、Skills、slash commands、sub-agents 打包成可安裝、可分享的能力單元。**Plugins 本身 Free 帳號即可安裝與瀏覽**，但主要使用環境（**代理任務**、**Claude Code**）為 Pro 專屬。

### 🟢 Local MCP / Desktop Extensions（本地擴充）— **Free**
> **📂 [進入主題筆記：Local_MCP](./Local_MCP/README.md)**  
> 在 Claude Desktop 透過 `claude_desktop_config.json` 加入本機 MCP 伺服器，讓 Claude 存取本機檔案、資料庫或執行本機指令。Free 可用。

### 🟣 Claude in Chrome（瀏覽器擴充功能）— **Pro / Max / Team / Enterprise**
> **📂 [進入主題筆記：claude_in_chrome](./claude_in_chrome/README.md)**  
> Anthropic 官方推出的 Chrome 擴充功能，能讓 Claude 直接進入您已登入的 Chrome 瀏覽器頁面，代為執行開分頁、點擊按鈕、填寫表單與讀取資料。（需 Pro / Max / Team / Enterprise 付費方案帳號登入使用）

### 🟣 代理任務（Agent Tasks）— **Pro / Max / Team / Enterprise**
> **📂 [進入主題筆記：Agent_Tasks](./Agent_Tasks/README.md)**  
> 2026 改版後已併入一般對話：直接說出目標，Claude 會自己拆解步驟、讀寫檔案、上網查資料、寫程式計算，完整做完多步驟工作。預設在雲端執行，關掉筆電也會繼續跑。內含 5 個由淺入深的職場實戰範例與練習檔。

### 🟣 Scheduled（排程任務）— **Pro / Max / Team / Enterprise**
> **📂 [進入主題筆記：Scheduled](./Scheduled/README.md)**  
> 在對話中說一句「每天早上 8 點幫我做」，就能把重複性工作交給 Claude 定時執行：每日簡報、週報彙整、定期研究追蹤等，即使電腦休眠也會準時在雲端執行。

### 🟣 內建瀏覽器（Built-in Browser）— **Pro / Max / Team / Enterprise**
> **📂 [進入主題筆記：Built_in_Browser](./Built_in_Browser/README.md)**  
> Claude Desktop 內建的瀏覽器，免安裝擴充功能。Claude 會在側邊面板自己開網頁、閱讀、點擊、填表單，適合比價、新聞追蹤、批次填表。和 Claude in Chrome 的差異與 4 個實作範例都在單元內。

### 🟣 Computer Use（Beta）— **Pro / Max Only**
> **📂 [進入主題筆記：Computer_Use](./Computer_Use/README.md)**  
> 讓 Claude 看螢幕、移動滑鼠、打字，直接操作電腦上的任何應用程式（Excel 桌面版、內部系統等）。需 Claude Desktop（macOS / Windows），Team / Enterprise 目前不支援。

### 🟣 其他 Pro 專屬功能 — **Pro Only**
- **Model Selector**：選擇 Opus 等更強模型
- **Research Mode**：深度多步研究
- **Claude for Microsoft 365 / Outlook**

---


← [返回專案首頁](../README.md)
