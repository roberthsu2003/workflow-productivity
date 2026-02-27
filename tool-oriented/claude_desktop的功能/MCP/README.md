# MCP (Model Context Protocol)

![MCP](./images/mcp流程圖.png)

## 說明MCP的運作原理影片連結：[MCP 運作原理](https://youtu.be/1UQ8uz4kuIc?si=emdXD4P_BB-_X_hb)

## MCP 架構說明

**Claude Desktop** 是 **MCP Client**，它通過 **MCP Server**（伺服器）來擴展功能。

### 架構組成

- **MCP Client（Claude Desktop）**：負責與使用者互動，並向 MCP Server 發送請求
- **MCP Server**：提供具體的功能實現，例如存取檔案系統、連接資料庫等

### MCP Server 的類型

1. **本地端 MCP Server**：在您的電腦上運行
2. **外部 MCP Server**：遠端服務或雲端服務

## 本地端 MCP Server 環境需求

要在本地端運行 MCP Server，您需要安裝以下開發環境：

### 必要工具

1. **Node.js**
   - MCP Server 通常使用 Node.js 開發
   - 安裝方式：前往 [Node.js 官網](https://nodejs.org/) 下載安裝，或使用套件管理器：
     ```bash
     # macOS (使用 Homebrew)
     brew install node
     
     # 驗證安裝
     node --version
     npm --version
     ```

2. **uv**（Python 套件管理器）
   - 用於管理 Python 開發的 MCP Server
   - 安裝方式：
     ```bash
     # macOS/Linux
     curl -LsSf https://astral.sh/uv/install.sh | sh
     
     # 驗證安裝
     uv --version
     ```

### 選擇性工具

- **Python**：部分 MCP Server 使用 Python 開發
- **Git**：用於下載和管理 MCP Server 專案

## MCP Server 的來源

### 使用本地端 MCP Server

1. **從 npm 安裝**（Node.js 版本）：
   ```bash
   npm install -g @modelcontextprotocol/server-filesystem
   ```

2. **從 Python 套件安裝**：
   ```bash
   pip install mcp-server-filesystem
   ```

3. **從 GitHub 下載並自行編譯**：
   ```bash
   git clone https://github.com/modelcontextprotocol/servers.git
   cd servers/src/filesystem
   npm install
   ```

### 使用外部 MCP Server

- 某些 MCP Server 提供雲端服務版本
- 透過 HTTP/HTTPS 連接到遠端 MCP Server
- 通常需要 API Key 或 OAuth 認證

## MCP 伺服器的功能

MCP 伺服器讓 Claude Desktop 能夠：

1. **連接外部工具和服務**
   - Google Drive、Slack、GitHub 等
   - 本地檔案系統
   - 資料庫和 API

2. **擴展 Claude 的能力**
   - 讀取和搜尋您的文件
   - 執行程式碼
   - 查詢資料庫
   - 自動化工作流程

## 管理 MCP 伺服器

您可以在 Claude Desktop 的設定檔中管理這些擴充功能：

### 設定位置

在 Claude Desktop 應用程式中：
- **設定位置**：`設定` → `Developer` → `MCP`
- 或直接編輯設定檔：
  - **Mac**：`~/Library/Application Support/Claude/claude_desktop_config.json`
  - **Windows**：`%APPDATA%\Claude\claude_desktop_config.json`

### 配置範例

#### 本地端 MCP Server 配置（使用 Node.js）

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "node",
      "args": [
        "/path/to/mcp-server-filesystem/dist/index.js"
      ],
      "env": {
        "ALLOWED_DIRECTORIES": "/Users/yourname/Documents"
      }
    }
  }
}
```

#### 本地端 MCP Server 配置（使用 Python/uv）

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "uv",
      "args": [
        "run",
        "mcp-server-filesystem"
      ]
    }
  }
}
```

#### 外部 MCP Server 配置

```json
{
  "mcpServers": {
    "external-service": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

## 常見的 MCP 伺服器

- **檔案系統存取**：讀取本地檔案
- **Google Drive**：存取雲端文件
- **Git**：程式碼版本控制
- **資料庫連接**：查詢 SQL 資料

## 與 Connectors 的差異

- **Connectors**：主要用於連接第三方服務（如 Notion、Linear），通常透過 UI 介面設定
- **MCP 伺服器**：更底層的擴展機制，需要手動配置設定檔，適合開發者和進階用戶

---

## 實際操作範例

以下是 2 個實際操作範例，涵蓋本地檔案系統整理和新聞資訊取得。每個範例都包含詳細的操作步驟和可直接複製貼上使用的對話範例：

### 📌 [範例 1：使用本地檔案系統 MCP Server 整理下載資料夾](./案例1-使用本地檔案系統MCP整理下載資料夾.md)

**目標：** 使用本地檔案系統 MCP Server 整理混亂的下載資料夾

**適用對象：**
- **學生**：整理下載的課程資料和作業檔案
- **上班族**：整理下載的工作文件和資料
- **一般使用者**：定期整理下載資料夾，保持整潔

**教學重點：**
- 展示如何設定本地檔案系統 MCP Server
- 學習如何使用 Claude 自動分類和整理檔案
- 了解檔案管理的自動化流程

**快速預覽：**
1. 安裝 Node.js 和設定 MCP Server
2. 設定 Claude Desktop 配置檔
3. 要求 Claude 自動分類檔案
4. 整理檔案名稱和刪除重複檔案

**相關功能：**
- 檔案分類（圖片、文件、影片等）
- 檔案重新命名
- 找出重複檔案
- 建立資料夾結構

---

### 📌 [範例 2：使用新聞摘要 MCP Server 獲取最新資訊](./案例2-使用新聞摘要MCP獲取最新資訊.md)

**目標：** 使用新聞摘要 MCP Server 取得最新新聞資訊並整理摘要

**適用對象：**
- **學生**：收集課程報告和研究所需的時事資料
- **上班族**：追蹤產業動態和最新趨勢
- **一般使用者**：追蹤感興趣主題的最新資訊

**教學重點：**
- 展示如何設定新聞摘要 MCP Server
- 學習如何使用外部 API（NewsAPI）
- 了解如何整理和分析新聞資訊

**快速預覽：**
1. 註冊 NewsAPI 取得 API Key
2. 設定 Claude Desktop 配置檔
3. 要求 Claude 搜尋和整理新聞
4. 生成每日新聞摘要報告

**相關功能：**
- 搜尋特定主題的新聞
- 整理新聞摘要
- 比較不同主題的新聞
- 生成每日新聞報告