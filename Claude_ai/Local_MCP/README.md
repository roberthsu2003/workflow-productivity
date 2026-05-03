# Local MCP Servers（本地端伺服器）

**Local MCP Servers** 是執行在您個人電腦（Mac/PC）上的擴充服務。與雲端託管的 Connectors 不同，本地 MCP 讓 Claude 能夠存取您**本機的檔案、資料庫、甚至是執行本機的腳本與指令**。

這是在 Claude Desktop 上進行深度客製化、實現「AI 操控電腦」的核心機制。

---

## 如何設定本地 MCP？

### 1. 進入開發者模式
- 開啟 **Claude Desktop**。
- 點擊左下角頭像 -> **Settings**。
- 在左側選單最下方找到 **Developer**。

### 2. 修改設定檔 (Edit Config)
- 點擊 **Edit Config** 按鈕，系統會以預設編輯器開啟 `claude_desktop_config.json`。
- 這個檔案定義了 Claude 啟動時要同時開啟哪些 MCP 伺服器。

### 3. 設定範例 (以 Time 伺服器為例)
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
