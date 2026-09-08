# ChatGPT Codex 教學講義

這份講義以 **ChatGPT 桌面版中的 Codex** 為主軸，分為「基礎核心單元」與「進階與代理功能」兩大部分，各單元皆清楚標示適用方案，方便對照使用。內容依 `Claude_ai` 的功能地圖建立，但採用 OpenAI 實際的名稱與操作方式。

> 🧭 想先了解整套資料夾如何組成，請看 [架構總覽](./ARCHITECTURE.md)；維護者可執行 `python3 chatGPT_codex/tools/validate_structure.py` 做完整性檢查。
>
> 🧪 學生可從[完整離線練習專案](./student-lab/README.md)開始；卡關時看[除錯手冊](./Troubleshooting/README.md)，完成後再開[參考答案](./Answer_Key/README.md)。沒有付費方案或外部服務權限，也能用偽資料完成核心學習目標。
> 外部服務章節統一依[離線實作模式](./Offline_Mode/README.md)完成，真實帳號連線只作選修展示。

> **官方來源**：[Codex 文件首頁](https://learn.chatgpt.com/docs) · [Pricing](https://learn.chatgpt.com/docs/pricing) · [Features 總覽](https://learn.chatgpt.com/docs/features) · [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
>
> 最後查核：2026-09-08。Codex 改版頻繁，授課前請以官方 [Changelog](https://learn.chatgpt.com/docs/changelog) 與 [Feature Maturity](https://learn.chatgpt.com/docs/feature-maturity) 為準。

---

## 🎯 方案速覽：Free / Go / Plus / Pro / Business

OpenAI 的方案切分比 Claude 細，共有五個常見層級。授課時最重要的分界線是 **Plus（$20）**——多數雲端與代理功能都從這一層才開始提供。

| 能力 | 🟢 Free | 🟡 Go<br>$8 | 🔵 Plus<br>$20 | 🟣 Pro<br>$100／$200 | 🏢 Business+ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 基本對話 / Web search / 檔案上傳 | ✓ | ✓ | ✓ | ✓ | ✓ |
| Codex 基本任務（讀檔、改檔、跑命令） | ✓（額度低） | ✓ | ✓ | ✓ | ✓ |
| Projects（專案與知識來源） | ✓ | ✓ | ✓ | ✓ | ✓ |
| `AGENTS.md` 專案規則 | ✓ | ✓ | ✓ | ✓ | ✓ |
| Skills（含自訂 `SKILL.md`） | ✓ | ✓ | ✓ | ✓ | ✓ |
| Codex CLI / IDE extension | ✓ | ✓ | ✓ | ✓ | ✓ |
| MCP（本機與遠端工具） | — | — | ✓ | ✓ | ✓ |
| **Plugins**（app 整合套件） | — | — | ✓（部分第一方受限） | ✓ | ✓ |
| **Image generation / Visualizations** | 有限 | 有限 | ✓ | ✓ | ✓ |
| **Voice** | — | — | ✓ | ✓ | ✓ |
| **雲端整合**（GitHub code review、Slack） | — | — | ✓ | ✓ | ✓ |
| **Codex cloud / Remote 跨裝置** | — | — | ✓ | ✓ | ✓ |
| **Sites**（發佈網站，public beta） | — | — | ✓ | ✓ | ✓ |
| **Scheduled tasks / Automations** | — | — | ✓ | ✓ | ✓ |
| 模型選擇（GPT‑5.6 Sol／Terra／Luna） | 受限 | 受限 | ✓ | ✓ | ✓ |
| GPT‑5.3‑Codex‑Spark、Fast mode | — | — | — | ✓ | 依方案 |
| 管理控制（SSO、RBAC、SCIM、稽核日誌） | — | — | — | — | ✓ |
| 用量上限 | 最低 | 輕量 | 基準 | 5×／20× | 同 Plus 起跳 |

> 💡 **教學提醒**：Free 帳號足以跑完「基礎核心單元」——Quickstart、Tasks、Projects、Agent Configuration、Skills 全部可練。但 **Connectors／Plugins／MCP／Automations／Sites／Remote 需要 Plus 以上**。建議講師端使用 Plus 或 Pro 展示這些章節，學生用 Free 完成前半段練習。

> [!IMPORTANT]
> **與 Claude 最大的觀念差異**：Claude 的重心是「對話 + 產出物」，Codex 的重心是「**代理在你的檔案系統上做事**」。Codex 會讀檔、改檔、執行命令、跑測試、回報 diff。因此每一章都要多問一句：**它被允許改什麼？怎麼驗收？**

---

## 🔁 與 Claude_ai 講義的章節對照

| Claude_ai 單元 | ChatGPT Codex 對應 | 本講義章節 |
|---|---|---|
| Settings | `config.toml`、permissions、sandbox、network | [Settings](./Settings/README.md) |
| Chats | Tasks / chats、提示詞、附件 | [Tasks](./Tasks/README.md) |
| Artifacts | Files、Preview、Visualizations、Sites | [Visualizations](./Visualizations/README.md) |
| Projects | Projects、local / worktree / cloud | [Projects](./Projects/README.md) |
| Custom Instructions | `AGENTS.md`（目錄作用域） | [Agent Configuration](./Agent_Configuration/README.md) |
| Connectors | Apps、plugins、OAuth 授權 | [Connectors](./Connectors/README.md) |
| Skills | `SKILL.md` skills | [Skills](./Skills/README.md) |
| Plugins | Skills + MCP server + optional UI | [Plugins](./Plugins/README.md) |
| Local MCP | MCP 設定與本機工具 | [MCP](./MCP/README.md) |
| Claude in Chrome | Browser / browser extension / computer use | [Browser](./Browser/README.md) |
| Cowork / Code | Desktop、CLI、IDE、local／worktree／cloud | [Workspaces](./Workspaces/README.md) |
| Scheduled | Scheduled tasks / heartbeat / cron | [Automations](./Automations/README.md) |
| Dispatch | Remote / cloud tasks、跨裝置接續 | [Remote](./Remote/README.md) |

---

## 📚 核心單元

### 🚀 Quickstart（快速開始）— **Free**
> **📂 [進入主題筆記：Quickstart](./Quickstart/README.md)**
> 上課第一步：安裝、登入、建立第一個 project，並用「只讀 → 小改 → 驗收」三段式跑完第一個 task。內含「安全第一次」的完整逐步流程。

### ⚙️ Settings（環境準備）— **Free**
> **📂 [進入主題筆記：Settings](./Settings/README.md)**
> 三個權限模式（Ask for Approval／Approve for Me／Full Access）、sandbox 範圍、網路存取與 `~/.codex/config.toml`。這是整份講義最該先讀懂的一章——它決定 Codex 能對你的電腦做到什麼程度。

### 🟢 Tasks（任務與提示詞）— **Free（核心必學）**
> **📂 [進入主題筆記：Tasks](./Tasks/README.md)**
> 學會 **GCSV 框架**（Goal／Context／Scope／Verification）撰寫高品質 task，並對照 Claude 的 RTCCF。內含五種任務型態（問答、診斷、修改、產檔、長時工作）的完整範本。

### 🟢 Projects（專案與知識來源）— **Free**
> **📂 [進入主題筆記：Projects](./Projects/README.md)**
> 把相關的 chats、檔案、指示與資料來源收在一起。Codex project 通常直接綁定一個本機資料夾或 Git repository，因此比 Claude Projects 多了「工作目錄」與「未提交變更」的概念。

### 🟢 Agent Configuration（`AGENTS.md`）— **Free**
> **📂 [進入主題筆記：Agent Configuration](./Agent_Configuration/README.md)**
> Codex 版的 Custom Instructions，但強大得多：**依目錄作用域層層疊加**，從 `~/.codex/AGENTS.md` 全域規則一路覆寫到 `services/payments/AGENTS.override.md`。這是讓 Codex 穩定產出的最高 CP 值投資。

### 🟢 Skills（技能）— **Free**
> **📂 [進入主題筆記：Skills](./Skills/README.md)**
> 用 `SKILL.md` 把可重複的專業流程封裝起來，在 ChatGPT 用 `@skill-name`、在 Codex 用 `$skill-name` 呼叫。內含四階範例：模仿者 → 創作者 → 整合者 → 自動化專家，以及 `@skill-creator` 與 Record & Replay 兩種快速產生法。

### 🔵 Visualizations / Sites（成品呈現）— **Plus 起**
> **📂 [進入主題筆記：Visualizations](./Visualizations/README.md)**
> Claude Artifacts 在 Codex 沒有一對一功能，而是拆成四種出口：workspace 檔案、Visualizations（互動圖表）、Sites（可發佈網站）、ImageGen（圖片）。本章教你如何選對出口。

### 🔵 Connectors（Apps 與外部資料）— **Plus 起**
> **📂 [進入主題筆記：Connectors](./Connectors/README.md)**
> 透過 app / plugin 的 OAuth 授權安全直連 Google Workspace、GitHub、Canva 等服務。
> 內含三大實戰次章節與完整配套偽檔案：
> - 📂 [01. Google Workspace 實戰](./Connectors/01_Google_Workspace/README.md)：Drive 跨檔分析、Gmail 摘要與行事曆調配。
> - 🎨 [02. Canva 設計自動化](./Connectors/02_Canva/README.md)：文案匹配範本、Brand Kit 色彩審查。
> - 🐙 [03. GitHub 工程協作](./Connectors/03_GitHub/README.md)：Issue 分流、PR 自動審查、Release note 產生。
> 進階閱讀：[權限與治理指南](./Connectors/Guide/Permissions_and_Governance.md)

### 🔵 Plugins（外掛套件）— **Plus 起**
> **📂 [進入主題筆記：Plugins](./Plugins/README.md)**
> 2026 年 6 月起，OpenAI 推出六大職能 plugin，開箱即連 62 個商務應用、內建 110 個現成 skill，另有 90+ 社群與第三方 plugin。本章教你判斷「該做 Skill、該做 MCP、還是直接裝 Plugin」。

### 🔵 MCP（Model Context Protocol）— **Plus 起**
> **📂 [進入主題筆記：MCP](./MCP/README.md)**
> 沒有現成 app／plugin 時的最後手段：用 MCP 把公司內部 API、資料庫接進 Codex。內含 `codex mcp add` 指令、`config.toml` 設定、stdio 與 HTTP 兩種伺服器、以及工具核准模式。

---

## 🟣 進階與代理功能

### 🔵 Browser / Computer Use（瀏覽器與電腦操作）— **Plus 起**
> **📂 [進入主題筆記：Browser](./Browser/README.md)**
> 三種上網方式的差別：內建 Browser（獨立設定檔）、Browser extension（沿用你的 Chrome 登入狀態）、Computer use（雲端另一台電腦）。本章的重點是**安全邊界**與「停在送出前」的課堂演練。

### 🔵 Workspaces（Desktop / CLI / IDE / Cloud）— **Free 起，雲端需 Plus**
> **📂 [進入主題筆記：Workspaces](./Workspaces/README.md)**
> Claude 的 Cowork / Code 在 OpenAI 分散於四種介面。本章說明何時該用哪一種、如何用 Git worktree 平行跑多個 task，以及 `/goal` 長時工作模式。

### 🔵 Automations（排程任務）— **Plus 起**
> **📂 [進入主題筆記：Automations](./Automations/README.md)**
> 把重複性工作交給 Codex 定時執行：週報彙整、庫存監控、競品追蹤。支援 RFC 5545 RRULE 精確排程，以及 Gmail／Slack／GitHub 事件觸發。

### 🔵 Remote（跨裝置交辦）— **Plus 起**
> **📂 [進入主題筆記：Remote](./Remote/README.md)**
> 對應 Claude Dispatch：從手機交辦任務，你的電腦實際執行，過程中可在手機上核准動作、審查 diff 與測試結果。

---

## 🗺️ 建議授課順序

| 節次 | 章節 | 方案門檻 | 重點 |
|---|---|---|---|
| 1 | [Quickstart](./Quickstart/README.md) → [Settings](./Settings/README.md) | Free | 先搞懂權限，再讓它動手 |
| 2 | [Tasks](./Tasks/README.md) | Free | GCSV 框架、五種任務型態 |
| 3 | [Projects](./Projects/README.md) → [Agent Configuration](./Agent_Configuration/README.md) | Free | 讓規則自動生效 |
| 4 | [Skills](./Skills/README.md) | Free | 把 SOP 變成可呼叫的能力 |
| 5 | [Connectors](./Connectors/README.md) → [Plugins](./Plugins/README.md) → [MCP](./MCP/README.md) | Plus | 接外部資料的三種層級 |
| 6 | [Visualizations](./Visualizations/README.md) → [Browser](./Browser/README.md) | Plus | 產出與驗證 |
| 7 | [Workspaces](./Workspaces/README.md) → [Automations](./Automations/README.md) → [Remote](./Remote/README.md) | Plus | 代理化與自動化 |

---

## 🏢 講義使用的示範資料

本講義所有範例圍繞兩家虛構公司，資料皆為教學用途捏造，可安全上傳測試：

| 公司 | 產業 | 用於哪些章節 |
|---|---|---|
| **潮汐物流（TideFlow Logistics）** | 跨境電商倉儲與配送，內部有 `tideflow-portal` 網站專案 | Projects、Agent Configuration、Skills、Automations、GitHub |
| **麥禾烘焙（MAIHO Bakery）** | 連鎖烘焙品牌，8 間直營門市 | Visualizations、Connectors／Canva、Tasks |

> 對照用：`Claude_ai` 講義使用的是「星橋科技」與「山嵐茶飲」。兩套資料刻意不同，方便同時開兩章做平台比較。

所有 CSV 示範資料由 [`tools/generate_sample_data.py`](./tools/README.md) 產生，使用固定亂數種子可重現。資料中刻意植入三種「教學埋伏」（真異常、離群但正常、資料缺漏），多個章節的解答依賴它們——詳見 [tools/README.md](./tools/README.md)。

---

[← 返回專案首頁](../README.md)
