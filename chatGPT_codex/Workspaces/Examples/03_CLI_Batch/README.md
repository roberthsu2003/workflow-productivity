# 範例 03：CLI 批次處理

> 🟢 **方案需求**：Free（Codex CLI）。
>
> [!WARNING]
> **Codex CLI 不支援 Visualizations 呈現。** 需要看圖表時請切換到桌面版。

**情境**：你已經在終端機裡，或需要 ssh 到遠端主機。開桌面版反而慢。

---

## 🖥️ 什麼時候該用 CLI

| 情境 | 用 CLI 嗎 |
| :--- | :---: |
| 已經在終端機裡工作 | ✅ |
| 需要 ssh 到遠端主機 | ✅ **只能用 CLI** |
| 要把 Codex 接進 shell 腳本 | ✅ |
| 要看 diff 的視覺化呈現 | ❌ 用桌面版 |
| 要建立 Visualizations | ❌ **CLI 不支援** |
| 教學示範 | ❌ 桌面版較好懂 |

---

## 🥇 練習一：基本操作

```bash
# 進入專案
cd ~/projects/tideflow-portal

# 啟動 Codex CLI
codex
```

### 常用的 `/` 指令

| 指令 | 用途 |
| :--- | :--- |
| `/permissions` | 檢視與切換權限模式 |
| `/mcp` | 檢視生效中的 MCP 伺服器與工具 |
| `/goal` | 進入長時工作模式 |
| `$skill-name` | 呼叫 skill（CLI 用 `$`，不是 `@`） |

> **第一件事永遠是 `/permissions`**，確認是 **Ask for Approval**。

---

## 🥈 練習二：批次處理多個檔案

**情境**：`data/` 底下有 12 個月的配送 CSV，要各自產出月報。

```markdown
## Goal
為 `data/` 底下每一個 `配送績效_2026-*.csv` 產出對應的月報。

## Context
- 檔案命名：`配送績效_2026-01.csv` 到 `配送績效_2026-12.csv`
- 月報格式參考 `templates/monthly_report.md`

## Scope
- **不要修改任何原始 CSV。**
- 輸出到 `reports/`，命名 `2026-MM_月報.md`
- **已存在的月報不要覆蓋**，跳過並在最後回報跳過了哪些
- **資料缺漏的月份**（中區 6 月）：月報照常產出，
  但明確標示缺漏，**不可用 0 或推估值填補**

## Verification
1. 逐月處理，每完成一個回報一行進度
2. 最後彙總：成功 N 個、跳過 M 個、有資料問題 K 個
3. **有資料問題的月份單獨列出**，說明是什麼問題
```

> **「逐月回報進度」在 CLI 特別有用**——你能看到它卡在哪一個檔案，而不是等十分鐘後才知道失敗。

---

## 🥉 練習三：接進 shell 腳本

CLI 的價值在於**可以被腳本呼叫**。

```bash
#!/usr/bin/env bash
# scripts/weekly_check.sh — 每週執行的檢查
set -euo pipefail

cd "$(dirname "$0")/.."

echo "=== 1. 測試 ==="
pnpm test || { echo "❌ 測試失敗，中止"; exit 1; }

echo "=== 2. 型別檢查 ==="
pnpm typecheck || { echo "❌ 型別檢查失敗，中止"; exit 1; }

echo "=== 3. 讓 Codex 做程式碼健檢 ==="
codex exec "檢查本週的變更（git log --since='7 days ago'），
依 AGENTS.md 的 code review rules 找出問題。
只讀取，不要修改任何檔案，不要提交。
沒有發現問題就回覆「本週無發現」。"
```

> [!IMPORTANT]
> **腳本化時，`Scope` 的限制要寫得更嚴。** 你不在現場，沒有人能按取消。
>
> 上面那段刻意寫了三重限制：只讀取、不修改、不提交。

> **注意**：`codex exec` 的實際指令名稱與參數可能隨版本變動，請以 `codex --help` 與 [官方 CLI 文件](https://learn.chatgpt.com/docs/cli)為準。

---

## 🏁 練習四：遠端主機

```bash
# ssh 到遠端後直接用
ssh ops@tideflow-server
cd /srv/tideflow-portal
codex
```

### 遠端使用的額外注意

> [!WARNING]
> - [ ] **權限模式**：遠端主機上更要維持 Ask for Approval
> - [ ] **sandbox 範圍**：確認 `workspace-write` 的 workspace 是你想的那個目錄
> - [ ] **不要在正式環境主機上做實驗**
> - [ ] **確認有備份或版控**——遠端主機上 `git restore` 可能救不回未提交的東西
> - [ ] **secrets**：遠端主機的 `.env` 通常是真的，格外小心

### 遠端 vs. Codex Remote

| | ssh + CLI | [Codex Remote](../../../Remote/README.md) |
| :--- | :--- | :--- |
| 你在哪 | 終端機 | **手機** |
| 執行在哪 | 遠端主機 | **你自己的電腦** |
| 適合 | 維運、伺服器上的工作 | 通勤時交辦 |

---

## 🔄 CLI 與桌面版的能力差異

| 能力 | CLI | 桌面版 |
| :--- | :---: | :---: |
| 讀檔、改檔、跑命令 | ✅ | ✅ |
| `AGENTS.md`、Skills、權限模式 | ✅ | ✅ |
| `/goal` 長時工作 | ✅ | ✅ |
| MCP | ✅ | ✅ |
| diff 視覺化 | ⚠️ 純文字 | ✅ |
| **Visualizations** | ❌ | ✅ |
| 內建瀏覽器 | ❌ | ✅ |
| 可接進 shell 腳本 | ✅ | ❌ |
| ssh 到遠端 | ✅ | ❌ |

---

## ✅ 驗收檢查清單

- [ ] 開始前用 `/permissions` 確認是 Ask for Approval
- [ ] 批次處理有逐項回報進度
- [ ] 批次處理沒有覆蓋既有檔案
- [ ] 資料缺漏的月份有標示，沒有填 0
- [ ] 腳本化的呼叫有三重限制（只讀、不改、不提交）
- [ ] 遠端使用前確認了 sandbox 範圍與備份

---

← [返回上層：Workspaces 範例](../README.md) ｜ [返回索引](../../../README.md)
