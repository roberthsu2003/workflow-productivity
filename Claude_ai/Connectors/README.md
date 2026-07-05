# Connectors（連接器）：AI 的資料橋樑

> **💡 三種擴充功能快速對照**
>
> | 類型 | 解決什麼 | 比喻 |
> |------|---------|------|
> | **Skills（技能）** | 教 Claude 怎麼把某類任務做好（不連外部服務） | 食譜／SOP |
> | **Connectors（連接器）** | 讓 Claude 能存取資料或操作其他系統 | 對外的插座、橋樑 |
> | **Plugins（外掛）** | 把多種能力打包成一個可安裝單位 | 整套工具箱 |
>
> **Connectors** 讓 Claude 連到外部服務、讀寫你的資料，底層多半是 MCP（Model Context Protocol）。例如 Google Drive、Gmail、Google Sheets、Supabase、n8n。提供的是**工具（tools）**，不是流程說明。  
> 若需要教 Claude 執行某類工作請看 [Skills](../Skills/README.md)；若要打包整套設定請看 [Plugins](../Plugins/README.md)。

> 🟢 **方案需求**：Free（可用）。Free 帳號可使用 Slack、Google Workspace 等官方連接器，以及任意 Remote MCP，但每段對話與每日訊息用量比 Pro 低（Pro 至少 5×）。

**Connectors** 是 Claude 的一個強大擴充功能。想像它是一座**專屬大橋**，將 Claude 直接連到您常用的雲端服務（如 Google Drive, Gmail, GitHub, Supabase 等）。

透過 Connectors，您不需要再手動將資料複製貼上到對話框。Claude 可以在您的授權下，直接「走過這座橋」去讀取、分析或摘要您放在雲端的資料。

---

## 為什麼要學 Connectors？

| 傳統做法 ❌ | 使用 Connectors ✅ |
| :--- | :--- |
| 打開信箱 -> 複製內文 -> 貼回 Claude | 在 Claude 直接說：「摘要我上週的郵件」 |
| 下載 Excel -> 上傳至對話框 | 讓 Claude 直接讀取 Google Sheets 的數據 |
| 手動整理行事曆衝突 | 讓 Claude 幫您掃描日曆並找出空檔 |

---

## 核心運作機制

為了確保資料傳輸的安全，Connectors 背後有兩個關鍵技術：

1.  **OAuth 2.0 (授權碼)**：這就像是一張「限時、限權」的通行證，讓 Claude 可以在不看到您密碼的情況下獲得存取權。
2.  **MCP (Model Context Protocol)**：這是兩端溝通的「共同語言」。

> **想要成為高手嗎？** 🛠️
> 如果您想深入了解 OAuth 如何運作、Access Token 存在哪裡，以及如何管理安全控管，請點擊閱讀：
> 👉 [**OAuth 2.0 與安全機制深度解析**](./OAuth.md)

---

## 🔌 Connectors 與 Extensions (擴充功能) 的關係

在 **Claude Desktop (桌面版)** 中，Connectors 與 Extensions 兩者在概念與 UI 上是高度綁定的：

1. **安裝與呈現**：當您在設定的 `Directory -> Connectors` 挑選並安裝某個連接器（例如 `Control Chrome` 或 `Context7`）之後，它會做為一項 **Extension (擴充功能)** 出現在您的 `Settings -> Extensions`（已安裝在您的電腦上）列表中。
2. **細粒度工具權限控制 (Tool permissions)**：
   在 `Settings -> Extensions` 中點進具體的擴充功能，您可以針對該連接器所屬的每個 Tool（例如 `Get Current Tab`、`Open URL`）進行獨立權限設定：
   - **允許 (Allow)**：AI 呼叫時直接執行。
   - **每次詢問 (Ask)**：AI 呼叫前需跳出視窗徵求您的同意（預設通常為人型小圖示）。
   - **禁止 (Deny)**：禁用該特定功能。
3. **擴充功能安裝包 (.MCPB 與 .DXT)**：在 Extensions 頁面下方，支援直接拖曳（Drag and Drop）手動安裝封裝檔案：
   - **`.MCPB` (Model Context Protocol Bundle)**：這是 MCP 伺服器的**執行程式封裝包**。它將伺服器程式碼、環境相依性與啟動設定直接打包成單一檔案，讓您拖曳即可一鍵安裝，完全免去手動安裝 Node.js/Python 與編輯 JSON 設定檔的繁瑣步驟。
   - **`.DXT` (Desktop Extension)**：這是擴充功能的**宣告與權限設定檔**。它定義了該擴充功能所需要的工具權限與 UI 配置，拖入後 Claude Desktop 會自動為其建立 Tool permissions 設定面板。

---

## 快速設定步驟

1.  **進入設定**：登入 [claude.ai](https://claude.ai)，點擊左下角頭像 -> **Settings** -> **Connectors**。
2.  **選擇服務**：找到您想連線的服務（例如 Google Calendar 或 Supabase）。
3.  **完成授權**：點擊 **Connect**，在跳出的視窗中登入該服務並點擊「允許」。
4.  **開始提問**：回到聊天室，直接用自然語言下指令。

---

## 經典範例：本週行程與準備清單

### 任務背景
當您連結了 **Google Calendar** 後，可以使用以下 Prompt 讓 Claude 幫您管理時間。

### RTCCF Prompt 範本
> **提示**：複製後請修改 `{ }` 內的內容。

```markdown
## Role
你是一位資深的行政效率專家。

## Task
請讀取我已連結的 **Google Calendar**，整理 **{請填：本週／下週}** 的會議摘要。
輸出需包含：時間、主題、地點/連結，以及針對每個會議的「準備建議」。

## Context
- 我的時區：Asia/Taipei。
- 若有行程衝突（重疊），請特別用「⚠️」標示。

## Constraint
- 僅根據日曆內容回答，不可自行推測行程。
- 語言：繁體中文。

## Format
- 使用 Markdown 表格呈現。
```

---

## 學生常見問題 FAQ

**Q：為什麼有些工具要寫設定檔，有些只要按 Connect 鈕？**
*   **本地 MCP**：像是在您電腦裡安裝小工具，需要改設定檔，適合存取本機檔案。
*   **Connectors (遠端 MCP)**：像是雲端服務對話，只要 OAuth 登入（Connect）就能用。

**Q：連線後，Claude 會偷看我所有的資料嗎？**
*   不會。Claude 只有在收到您的指令、且該指令需要用到相關資料時，才會透過 Connectors 去索取資料。您也可以隨時在設定中切斷連線。

---

← [返回上層：Claude_AI 索引](../README.md) · [前往下一章：OAuth 詳解](./OAuth.md)