# Claude_AI 教學講義（Free 方案為主）

這份講義以 **Claude Free 方案**為主軸，分為「基礎核心單元」與「進階與代理功能」兩大部分，各單元皆清楚標示適用於 Free 還是 Pro 方案，方便對照使用。

> **官方來源**：[Claude Pricing](https://claude.com/pricing) · [What is the Pro plan?](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan) · [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

---

## 🎯 方案速覽：Free vs Pro

| 能力 | 🟢 Free | 🔵 Pro（$20/月） |
| :--- | :---: | :---: |
| 基本對話（Chats）/ Web 搜尋 / Memory | ✓ | ✓ |
| Artifacts（互動成品） | ✓ | ✓ |
| 程式碼執行 / 產出 Word・Excel・PPT・PDF | ✓ | ✓ |
| Connectors（Slack / Google Workspace / Remote MCP） | ✓（有用量限制） | ✓ |
| Skills（含自訂 SKILL.md） | ✓ | ✓ |
| Desktop Extensions（本地 MCP） | ✓ | ✓ |
| Extended Thinking | ✓ | ✓ |
| **Projects**（雲端知識沙盒） | ✓（限 5 個） | ✓ |
| **Model selector**（Opus 等） | ✗ | ✓ |
| **Research Mode** | ✗ | ✓ |
| **Cowork**（協作與代理模式） | ✗ | ✓ |
| **Scheduled**（排程任務，Cowork Beta） | ✗ | ✓ |
| **Dispatch**（手機／電腦跨裝置代理，Beta） | ✗ | ✓（僅 Pro / Max） |
| **Claude Code**（終端機開發工具） | ✗ | ✓ |
| **Plugins**（外掛安裝與瀏覽） | ✓ | ✓ |
| **Plugins**（於 Code 及 Cowork 內使用） | ✗ | ✓ |
| **Computer Use（Beta）** | ✗ | ✓ |
| 使用量上限 | 較低 | 至少 5 倍 |

> 💡 **教學提醒**：用 Free 方案就能跑完「基礎核心單元」全部範例，以及 Projects（限 5 個）。若課堂上要示範 Plugins、Claude Code、Cowork 等 Pro 專屬功能，建議講師端使用 Pro 帳號展示，學生用 Free 帳號完成大部分練習。

---

## 📚 核心單元

### ⚙️ Settings（環境準備）— **Free**
> **📂 [進入主題筆記：Settings](./Settings/README.md)**  
> 上課第一步：開啟必要功能（Artifacts、Analysis Tool、快捷鍵）。Free 可用大部分基本設定。

### 🟢 Chats（對話）— **Free（核心必學）**
> **📂 [進入主題筆記：Chats](./Chats/README.md)**  
> 學會 **RTCCF 框架**（Role/Task/Context/Constraint/Format）撰寫高品質 Prompt，並透過自然指令產出 Markdown / Word / Excel / PowerPoint / PDF。  
> 內含五個產出範例（.md / .docx / .xlsx / .pptx / .pdf），全部 Free 可用。

### 🟢 Artifacts（成品）— **Free**
> **📂 [進入主題筆記：Artifacts](./Artifacts/README.md)**  
> 在側欄即時顯示可互動的 HTML、React、SVG、Mermaid 內容，適合做小工具原型、查詢頁、資訊圖。最容易讓學生產生成就感的章節。

### 🟢 Projects（雲端知識沙盒）— **Free（限 5 個）／Pro（無限制）**
> **📂 [進入主題筆記：Projects](./Projects/README.md)**  
> 為每個任務建立獨立的雲端知識空間，可上傳專屬檔案、設定 Custom Instructions、勾選專屬 Connectors，實現「跨對話」記憶共享與專案隔離。Free 方案最多可建立 5 個 Project；Pro 方案無數量限制。

### 🟢 Connectors（連接器）— **Free（用量限制）**
> **📂 [進入主題筆記：Connectors](./Connectors/README.md)**  
> 透過 OAuth 連接 Slack、Google Workspace（Gmail、Drive、Calendar）以及任意 Remote MCP。Free 可用但有用量限制。  
> 進階閱讀：[OAuth 2.0 授權機制深度解析](./Connectors/OAuth.md)

### 🟢 Skills（技能）— **Free**
> **📂 [進入主題筆記：Skills](./Skills/README.md)**  
> 自訂 `SKILL.md` 讓 Claude 變成你的數位分身。Free 帳號即可建立、測試與使用自訂 Skill（需開啟 code execution）。  
> 內含四階範例：模仿者 → 創作者 → 整合者 → 自動化專家。  
> 💼 **特別專題**：[創投 (VC) 專屬 Skill 與 Playwright MCP 自動化實戰](./Skills/VC_Playwright/README.md)（結合動態網頁爬取與創投商業分析框架）。

### 🟡 Plugins（外掛打包）— **Free 可安裝；Cowork / Code 需 Pro**
> **📂 [進入主題筆記：Plugins](./Plugins/README.md)**  
> 將 Connectors、Skills、slash commands、sub-agents 打包成可安裝、可分享的能力單元。**Plugins 本身 Free 帳號即可安裝與瀏覽**，但主要使用環境（**Claude Code**、**Cowork**）為 Pro 專屬；Free 帳號可在一般聊天中安裝，但無法使用完整的 Cowork／Code 工作流程。

### 🟢 Local MCP / Desktop Extensions（本地擴充）— **Free**
> **📂 [進入主題筆記：Local_MCP](./Local_MCP/README.md)**  
> 在 Claude Desktop 透過 `claude_desktop_config.json` 加入本機 MCP 伺服器，讓 Claude 存取本機檔案、資料庫或執行本機指令。Free 可用。

### 🟣 Claude in Chrome（瀏覽器擴充功能）— **Pro / Max / Team / Enterprise**
> **📂 [進入主題筆記：claude_in_chrome](./claude_in_chrome/README.md)**  
> Anthropic 官方推出的 Chrome 擴充功能，能讓 Claude 直接進入您已登入的 Chrome 瀏覽器頁面，代為執行開分頁、點擊按鈕、填寫表單與讀取資料。（需 Pro / Max / Team / Enterprise 付費方案帳號登入使用）

### 🟣 Cowork / Code（進階代理工具）— **Pro / Max / Team / Enterprise**
> **📂 [進入主題筆記：cowork](./cowork/README.md)**  
> 專為協作與自動化設計的獨立工作空間，支援自主多步驟任務執行、結合背景運算與排程，讓 Claude 成為能獨立運作的數位神隊友。
> 專為協作與開發設計，會大量使用 **Sub-agents（子代理）** 技術：
> - 主 AI 為了完成複雜任務，會自動派發多個「分身」執行子任務（一個查資料、一個寫程式），最後彙整結果。
> - 大幅提升處理複雜任務的精準度。

### 🟣 Scheduled（排程任務）— **Pro / Max / Team / Enterprise**
> **📂 [進入主題筆記：Scheduled](./Scheduled/README.md)**  
> 把重複性工作交給 Claude 自動定時執行：每日簡報、週報彙整、定期研究追蹤等，即使電腦休眠也會準時在雲端執行。

### 🟣 Dispatch（Beta）— **Pro / Max Only**
> **📂 [進入主題筆記：Dispatch](./Dispatch/README.md)**  
> 從手機交辦任務，Claude 在你的電腦上實際執行，使用本機檔案、Connectors 與應用程式，完成後把成品傳回手機。

### 🟣 其他 Pro 專屬功能 — **Pro Only**
- **Model Selector**：選擇 Opus 等更強模型
- **Research Mode**：深度多步研究
- **Computer Use（Beta）**：讓 Claude 看見螢幕、操作滑鼠
- **Claude for Microsoft 365 / Outlook**

---


← [返回專案首頁](../../README.md)
