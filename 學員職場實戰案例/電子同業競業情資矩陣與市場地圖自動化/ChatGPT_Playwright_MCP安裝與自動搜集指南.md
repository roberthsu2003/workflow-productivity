# Playwright MCP 安裝與情資自動搜集指南（ChatGPT 桌面版 ＆ Antigravity）

> 💡 **核心價值**：在進行「39 家上市櫃同業競爭情資與動能矩陣」分析時，資料搜集通常有兩種路徑：
> 1. **一般方法（基礎版）**：利用 ChatGPT / Claude / Gemini 內建的網路搜尋（Web Search），由 AI 自動搜尋公開財經新聞與概括資料。
> 2. **Playwright MCP 方法（專業進階版）**：在 **ChatGPT 桌面版** 或 **Antigravity IDE** 中掛載 **Playwright MCP 伺服器**，賦予 AI 直接操控真實瀏覽器的能力，能深入執行 JavaScript 動態渲染網頁（如公開資訊觀測站 MOPS、券商專業資料庫），精準截取表格與最新財報數據，徹底杜絕數據通靈！


---

## 🆚 兩種資料搜集方式深度對比

| 比較項目 | 方法一：一般 AI 內建 Web Search | 方法二：ChatGPT 桌面版 + Playwright MCP |
| :--- | :--- | :--- |
| **技術原理** | 透過搜尋引擎 API（如 Bing / Google）檢索靜態網頁摘要 | 透過 MCP 協定由 AI 本地啟動無頭/有頭 Chromium 瀏覽器，即時渲染網頁 DOM |
| **動態網頁支援** | ⚠️ 弱。若遇到需點擊分頁、下拉選單或 AJAX 非同步加載的網站容易抓空 | 🏆 極強。支援等待頁面渲染、點擊互動、截圖與讀取無障礙樹（Accessibility Tree） |
| **抗阻擋與反爬蟲** | 容易被防爬蟲機制阻擋或只拿到快取舊資料 | 模擬真實瀏覽器行為，可順暢讀取臺灣證券交易所與公開資訊觀測站 |
| **設定門檻** | 零門檻，打開 ChatGPT 對話框即可直接使用 | 需具備 Node.js 環境，並在 ChatGPT 桌面版設定介面新增一次 MCP 伺服器 |
| **適用情境** | 快速掌握公司簡介、產品方向、重大概念題材 | 需要 39 家精確營收 YoY%、特定月份營收、法說會精準數據與財報表格 |

---

## 🛠️ ChatGPT 桌面版安裝 Playwright MCP 步驟教學

### 步驟 0：前置環境確認（Node.js / npx）
Playwright MCP 是由微軟（Microsoft）官方維護的 MCP 伺服器套件，底層透過 Node.js 執行。請先確認您的電腦已安裝 Node.js：

1. 開啟終端機（Terminal）：
   - Mac：按下 `Command + 空白鍵`，輸入 `Terminal` 並開啟。
   - Windows：按下 `Win + R`，輸入 `cmd` 或 `powershell` 開啟。
2. 輸入以下指令確認版本（建議 Node.js v18 以上，推薦 v20+）：
   ```bash
   node -v
   npx -v
   ```
   > 💡 *若尚未安裝 Node.js，請至 [Node.js 官方網站](https://nodejs.org/) 下載 LTS 版本安裝。*

---

### 步驟 1：開啟 ChatGPT 桌面版之 MCP 設定頁面

1. 開啟 **ChatGPT 桌面應用程式**（支援 macOS / Windows 桌面版本）。
2. 點擊左下角個人頭像或齒輪圖示，進入 **「設定」**（Settings）。
3. 在左側選單中，點選 **「整合」** 區塊下的 **「外掛程式」**（Plugins & Integrations）。
4. 在上方標籤頁中，切換至 **「MCP」** 分頁。
5. 點擊右上角的 **「新增」**（Add MCP Server）按鈕。

---

### 步驟 2：填寫 Playwright MCP 伺服器參數

在彈出的設定視窗中，請對照以下欄位精準填入：

| 設定欄位 | 填寫內容 | 說明 |
| :--- | :--- | :--- |
| **伺服器名稱** | `playwright` 或 `Playwright MCP` | 自訂名稱，方便識別辨識 |
| **啟動指令 (Command)** | `npx` | 使用 Node.js 的套件即時執行器 |
| **引數 (Arguments)** | 依序新增 2 個引數：<br>1. `-y`<br>2. `@playwright/mcp@latest` | 點擊「+ 新增引數」按鈕分開填寫：<br>• 第 1 列填：`-y`<br>• 第 2 列填：`@playwright/mcp@latest` |
| **環境變數 (Env Variables)** | *(留空即可)* | 無特殊代理設定時不需填寫 |
| **環境變數透傳** | *(留空即可)* | 維持預設 |
| **工作目錄 (Working Dir)** | 專案目錄路徑或任意暫存目錄 | 例如：`/Users/你的使用者名稱/Documents/GitHub/workflow-productivity/...` |

> 📌 **進階參數選用提示**：
> 若您希望執行時看到瀏覽器實際彈出並在畫面上自動翻頁找資料，保持上述預設即可；若您希望它在背景默默執行不彈出瀏覽器視窗，可以在引數清單中額外「+ 新增引數」填入 `--headless`。

---

### 步驟 3：儲存並啟動 Playwright MCP 服務

1. 點擊右下角的 **「儲存」**（Save）按鈕。
2. 回到「MCP 伺服器」列表頁面，確認 **playwright** 伺服器旁的開關已切換至 **開啟（藍色）** 狀態。
3. 此時 ChatGPT 桌面版已成功連線至 Playwright MCP，獲得自主操控瀏覽器提取網頁資訊的能力！

---

## 🚀 如何在對話中呼叫 Playwright MCP 查證 39 家同業最新月營收？

當您完成 Playwright MCP 設定後，可以在 ChatGPT / Antigravity 對話視窗中，下達指定使用 Playwright 的官方查證指令：

### 專屬提示詞範例（搭配 Playwright MCP）：

```text
你好，我已經啟用了 Playwright MCP 工具。
我需要你扮演熟悉台灣上市櫃公司月營收公告與公開資訊查詢方式的財務資料研究分析師，依據當下最新日期，針對上傳的《素材_同業清單_被動元件.xlsx》（39 家台灣上市櫃被動元件廠商），執行最新月營收查證與分析：

請嚴格遵循兩階段工作流：
1. 【調用 Playwright 查證官方數據】：透過 Playwright 瀏覽器工具或官方端點，實際訪問公開資訊觀測站（MOPS）、臺灣證券交易所（TWSE）或櫃買中心（TPEx），逐筆核對這 39 家公司的官方名稱、M 營收、M-1 營收與 M-12 營收，並記錄公告/出表日期。
2. 【執行運算與排名】：計算各公司月增減金額、月增率、年增減金額與年增率，並排出月增最高/最低 Top 10 與年增最高/最低 Top 10 排行榜。
3. 【交付 Markdown 報告並停下等待】：先產出一份結構完整的繁體中文 Markdown 報告供我審核。交付後請主動停下並詢問我是否同意建立 Excel。在收到我明確回覆「同意建立 Excel」之前，嚴禁產出任何 XLSX 檔案！
```

---

## 💡 常見問題與排錯指南（Troubleshooting）

1. **Q：執行時提示 `npx: command not found`？**
   * **原因**：系統環境變數 PATH 未正確加載 Node.js 路徑。
   * **解法**：在終端機中執行 `which npx`，若輸出路徑為 `/usr/local/bin/npx` 或 `/opt/homebrew/bin/npx`，可直接將設定介面中的「啟動指令」由 `npx` 改為該完整絕對路徑。

2. **Q：Playwright 第一次啟動時需要下載瀏覽器核心？**
   * **說明**：首次執行時，Playwright 會自動在後台下載相容的 Chromium 核心，約需 30-60 秒，請耐心等待一次即可。

3. **Q：一般 Web Search 與 Playwright MCP 該如何選擇？**
   * **初學者 / 快速發想**：先使用一般 Web Search（步驟 9-1 與 9-2），零安裝即可體驗 AI 自動搜集資料的威力。
   * **企業級專案 / 需精準數據**：使用 Playwright MCP，讓 AI 如同真人分析師般即時閱覽網頁與財報，取得 100% 準確之商業情資！

---

## 🤖 手動安裝 Playwright MCP 到 Antigravity

如果你是使用 **Antigravity IDE** 或 **Antigravity CLI**，可以透過編輯 JSON 設定檔的方式將 Playwright MCP 掛載進來：

### 1. 前置需求

- **Node.js 18+**（已在終端機驗證 `node --version`、`npx --version` 可正常執行）
- **Antigravity IDE / CLI** 已安裝並可正常運行

### 2. 設定檔位置

* **全域共用（建議優先修改這個）**：
  ```bash
  ~/.gemini/config/mcp_config.json
  ```
* **IDE 專用（會自動同步，可一併檢查）**：
  ```bash
  ~/.gemini/antigravity/mcp_config.json
  ~/.gemini/antigravity-ide/mcp_config.json
  ```
* **工作區專用（只對單一專案有效）**：
  ```bash
  <你的專案目錄>/.agents/mcp_config.json
  ```

> 💡 **IDE 快速開啟捷徑**：  
> 在 Antigravity Agent 側邊欄右上角點擊 `...` ➔ `MCP Servers` ➔ `Manage MCP Servers` ➔ `View raw config` 即可直接編輯設定檔。

### 3. 配置內容

將 `mcp_config.json` 內容更新為：

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

若原本已有其他 MCP Server，請保留既有設定並在 `mcpServers` 物件中新增 `playwright` 欄位：

```json
{
  "mcpServers": {
    "existing-server": {
      "...": "..."
    },
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

### 4. 常用進階參數

若需要指定瀏覽器核心或視窗顯示模式，可調整 `args` 陣列：

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--browser",
        "chrome"
      ]
    }
  }
}
```

**常用選項對照表**：

| 需求 | 參數 | 說明 |
| :--- | :--- | :--- |
| **使用 Chrome 瀏覽器** | `--browser chrome` | 指定使用系統已安裝的 Google Chrome |
| **使用 Edge / Firefox / WebKit** | `--browser msedge` / `firefox` / `webkit` | 切換至其他瀏覽器核心 |
| **顯示真實瀏覽器視窗** | `--headless=false` | 啟動有頭模式，方便親眼觀看 AI 爬取畫面 |
| **啟用視覺截圖能力** | `--caps vision` | 賦予模型對頁面畫面進行視覺多模態理解 |

### 5. 驗證設定與套件

開啟終端機執行以下指令，確認 JSON 語法無誤且套件可正常運作：

```bash
# 驗證 JSON 格式
python3 -c "import json; print(json.load(open('$HOME/.gemini/config/mcp_config.json')))"

# 驗證 Playwright MCP CLI 是否正常
npx -y @playwright/mcp@latest --help
```
*終端機有印出 `Usage: Playwright MCP [options]` 即代表可正常啟動！*

### 6. 啟用與確認連線

1. 儲存設定檔。
2. 重新啟動 Antigravity IDE。
3. 進入 `MCP Servers` 面板，確認 **`playwright`** 狀態顯示為已連線（綠燈），即可開始調用！

