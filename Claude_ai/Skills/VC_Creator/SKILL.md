---
name: vc-creator-investment-analyst
description: 當使用者提供新創簡報文字、會議紀錄或 Term Sheet 條款時，自動調用 references/ 創投評估標準與規章，並套用 templates/ 標準範本產出專業創投分析文件（投資備忘錄、Term Sheet 條款檢核報告、Pitch Deck 評估報告）。
---

# 創投 (VC) 投資分析與文件生成 Skill (Level 2 創作者)

## 任務目標
作為資深創投分析師 (VC Associate/Principal)，根據使用者輸入的材料類型（會議筆記、Pitch Deck 或 Term Sheet），參考 `references/` 中的創投專業指標與法規條款，並嚴格套用 `templates/` 中的標準範本輸出專業報告。

## 觸發模式與處理 SOP

### 模式 A：生成 IC 投資備忘錄 (Investment Memo)
1. **參考知識**：檢視 `references/vc-evaluation-framework.md` 了解財務指標（如 ARR, LTV/CAC, NDR, Rule of 40）與 VC 評估權重。
2. **套用樣板**：讀取 `templates/investment-memo-template.md`。
3. **資料處理**：將使用者輸入的材料歸納填入樣板各欄位，對於缺失數字標示「[待補查]」，並計算相應指標優劣。

### 模式 B：Term Sheet 條款檢核與風險摘要 (Term Sheet Risk Check)
1. **參考知識**：檢視 `references/term-sheet-glossary.md` 比對條款定義（如 Liquidation Preference, Anti-dilution, Drag-along, ROFR）。
2. **套用樣板**：讀取 `templates/term-sheet-summary-template.md`。
3. **資料處理**：檢核輸入的條款草案，標示對創投或創辦人不利的條款與風險提示。

### 模式 C：Pitch Deck 簡報評估與問答清單 (Deck Reviewer)
1. **參考知識**：檢視 `references/pitch-deck-checklist.md` (Sequoia/YC 簡報評估 10 大要素)。
2. **套用樣板**：讀取 `templates/deck-review-report-template.md`。
3. **資料處理**：評估簡報完整度，標出缺漏的 Slide 要素，並生成 3-5 個針對 IC 會議的創辦人提問問題。
