# 💼 創投 (VC) 財報數據分析與 Code Execution 自動化實戰

> 🟢 **方案需求**：Free / Pro / Team / Enterprise 方案皆適用 (需支援 Python / Code Interpreter / Code Execution 功能)  
> 💼 **適用對象**：創投分析師 (VC Analyst / Associate)、財務盡調審查員 (Financial Due Diligence Auditor) 與投資經理 (Investment Manager)。  
> 🎓 **核心技術**：展示 **「進階數據與 Code Execution 整合」** 技巧 —— 如何讓 Claude 在接收 Excel/CSV 財務報表後，**主動提供互動式分析選單**，並呼叫 **Python 進行 100% 精準的財務運算與圖表繪製**，產出令投資委員會 (IC) 驚豔的專業盡調報告。

---

## 💡 為什麼創投財報分析必須結合 Code Execution？

在創投日常投前盡調 (Due Diligence) 或投後管理 (Portfolio Management) 中，處理財務報表面臨兩大核心痛點：

1. **零容忍的數據幻覺 (Zero Tolerance for Hallucinations)**：財務數字（如 Cash Runway、EBITDA、Gross Margin、NDR）不能由 LLM 憑空猜測估算，必須經由程式碼逐行進行精準加減乘除與動態彙整。
2. **視覺化與圖表需求 (Visualization for IC Committee)**：高階主管與投資委員會 (IC) 需要直觀的趨勢圖表（如現金流消長趨勢、營收與 OpEx 堆疊圖），而非單純的文字表格。

透過本 Skill，您可以實現 **「上傳 Excel → 自動掃描欄位 → 彈出建議選單 → 點選模式 → Python 計算與繪圖 → 產出標準 IC Markdown 報告」** 的全自動化工作流。

---

## 📁 創投 Code Execution Skill 實體目錄結構

```text
VC_Financial_Analyzer/
├── README.md                              # 本實戰教學說明文件
├── SKILL.md                               # 主 Skill 檔 (定義選單生成、路由與 Code Execution 規範)
├── references/                            # 📚 創投專業參考知識庫
│   ├── financial-metrics-guide.md        # 1. VC 財務指標、SaaS Unit Economics 與 Red Flag 警訊庫
│   └── code-execution-rules.md           # 2. Python pandas/matplotlib 代碼執行與圖表繪製規範
├── templates/                             # 📄 標準 Markdown 輸出樣板
│   └── financial-report-template.md      # 1. 創投 IC 標準財務盡調與營運分析報告樣板
└── scripts/                               # 🛠️ 測試腳本與數據工具
    └── generate_sample_excel.py          # 自動生成示範用創投財報 Excel (.xlsx) 腳本
```

---

## 🛠️ 1 個 Skill 支援 5 大互動式財務分析模式

本 Skill 名稱定義為 `vc-financial-analyzer`。當您將 Excel 檔案拖入對話框時，Skill 會先執行 **Phase 1 結構掃描**，並向您提示以下 5 種分析模式供您選擇：

```yaml
---
name: vc-financial-analyzer
description: >-
  當使用者上傳創投被投/標的公司之 Excel 財務報表 (.xlsx, .xls, .csv) 時，
  自動讀取檔案結構與工作表，向使用者提供 5 大專業財務分析模式選單。
  使用者選擇後，自動調用 Python Code Execution 進行精準數據計算與圖表視覺化渲染，
  並結合 references/ 創投規章與 templates/ 產出高階投資報告。
---
```

---

### 🔍 5 大分析模式詳細介紹

<details>
<summary><b>📊 模式 1：財務健康度與 Cash Runway 深度診斷</b></summary>

- **應用場景**：評估新創公司現金還能撐多久、每月淨燒錢速度是否過快，以及何時達到損益平衡。
- **Python 運算與圖表**：
  - 計算每月 Net Burn Rate 與 Runway 剩餘月數。
  - 繪製期末現金餘額與 6 個月安全警戒線 (Safety Horizon) 趨勢圖。
</details>

<details>
<summary><b>📈 模式 2：營收與成本結構成長趨勢分析</b></summary>

- **应用場景**：分析新創公司的營收成長動力（MRR 增幅）、毛利率變化，以及研發 (R&D) / 行銷 (S&M) / 管理 (G&A) 費用結構是否健康。
- **Python 運算與圖表**：
  - 計算 MoM / YoY 營收成長率與 Gross Margin %。
  - 繪製 Revenue vs. OpEx 雙軸消長圖。
</details>

<details>
<summary><b>🎯 模式 3：SaaS Unit Economics 與客戶動態分析</b></summary>

- **應用場景**：針對 SaaS 或訂閱制標的，評估客戶留存狀況與單一客戶獲利能力。
- **Python 運算與圖表**：
  - 自動運算 ARPU (平均客單價)、Churn Rate (流失率) 與 NDR (淨營收留存率)。
  - 對照頂尖 VC 基準 (如 Top-tier NDR ≥ 120%) 輸出評價。
</details>

<details>
<summary><b>🚨 模式 4：財務異常與 Red Flags 風險預警</b></summary>

- **應用場景**：投前財務盡調 (FDD) 快速掃描，尋找報表中隱藏的財務陷阱。
- **Python 運算與圖表**：
  - 比對 `references/financial-metrics-guide.md`，自動標示毛利急降、行銷費用爆增但新客停滯等異常項目。
</details>

<details>
<summary><b>🏆 模式 5：全方位創投 IC 委員會財務盡調簡報 (推薦)</b></summary>

- **應用場景**：需要一份包含完整數據、雙張趨勢圖表、風險預警與創辦人提問清單的完整簡報。
- **Python 運算與圖表**：
  - 綜合執行模式 1~4 之運算，渲染全套視覺化圖表，並套用 `templates/financial-report-template.md` 產出高品質報告。
</details>

---

## 🚀 實戰體驗：Step-by-Step 測試教學

### 步驟 1：生成示範用 Excel 財務報表
若您手邊暫無 Excel 報表，可執行目錄下的 Python 腳本生成一份標準的創投測試財報：

```bash
uv run --with pandas --with openpyxl python3 scripts/generate_sample_excel.py
```
> 執行後將在目錄下生成 `sample_startup_financials.xlsx`（包含損益表 P&L、現金流與 Runway、營運指標 KPIs 三張工作表）。

### 步驟 2：上傳 Excel 檔案並觸發 Skill
將 `sample_startup_financials.xlsx` 上傳至 Claude，並輸入提示詞：

```text
請幫我分析這份公司的財務報表。
```

### 步驟 3：選擇分析模式並觀看 Code Execution 成果
Claude 將自動掃描 Excel 欄位，彈出 5 大分析建議選單。回覆數字（例如：`5`），Claude 即會自動編寫 Python 程式碼進行數據運算與圖表繪製，並產出完美的財務盡調報告！

---

← [返回 Skill 主索引](../README.md)
