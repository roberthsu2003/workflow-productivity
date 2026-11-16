# 🟢 02. ChatGPT 桌面版 安裝 Playwright MCP 教學

> 📌 **適用版本**：ChatGPT Desktop（macOS / Windows 桌面應用程式，包含開發者 / Codex 環境）。

---

## 📋 安裝前確認
1. 本機已安裝 **[Node.js (LTS)](https://nodejs.org/)**。
2. ⚠️ **Windows 使用者提醒**：安裝完 Node.js 或修改 Playwright 設定後，**務必重新開機**，避免桌面版找不到 `npx` 環境變數。

---

## ⚙️ 設定步驟（Local `stdio` 本機直連模式）

### 步驟 1：開啟桌面版 MCP 設定
1. 啟動 **ChatGPT 桌面版**。
2. 進入應用程式設定頁面（**Settings ➔ MCP servers** 或本機設定檔 `config.toml` / 開發者設定面板），選擇新增本機 `stdio` 類型的 MCP 伺服器。

### 步驟 2：填入 Playwright MCP 設定
* **JSON 設定方式**（若設定介面支援貼入 JSON）：
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

* **表單欄位填入方式**（若為圖形化新增介面）：
  * **Name**：`playwright`
  * **Transport / Type**：`stdio`（本機標準輸入輸出）
  * **Command**：`npx`
  * **Arguments**：`@playwright/mcp@latest`

> 💡 **選用設定（無頭模式）**：若不需要看到瀏覽器視窗，可在參數最後加上 `--headless`。若要操作人工登入網站，請維持預設有頭模式。

### 步驟 3：重啟生效（Windows 修改後請重開機）
* **macOS**：儲存後完全退出 ChatGPT 桌面版再重新開啟。
* **Windows**：儲存設定後請**重新開機**，讓 Playwright 背景行程與系統路徑正確生效。

---

## ✅ 驗證連線成功
在 ChatGPT 桌面版開啟新對話（確認已勾選／啟用 `playwright` 工具），輸入以下指令測試：
```text
請使用 Playwright 開啟台灣銀行牌告匯率（https://rate.bot.com.tw），擷取今日美金與日圓匯率並整理成 Markdown 表格。
```

---

[← 返回本機 Playwright 網頁爬蟲實戰指南](./README.md)
