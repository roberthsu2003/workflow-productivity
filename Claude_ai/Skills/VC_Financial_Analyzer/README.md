# 💼 創投 (VC) 財報數據分析與 Code Execution 自動化實戰

> 🟢 **方案需求**：Free / Pro / Team / Enterprise 方案皆適用 (需開啟 Claude.ai 之 Code Execution / Analysis Tool 功能)  
> 💼 **適用對象**：創投分析師 (VC Analyst / Associate)、財務盡調審查員 (Financial Due Diligence Auditor) 與投資經理 (Investment Manager)。  
> 🎓 **核心技術**：展示 **「RTCCF 提示詞架構」** 與 **「零程式基礎 Code Execution 整合」** 技巧 —— 學員**完全不需要懂任何程式碼**，只需將 Excel 拖入對話框，Skill 就會依據 RTCCF 架構指引 Claude.ai **在雲端背景自動執行 Python 計算與繪圖**，產出專業的 IC 盡調報告。

---

## 💡 為什麼本 Skill 使用 RTCCF 提示詞架構？

**RTCCF (Role, Task, Context, Constraint, Format)** 是設計高階 Agent Skill 的黃金提示詞框架：
1. **R (Role 角色)**：明確定義 Claude 為「創投資深財務盡調專家 (VC Senior FDD Analyst)」。
2. **T (Task 任務)**：指定掃描 Excel、提供選單、背景運算繪圖與產出報告之任務鏈。
3. **C (Context 背景)**：結合 `references/` 中的創投指標庫與 Code 繪圖規範。
4. **C (Constraint 限制)**：要求 100% 零數據幻覺 (全由背景 Code Execution 精確計算) 與繁體中文輸出。
5. **F (Format 格式)**：嚴格套用 `templates/financial-report-template.md` 樣板。

---

## 🧩 數據運作原理解密：從 Excel 欄位到 Markdown 填空樣板

很多學員會好奇：「**我們上傳的是 Excel (.xlsx) 試算表，為什麼產出的範例樣板是 `.md` (Markdown) 檔案？**」

這正是 AI 現代工作流中 **「速讀報告生成 + 精準數據運算」** 的核心運作機制：

```mermaid
graph LR
    A[1. 原始 Excel 報表<br/>.xlsx 數據列與欄] --> B[2. 背景 Code Execution<br/>自動讀取並算出財務指標]
    B --> C[3. 填入 Markdown 樣板<br/>替換 {{變數}} 填空欄位]
    C --> D[4. 對話框呈獻速讀報告<br/>+ 可選匯出新 Excel]
```

1. **原始數據 (Excel 欄位)**：提供基礎表格與數字（如`總營收`、`營業費用`、`期末現金`）。
2. **背景運算 (Code Execution)**：Claude 背景自動執行算術，計算出高階財務指標（如 `MRR 成長率`、`Gross Margin %`、`Runway 營運月數`）。
3. **樣板填空 (`templates/financial-report-template.md`)**：Markdown 檔案定義了報告的架構與美感，裡面的 `{{CURRENT_MRR}}`、`{{RUNWAY_MONTHS}}`、`{{GROSS_MARGIN}}` 就是留給 Claude 的 **「數據填空標籤 (Placeholders)」**。
4. **報告產出**：Claude 將背景算好的精準數字填入 Markdown 標籤中，在對話視窗呈獻出一份帶有標題、總覽表格與趨勢圖片的專業速讀報告；若學員需要，也可以請 Claude 另存一份全新的 Excel 檔下載。

---


## 📁 創投 Level 3 Skill 實體目錄結構

```text
VC_Financial_Analyzer/
├── README.md                              # 本實戰教學說明文件 (RTCCF 與零程式基礎導覽)
├── SKILL.md                               # 主 Skill 檔 (以 RTCCF 提示詞框架撰寫之 SOP)
├── references/                            # 📚 創投專業參考知識庫 (給 Claude 背景參考的 Context)
│   ├── financial-metrics-guide.md        # 1. VC 財務指標 (Runway, Burn Rate, NDR) 與 Red Flag 警訊
│   └── code-execution-rules.md           # 2. 指引 Claude 背景自動寫代碼與畫圖的美感規範
├── templates/                             # 📄 標準 Markdown 輸出樣板 (Format)
│   └── financial-report-template.md      # 1. 創投 IC 標準財務盡調與營運分析報告樣板
└── examples/                              # 📁 零門檻！學員專用練習檔
    └── sample_startup_financials.xlsx    # 學員可直接下載上傳測試的範例 Excel 財報
```

---

## 🛠️ 1 個 Skill 支援 5 大互動式 RTCCF 分析模式

本 Skill 名稱定義為 `vc-financial-analyzer`。當學員將 Excel 檔案拖入 Claude.ai 對話框時，Skill 會自動驅動 Claude 在背景掃描 Excel 欄位，並彈出以下 5 種分析選單供學員點選：

```yaml
---
name: vc-financial-analyzer
description: >-
  當使用者上傳創投被投/標的公司之 Excel 財務報表 (.xlsx, .xls, .csv) 時，
  自動讀取檔案結構與工作表，向使用者提供 5 大專業財務分析模式選單。
  使用者選擇後，背景自動呼叫 Python Code Execution 進行精準數據計算與圖表視覺化渲染，
  並結合 references/ 創投規章與 templates/ 產出高階投資報告。
---
```

---

### 🔍 5 大分析模式 RTCCF 架構細節

<details>
<summary><b>🔹 模式 1：財務健康度與 Cash Runway 深度診斷 (Runway Auditor)</b></summary>

- **R (Role)**：創投風險管理分析師 (VC Risk & Runway Auditor)。
- **T (Task)**：估算剩餘營運月數 (Runway) 與月燒錢速度 (Net Burn Rate)。
- **C (Context)**：對照 `references/financial-metrics-guide.md` 中的「Runway < 6 個月極高風險」警訊。
- **C (Constraint)**：背景繪製「現金餘額 vs. Runway 趨勢圖」，並劃設 6 個月紅色虛線警戒線。
- **F (Format)**：輸出包含 Runway 斷裂點與損益平衡估算的摘要表。

</details>

<details>
<summary><b>🔹 模式 2：營收與成本結構成長趨勢分析 (SaaS Financial Analyst)</b></summary>

- **R (Role)**：創投營運指標分析師 (SaaS Financial Analyst)。
- **T (Task)**：計算 MoM / YoY 營收成長率與 Gross Margin %。
- **C (Context)**：檢視 R&D、S&M、G&A 費用占比結構。
- **C (Constraint)**：背景繪製「Revenue vs. OpEx 雙 Y 軸消長圖」（採用深藍與鐵灰配色）。
- **F (Format)**：輸出營收結構與毛利變遷分析表。

</details>

<details>
<summary><b>🔹 模式 3：SaaS Unit Economics 與客戶動態分析 (SaaS Unit Economics Specialist)</b></summary>

- **R (Role)**：SaaS 專項投資經理 (SaaS Unit Economics Specialist)。
- **T (Task)**：評估 ARPU、Churn Rate、NDR 留存率與 LTV/CAC。
- **C (Context)**：比對 Top-tier VC 基準 (如 NDR ≥ 120%)。
- **C (Constraint)**：數字必須由背景 Code Execution 運算，禁止假造。
- **F (Format)**：輸出客戶留存與獲客效率矩陣。

</details>

<details>
<summary><b>🔹 模式 4：財務異常與 Red Flags 風險預警 (FDD Red Flag Auditor)</b></summary>

- **R (Role)**：財務盡調稽核專家 (FDD Red Flag Auditor)。
- **T (Task)**：掃描財報異動點，標示高風險項目。
- **C (Context)**：引用 `references/financial-metrics-guide.md` 之 Red Flag 檢核清單。
- **C (Constraint)**：分級標示 🔴 紅燈 (高度風險) 與 🟡 黃燈 (需注意)。
- **F (Format)**：輸出 Red Flag 風險檢核清單與稽核說明。

</details>

<details>
<summary><b>🔹 模式 5：全方位創投 IC 委員會財務盡調簡報 (VC Managing Partner & IC Chair)</b></summary>

- **R (Role)**：創投合夥人與 IC 委員會主席 (VC Managing Partner & IC Chair)。
- **T (Task)**：綜合執行模式 1~4，產出全覽式財務盡調簡報。
- **C (Context)**：結合上述所有專業知識庫與視覺化圖表。
- **C (Constraint)**：包含 IC 必問創辦人的 3 大關鍵財務問題。
- **F (Format)**：完全套用 `templates/financial-report-template.md` 產出完整 Markdown 報告。

</details>

---

## 🚀 學員實戰體驗：零程式碼操作 3 步驟

學員在 Claude.ai 介面上只需執行以下步驟，完全不需要開任何命令列或編寫程式：

### 步驟 1：取得測試用 Excel 財報（二選一）
- **方式 A (直接下載)**：直接從本項目的 `examples/` 資料夾下載 [sample_startup_financials.xlsx](file:///Users/roberthsu2003/Documents/GitHub/workflow-productivity/Claude_ai/Skills/VC_Financial_Analyzer/examples/sample_startup_financials.xlsx)。
- **方式 B (請 Claude 生成)**：在對話視窗直接對 Claude 說：「`請幫我生成一份測試用的創投財務報表 Excel 檔`」，Claude 就會透過背景 Python 自動產出一個 `.xlsx` 檔案供您下載。

### 步驟 2：上傳 Excel 並觸發 Skill
將 `sample_startup_financials.xlsx` 上傳至 Claude.ai 對話框，並輸入：

```text
請幫我分析這份公司的財務報表。
```

### 步驟 3：選擇分析模式，觀看自動產出報告
Claude 會自動掃描 Excel 結構並彈出 5 大建議選單。您只需回覆數字（例如輸入 `5`），Claude 即可在背景自動運算、自動繪製圖表，並呈現漂亮的繁體中文財務盡調報告！

---

← [返回 Skills 主頁](../README.md) | 🏠 [返回專案總首頁](../../README.md)

