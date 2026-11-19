📍 [常見的 AI 應用](../README.md) › [本機網頁爬蟲](README.md) › **安裝 01：Claude Desktop**

# 🟣 01. Claude Desktop 安裝 Playwright MCP 教學

> 🟢 **方案需求**：Claude **Free / Pro** 帳號皆可使用，只需下載安裝電腦桌面版（Mac / Windows）。

---

## 📋 安裝前確認
1. 本機已安裝 **[Node.js (LTS)](https://nodejs.org/)**。
2. ⚠️ **Windows 使用者提醒**：安裝完 Node.js 後請先**重新開機**一次，確保 `npx` 可在全系統路徑被正確呼叫。

---

## ⚙️ 設定步驟

### 步驟 1：開啟開發者設定檔
1. 啟動 **Claude Desktop**。
2. 點擊左下角個人頭像 ➔ **Settings**。
3. 於左側選單點擊 **Developer**，點擊 **Edit Config** 按鈕，系統會開啟 `claude_desktop_config.json`。

> 📁 **設定檔本機路徑參考**：
> - **macOS**：`~/Library/Application Support/Claude/claude_desktop_config.json`
> - **Windows**：`%APPDATA%\Claude\claude_desktop_config.json`

### 步驟 2：貼入 Playwright MCP 設定
將以下 JSON 內容貼入 `claude_desktop_config.json`（若檔案原本有其他設定，請將 `"playwright": { ... }` 併入 `"mcpServers"` 內）：

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

> 💡 **選用設定（背景無頭模式）**：若不希望每次爬取都彈出瀏覽器視窗，可改為：  
> `"args": ["@playwright/mcp@latest", "--headless"]`  
> *（注意：若要操作「人機協作手動登入 / 2FA」範例，請**不要**加 `--headless`）*

### 步驟 3：重啟生效（Windows 修改後請重開機）
* **macOS**：儲存檔案後，**完全結束 Claude Desktop（`Cmd + Q`）再重新開啟**。
* **Windows**：儲存檔案後，建議直接**重新開機（Restart）**，確保 Playwright 瀏覽器驅動與環境設定完整載入。

---

## ✅ 驗證連線成功
1. 回到 Claude Desktop 的 **Settings ➔ Developer**，確認 `playwright` 旁邊顯示為 **Running（藍色／綠色燈號）**。
2. 在對話框輸入以下測試指令，若能自動彈出瀏覽器並回傳匯率表格即完成安裝：
   ```text
   請使用 Playwright 開啟台灣銀行牌告匯率（https://rate.bot.com.tw），幫我整理今日美金與日圓的現金買入／賣出匯率。
   ```

---

🧭 [⬆ 回到：本機網頁爬蟲](README.md) ｜ [下一頁：安裝 02：ChatGPT 桌面版 ➡](02_ChatGPT_桌面版_Playwright安裝.md)
