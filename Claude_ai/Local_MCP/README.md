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
  - **推薦方式（一般使用者）**：前往 [Node.js 官方網站](https://nodejs.org/) 下載並安裝 **LTS (長期支援版本)** 官方安裝包（`.pkg` 或 `.msi`），依預設提示完成安裝即可。
  - **命令行方式（進階使用者）**：
    - **macOS (Homebrew)**：`brew install node`
    - **Windows (Winget)**：`winget install OpenJS.NodeJS`

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
直接下指令測試，例如您可以輸入以下經過潤飾的實用 Prompt：

* **範例一 (單純網頁資訊爬取)**：
  ````markdown
  """
  請使用 Playwright 開啟台灣銀行牌告匯率網頁（https://rate.bot.com.tw），查詢今日美金 (USD)、日圓 (JPY) 與 歐元 (EUR) 對新台幣的『現鈔買入』與『現鈔賣出』匯率，並將結果整理成 Markdown 表格輸出。
  """
  ````

* **範例二 (動態搜尋與商品比價)**：
  ````markdown
  """
  請使用 Playwright 開啟 momo 購物網（https://www.momoshop.com.tw），在搜尋框中輸入『毛寶洗碗精』並進行搜尋。請幫我收集搜尋結果前 5 筆商品的『商品名稱』與『促銷價格』，並將結果整理成 Markdown 表格輸出。
  """
  ````

* **範例三 (競品市場調查與對比分析)**：
  ````markdown
  """
  請使用 Playwright 開啟 momo 購物網（https://www.momoshop.com.tw）：
  1. 在搜尋框中輸入『毛寶 小蘇打洗碗精 無香精』並進行搜尋，先幫我記錄我方產品的促銷價格與規格。
  2. 接著，重新搜尋『小蘇打洗碗精』，尋找其他競爭品牌（例如橘子工坊、茶籽堂、淨毒五郎等）的類似產品。
  3. 幫我收集前 5 筆競品商品的『品牌名稱』、『商品名稱』、『容量』與『促銷價格』。
  4. 最後，將我方產品與這 5 筆競品進行交叉對比，整理成一個 Markdown 比較表格，並針對我們產品的價格競爭力提供簡單的對比建議。
  """
  ````

Claude 會自動呼叫 `browser_navigate`、`browser_snapshot` 這類工具，實際在您的電腦上打開一個瀏覽器視窗，前往該網站並自動爬取資料呈現在對話框中。

##### 實務注意事項

* **官方套件**：官方套件是 `@playwright/mcp`（Microsoft 出的）。市面上還有一個 `@executeautomation/playwright-mcp-server`，是另一個社群專案、API 不太一樣，設定時請注意別搞混。
* **預設為有頭模式 (Headed Mode)**：預設是「看得見」的瀏覽器，非常適合教學展示，您可以親眼看到自動化過程；若需要跑批次或背景執行時，才需特別加上 `-headless` 參數。
* **登入型網站**：因為瀏覽器是可見的，遇到需要登入的頁面，可以讓 Claude 開到登入頁，您自己手動完成登入，之後 Claude 接手繼續操作，Cookie 會在該次 session 內保留。
* **低門檻操作**：這是 Claude 自己在寫/呼叫指令，不是您自己寫 Playwright 程式碼，對不熟程式的老師或學生來說門檻很低，非常適合當作教學示範。
* **正式爬蟲建議**：如果要做「排程、大量爬取」的正式爬蟲（例如每天固定抓某個資料），Playwright MCP 這種互動式操控比較適合「示範、探索、驗證邏輯」，真正大量執行時，仍建議請 Claude 幫您產生一支獨立的 Python/Node Playwright 腳本，排程執行會更穩定且節省資源。

---

## 🛠️ 管理與排錯

在 **Settings -> Developer** 畫面中，您可以即時監控本地伺服器的連接狀態。

### 1. 狀態與控制項說明

- **Running (藍色標籤)**：
  - **意義**：代表該 MCP 伺服器已在本機電腦的背景成功啟動，且與 Claude Desktop 建立起正常的 MCP 協定通訊（握手成功）。
  - **效果**：該伺服器所提供的工具（Tools）已載入至 Claude 中，對話時 Claude 可隨時調用。
- **View Logs**：當伺服器無法啟動（例如顯示為紅色錯誤或停止）時，點擊此處查看詳細的錯誤日誌，這是除錯最關鍵的第一步。
- **垃圾桶圖示**：點擊可直接從 `claude_desktop_config.json` 中移除該伺服器的設定。
- **Extension 代管狀態 (Managed by an extension)**：
  - 如果伺服器狀態顯示 `"This server is managed by an extension"`（此伺服器由擴充功能管理），代表它是由您在 `Settings -> Extensions` 安裝的 Connector 所託管。
  - **無法直接編輯 JSON**：這類伺服器不需要、也無法透過手動編輯 `claude_desktop_config.json` 來啟動或以垃圾桶圖示刪除。若要管理（如啟用、停用、卸載、調整單一 Tools 讀寫權限），必須至 `Settings -> Extensions` 頁面進行操作。

### 2. ⚠️ 啟用過多 MCP 伺服器的負面影響

雖然 MCP 帶來極高擴充性，但**同時啟用過多伺服器（例如 5 個以上）**會對使用體驗產生以下副作用：

1. **AI 決策混淆與 Token 消耗 (Tool Bloat)**
   - 每個伺服器都會將工具的定義與格式作為系統提示詞（System Prompt）輸入給 Claude，這會消耗大量 Context Window Token，增加每次對話的隱性成本。
   - 可用工具過多或功能相似時，Claude 容易混淆、用錯工具，或是拉長思考與回覆的時間。
2. **本機資源消耗 (Resource Drain)**
   - 每個本地 MCP 都是在背景執行的獨立 Python/Node.js 進程。
   - 像是 Playwright 等需要操作瀏覽器的 MCP，在執行時會吃掉大量的記憶體 (RAM) 與 CPU，開太多會導致電腦卡頓或耗電。
3. **啟動超時與連線不穩定**
   - Claude Desktop 在啟動時會同時初始化所有定義的伺服器。伺服器過多容易導致啟動變慢，甚至因為搶奪硬體資源而發生載入逾時（Timeout）錯誤。
4. **安全風險增加**
   - 本地 MCP 具備存取本機檔案與執行指令的高權限。加載過多未經審查的第三方 MCP 伺服器，會增加系統的安全威脅。

> 💡 **最佳實踐**：建議平時僅啟用當下工作必備的 2~4 個 MCP 伺服器。
> 
> #### 📝 如何在 JSON 設定檔中「註解」停用？
> 
> ⚠️ **特別注意**：`claude_desktop_config.json` 使用的是標準 **JSON 格式，JSON 預設不支援 `//` 或 `/* */` 的註解語法**。如果您直接在檔案中加入註解，會導致 Claude Desktop 解析失敗而無法啟動或載入任何 MCP。
> 
> 若想暫時停用某個 MCP 伺服器，請使用以下安全替代方案：
> 
> 1. **重新命名鍵名 (推薦)**：在伺服器名稱前加上底線（例如將 `"playwright"` 修改為 `"_playwright"`）。這樣既能完整保留該伺服器的參數設定，Claude 啟動時也會因為識別不到標準名稱而自動忽略它。
>    ```json
>    {
>      "mcpServers": {
>        "_playwright": {
>          "command": "npx",
>          "args": ["@playwright/mcp@latest"]
>        }
>      }
>    }
>    ```
> 2. **剪下備份法**：將不使用的伺服器 JSON 區塊剪下，暫時存放在外部的 `.txt` 或 `.md` 檔案中，需要使用時再貼回。

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
