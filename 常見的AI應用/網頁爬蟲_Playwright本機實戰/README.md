📍 [常見的 AI 應用](../README.md) › **本機網頁爬蟲**

# 🕷️ 本機網頁爬蟲與動態資料蒐集（Desktop AI × Playwright）

> 💡 **為什麼一定要用「桌面版 AI ＋ 本機 Playwright」？**  
> 雲端網頁版 AI（瀏覽器上的 ChatGPT / Claude）受限於官方雲端伺服器 IP 與網路白名單，遇到 **JavaScript 動態渲染、Cloudflare 防爬、公司內網或需要帳密／2FA 登入的網頁** 時往往直接失敗。  
> 唯有使用 **桌面版 AI（Claude Desktop、ChatGPT 桌面版、Antigravity）** 搭配 **本機 Playwright**，才能直接以您自己電腦的網路環境與真實瀏覽器（Chromium）完成自動化爬取、滾動載入、人機協作登入與視覺截圖存證！

---

## 📋 第 1 步：先安裝本機前置環境（Node.js）

三套桌面版 AI 都是透過 Node.js 的 `npx` 指令來啟動微軟官方的 `@playwright/mcp@latest`，**不需要安裝 Python 或 `uv`**：

1. 前往 **[Node.js 官方網站](https://nodejs.org/)** 下載並安裝 **LTS（長期支援版本）**。
   - macOS（Homebrew）：`brew install node`
   - Windows（Winget）：`winget install OpenJS.NodeJS`
2. 打開終端機（Mac 終端機 / Windows PowerShell）輸入 `node -v` 與 `npx -v`，確認有顯示版本號即可。

> ⚠️ **Windows 使用者必看（非常重要）**：  
> Windows 電腦在安裝完 **Node.js** 或**修改 Playwright MCP 設定後，務必「重新開機」**！  
> 若沒有重新開機，Windows 的系統環境變數（`PATH`）與背景行程可能尚未更新，會導致桌面版 AI 啟動 Playwright 時找不到 `npx` 而亮紅燈失敗。

---

## 🖥️ 第 2 步：選擇您的桌面版 AI，獨立查看安裝教學

為了讓您依照自己習慣的工具快速上手，三套桌面版 AI 的 Playwright MCP 安裝步驟已**分頁整理**如下，請點選您使用的工具：

| 桌面版 AI 工具 | 說明與設定重點 | 前往獨立安裝頁 |
| :--- | :--- | :--- |
| **Claude Desktop** | 透過 `Settings ➔ Developer ➔ Edit Config` 編輯 `claude_desktop_config.json`（Free / Pro 皆可用） | [👉 01. Claude Desktop 安裝教學](./01_Claude_Desktop_Playwright安裝.md) |
| **ChatGPT 桌面版** | 透過本機 `Settings ➔ MCP servers`（Local `stdio`）或 `config.toml` 加入 Playwright | [👉 02. ChatGPT 桌面版 安裝教學](./02_ChatGPT_桌面版_Playwright安裝.md) |
| **Antigravity（桌面版）** | 透過 `mcp_config.json` 或內建 MCP 設定面板加入 `@playwright/mcp@latest` | [👉 03. Antigravity 安裝教學](./03_Antigravity_Playwright安裝.md) |

> 💡 **視窗模式小提醒**：  
> 預設啟動即為**有頭模式（Headed Mode）**，執行時會彈出真實的瀏覽器視窗，方便您確認畫面與手動輸入帳密；若不希望彈出視窗，可在 `"args"` 陣列最後面加上 `"--headless"`。

---

## 📚 第 3 步：跨產業 Playwright 實戰範例庫

安裝並確認連線成功後，直接將以下範例中的 Prompt 貼到您的桌面版 AI 對話框即可開始實戰：

| 產業／情境 | 實戰重點 | 前往查看 |
| :--- | :--- | :--- |
| **🛒 電商與零售比價** | 台灣銀行牌告匯率、momo 動態搜尋比價、競品交叉分析、**人機協作半自動登入查訂單** | [👉 電商實戰範例](./examples/ecommerce.md) |
| **💼 創投（VC）動態調研** | 科技新聞自動彙整、新創官網 JS 滾動載入與**網頁截圖存證**、雙標的橫向對比 | [👉 創投實戰範例](./examples/venture_capital.md) |
| **🌿 綠能與政府公開資訊** | 台電即時電力供需爬取、能源署／氣候變遷署動態公告追蹤、無 API 儀表板截圖存證 | [👉 綠能實戰範例](./examples/green_energy.md) |

---

🧭 [⬆ 回到：常見的 AI 應用](../README.md) ｜ [下一頁：安裝 01：Claude Desktop ➡](01_Claude_Desktop_Playwright安裝.md)
