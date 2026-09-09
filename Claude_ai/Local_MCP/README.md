# Local MCP Servers（本地端伺服器）安裝配置與操作手冊

> 🟢 **方案需求**：Free / Pro 皆適用。Claude Desktop 的 Local MCP 機制在免費帳號即開放，只需下載電腦桌面版並啟用 Developer 模式。  
> 💡 **核心概念**：**Local MCP Servers** 是直接執行在您個人電腦（Mac / Windows）上的擴充伺服器。不同於雲端託管的 Connectors，本地 MCP 能讓 Claude 存取本機檔案系統、資料庫、真實瀏覽器以及本機終端腳本，是實現「AI 操控電腦」的核心基礎。

---

## 📑 目錄導覽

1. [運作架構與核心優勢](#-運作架構與核心優勢)
2. [前置環境安裝（Node.js 與 uv）](#-前置環境安裝nodejs-與-uv)
3. [快速配置流程（claude_desktop_config.json）](#-快速配置流程)
4. [常用核心 MCP 伺服器配置範本](#-常用核心-mcp-伺服器配置範本)
5. [維運管理與排錯技巧](#-維運管理與排錯技巧)
6. [🚀 跨產業實戰應用案例庫（Industry Scenarios）](#-跨產業實戰應用案例庫industry-scenarios)
7. [觀念比較：本地 MCP vs. 遠端 Connectors](#-觀念比較本地-mcp-vs-遠端-connectors)

---

## 🏗️ 運作架構與核心優勢

```text
┌─────────────────────────────────────────────────────────────┐
│ 個人電腦本機 (Mac / Windows)                                 │
│                                                             │
│  Claude Desktop (對話介面)                                  │
│        │                                                    │
│        ▼ [MCP 協定 (標準輸入/輸出 stdio)]                    │
│  Local MCP Server (本機背景行程，如 Playwright MCP)          │
│        │                                                    │
│        ▼ [本機 API / 驅動程式]                              │
│  真實本機環境 (Chromium 瀏覽器 / 本機目錄 / 腳本執行)        │
└─────────────────────────────────────────────────────────────┘
```

### 突破「雲端網路白名單」限制
- **雲端網頁版 (`claude.ai`)**：連線工具跑在官方雲端伺服器，受限於安全性白名單政策，無法存取未經授權的網站或企業內部網路，且極易觸發目標網站的反爬機制。
- **本地 MCP (Claude Desktop)**：直接以**您個人電腦的網路環境與 IP 權限**發出請求。只要您的電腦瀏覽器開得起來的網站（包含公司內部 Intranet、需登入系統、動態 JS 渲染網頁），本地 MCP 都能順暢存取與操作。

---

## 📋 前置環境安裝（Node.js 與 uv）

大部分本地 MCP 伺服器是以 **Node.js** 或 **Python** 開發。為了讓 Claude 能以暫存或背景方式自動啟動這些伺服器，建議先於本機安裝好以下兩大執行環境：

### 1. Node.js (提供 `npx` 指令)
- **主要用途**：執行 JavaScript/TypeScript 開發的 MCP 伺服器（如 `@playwright/mcp`）。
- **安裝方式**：
  - **推薦方式（一般使用者）**：前往 [Node.js 官方網站](https://nodejs.org/) 下載安裝 **LTS（長期支援版本）**。
  - **命令列安裝**：
    - **macOS (Homebrew)**：`brew install node`
    - **Windows (Winget)**：`winget install OpenJS.NodeJS`

### 2. uv (提供 `uvx` 指令)
- **主要用途**：以極速臨時虛擬環境運行 Python 開發的 MCP 伺服器（如 `mcp-server-time`），無需手動管理 Python 環境。
- **安裝方式**：
  - **macOS / Linux**：
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    （或 `brew install uv`）
  - **Windows (PowerShell)**：
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
    （或 `winget install astral-sh.uv`）

---

## ⚙️ 快速配置流程

### 步驟 1：開啟開發者模式
1. 啟動 **Claude Desktop**。
2. 點擊左下角個人頭像 ➔ **Settings**。
3. 於左側選單點擊 **Developer**。

### 步驟 2：編輯設定檔
點擊 **Edit Config** 按鈕，系統會以預設文字編輯器開啟 `claude_desktop_config.json`。

> 📁 **設定檔本機路徑備忘**：
> - **macOS**：`~/Library/Application Support/Claude/claude_desktop_config.json`
> - **Windows**：`%APPDATA%\Claude\claude_desktop_config.json`

---

## 📦 常用核心 MCP 伺服器配置範本

將以下設定貼入 `claude_desktop_config.json` 中的 `mcpServers` 物件內：

### 1. Playwright 伺服器（動態網頁爬蟲與自動化）
由 Microsoft 官方維護，能啟動真實瀏覽器執行網頁滾動、截圖、按鈕點擊與動態內容讀取。

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

> 💡 **視窗模式提示**：
> - **預設有頭模式 (Headed)**：執行時會彈出可見的瀏覽器視窗，適合需要視覺化確認、截圖存證或人工手動登入的場合。
> - **無頭/背景模式 (Headless)**：若不希望彈出視窗干擾工作，可在 `args` 陣列加入 `"--headless"`：
>   `"args": ["@playwright/mcp@latest", "--headless"]`

### 2. Time 伺服器（本地即時時間）
提供 Claude 精確的時間感知與時區換算能力。

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

### 3. 多伺服器整合範例

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time"]
    }
  }
}
```

設定完成後，**完全關閉並重啟 Claude Desktop** 即可生效。

---

## 🛠️ 維運管理與排錯技巧

### 1. 狀態燈號判讀
在 **Settings ➔ Developer** 頁面中：
- **Running (藍色/綠色)**：表示 MCP 伺服器行程已成功啟動並與 Claude 完成握手連線。
- **View Logs**：若伺服器啟動失敗或亮紅燈，點擊此處可檢視詳細的錯誤輸出，是排查環境變數與套件安裝問題的首要步驟。
- **Managed by an extension**：若顯示由擴充套件代管，代表該伺服器是由 `Settings -> Extensions` 安裝，無法透過手動編輯 JSON 進行管理。

### 2. 避免「工具過載 (Tool Bloat)」與資源損耗
- **Token 消耗**：每個啟用的 MCP 都會將其定義注入至 System Prompt，啟用過多會壓縮 Context Window。
- **電腦效能**：像 Playwright 每次開啟瀏覽器皆會佔用 CPU 與記憶體，建議平時僅啟用當前任務所需的 **2～4 個 MCP 伺服器**。

### 3. 如何安全「停用」暫不使用的伺服器？
> ⚠️ **重要提醒**：`claude_desktop_config.json` 為標準 JSON，**不支援 `//` 或 `/* */` 註解語法**，寫入註解會導致 Claude Desktop 解析失敗。

**推薦做法（改名停用法）**：
在伺服器名稱前加入底線（例如將 `"playwright"` 改為 `"_playwright"`），Claude 啟動時會忽略非標準名稱，同時完整保留所有參數設定：
```json
{
  "mcpServers": {
    "_playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

---

## 🚀 跨產業實戰應用案例庫（Industry Scenarios）

本目錄規劃了針對不同垂直產業的真實實務 Prompt 與驗證流程。請點擊連結檢視完整教學：

| 產業賽道 | 案例文件連結 | 核心任務說明 |
| :--- | :--- | :--- |
| 💼 **創投與投資評估 (VC)** | [**創投產業實務範例**](./examples/venture_capital.md) | • 公開科技新聞爬取（半導體先進封裝、CPO 矽光子情報）<br>• 新創標的官網動態渲染、截圖存證與產品/市場/團隊分析<br>• 競品初階 DD 交叉比對矩陣 |
| 🛒 **電商與零售通路 (Retail)** | [**電商與零售實務範例**](./examples/ecommerce.md) | • 公開匯率牌告爬取（台灣銀行）<br>• 電商動態搜尋與商品比價（momo 購物網）<br>• 競品規格矩陣交叉對比<br>• 需 2FA/密碼驗證之會員後台半自動登入協作 |
| 🌐 **更多產業案例** | *持續擴充中* | 歡迎依照 `examples/` 格式新增醫療生技、金融風控、智慧製造等產業情境 |

> 💡 **如何新增自訂產業範例**：
> 1. 於 `Claude_ai/Local_MCP/examples/` 目錄下建立 `<industry_name>.md`。
> 2. 參照範例格式撰寫：業務背景 ➔ 實作 Prompt 任務 ➔ Checklist 檢核點。
> 3. 將新文件連結登錄於本表格中。

---

## ⚖️ 觀念比較：本地 MCP vs. 遠端 Connectors

| 特性 | 本地端伺服器 (Local MCP) | 雲端連接器 (Remote Connectors) |
| :--- | :--- | :--- |
| **執行主機** | 您個人的電腦本機 (Mac / PC) | 服務商官方雲端伺服器 |
| **授權驗證** | 本機系統權限 / 本地 Session | **OAuth 2.0 網頁授權** |
| **設定方式** | 編輯 `claude_desktop_config.json` | 於網頁介面點擊授權按鈕 |
| **最佳應用情境** | • 存取本機私有資料與本機目錄<br>• 存取企業內部網路 (Intranet)<br>• 驅動真實瀏覽器爬取動態網頁 | • 存取雲端 SaaS 服務（Gmail、Google Drive、GitHub、Notion、Supabase） |

---

← [返回 Claude AI 模組總覽](../README.md)
