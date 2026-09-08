# 範例 02：`/goal` 長時遷移

> 🟢 **方案需求**：Free（`/goal` 在桌面版、CLI、IDE extension 均可用）。

**情境**：把整個 repo 的日期處理從 moment.js 遷移到 date-fns。牽涉 40+ 個檔案，需要多步驟，而且你要能中途喊停調整方向。

> **這是 `/goal` 的典型場景**：一次性、多步驟、需要人在旁邊掌舵。

---

## 🆚 先確認要用哪一個

| 你的工作 | 用什麼 |
| :--- | :--- |
| 單一明確的小任務 | 一般 [task](../../../Tasks/README.md) |
| **一次性、多步驟、需要中途掌舵** | **`/goal`** |
| 週期性重複執行 | [Automation](../../../Automations/README.md) |

---

## 🥇 練習一：寫一個能自我驗證的 goal

> [!IMPORTANT]
> **goal 的文字同時是初始提示與完成條件。** Codex 用它來驗證自己的進度。
>
> 官方原則：*"Write a goal that lets ChatGPT verify its own progress."*

```markdown
/goal

## Outcome
將 tideflow-portal 的日期處理從 moment.js 全面遷移到 date-fns，行為完全不變。

**完成條件**（可機器驗證）：
- `grep -r 'from "moment"' src/` 無結果
- `grep -r "require('moment')" src/` 無結果
- moment 已從 package.json 移除
- `pnpm test` 全綠
- `pnpm typecheck` 無錯誤

## Constraints
- **分三批**：先 `src/lib/`，通過測試後做 `src/api/`，最後 `src/ui/`。
- **每批完成後暫停，等我確認再繼續。**
- **不可修改測試的斷言內容**——測試是判斷行為未變的唯一依據。
- 不要順手做其他重構、格式調整或型別補強。
- 時區相關的轉換集中在 `src/lib/datetime.ts`，這個檔案最需要小心。

## Verification
每批結束時回報：
1. 改了哪些檔案（清單）
2. `pnpm test` 的實際輸出
3. **你不確定的轉換點**（moment 與 date-fns 語意不完全對等的地方）
4. 這一批的行為是否可能與原本不同？哪裡？
```

### 為什麼完成條件要「可機器驗證」

| ❌ 模糊 | ✅ 可驗證 |
| :--- | :--- |
| 「完全移除 moment」 | `grep -r 'from "moment"' src/` 無結果 |
| 「測試要通過」 | `pnpm test` 全綠 |
| 「行為不變」 | 不修改測試斷言，且測試全綠 |

**模糊的完成條件會讓它提早宣告完成。**

---

## 🥈 練習二：中途介入

`/goal` 執行時，進度介面可以**暫停、恢復、編輯、清除**。你也可以在同一個 chat 送出後續訊息，**不必中斷工作**。

### 情境 A：發現方向不對

```text
暫停一下。

我看到你把 `moment().startOf('day')` 轉成 `startOfDay(new Date())`，
但我們的系統是以 Asia/Taipei 為準，不是伺服器本地時區。

請調整做法：所有涉及「今天」的判斷，都要明確指定時區。
先不要繼續，告訴我這會影響哪些已經改好的檔案。
```

### 情境 B：補充背景

```text
補充一個你不會知道的背景：
`src/api/report.ts` 的日期格式是給下游系統吃的，格式一個字都不能變。
那個檔案請特別小心，改完後把前後的輸出字串貼給我對照。
```

> **這兩種介入都不需要中斷 goal。** 這是 `/goal` 與一般 task 最大的差別——**它是一段持續的工作，不是一次問答。**

---

## 🥉 練習三：處理「語意不對等」

遷移最大的風險不是漏改，是**改了但語意不同**。

```markdown
在第一批（src/lib/）完成後，追加這個要求：

請列出所有 moment 與 date-fns 語意**不完全對等**的轉換點，
並針對每一處說明：
1. moment 原本的行為
2. date-fns 的行為
3. **兩者在什麼情況下會產生不同結果**
4. 我們的程式碼會遇到那種情況嗎？

不確定的一律列出來，不要自己判斷「應該沒差」。
```

### 常見的不對等點（供對照）

| 面向 | moment | date-fns |
| :--- | :--- | :--- |
| 可變性 | **可變**（`.add()` 會改原物件） | 不可變（回傳新物件） |
| 無效日期 | `Invalid Date` 物件 | 多數函式回傳 `Invalid Date`，行為需逐一確認 |
| 時區 | 需 moment-timezone | 需 date-fns-tz |
| 週的起始 | 依 locale | 需明確指定 `weekStartsOn` |
| 月底加月 | 1/31 + 1 month = 2/28 | 行為需確認 |

> **「月底加一個月」是經典陷阱。** 如果你的系統有訂閱制或帳期計算，這裡出錯會直接影響帳務。

---

## 🏁 練習四：驗收

```bash
# 完成條件逐項確認
grep -r 'from "moment"' src/           # 應無輸出
grep -r "require('moment')" src/       # 應無輸出
grep -n '"moment"' package.json        # 應無輸出
pnpm test                              # 應全綠
pnpm typecheck                         # 應無錯誤

# 確認測試沒被動過
git diff main --stat -- tests/         # 應只有新增，沒有修改既有斷言
```

> [!WARNING]
> **最後一項最重要。** 如果 `tests/` 底下有既有斷言被修改，代表它**為了讓測試通過而改了測試**——那整個遷移的「行為不變」保證就失效了。
>
> 這是 `Constraints` 裡「不可修改測試的斷言內容」那一條的實際驗收方式。

---

## ✅ 驗收檢查清單

- [ ] goal 的完成條件是**可機器驗證**的（grep / 測試命令）
- [ ] 有寫「每批完成後暫停」
- [ ] 有禁止修改測試斷言
- [ ] 有禁止順手做其他重構
- [ ] 中途介入時沒有中斷 goal
- [ ] 有列出語意不對等的轉換點
- [ ] `git diff -- tests/` 確認斷言未被修改
- [ ] 所有完成條件逐項驗證通過

---

← [返回上層：Workspaces 範例](../README.md) ｜ [返回索引](../../../README.md)
