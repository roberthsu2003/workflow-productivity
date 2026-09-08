# Settings（設定）：權限、Sandbox 與 `config.toml`

> 🟢 **方案需求**：Free（權限與 sandbox 設定全方案可用；MCP 與雲端相關設定需 🔵 Plus 起）

在 Claude，Settings 是「解鎖隱藏能力」的開關。在 Codex，Settings 是**安全閘門**——它決定這個代理能讀哪些檔案、能改哪些檔案、能不能上網、要不要先問你。

> [!IMPORTANT]
> **請在讓 Codex 動手之前先讀完這一章。** Codex 預設就會修改你的檔案並執行命令。權限設錯的代價不是「答案不好」，而是「檔案被改壞」。

---

## 🔐 三種權限模式（Permission Modes）

Codex 的權限由兩個獨立概念組成：**sandbox（能碰哪些檔案／網路）** 與 **approval policy（要不要先問你）**。官方把常見組合包成三個模式：

| 模式 | Sandbox | Approval | 審核者 | 它能做什麼 |
| :--- | :--- | :--- | :---: | :--- |
| **Ask for Approval**<br>（預設，建議教學用） | `workspace-write` | `on-request` | 你 | 讀寫目前 workspace 內的檔案、執行例行本機命令。**要上網或跨出 workspace 邊界前會停下來問你。** |
| **Approve for Me**<br>（自動審核） | `workspace-write` | 自動 | 系統 | 檔案範圍同上，但額外權限請求由系統自動審核，不中斷你。 |
| **Full Access** | 無限制 | 不需核准 | — | 可修改電腦上任何檔案、可直接連網執行命令。 |

> [!WARNING]
> **Full Access 與 Approve for Me 有明確的安全風險。**
> - 課堂與初學一律使用 **Ask for Approval**。
> - 只有在「乾淨的容器 / 拋棄式 VM / 已完整 commit 的 repo」中才考慮 Full Access。
> - 一旦開啟 Full Access，網頁內容或檔案裡的惡意指令（prompt injection）就有機會直接對你的電腦生效。

### 怎麼切換

- **ChatGPT 桌面版**：`Settings` → `General` → `Permissions`
- **Codex CLI**：在對話中輸入 `/permissions`
- **設定檔**：在 `config.toml` 中直接指定 `sandbox_mode` 與 `approval_policy`

---

## 📁 Sandbox 範圍怎麼理解

`workspace-write` 的「workspace」指的是**目前 project 的工作目錄**（加上暫存目錄），不是整台電腦。

```text
~/projects/tideflow-portal/     ← workspace 根目錄，可讀可寫
├── src/                        ✓ 可改
├── tests/                      ✓ 可改
└── .env                        ⚠ 可讀可改 —— 請見下方警告

~/Documents/報稅資料/            ✗ 需要核准才能碰
/etc/                           ✗ 需要核准才能碰
```

> [!WARNING]
> **Sandbox 不會自動保護 workspace 內的機密。** `.env`、憑證、客戶名單只要放在 workspace 裡，`workspace-write` 就碰得到。請用 `.gitignore` 之外的手段處理：把機密移出 workspace，或在 `AGENTS.md` 明文禁止讀寫，並保持 Ask for Approval。

---

## 🗂️ `config.toml`：設定檔的位置與優先序

| 層級 | 路徑 | 用途 |
| :--- | :--- | :--- |
| 使用者 | `~/.codex/config.toml` | 你的個人預設值，跨所有專案生效 |
| 專案 | `<repo>/.codex/config.toml` | 該 repo 的覆寫值，可提交給團隊共用 |

**優先序（後者被前者覆蓋）**：

```text
CLI 旗標  →  專案 config  →  profiles  →  使用者 config  →  系統 config  →  內建預設值
```

### 常用設定一覽

| 設定鍵 | 用途 | 範例值 |
| :--- | :--- | :--- |
| `model` | 預設模型 | `"gpt-5.6"` |
| `model_reasoning_effort` | 推理強度 | `"low"` / `"medium"` / `"high"` |
| `sandbox_mode` | 檔案存取範圍 | `"workspace-write"` |
| `approval_policy` | 核准行為 | `"on-request"` |
| `web_search` | 網路搜尋來源 | `"cached"` |
| `project_doc_max_bytes` | `AGENTS.md` 讀取上限 | `32768`（32 KiB，預設） |
| `[mcp_servers.<name>]` | MCP 伺服器 | 見 [MCP 章節](../MCP/README.md) |

### 教學建議的 `~/.codex/config.toml`

```toml
# 教學／日常安全預設值
model = "gpt-5.6"
model_reasoning_effort = "high"

# 只能寫入專案目錄，跨界或上網前先問我
sandbox_mode   = "workspace-write"
approval_policy = "on-request"

# 網路搜尋走快取，減少不必要的外連
web_search = "cached"

[features]
hooks = true

# 只把必要的環境變數帶進子行程，避免 token 外洩
[shell_environment_policy]
ignore_default_excludes = false

[shell_environment_policy.filters]
PATH = "include"
HOME = "include"
```

> [!IMPORTANT]
> **不要把 API key、token 寫進 `config.toml`。** 改用環境變數或系統的 secret store，在設定中只引用變數名稱。`.codex/config.toml` 若提交進 Git，任何有 repo 讀取權的人都看得到。

---

## 🔀 個人偏好 vs. 團隊規則：該寫在哪裡？

這是 Codex 最容易搞混的地方。三個檔案各有分工：

| 我想設定的東西 | 寫在哪 | 會不會提交進 Git |
| :--- | :--- | :---: |
| 模型、推理強度、快捷鍵、通知 | `~/.codex/config.toml` | ✗ 個人的 |
| 這個 repo 的 sandbox 與核准政策 | `<repo>/.codex/config.toml` | ✓ 團隊共用 |
| 建置命令、架構邊界、程式風格、驗收要求 | `<repo>/AGENTS.md` | ✓ 團隊共用 |
| 這一次任務的臨時要求 | 直接寫在 task 裡 | — |

> 詳見 [Agent Configuration 章節](../Agent_Configuration/README.md)。原則是：**設定檔管「能力邊界」，`AGENTS.md` 管「工作規範」，task 管「這一次要做什麼」。**

---

## 📋 功能對應清單：我要如何開啟……？

- **我要調整 Codex 能不能改我的檔案** → `Settings` → `General` → `Permissions`，或 CLI 輸入 `/permissions`
- **我要串接 Google Drive、GitHub、Canva** → `Settings` → `Apps / Plugins`（見 [Connectors](../Connectors/README.md)）
- **我要接自家內部 API 或資料庫** → 編輯 `~/.codex/config.toml` 的 `[mcp_servers.*]`（見 [MCP](../MCP/README.md)）
- **我要讓手機可以交辦任務給這台電腦** → `Settings` → `Connections`（見 [Remote](../Remote/README.md)）
- **我要管理訂閱方案或帳單** → ChatGPT 帳號設定的 `Billing`

---

## ✅ 課堂檢查清單

開始任何實作前，請學員逐項確認：

- [ ] 權限模式是 **Ask for Approval**
- [ ] 練習用的 repo 已 `git commit` 或已備份（Codex 改壞時可以 `git restore`）
- [ ] 練習資料夾裡**沒有**真實的 `.env`、客戶名單或憑證
- [ ] 知道 `Ctrl/Cmd + C`（CLI）或介面上的停止鍵在哪
- [ ] 已閱讀本章的 Full Access 警告

---

## 小結

| 概念 | Claude 對應 | Codex 的差異 |
|---|---|---|
| 功能開關 | Settings → Capabilities | Codex 幾乎沒有「功能開關」，改為**權限模式** |
| 檔案存取 | 上傳檔案到對話 | 直接讀寫本機 workspace |
| 安全邊界 | 由平台代管 | **由你設定**，設錯後果自負 |
| 團隊規則 | Project Custom Instructions | `AGENTS.md`（可依目錄層層覆寫） |

**官方說明**：[Permissions](https://learn.chatgpt.com/docs/permission-modes) · [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic) · [Sandboxing](https://learn.chatgpt.com/docs/security-administration)

---

← [返回上層：ChatGPT Codex 索引](../README.md)
