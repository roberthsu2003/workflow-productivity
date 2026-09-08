# 實作練習：使用現成 Plugin（工程與開發實戰）

> 🔵 **方案需求**：Plugins 需 Plus 起。`$skill-creator` 為 🟢 Free。
> 💻 **開發主軸**：這是 **Codex 的主場**。Claude 需要靠 skill 補足的工程能力，Codex 是原生的。

Claude 的對應章節介紹 `claude-api`、`mcp-builder`、`frontend-design`、`web-artifacts-builder`、`webapp-testing`、`skill-creator` 六個官方 Skill。

---

## 🎯 先講一個重要差異

> [!IMPORTANT]
> **Claude 需要 skill 才能做的工程工作，Codex 大多是內建行為。**
>
> | Claude 官方 Skill | Codex 的做法 |
> | :--- | :--- |
> | `webapp-testing` | **直接跑你的測試命令**（`pnpm test`），不需要 skill |
> | `frontend-design` | 寫進 `AGENTS.md` 的風格規則 |
> | `web-artifacts-builder` | Sites / Visualizations |
> | `mcp-builder` | [MCP 章節](../../MCP/README.md) |
> | `skill-creator` | **`$skill-creator`**（同名，Codex 也有） |
>
> **所以這一章的重點不是「怎麼呼叫 skill」，而是「怎麼讓 Codex 用對的方式做工程」。**

---

## 🛠️ 前置步驟

1. `Settings` → `Plugins`，安裝 **GitHub**
2. 選用：**Chrome**（控制瀏覽器）、**Computer Use**（控制 Mac 應用程式）
3. 準備一個測試 repo——**不要用公司正式專案**
4. 確認權限模式是 **Ask for Approval**

---

## 練習 A：前端開發與視覺驗證（對應 `frontend-design` + `webapp-testing`）

### 📖 說明

Claude 需要 `frontend-design` skill 來避開「AI 生成感」的排版。Codex 的做法不同：**把風格規則寫進 `AGENTS.md`，一次寫好、永久生效。**

### Step 1：先立規則

```markdown
# 在 repo 的 AGENTS.md 加入

## Frontend
- 使用專案既有的元件庫，**不要引入新的 UI 框架**。
- 樣式一律用 Tailwind utility class，不寫獨立 CSS 檔。
- 元件放 `src/components/`，頁面放 `src/app/`。
- **RWD 必要**：所有版面須在 375px / 768px / 1440px 下正常。
- 互動元素須可鍵盤操作，並有可見的 focus 樣式。
- 顏色一律用 design token，**不可硬編碼色碼**。
```

### Step 2：開發並實際驗證

```markdown
## Goal
修正結帳頁在 Safari 17 窄螢幕下運費列溢出容器的問題。

## Context
- 重現：Safari 17，寬度 < 768px，`/checkout` 頁面
- 相關檔案推測在 `src/checkout/` 底下

## Scope
- 只修正溢出問題，**不要調整頁面其他版面**。
- 遵守 AGENTS.md 的 Frontend 規則。
- 不引入新套件。

## Verification
- **用瀏覽器實際開啟 `http://localhost:3000/checkout` 確認**
- 在 375px / 768px / 1440px 三個寬度各截一張圖
- 執行 `pnpm test`，必須全綠
- 提供 diff 摘要
```

> [!IMPORTANT]
> **`Verification` 裡的「用瀏覽器實際開啟」是關鍵。**
>
> 沒有這一句，Codex 會改完程式碼說「應該修好了」。有了這一句，它會**真的去看**。
> 這就是 Claude 的 `webapp-testing` skill 想達成的事——在 Codex 只需要寫進驗收條件。
>
> 見 [Browser 章節](../../Browser/README.md)。

---

## 練習 B：GitHub 工作流（對應 Claude 沒有的能力）

### 📋 GCSV Prompt

```markdown
## Goal
分流 tideflow-portal 的開放 Issue，為下週 sprint 排出優先序。

## Scope
- **只讀取。不要建立、修改、關閉或指派任何 Issue，不要留言。**

## Verification
1. 先寫出你的優先度判準（在排序**之前**）
2. 逐一評分
3. 選出 4 個並排序
4. **明確說出捨棄了什麼與代價**
5. 最後列出你實際呼叫了哪些 GitHub 操作，讓我確認全部都是讀取
```

> 完整練習見 [Connectors / GitHub](../../Connectors/03_GitHub/README.md)（含 Issue 分流、PR 審查、Release note 三個子章節與示範資料）。

---

## 練習 C：用 `$skill-creator` 產生 skill（對應 `skill-creator`）

### 📖 說明

**這是唯一 Claude 與 Codex 同名的 skill。** 用對話描述流程，讓它幫你產生 `SKILL.md`。

### 📋 Prompt

```text
$skill-creator

我想做一個 skill，用途是：檢查 PR 是否符合團隊的 code review 規則。

流程：
1. 讀取 repo 根目錄 AGENTS.md 的 "Code review rules" 章節
2. 逐條檢查 PR 的變更
3. 每條意見包含：規則編號、檔案行號、問題描述、具體修法、嚴重度
4. 特別區域另有加嚴規則（src/legacy/ 只修 bug 不重構）

限制：
- 絕不 approve、merge 或修改程式碼
- 沒發現問題時不要留言
- 規則沒涵蓋的情況標示「規則未涵蓋」，不要自行判定

請產生 SKILL.md，並幫我想一個精確的 description，
說清楚何時該用、何時不該用。
```

### 🎯 驗收：`description` 的品質

`$skill-creator` 產出的 `description` 是最該檢查的一行。

| ❌ 它可能產出 | ✅ 你該改成 |
| :--- | :--- |
| 「檢查 PR 的程式碼品質」 | 「依 repo AGENTS.md 的 code review rules 審查 PR 變更並留下意見。適用於已開啟的 PR；**不要用於**撰寫程式碼、修正問題、approve 或 merge。」 |

**加上「不要用於」那半句，才能防止它在你只是想討論架構時跳出來。**

### 替代方案：Record & Replay

**示範一次流程，讓系統自動轉成 skill**——不必手寫指示。適合流程步驟多但你講不清楚的情況。

---

## 練習 D：建立 MCP server（對應 `mcp-builder`）

當公司內部系統沒有現成 plugin 時，才需要這一步。

```markdown
## Goal
為潮汐物流的內部配送查詢 API 建立一個 MCP server。

## Scope
- 建立 `mcp-server/` 目錄，不要修改既有程式碼。
- **只實作唯讀工具**：`search_shipments`、`get_shipment_detail`。
  寫入工具這一輪不做。
- token 一律從環境變數讀取，**不可寫死**。

## Verification
- 工具名稱具體（不是 `query`、`do_action`）
- 參數使用嚴格 JSON Schema（型別、必填、列舉值、`additionalProperties: false`）
- **回傳不含個資欄位**（姓名、電話、地址、身分證號）
- 錯誤訊息能讓模型判斷下一步（不是 "Error"）
- 附上 `~/.codex/config.toml` 的設定範例，token 用 `bearer_token_env_var` 引用
```

> 完整說明見 [MCP 章節](../../MCP/README.md)，含 `codex mcp add` 指令與五條設計原則。

---

## 練習 E：Chrome 與 Computer Use plugin

> [!WARNING]
> **Chrome plugin 沿用你現有的 Chrome 登入狀態。** Codex 在那些分頁上擁有和你一樣的權限——包含網銀、公司後台。**只授權必要的頁面。**

課堂建議：優先使用**內建 Browser**（獨立設定檔，風險低得多），不是 Chrome plugin。

```markdown
## Goal
用內建 Browser 開啟本機開發伺服器，確認我剛才的修改真的生效。

## Scope
- 只開啟 `http://localhost:3000`，不要導航到其他網站。
- **不可點擊任何送出、購買、註冊或刪除按鈕。**

## Verification
截圖 + 描述目前畫面狀態。
```

見 [Browser 章節](../../Browser/README.md)的「停在送出前」課堂演練。

---

## 🔄 與 Claude 官方 Skill 的完整對照

| Claude 官方 Skill | Codex 對應 | 需要 skill 嗎 |
| :--- | :--- | :---: |
| `claude-api` | 不適用（那是 Anthropic API） | — |
| `mcp-builder` | [MCP 章節](../../MCP/README.md) | 自建 |
| `frontend-design` | **寫進 `AGENTS.md`** | ❌ 不需要 |
| `web-artifacts-builder` | [Sites / Visualizations](../../Visualizations/README.md) | ❌ 內建 |
| `webapp-testing` | **直接跑測試 + Browser 驗證** | ❌ 內建 |
| `skill-creator` | **`$skill-creator`** | ✅ 同名 |
| — | **GitHub plugin** | ➕ Codex 額外 |
| — | **Chrome / Computer Use plugin** | ➕ Codex 額外 |

> **結論**：Claude 用 skill 補足工程能力；**Codex 本來就是工程代理**，多數情況只需要把規則寫進 `AGENTS.md` 與驗收條件。

---

## ✅ 驗收檢查清單

- [ ] 前端規則寫在 `AGENTS.md`，不是每次重複交代
- [ ] 驗收條件有要求「**實際用瀏覽器確認**」
- [ ] GitHub 練習全程只讀，沒有 approve / merge / 留言
- [ ] `$skill-creator` 產出的 `description` 有補上「不要用於」
- [ ] MCP server 只做唯讀、回傳不含個資、token 走環境變數
- [ ] Browser 練習用內建 Browser，不是 Chrome plugin

---

← [返回上層：Skills](../README.md) ｜ [返回索引](../../README.md)
