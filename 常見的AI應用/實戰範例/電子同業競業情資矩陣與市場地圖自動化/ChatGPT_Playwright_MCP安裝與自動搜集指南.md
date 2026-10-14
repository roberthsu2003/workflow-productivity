# ChatGPT 桌面版安裝 Playwright MCP 與情資自動搜集指南

> 💡 **核心價值**：在進行「39 家上市櫃同業競爭情資與動能矩陣」分析時，資料搜集通常有兩種路徑：
> 1. **一般方法（基礎版）**：利用 ChatGPT / Claude / Gemini 內建的網路搜尋（Web Search），由 AI 自動搜尋公開財經新聞與概括資料。
> 2. **Playwright MCP 方法（專業進階版）**：在 ChatGPT 桌面版中掛載 **Playwright MCP 伺服器**，賦予 AI 直接操控真實瀏覽器的能力，能深入執行 JavaScript 動態渲染網頁（如公開資訊觀測站 MOPS、券商專業資料庫），精準截取表格與最新財報數據，徹底杜絕數據通靈！

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

## 🚀 如何在對話中呼叫 Playwright MCP 搜集 39 家同業情資？

當您完成 Playwright MCP 設定後，可以在 ChatGPT 對話視窗中，將原本的提示詞升級為指定使用 Playwright 的高階指令：

### 專屬提示詞範例（搭配 Playwright MCP）：

```text
你好，我已經在 ChatGPT 中啟用了 Playwright MCP 工具。
我需要你扮演資深科技產業首席分析師，幫我針對上傳的《素材_同業清單_被動元件.xlsx》（39 家台灣上市櫃被動元件廠商），進行深度競業情資搜集：

請依序執行以下工作：
1. 【調用 Playwright 瀏覽器工具】：針對名單中的關鍵同業（例如 6449 鈺邦、4760 勤凱、3357 臺慶科、3090 日電貿、2327 國巨 等），透過 Playwright 訪問公開資訊觀測站（MOPS）或主要財經網站，精準獲取其「最新單月營收 YoY%」以及在「AI 伺服器 / 車用電子」的最新法說會佈局亮點。
2. 【標準化產業板塊】：將 39 家廠商標準重組為電容、電感、電阻保護、頻率射頻、上游材料、代理通路六大板塊。
3. 【動能評級分群】：依據爬梳到的真實營收與產品規格，劃分 🔥高成長領先、🟢穩健獲利、⚠️轉型承壓 三大動能標籤。
4. 【輸出 Markdown 檢核表】：請將搜集與驗證後的完整 39 家資料整理成《被動元件同業競業情資收集檢核表.md》輸出，並停下來等待我確認。在我回覆「確認無誤」之前，請勿直接生成 Excel 檔案。
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
