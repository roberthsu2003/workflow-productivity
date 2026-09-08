# 💼 特別專題：投資研究與盡職調查

> 🔵 **方案需求**：Plus 起（Public Equity Investing、Investment Banking plugin）。
> 純資料分析部分（讀 xlsx、算指標）🟢 Free 亦可。

對應 `Claude_ai` 講義的 **VC 專題**（`VC_Creator`、`VC_Financial_Analyzer`、`VC_Playwright`）。

OpenAI 在 2026 年 6 月推出的六大職能 plugin 中，有兩個正好對應這個領域：

| Plugin | 用途 |
| :--- | :--- |
| **Public Equity Investing** | 公開市場的研究與分析工作流 |
| **Investment Banking** | 交易、財務模型、盡職調查 |

---

## 🎯 兩個次章節

| 次章節 | 情境 | 核心能力 |
| :--- | :--- | :--- |
| [01. 公開市場研究](./01_Public_Equity_Research/README.md) | 從公開資訊建立標的研究筆記 | **來源可追溯**、區分事實與推論 |
| [02. 財務盡職調查](./02_Investment_Banking_DD/README.md) | 審視新創的財務預估合理性 | **質疑假設**、找出說不通的地方 |

---

## ⚠️ 這個專題的特殊風險

> [!WARNING]
> ### 投資分析是最不能容忍幻覺的領域
>
> 一個編造的財務數字、一個沒有來源的市場規模、一個看似合理實則捏造的競品比較——都可能導致真金白銀的錯誤決策。
>
> **本專題所有練習都要求**：
> 1. **每一個數字都要有來源**（檔案位置或網址 + 日期）
> 2. **嚴格區分「資料顯示」與「我推論」**
> 3. **不確定的一律說不確定**，不要用專業語氣包裝猜測
> 4. **不做投資建議**——分析是分析，建議是人的責任

### 建議寫進 `AGENTS.md` 的紅線

```markdown
## Investment analysis boundaries
- 每一個財務數字都必須標註來源（檔案+工作表+儲存格，或網址+日期）。
- 嚴格區分三種陳述並明確標示：
  【事實】來源明確可查證　【推論】基於事實的合理推導　【假設】無資料支持的設定
- 不提供買賣建議、不預測股價、不給目標價。
- 找不到資料時說「查無資料」，**不得以產業慣例或類比推估代替**。
- 管理層提供的預估一律標示為【管理層說法】，不可當成事實陳述。
```

---

## 📂 示範資料

[`受評標的_財務摘要_2023-2026E.xlsx`](./02_Investment_Banking_DD/sample_files/受評標的_財務摘要_2023-2026E.xlsx)

三個工作表：損益表、關鍵指標、假設說明。**刻意埋了三個說不通的地方**——見 [02 章節](./02_Investment_Banking_DD/README.md)。

---

## 🔄 與 Claude VC 專題的對照

| Claude | Codex | 差異 |
| :--- | :--- | :--- |
| `VC_Creator`（自建 skill） | 自建 skill + **Investment Banking plugin** | Codex 有現成 plugin |
| `VC_Financial_Analyzer` | [02. 財務盡職調查](./02_Investment_Banking_DD/README.md) | 相近 |
| `VC_Playwright`（Playwright MCP 爬蟲） | [Browser 自動化](../Browser_Automation/README.md) | **Codex 用內建 Browser，不需要 MCP** |
| — | **Public Equity Investing plugin** | ➕ Codex 額外 |

> **最大差異在爬蟲那一塊**：Claude 需要接 Playwright MCP 才能動態爬網頁；
> **Codex 內建 Browser 就能做**，不需要額外的 MCP 設定。見 [Browser 自動化章節](../Browser_Automation/README.md)。

---

← [返回上層：Skills](../README.md) ｜ [返回索引](../../README.md)
