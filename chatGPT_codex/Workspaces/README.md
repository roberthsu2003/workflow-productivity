# Workspaces：Desktop、CLI、IDE 與 Cloud

> 🟢 **方案需求**：Desktop / CLI / IDE 為 Free；**Cloud 環境與背景工作需 🔵 Plus**。

Claude 把協作與開發集中在 **Cowork / Code** 兩個產品。OpenAI 則把同樣的能力**分散在四種介面**，加上 local / worktree / cloud 三種執行環境，以及 task 之間的協調機制。

這一章回答兩個問題：**該用哪個介面？多個 task 怎麼不打架？**

---

## 🖥️ 四種介面

| 介面 | 適合 | 有什麼 | 沒有什麼 |
| :--- | :--- | :--- | :--- |
| **ChatGPT 桌面版** | 課堂教學、日常工作 | 多 task、diff 檢視、內建終端機、瀏覽器、成品預覽、Visualizations | — |
| **Codex CLI** | 終端機工作流、遠端主機、腳本化 | 完整代理能力、`/` 指令、可 pipe | **不能渲染 Visualizations** |
| **IDE extension** | 邊寫邊問、就地修改 | 在 VS Code / JetBrains 內理解與修改程式碼 | **不能渲染 Visualizations** |
| **Codex cloud / web** | 背景長時工作、跨裝置 | 可重現的遠端執行 | 看不到你未提交的本機變更 |

### 怎麼選

```text
我現在在做什麼？
├─ 在教學 / 需要看圖表與 diff        → 桌面版
├─ 已經在終端機裡 / 要 ssh 到遠端     → CLI
├─ 正在 IDE 裡寫程式，只想問一小段    → IDE extension
└─ 要跑很久 / 想關筆電 / 從手機接續   → Cloud（見 Remote 章節）
```

> [!IMPORTANT]
> **四種介面共用同一套核心概念**：project、task、permission mode、`AGENTS.md`、skills。學會一個，其他三個只是 UI 差異。但**登入方式與部分功能不同**，請以 [官方 CLI 文件](https://learn.chatgpt.com/docs/cli) 與 [IDE 文件](https://learn.chatgpt.com/docs/ide) 為準。

---

## 🌳 三種執行環境與平行工作

| 環境 | 檔案在哪 | 隔離性 |
| :--- | :--- | :---: |
| **Local / checkout** | 你目前的工作目錄 | ✗ 無 |
| **Worktree** | Git worktree 建立的獨立目錄 | ✅ 分支與檔案完全隔離 |
| **Cloud** | 遠端環境 | ✅ 完全隔離 |

### ⚠️ 平行工作的黃金規則

> [!WARNING]
> **可以同時開多個 chat，但絕不要讓兩個 chat 同時修改同一批檔案。**
>
> 兩個代理各自以為自己是唯一的作者，會互相覆蓋。這是使用 Codex 最常見、也最難除錯的災難。

### 正確做法：一個 task 一個 worktree

```bash
# 主目錄：task A 處理結帳頁 bug
cd ~/projects/tideflow-portal

# task B 要做日期函式庫遷移 → 開獨立 worktree
git worktree add ../tideflow-portal-migrate feat/date-migration

# task C 要寫文件 → 再開一個
git worktree add ../tideflow-portal-docs docs/agents-md
```

每個 Codex chat 綁定不同目錄，三個 task 完全互不干擾。

完成後清理：

```bash
git worktree list                              # 確認現況
git worktree remove ../tideflow-portal-migrate # 移除
```

### 什麼情況可以共用同一個目錄

| 情境 | 可以嗎 |
| :--- | :---: |
| 一個 task 改檔，另一個 task **只讀分析** | ✅ 但改檔中途的讀取結果可能不一致 |
| 兩個 task 改**完全不同的檔案** | ⚠️ 風險仍在（測試、lock 檔、建置產物會衝突） |
| 兩個 task 改同一批檔案 | ❌ **絕對不行** |

**簡單記法：只要有兩個以上會改檔的 task，就開 worktree。**

---

## 🎯 一次性 vs. 週期性：`/goal` 與 Automation

| 你的工作 | 用什麼 | 章節 |
| :--- | :--- | :--- |
| 一次性、多步驟、需要你中途掌舵 | **`/goal`** | 本章 |
| 週期性重複執行 | **Automation** | [Automations](../Automations/README.md) |
| 單一明確的小任務 | 一般 task | [Tasks](../Tasks/README.md) |

### `/goal` 長時工作模式

在桌面版、CLI 或 IDE extension 輸入 **`/goal`** 進入。goal 的文字**同時是初始提示與完成條件**——Codex 會用它來驗證自己的進度。

**有效的 goal 包含三件事**：

| 要素 | 說明 |
| :--- | :--- |
| **Outcome** | 你要的具體結果 |
| **Constraints** | 必要的工具、邊界、不可採用的做法 |
| **Verification** | 證明完成的測試、量測或審查標準 |

> 官方原則：*"Write a goal that lets ChatGPT verify its own progress."*
> **寫一個能讓它自己驗證進度的目標。**

### 執行中的控制

goal 執行時，進度介面可以：

- **暫停 / 恢復**
- **編輯** goal 內容
- **清除**重來
- 在同一個 chat 送出後續訊息，補充背景或調整限制，**不必中斷工作**

執行過程中 sandbox 政策與核准要求持續生效——需要決策時它會停下來問你。

### 範例

```markdown
/goal

## Outcome
將 tideflow-portal 的日期處理從 moment.js 全面遷移到 date-fns，行為完全不變。
完成條件：`grep -r 'from "moment"' src/` 無結果，且 `pnpm test` 全綠。

## Constraints
- 分三批：先 `src/lib/`，通過測試後做 `src/api/`，最後 `src/ui/`。
- **每批完成後暫停等我確認。**
- 不可修改測試的斷言內容——測試是判斷行為未變的唯一依據。
- 不要順手做其他重構或格式調整。

## Verification
- 每批回報：改了哪些檔案、測試輸出、你不確定的轉換點。
- 時區相關的轉換（`src/lib/datetime.ts`）需額外說明對應關係。
```

---

## 🧭 Task 協調的實務建議

| 原則 | 說明 |
| :--- | :--- |
| **一個 task 一個目標** | 不相干的目標拆開，避免上下文互相干擾 |
| **會改檔就開 worktree** | 見上方黃金規則 |
| **共用規則寫 `AGENTS.md`** | 不要在每個 task 重複交代（見[該章節](../Agent_Configuration/README.md)） |
| **重複流程做成 Skill** | 見 [Skills](../Skills/README.md) |
| **長工作用 `/goal`，週期工作用 Automation** | 選錯會很痛苦 |
| **每個階段都要能 `git diff`** | 無法審查的變更等於沒做 |

---

## 📖 教材範例

| 範例 | 練什麼 |
|---|---|
| [01. 平行 Worktree](./Examples/01_Parallel_Worktrees/README.md) | 三個 task 同時改同一個 repo 而不打架 |
| [02. `/goal` 長時遷移](./Examples/02_Goal_Migration/README.md) | 可機器驗證的完成條件、中途介入、語意不對等 |
| [03. CLI 批次處理](./Examples/03_CLI_Batch/README.md) | 終端機工作流、腳本化、遠端主機 |

---

## 🔄 與 Claude Cowork / Code 的對照

| 面向 | Claude Cowork / Code | Codex |
| :--- | :--- | :--- |
| 產品形態 | 兩個獨立產品 | **四種介面，同一套核心** |
| 方案門檻 | Pro / Max / Team / Enterprise | 🟢 **Free 起**（Cloud 需 Plus） |
| 平行處理 | Sub-agents（自動派發分身） | **多 task + Git worktree**（由你控制） |
| 長時工作 | 背景執行 | **`/goal`**（可暫停、編輯、恢復） |
| 隔離機制 | 平台管理 | **Git worktree / cloud environment** |

> **最大的心智差異**：Claude 的 sub-agents 是**模型自己決定**要派幾個分身；Codex 的平行化是**你自己開 worktree、自己開 chat**。控制權在你手上，代價是你要自己管理。

---

## 小結

| 決定 | 選擇 |
|---|---|
| 教學、要看圖表與 diff | 桌面版 |
| 已在終端機 / 遠端主機 | CLI |
| 正在 IDE 寫程式 | IDE extension |
| 要跑很久 / 跨裝置 | Cloud（見 [Remote](../Remote/README.md)） |
| 兩個以上會改檔的 task | **一定要開 worktree** |
| 一次性多步驟工作 | `/goal` |
| 週期性工作 | [Automation](../Automations/README.md) |

**官方說明**：[Long-running work](https://learn.chatgpt.com/docs/long-running-work) · [Codex CLI](https://learn.chatgpt.com/docs/cli) · [IDE extension](https://learn.chatgpt.com/docs/ide) · [Codex cloud](https://learn.chatgpt.com/docs/cloud)

---

← [返回上層：ChatGPT Codex 索引](../README.md)
