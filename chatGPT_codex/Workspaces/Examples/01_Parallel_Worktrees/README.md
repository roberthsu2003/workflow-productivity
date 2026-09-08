# 範例 01：平行 Worktree

> **練習專案**：先依 [`student-lab`](../../../student-lab/README.md)建立 `tideflow-portal` Git repository，再執行本章命令。專案內已有程式、測試與刻意保留的 review 題。

> 🟢 **方案需求**：Free。

**情境**：週一早上，你手上有三件不相干的事要改同一個 repo：修結帳頁的 bug、遷移日期函式庫、補 `AGENTS.md`。你想同時進行。

> **這是使用 Codex 最容易出災難的場景**，也是最值得練的。

---

## ⚠️ 先看災難長什麼樣

> [!WARNING]
> ### 不要在同一個目錄開三個 chat 同時改檔
>
> 三個代理各自以為自己是唯一的作者：
> - Chat A 讀了 `package.json`，準備加一個依賴
> - Chat B 同時也讀了 `package.json`，準備移除 moment.js
> - Chat A 寫入 → Chat B 寫入 → **A 的變更消失了**
>
> 更糟的是**你不會立刻發現**。測試可能還是綠的，問題要到幾天後才浮現。

---

## 🥇 練習一：建立三個隔離的工作區

```bash
# 主目錄留給 task A（結帳頁 bug）
cd ~/projects/tideflow-portal
git status                    # 確認乾淨
git checkout -b fix/checkout-shipping

# task B：日期函式庫遷移
git worktree add ../tideflow-portal-migrate -b feat/date-migration

# task C：文件
git worktree add ../tideflow-portal-docs -b docs/agents-md

# 確認
git worktree list
```

預期輸出：

```text
/Users/you/projects/tideflow-portal           abc1234 [fix/checkout-shipping]
/Users/you/projects/tideflow-portal-migrate   abc1234 [feat/date-migration]
/Users/you/projects/tideflow-portal-docs      abc1234 [docs/agents-md]
```

**三個目錄、三個分支、三份完整的檔案。互不干擾。**

---

## 🥈 練習二：三個 chat 各自綁定

在 Codex 中開三個 chat，各自綁定不同目錄：

| Chat | 工作目錄 | Task |
| :--- | :--- | :--- |
| A | `tideflow-portal` | 修正門市自取仍計運費 |
| B | `tideflow-portal-migrate` | moment.js → date-fns |
| C | `tideflow-portal-docs` | 補 `AGENTS.md` 的 e2e 測試說明 |

### 每個 task 都要寫明工作目錄

```markdown
## Goal
修正門市自取時仍計算運費的問題。

## Context
- **工作目錄：`~/projects/tideflow-portal`（分支 fix/checkout-shipping）**
- 根本原因已確認：`src/checkout/calcShipping.ts:52` 未處理 PICKUP

## Scope
- 可修改：`src/checkout/calcShipping.ts` 與對應測試
- **不要切換分支、不要操作其他 worktree 目錄。**
- 不要 push。

## Verification
- 新增 PICKUP 情境的回歸測試
- `pnpm test` 全綠
- 提供 diff 摘要
```

> **「不要切換分支、不要操作其他 worktree 目錄」這一句很重要。** 沒有它，代理可能為了「順便看一下」而 `cd` 出去。

---

## 🥉 練習三：觀察隔離是否真的有效

刻意製造一個會衝突的情境：

```markdown
在 Chat B（migrate worktree）中：

## Goal
移除 moment.js，改用 date-fns。

## Scope
- 工作目錄：`~/projects/tideflow-portal-migrate`
- 會修改 `package.json`

## Verification
完成後回報 package.json 的變更。
```

同時在 Chat C：

```markdown
在 Chat C（docs worktree）中：

## Goal
在 AGENTS.md 補上 e2e 測試說明。

## Scope
- 工作目錄：`~/projects/tideflow-portal-docs`
- 只修改 AGENTS.md
```

### 驗收

```bash
# 三個目錄各自檢查
cd ~/projects/tideflow-portal          && git status --short
cd ~/projects/tideflow-portal-migrate  && git status --short
cd ~/projects/tideflow-portal-docs     && git status --short
```

**每個目錄應該只看到自己那個 task 的變更。** 如果 A 的目錄裡出現了 B 的變更，代表有 chat 跑錯目錄了。

---

## 🏁 練習四：合併與清理

```bash
# 依序合併（每次合併後跑測試）
cd ~/projects/tideflow-portal
git checkout main

git merge fix/checkout-shipping && pnpm test
git merge docs/agents-md        && pnpm test
git merge feat/date-migration   && pnpm test
```

> [!IMPORTANT]
> **合併順序有講究**：把**影響範圍最大**的（日期函式庫遷移）放最後。
> 前面的小變更先進去，最後那個大的才知道要對哪個基準做調整。

### 清理

```bash
git worktree remove ../tideflow-portal-migrate
git worktree remove ../tideflow-portal-docs
git worktree list          # 確認只剩主目錄
git branch -d feat/date-migration docs/agents-md fix/checkout-shipping
```

> **記得清理。** 遺留的 worktree 會讓下次 `git worktree add` 用到同名路徑時失敗，而且佔磁碟空間。

---

## 📋 什麼時候可以不開 worktree

| 情境 | 需要 worktree 嗎 |
| :--- | :---: |
| 兩個以上 task **會改檔** | ✅ **一定要** |
| 一個 task 改檔，另一個**只讀分析** | ⚠️ 可以，但讀到的可能是改到一半的狀態 |
| 兩個 task 改**完全不同的檔案** | ⚠️ 仍有風險（lock 檔、建置產物、測試會衝突） |
| 只有一個 task | ❌ 不需要 |

**簡單記法：只要有兩個以上會改檔的 task，就開 worktree。**

---

## ✅ 驗收檢查清單

- [ ] 三個 worktree 建立成功，`git worktree list` 顯示三筆
- [ ] 每個 task 的 `Context` 都寫明了工作目錄
- [ ] 每個 task 的 `Scope` 都禁止切換分支與跨目錄操作
- [ ] 三個目錄的 `git status` 各自只有自己的變更
- [ ] 合併時把影響最大的放最後
- [ ] **清理完成**，`git worktree list` 只剩主目錄

---

← [返回上層：Workspaces 範例](../README.md) ｜ [返回索引](../../../README.md)
