# Skills 四階實作範例

> 🟢 **方案需求**：Free（建立、安裝與使用自訂 skill 全方案可用）

四個 skill，難度遞增，各自示範 `SKILL.md` 資料夾的一種能力層級。

---

## 🪜 四階概覽

| 階段 | Skill | 新增能力 | 資料夾內容 |
| :---: | :--- | :--- | :--- |
| **L1** | [模仿者：email-polisher](./Level1_Email_Polisher/) | 只有指示 | `SKILL.md` |
| **L2** | [創作者：daily-ops-brief](./Level2_Daily_Ops_Brief/) | + 輸出範本 | `SKILL.md` + `templates/` |
| **L3** | [整合者：expense-auditor](./Level3_Expense_Auditor/) | + 規範參照與判斷 | `SKILL.md` + `references/` + `templates/` |
| **L4** | [自動化專家：meeting-secretary](./Level4_Meeting_Secretary/) | + 可執行程式 | `SKILL.md` + `scripts/` + `references/` |

---

## 📍 安裝

```bash
# 個人 skill（跨所有專案可用）
cp -r Level1_Email_Polisher ~/.agents/skills/email-polisher

# 團隊 skill（提交進 Git，全隊自動取得）
cp -r Level2_Daily_Ops_Brief <你的repo>/.agents/skills/daily-ops-brief
cd <你的repo> && git add .agents && git commit -m "feat(skills): 新增每日營運簡報 skill"
```

> 完整的作用域與優先序見 [Skills 主章節](../README.md#-安裝位置)。

---

## ▶️ 呼叫

| 介面 | 語法 |
| :--- | :--- |
| ChatGPT | `@email-polisher` |
| Codex | `$email-polisher` |

也可以不明確呼叫——請求符合 `description` 時會自動載入。

---

## 🎓 建議的教學順序

### 第一節：L1（20 分鐘）

**重點**：`description` 決定一切。

讓學員故意把 `description` 寫模糊（「處理郵件相關的事」），觀察它在不該觸發時被觸發、該觸發時沒觸發。再改成精確版本，比較差異。

### 第二節：L2（25 分鐘）

**重點**：輸出格式從「請它照著做」變成「給它範本」。

比較兩種寫法的穩定度：
- 在 `SKILL.md` 裡用文字描述格式
- 在 `templates/` 放一個實際範本檔

跑五次，看哪一種輸出比較一致。

### 第三節：L3（30 分鐘）

**重點**：skill 開始做**判斷**，不只是格式化。

L3 需要比對規範（差旅費上限、單據要求）並下判定。這裡會遇到第一個真正的難題：**規範有模糊地帶時，skill 該替你決定，還是該標示「待人工判斷」？**

### 第四節：L4（30 分鐘）

**重點**：`scripts/` 會被實際執行。

除了功能，更要講**安全**：安裝來源不明的 skill 前必須讀過 `scripts/`。這是 skill 生態系最主要的風險面。

---

## 🧰 十個辦公流程延伸練習

四階範例教「怎麼做 skill」；這十個練習教「**做什麼樣的 skill**」。

| # | 練習 | 階 | 核心教學點 |
|:--:|---|:--:|---|
| 01 | [社群貼文文案](./Office_Workflow_01_Copywriter.md) | L1 | 不新增使用者未提供的事實 |
| 02 | [待辦事項擷取](./Office_Workflow_02_Task_Extractor.md) | L1 | **「盡快」不是期限** |
| 03 | [客戶報價單](./Office_Workflow_03_Customer_Quotation/README.md) | L2 | **資訊不全就停下來問**，不填預設值 |
| 04 | [會議行動計畫](./Office_Workflow_04_Meeting_Action_Plan/README.md) | L2 | 附和 ≠ 決議 |
| 05 | [請假職務交接](./Office_Workflow_05_Leave_Handover/README.md) | L3 | **抓出代理人權限不足的事項** |
| 06 | [採購比價查核](./Office_Workflow_06_Purchase_Checker/README.md) | L3 | **最低價不等於該選**（規格未驗證、無保固） |
| 07 | [客戶 CRM 與承諾追蹤](./Office_Workflow_07_Customer_CRM/README.md) | L3 | **「應該不會」不是承諾** |
| 08 | [每週簡報彙整](./Office_Workflow_08_Weekly_Brief.md) | L4 | 通知條件寫進 skill |
| 09 | [簽核進度追蹤](./Office_Workflow_09_Approval_Tracker.md) | L4 | **「來不及」比「卡關」更重要** |
| 10 | [營運儀表板](./Office_Workflow_10_Operations_Dashboard.md) | L4 | 資料新鮮度、數字不一致時兩個都顯示 |

> **貫穿十個練習的一條線**：允許並要求 skill 說「我不知道」「這個要問人」「資料缺漏」。

---

## ⚠️ 共通的設計原則

無論哪一階，好的 skill 都具備：

- [ ] `description` 同時寫了「**何時該用**」與「**何時不該用**」
- [ ] 流程是編號步驟，不是散文
- [ ] 明確寫出**不可以做什麼**
- [ ] 輸出格式具體到可以驗收
- [ ] 沒有把單次任務的細節寫進去
- [ ] 用三個真實案例測過，**包含一個不該觸發的案例**

---

## 🔄 與 Claude Skills 範例的對照

`Claude_ai/Skills/Examples` 的流程內容**可以直接參考沿用**——四階設計的教學邏輯是共通的。需要改的是：

| 項目 | Claude | Codex |
| :--- | :--- | :--- |
| 安裝路徑 | 帳號／Project 層級（雲端） | `~/.agents/skills/` 或 `<repo>/.agents/skills/` |
| 呼叫語法 | 自動觸發為主 | `@name`（ChatGPT）／ `$name`（Codex） |
| 團隊分享 | 介面分享 | **`git commit`** |
| 額外資料夾 | `references/`、`templates/`、`scripts/`、`assets/` | 相同，另可加 `agents/openai.yaml` |

---

← [返回上層：Skills](../README.md) ｜ [返回索引](../../README.md)
