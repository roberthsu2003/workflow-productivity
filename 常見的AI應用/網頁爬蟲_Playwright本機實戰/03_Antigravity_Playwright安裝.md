# 🔵 03. Antigravity 安裝 Playwright MCP 教學

> 📌 **適用環境**：Google **Antigravity** 桌面版 / IDE。

---

## 📋 安裝前確認
1. 本機已安裝 **[Node.js (LTS)](https://nodejs.org/)**。
2. ⚠️ **Windows 使用者提醒**：安裝完 Node.js 或修改 `mcp_config.json` 的 Playwright 設定後，**務必重新開機**，確保本機 `npx` 指令與瀏覽器程序可正常啟動。

---

## ⚙️ 設定步驟

### 步驟 1：開啟 Antigravity 的 `mcp_config.json`
1. 啟動 **Antigravity**。
2. 打開 **MCP 設定面板 / Manage MCP Servers**，點擊開啟 **`mcp_config.json`** 設定檔。

### 步驟 2：貼入 Playwright MCP 設定
將以下設定加入 `mcp_config.json` 的 `"mcpServers"` 物件中：

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

> 💡 **選用參數**：
> - **背景無頭模式**：`"args": ["-y", "@playwright/mcp@latest", "--headless"]`
> - **指定瀏覽器**：`"args": ["-y", "@playwright/mcp@latest", "--browser=firefox"]`
> - **模擬手機裝置**：`"args": ["-y", "@playwright/mcp@latest", "--device=iPhone 15"]`

### 步驟 3：儲存並重啟（Windows 修改後請重開機）
* **macOS**：儲存 `mcp_config.json` 後，重新載入或重啟 Antigravity。
* **Windows**：儲存 `mcp_config.json` 後，建議**重新開機**，確保環境變數與 Playwright Chromium 驅動完整載入。

---

## ✅ 驗證連線成功
1. 在 Antigravity MCP 面板確認 `playwright` 狀態燈號亮起綠燈（或於對話框輸入 `/mcp` 檢查）。
2. 輸入以下測試指令，確認能自動開啟真實瀏覽器並回傳結果：
   ```text
   請使用 Playwright 開啟台灣銀行牌告匯率網頁（https://rate.bot.com.tw），整理今日美金與日圓的現金買入與賣出匯率表格。
   ```

---

[← 返回本機 Playwright 網頁爬蟲實戰指南](./README.md)
