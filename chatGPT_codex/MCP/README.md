# MCP（Model Context Protocol）

> 🔵 **方案需求**：Plus 起。CLI 設定需可編輯 `~/.codex/config.toml`。

MCP 讓 Codex 連接**本機或遠端的工具與資料來源**：公司內部 API、資料庫、文件伺服器，或任何沒有現成 plugin 的系統。

> [!IMPORTANT]
> **這是最後手段，不是第一選擇。** 先確認 [Connectors](../Connectors/README.md) 的三層判斷：有現成 app / plugin 就用現成的。自建 MCP 意味著你要自己負責認證、逾時、重試、稽核與錯誤處理。

---

## 🧠 MCP 在做什麼

MCP 是一套開放協定，把「外部能力」包裝成 Codex 看得懂的**工具（tools）**。

```text
Codex  ──呼叫工具──▶  MCP server  ──▶  你的資料庫 / API / 檔案系統
       ◀──回傳結果──
```

Codex 只看到工具的**名稱、描述與參數 schema**；MCP server 負責真正去做事。

---

## 🔌 兩種 MCP server

| 類型 | 怎麼跑 | 適合 | 設定關鍵 |
| :--- | :--- | :--- | :--- |
| **STDIO**（本機程序） | Codex 在你電腦上啟動一個子程序 | 本機檔案、本機資料庫、離線工具 | `command`、`args`、`env` |
| **HTTP**（遠端端點） | 連到一個網址 | 公司內部服務、SaaS、團隊共用 | `url`、bearer token / OAuth |

---

## ⚡ 最快的加入方式：CLI

```bash
# 基本語法
codex mcp add <server-name> --env VAR1=VALUE1 -- <stdio-command>

# 實例：加入 Context7 文件查詢伺服器
codex mcp add context7 -- npx -y @upstash/context7-mcp
```

### 管理指令

```bash
codex mcp list              # 列出已設定的伺服器
codex mcp login <name>      # 對需要 OAuth 的伺服器進行認證
codex mcp --help            # 查看全部可用子指令
```

在 Codex 對話中輸入 **`/mcp`** 可查看目前生效的伺服器與工具。

---

## 📝 用 `config.toml` 設定

編輯 `~/.codex/config.toml`，在 `[mcp_servers.<server-name>]` 表格中設定。

### STDIO 伺服器

```toml
[mcp_servers.tideflow_db]
command = "python"
args    = ["-m", "tideflow_mcp.server"]

# 用環境變數傳遞連線資訊，不要把密碼寫在這裡
[mcp_servers.tideflow_db.env]
TIDEFLOW_DB_HOST = "db.internal.tideflow.example"
TIDEFLOW_DB_USER = "codex_readonly"
```

### HTTP 伺服器（Bearer token）

```toml
[mcp_servers.tideflow_api]
url = "https://mcp.internal.tideflow.example/v1"

# 只寫「環境變數名稱」，不要寫 token 本身
bearer_token_env_var = "TIDEFLOW_MCP_TOKEN"
```

### HTTP 伺服器（OAuth）

```toml
[mcp_servers.partner_service]
url = "https://mcp.partner.example/v1"
```

設定完成後執行認證：

```bash
codex mcp login partner_service
```

### 自訂 HTTP 標頭

```toml
[mcp_servers.tideflow_api]
url = "https://mcp.internal.tideflow.example/v1"

[mcp_servers.tideflow_api.http_headers]
X-Tenant-Id = "tideflow-prod"

# 從環境變數帶入的標頭
[mcp_servers.tideflow_api.env_http_headers]
X-Api-Key = "TIDEFLOW_API_KEY"
```

> [!WARNING]
> **絕不把 token、密碼或 API key 直接寫進 `config.toml`。** 一律用 `bearer_token_env_var` 或 `env_http_headers` 引用環境變數名稱。專案層的 `.codex/config.toml` 若提交進 Git，任何有 repo 讀取權的人都看得到。

---

## 🔐 工具核准模式

用 `default_tools_approval_mode` 控制工具執行前要不要問你：

| 值 | 行為 | 建議 |
| :--- | :--- | :--- |
| `auto` | 直接執行，不詢問 | ⚠️ 只給完全信任且唯讀的伺服器 |
| `prompt` | **每次使用都詢問** | ✅ 初次接入時用這個 |
| `writes` | 只在非唯讀工具時詢問 | ✅ 日常實務的平衡點 |
| `approve` | 需要完整核准流程 | 高風險環境 |

```toml
[mcp_servers.tideflow_db]
command = "python"
args    = ["-m", "tideflow_mcp.server"]
default_tools_approval_mode = "writes"   # 讀不問、寫才問
```

---

## 🏗️ 設計自家 MCP server 的原則

如果你要為公司內部系統寫 MCP server，這五條規則決定了它好不好用：

### 1. 工具名稱與描述要清楚

Codex 靠描述決定要不要呼叫。

| ❌ | ✅ |
| :--- | :--- |
| `query` — 「查詢資料」 | `search_shipments` — 「依日期區間與區域代碼查詢配送單，回傳最多 100 筆。不含個資欄位。」 |
| `do_action` | `create_shipment_note`、`cancel_shipment`（拆成具名工具） |

### 2. 參數使用嚴格 schema

明確的型別、必填欄位與列舉值，能大幅減少呼叫錯誤。

```json
{
  "name": "search_shipments",
  "inputSchema": {
    "type": "object",
    "properties": {
      "start_date": { "type": "string", "format": "date" },
      "end_date":   { "type": "string", "format": "date" },
      "region":     { "type": "string", "enum": ["North", "Central", "South", "East"] },
      "limit":      { "type": "integer", "minimum": 1, "maximum": 100, "default": 50 }
    },
    "required": ["start_date", "end_date"],
    "additionalProperties": false
  }
}
```

### 3. 查詢與寫入工具分開

```text
✅ search_shipments      （唯讀）
✅ get_shipment_detail   （唯讀）
✅ update_shipment_note  （寫入，需核准）
❌ shipment_tool(action="delete")   ← 不要用參數區分危險程度
```

**理由**：工具核准模式的 `writes` 選項要能區分讀寫，才有意義。

### 4. 回傳最少必要資料

> [!WARNING]
> **MCP 回傳的內容會進入模型的上下文。** 回傳整張資料表不只浪費 token，還可能把個資、憑證或商業機密送進不該去的地方。
>
> - 預設不回傳個資欄位（姓名、電話、地址、身分證號）
> - 需要時提供遮罩版本（`王**`、`09xx-xxx-123`）
> - 設定合理的筆數上限，並在超過時明確告知被截斷

### 5. 明確處理認證、逾時、重試與錯誤

錯誤訊息要能讓模型判斷下一步：

```text
❌ "Error"
❌ "Something went wrong"
✅ "查無資料：指定區間 2026-08-01 ~ 2026-08-31 內無符合條件的配送單。"
✅ "權限不足：此 token 無 shipments:write 權限，請聯繫管理員。"
✅ "逾時：查詢超過 30 秒，請縮小日期區間後重試。"
```

---

## 🧪 課堂練習：安全地接第一個 MCP server

1. 選一個**唯讀、公開**的 MCP server（例如文件查詢類），不要用內部系統。
2. 加入並設定為每次詢問：
   ```bash
   codex mcp add context7 -- npx -y @upstash/context7-mcp
   ```
   ```toml
   [mcp_servers.context7]
   default_tools_approval_mode = "prompt"
   ```
3. 在對話中輸入 `/mcp`，確認伺服器與工具清單。
4. 執行一個只讀 task，觀察每次工具呼叫的核准提示。
5. 讀懂它實際呼叫了什麼、回傳了什麼，再考慮改成 `writes`。

---

## 🔄 與 Claude Local MCP 的對照

| 面向 | Claude Desktop | Codex |
| :--- | :--- | :--- |
| 設定檔 | `claude_desktop_config.json` | **`~/.codex/config.toml`** |
| 格式 | JSON | TOML |
| 加入方式 | 手動編輯 JSON | **`codex mcp add` 指令** 或編輯 TOML |
| 查看現況 | 重啟後看介面 | **`/mcp`** 或 `codex mcp list` |
| 工具核准 | 逐次詢問 | **四段式 `default_tools_approval_mode`** |
| 方案門檻 | 🟢 Free | 🔵 **Plus 起** |

---

## 小結

| 要點 | 說明 |
|---|---|
| 何時用 MCP | 沒有現成 app / plugin 時的最後手段 |
| 兩種伺服器 | STDIO（本機程序）、HTTP（遠端端點） |
| 加入方式 | `codex mcp add` 或 `~/.codex/config.toml` |
| 認證 | `bearer_token_env_var` 或 `codex mcp login`，**絕不寫死 token** |
| 核准 | 初期 `prompt`，穩定後 `writes` |
| 設計原則 | 具名工具、嚴格 schema、讀寫分離、最少回傳、明確錯誤 |

> 欄位與 CLI 指令可能更新。請依 [官方 MCP 文件](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) 設定，**不要照抄來源不明的 token 或啟動命令**。

**官方說明**：[MCP](https://learn.chatgpt.com/docs/extend/mcp) · [Advanced config](https://learn.chatgpt.com/docs/config-file/config-advanced)

---

← [返回上層：ChatGPT Codex 索引](../README.md)
