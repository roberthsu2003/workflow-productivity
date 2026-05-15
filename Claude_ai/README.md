# Claude_AI 教學講義（Free 方案為主）

這份講義以 **Claude Free 方案**為主軸，學生不需付費即可完成所有第一部練習。第二部「Pro 進階」清楚標示為需升級才能使用，作為延伸補充。

> **官方來源**：[Claude Pricing](https://claude.com/pricing) · [What is the Pro plan?](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan) · [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

---

## 🎯 方案速覽：Free vs Pro

| 能力 | 🟢 Free | 🔵 Pro（$20/月） |
| :--- | :---: | :---: |
| 基本對話（Chats）/ Web 搜尋 / Memory | ✓ | ✓ |
| Artifacts（互動成品） | ✓ | ✓ |
| 程式碼執行 / 產出 Word・Excel・PPT・PDF | ✓ | ✓ |
| Skills（含自訂 SKILL.md） | ✓ | ✓ |
| Connectors（Slack / Google Workspace / Remote MCP） | ✓（有用量限制） | ✓ |
| Desktop Extensions（本地 MCP） | ✓ | ✓ |
| Extended Thinking | ✓ | ✓ |
| **Projects**（雲端知識沙盒） | ✗ | ✓（無上限） |
| **Model selector**（Opus 等） | ✗ | ✓ |
| **Research Mode** | ✗ | ✓ |
| **Claude Code / Cowork** | ✗ | ✓ |
| **Plugins**（在 Code/Cowork 內使用） | ✗ | ✓ |
| **Computer Use（Beta）** | ✗ | ✓ |
| 使用量上限 | 較低 | 至少 5 倍 |

> 💡 **教學提醒**：用 Free 方案就能跑完第一部全部範例。若課堂上要示範 Projects、Plugins、Claude Code 等，建議講師端使用 Pro 帳號展示，學生用 Free 帳號完成 80% 練習。

---

## 📚 第一部：Free Tier 入門到精通（核心課程）

### ⚙️ 1. Settings（環境準備）
> **📂 [進入主題筆記：Settings](./Settings/README.md)**  
> 上課第一步：開啟必要功能（Artifacts、Analysis Tool、快捷鍵）。Free 可用大部分基本設定。

### 🟢 2. Chats（對話）— **核心必學**
> **📂 [進入主題筆記：Chats](./Chats/README.md)**  
> 學會 **RTCCF 框架**（Role/Task/Context/Constraint/Format）撰寫高品質 Prompt，並透過自然指令產出 Markdown / Word / Excel / PowerPoint / PDF。  
> 內含五個產出範例（.md / .docx / .xlsx / .pptx / .pdf），全部 Free 可用。

### 🟢 3. Artifacts（成品）
> **📂 [進入主題筆記：Artifacts](./Artifacts/README.md)**  
> 在側欄即時顯示可互動的 HTML、React、SVG、Mermaid 內容，適合做小工具原型、查詢頁、資訊圖。最容易讓學生產生成就感的章節。

### 🟢 4. Skills（技能）
> **📂 [進入主題筆記：Skills](./Skills/README.md)**  
> 自訂 `SKILL.md` 讓 Claude 變成你的數位分身。Free 帳號即可建立、測試與使用自訂 Skill（需開啟 code execution）。  
> 內含四階範例：模仿者 → 創作者 → 整合者 → 自動化專家。

### 🟢 5. Connectors（連接器）
> **📂 [進入主題筆記：Connectors](./Connectors/README.md)**  
> 透過 OAuth 連接 Slack、Google Workspace（Gmail、Drive、Calendar）以及任意 Remote MCP。Free 可用但有用量限制。  
> 進階閱讀：[OAuth 2.0 授權機制深度解析](./Connectors/OAuth.md)

### 🟢 6. Local MCP / Desktop Extensions（本地擴充）
> **📂 [進入主題筆記：Local_MCP](./Local_MCP/README.md)**  
> 在 Claude Desktop 透過 `claude_desktop_config.json` 加入本機 MCP 伺服器，讓 Claude 存取本機檔案、資料庫或執行本機指令。Free 可用。

---

## 🚀 第二部：Pro 進階（選讀，需升級 $20/月）

> 以下章節需 Pro 方案才能使用。Free 帳號可閱讀觀念，但無法實作。建議學生熟悉第一部後再考慮升級。

### 🔵 7. Projects（雲端知識沙盒）— **Pro Only**
> **📂 [進入主題筆記：Projects](./Projects/README.md)**  
> 為每個任務建立獨立的雲端知識空間，可上傳專屬檔案、設定 Custom Instructions、勾選專屬 Connectors，實現「跨對話」記憶共享與專案隔離。

### 🟣 8. Plugins（外掛打包）— **Pro / Cowork / Code Only**
> **📂 [進入主題筆記：Plugins](./Plugins/README.md)**  
> 將 Connectors、Skills、slash commands、sub-agents 打包成可安裝、可分享的能力單元，主要在 **Claude Code** 與 **Cowork** 環境使用。

### 🟣 9. Cowork / Code（進階代理工具）— **Pro Only**
> 專為協作與開發設計，會大量使用 **Sub-agents（子代理）** 技術：
> - 主 AI 為了完成複雜任務，會自動派發多個「分身」執行子任務（一個查資料、一個寫程式），最後彙整結果。
> - 大幅提升處理複雜任務的精準度。

### 🟣 10. 其他 Pro 專屬功能
- **Model Selector**：選擇 Opus 等更強模型
- **Research Mode**：深度多步研究
- **Computer Use（Beta）**：讓 Claude 看見螢幕、操作滑鼠
- **Claude for Microsoft 365 / Outlook**

---

## 🗺️ 學習路徑建議

```
第 1 週：Settings + Chats（RTCCF 框架）
第 2 週：Artifacts（做出第一個互動小工具）
第 3 週：Skills（建立第一個自訂 SKILL.md）
第 4 週：Connectors + Local MCP（讓 Claude 讀取你的資料）
─────────────── Free 方案到此能完成 ───────────────
第 5 週：Projects 觀念講解（需 Pro 升級實作）
第 6 週：Plugins / Cowork / Code 概覽
```

---

## 📝 使用本講義的小提醒

1. **每個主題資料夾內都有 `README.md`**，包含觀念說明、設定步驟與 RTCCF Prompt 範本。
2. **Examples 子資料夾**收錄漸進式範例（Level 1 → Level 4），學生可直接複製貼上練習。
3. **Free Tier 用量限制**：5 小時內訊息數量有限，請學生分散練習時段，避免課堂上同時觸發。
4. **隱私提醒**：示範時請使用測試資料，勿上傳真實個資或機密文件。

---

← [返回專案首頁](../../README.md)
