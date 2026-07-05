# Local MCP Servers（本地端伺服器）

> 🟢 **方案需求**：Free（可用）。Claude Desktop 的 Desktop Extensions / Local MCP 機制在 Free 帳號即開放，需要的只是下載桌面版並開啟 Developer 模式。

**Local MCP Servers** 是執行在您個人電腦（Mac/PC）上的擴充服務。與雲端託管的 Connectors 不同，本地 MCP 讓 Claude 能夠存取您**本機的檔案、資料庫、甚至是執行本機的腳本與指令**。

這是在 Claude Desktop 上進行深度客製化、實現「AI 操控電腦」的核心機制。

---

## 📋 前置準備：執行環境 (uv 與 Node.js)

本地 MCP 伺服器本質上是執行在您個人電腦上的程式，它們多數是基於 **Python** 或 **Node.js (JavaScript/TypeScript)** 開發。
為了讓 Claude 能夠下載並啟動這些伺服器，您的電腦需要先安裝 `uv` 與 `Node.js`。

### 1. Node.js (與 npx)
- **為什麼需要**：許多 MCP 伺服器是用 JavaScript/TypeScript 寫成的。`npx` 是 Node.js 內建的工具，它能讓 Claude Desktop 直接從網路下載並執行 Node.js 開發的 MCP 伺服器（例如 Playwright MCP），免去手動管理本地套件的麻煩。
- **如何安裝**：
  - **macOS**：推薦使用 Homebrew 安裝。開啟終端機並輸入：
    ```bash
    brew install node
    ```
  - **Windows**：推薦使用 Winget 安裝。開啟 PowerShell 並輸入：
    ```powershell
    winget install OpenJS.NodeJS
    ```
  - **官方安裝包**：您也可以前往 [Node.js 官方網站](https://nodejs.org/) 下載並安裝 LTS 版本。

### 2. uv (與 uvx)
- **為什麼需要**：許多 MCP 伺服器是用 Python 寫成的。`uv` 是極速的 Python 套件與環境管理工具，而 `uvx` 能讓 Claude Desktop 自動在臨時的虛擬環境中下載並運行 Python 的 MCP 伺服器（例如 Time MCP），不需要您手動建立或管理繁瑣的 Python 環境。
- **如何安裝**：
  - **macOS / Linux**：開啟終端機並輸入：
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    （或使用 Homebrew：`brew install uv`）
  - **Windows**：開啟 PowerShell 並輸入：
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
    （或使用 Winget：`winget install astral-sh.uv`）

---

## 如何設定本地 MCP？

### 1. 進入開發者模式
- 開啟 **Claude Desktop**。
- 點擊左下角頭像 -> **Settings**。
- 在左側選單最下方找到 **Developer**。

### 2. 修改設定檔 (Edit Config)
- 點擊 **Edit Config** 按鈕，系統會以預設編輯器開啟 `claude_desktop_config.json`。
- 這個檔案定義了 Claude 啟動時要同時開啟哪些 MCP 伺服器。

### 3. 設定範例

#### 範例 A：Time 伺服器 (時間查詢)

如果您想讓 Claude 具備查詢精確本地時間的能力，可以在 `mcpServers` 區塊加入以下內容：

```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time"]
    }
  }
}
```

- **command**: 啟動指令（如 `uvx`, `npx`, `python` 等）。
- **args**: 傳遞給指令的參數或套件名稱。

#### 範例 B：Playwright 伺服器 (網頁自動化與爬蟲)

因為 Claude Desktop 跑在您自己的電腦上，MCP Server（包含 Playwright MCP）也是在本機執行，沒有像 claude.ai 網頁版那樣的網路白名單限制，可以正常連上任何網站。

##### 運作原理

```
Claude Desktop (對話介面)
      ↓ MCP 協定 (navigate、click、type...)
Playwright MCP Server (本機執行)
      ↓
真實瀏覽器 (Chromium/Firefox/WebKit)
```

您使用自然語言下指令，Claude 會把它翻譯成 Playwright 的操作（開啟網址、點擊、輸入文字、截圖、讀取頁面內容），實際執行的是本機那個瀏覽器。

##### 設定步驟

> 🟢 **前置需求**：Node.js 18 以上版本

編輯 Claude Desktop 的設定檔 `claude_desktop_config.json`（路徑請參考前述）：

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

##### 測試方式

重新啟動 Claude Desktop。連線成功後會在介面上看到 `playwright` 這個 MCP Server 已連接。
直接下指令測試，例如：
> 「用 Playwright 開啟 https://example.com，把頁面上的標題抓出來」

Claude 會呼叫 `browser_navigate`、`browser_snapshot` 這類工具，實際打開一個瀏覽器視窗執行。

##### 實務注意事項

* **官方套件**：官方套件是 `@playwright/mcp`（Microsoft 出的）。市面上還有一個 `@executeautomation/playwright-mcp-server`，是另一個社群專案、API 不太一樣，設定時請注意別搞混。
* **預設為有頭模式 (Headed Mode)**：預設是「看得見」的瀏覽器，非常適合教學展示，您可以親眼看到自動化過程；若需要跑批次或背景執行時，才需特別加上 `-headless` 參數。
* **登入型網站**：因為瀏覽器是可見的，遇到需要登入的頁面，可以讓 Claude 開到登入頁，您自己手動完成登入，之後 Claude 接手繼續操作，Cookie 會在該次 session 內保留。
* **低門檻操作**：這是 Claude 自己在寫/呼叫指令，不是您自己寫 Playwright 程式碼，對不熟程式的老師或學生來說門檻很低，非常適合當作教學示範。
* **正式爬蟲建議**：如果要做「排程、大量爬取」的正式爬蟲（例如每天固定抓某個資料），Playwright MCP 這種互動式操控比較適合「示範、探索、驗證邏輯」，真正大量執行時，仍建議請 Claude 幫您產生一支獨立的 Python/Node Playwright 腳本，排程執行會更穩定且節省資源。

---

## 🛠️ 管理與排錯

在 **Settings -> Developer** 畫面中，您可以即時監控伺服器狀態：
- **Running (綠色)**：伺服器運作正常，Claude 已載入其 Tools。
- **View Logs**：當伺服器無法啟動時，點擊此處查看詳細的錯誤訊息（Debug 的第一步）。
- **垃圾桶圖示**：從設定中移除該伺服器。

---

## 觀念比較：本地 MCP vs. 遠端 Connectors

| 特性 | 本地 MCP (Local) | 遠端連接器 (Connectors) |
| :--- | :--- | :--- |
| **執行位置** | 您自己的電腦 | 服務商的雲端伺服器 |
| **驗證方式** | 系統權限 (Local Auth) | **OAuth 2.0** |
| **設定方式** | 修改 JSON 設定檔 | 網頁按鈕一鍵授權 |
| **擅長任務** | 存取本機檔案、私有資料、內網設備 | 存取 Gmail、GitHub、Supabase 雲端資料 |

---

## 常用工具建議
- **uvx**: Python 生態系的快速執行工具（推薦使用）。
- **npx**: Node.js 生態系的快速執行工具。
- **Smithery.ai**: 可以搜尋並發現更多社群建立的 MCP 伺服器。

---

← [返回上層：Claude_AI 索引](../README.md)
