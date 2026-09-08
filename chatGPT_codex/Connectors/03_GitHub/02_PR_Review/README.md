# 03-2. PR 自動審查

> 🔵 **方案需求**：Plus 起（GitHub code review 整合）。

**情境**：潮汐物流的工程團隊有一份 code review 規則，但實際執行時大家記得的條目不同，審查品質不穩定。你要讓 Codex 成為第一道穩定的關卡。

> **關鍵觀念**：Codex 的角色是**留下審查意見**，不是做決定。它不 approve、不 merge、不改碼。

---

## 📂 示範資料

[`AGENTS_code_review_rules.md`](./sample_files/AGENTS_code_review_rules.md) — 完整的 review 規則，含：

- 8 條 🔴 阻擋級規則
- 6 條 🟡 警告級規則
- 3 條 🟢 建議級規則
- 三個特別區域（`src/legacy/`、`services/payments/`、`migrations/`）
- 審查意見的格式要求與安全替代方案

可直接審查的程式位於 [`student-lab/tideflow-portal/src/checkout/calcTotal.js`](../../../student-lab/tideflow-portal/src/checkout/calcTotal.js)。沒有 GitHub 權限時，直接在本機對該檔做 review；有權限時再由自己的副本建立 PR，**不要把練習 PR 開到教材 repository**。

---

## 🥇 練習一：把規則裝進 `AGENTS.md`

規則放在文件裡沒人看，放進 `AGENTS.md` 才會自動生效。

```markdown
## Goal
把 code review 規則併入 repo 的 AGENTS.md，讓後續所有審查自動遵守。

## Context
- 規則來源：`AGENTS_code_review_rules.md`
- 目標檔案：repo 根目錄的 `AGENTS.md`

## Scope
- **只修改 `AGENTS.md`**，不要動其他檔案。
- 若 `AGENTS.md` 已有內容，**append 一個新章節，不要覆蓋既有內容**。
- 保留規則編號（B-1、W-3…），後續審查意見要引用。

## Verification
- 完成後顯示 diff。
- 確認既有內容未被刪除。
- 說明你把規則放在哪個章節，以及為什麼。
```

### 進階：用子目錄覆寫

`services/payments/` 有額外要求。**這正是 `AGENTS.override.md` 的用途。**

```markdown
額外建立 `services/payments/AGENTS.override.md`，寫入該目錄的加嚴規則：
- 任何變更必須同時更新 CHANGELOG.md
- 對外 API 錯誤碼不可變更語意，只能新增
- 測試覆蓋率不得低於 90%

不要修改根目錄的 AGENTS.md。
```

> 見 [Agent Configuration 章節](../../../Agent_Configuration/README.md)的作用域說明。

---

## 🥈 練習二：審查一個 PR

```markdown
## Goal
審查 PR #<編號>，依 AGENTS.md 的 code review rules 逐條檢查。

## Scope
> 🚫 **絕對紅線**
- **不要 approve、不要 merge、不要關閉這個 PR。**
- **不要修改 PR 中的任何程式碼。**
- 只留下審查意見。

## Verification
每一條意見必須包含五個要素：
1. 規則編號（B-1 / W-3 / S-2…）
2. 檔案與行號
3. 問題描述（一句話）
4. **具體的修法建議**（不可寫「請改善」）
5. 嚴重度（🔴 / 🟡 / 🟢）

最後回報：
- 你逐條檢查了哪些規則（列出編號）
- 🔴 幾條、🟡 幾條、🟢 幾條
- **若沒有發現問題，明說「未發現問題」，不要為了交差而編造意見**
```

### 建立測試用 PR

課堂上可以刻意寫一個含多種違規的 PR：

```typescript
// src/checkout/calcTotal.ts — 刻意含 4 種違規
export async function calcTotal(orderId: string) {
  // 🔴 B-2: 字串拼接 SQL
  const rows = await db.query(`SELECT * FROM orders WHERE id = '${orderId}'`);

  // 🔴 B-1: 浮點數金額
  let subtotal = 0.0;
  for (const item of rows[0].items) {
    subtotal += parseFloat(item.price) * item.qty;
  }

  // 🔴 B-3: 未處理的 Promise rejection
  updateOrderCache(orderId, subtotal);

  // 🔴 B-7: 日誌含個資
  console.log(`Order ${orderId} by ${rows[0].cardholderName}, card ${rows[0].cardNumber}`);

  return subtotal;
}
```

**預期抓到 4 條 🔴**：B-2（SQL 拼接）、B-1（浮點數金額）、B-3（未 await 且無錯誤處理）、B-7（日誌含卡號與持卡人姓名）。

> **加分題**：這個 PR 是 bug 修正嗎？如果是，**B-8 要求必須有回歸測試**——有嗎？

---

## 🥉 練習三：測試「特別區域」規則

`src/legacy/` 的規則是「只修 bug，不要重構」。這條規則違反工程師的直覺，特別容易被忽略。

```markdown
## Goal
審查一個修改了 `src/legacy/` 的 PR。

## Context
這個 PR 修了一個 bug，但同時：
- 把 `var` 改成 `const`
- 加了 TypeScript 型別標註
- 重新命名了幾個變數（`cnt` → `count`）

## Scope
- 不要 approve、merge 或修改程式碼。

## Verification
判斷：這些額外變更**符合還是違反** `src/legacy/` 的規則？
說明你的判斷依據（引用規則原文）。
```

**正確答案**：🔴 **違反**。規則明確寫「只修正 bug，不要重構、不要改風格、不要加型別」。

> **教學重點**：這些變更客觀上都是「改善」。但規則之所以存在，是因為 `src/legacy/` **沒有測試覆蓋**——任何改動都是風險。
>
> 好的審查會指出違規，**同時說明規則背後的理由**，而不是機械式套用。

---

## 🏁 練習四：把審查做成 Automation

```markdown
## Goal
建立一個排程：當 tideflow-portal 有新 PR 開啟時，自動執行 code review。

## Scope
- **只留審查意見，不要 approve、merge 或修改程式碼。**
- 沒有發現問題時**不要留言**（避免通知疲勞）。

## Verification
- 先手動跑通一次再排程
- 設定事件觸發：PR opened
- 意見格式依 AGENTS.md 的五要素要求
```

> 事件觸發需在 ChatGPT 網頁版或行動版建立，企業環境需管理員開啟 **Allow event-triggered scheduled tasks**。詳見 [Automations 章節](../../../Automations/README.md)。

---

## ✅ 驗收檢查清單

- [ ] 規則已寫進 `AGENTS.md`，且未覆蓋既有內容
- [ ] `services/payments/AGENTS.override.md` 已建立
- [ ] 審查意見含完整五要素（規則編號、位置、描述、**具體修法**、嚴重度）
- [ ] 抓到測試 PR 的 4 條 🔴
- [ ] 正確判定 `src/legacy/` 的重構為違規
- [ ] **沒有 approve、merge、關閉或修改任何 PR**
- [ ] 沒有問題時沒有編造意見

---

← [返回上層：GitHub](../README.md) ｜ [返回索引](../../../README.md)
