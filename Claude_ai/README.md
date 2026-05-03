# Claude_AI 核心全指南

這份指南旨在幫助您從一位「對話者」進化為「AI 自動化專家」。內容涵蓋了 Claude 的基礎互動、知識管理、以及最強大的 MCP 擴充生態系。

---

## 🟢 基礎互動與產出 (Core Interaction)

### Chats（對話）
> **📂 [進入主題筆記：Chats](./Chats/README.md)**  
> Claude 的主要互動介面。學習如何透過對話下指令、上傳檔案，並使用 RTCCF 框架產出高品質內容。

### Artifacts（成品／Artifact）
> **📂 [進入主題筆記：Artifacts](./Artifacts/README.md)**  
> 獨立的內容顯示區塊。適合預覽程式碼、互動式網頁原型（React/HTML）或視覺化圖表，實現與 AI 的協作編輯。

---

## 🔵 知識管理與協作 (Organization)

### Projects（專案）
> **📂 [進入主題筆記：Projects](./Projects/README.md)**  
> **您的雲端知識沙盒**。可上傳專案知識、設定專屬指令，並實現「跨對話」的記憶共享。建議在此進行專案隔離以提升推理精確度。

---

## 🔴 擴充能力與連線 (Capabilities & MCP)

### Skills（技能）
> **📂 [進入主題筆記：Skills](./Skills/README.md)**  
> **動態任務調度員**。封裝專業的工作流與指令，可搭配 Function Calling 或本地工具執行特定專長任務。

### Connectors（連接器）
> **📂 [進入主題筆記：Connectors](./Connectors/README.md)**  
> **雲端資料橋樑 (OAuth)**。透過 MCP 協議將 Claude 連接到 Google Workspace、GitHub、Supabase 等雲端服務。
> - **進階閱讀**：[OAuth 2.0 授權機制深度解析](./Connectors/OAuth.md)

### Local MCP（本地端伺服器）
> **📂 [進入主題筆記：Local_MCP](./Local_MCP/README.md)**  
> **本地功能擴充**。透過修改設定檔，讓 Claude 存取您電腦中的檔案、資料庫或執行本機指令。

### Plugins（外掛／套件）
> **📂 [進入主題筆記：Plugins](./Plugins/README.md)**  
> **能力打包與分享**。將 Connectors、Skills 與指令打包成單一單元，便於團隊間的標準化協作。

---

## 🟣 進階代理工具 (Advanced Agents)

### Cowork / Code
> **專為協作與開發設計**。Cowork 專注於多步驟任務代理；Claude Code 則是程式開發者在終端機或 IDE 中的代理利器。

---

## ⚙️ 系統指揮中心 (System)

### Settings（設定）
> **📂 [進入主題筆記：Settings](./Settings/README.md)**  
> 全域功能開關。包括快捷鍵設定、**Browser Use**、**Computer use (Beta)** 以及各類能力的啟動路徑。

---

← [返回專案首頁](../../README.md)
