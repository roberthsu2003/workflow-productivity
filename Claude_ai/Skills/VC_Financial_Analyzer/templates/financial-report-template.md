# 💼 [標的公司名稱] 財務分析與盡職調查報告 (Financial Due Diligence Report)

> **報告產生時間**：{{REPORT_DATE}}  
> **評估模式**：{{ANALYSIS_MODE_NAME}}  
> **數據來源檔案**：`{{SOURCE_FILE_NAME}}`  
> **分析執行工具**：Code Interpreter (Python Pandas & Matplotlib Engine)

---

## 📊 1. 執行摘要 (Executive Summary)

* **整體財務健康評級**：{{HEALTH_RATING_BADGE}} (🟢 強健 / 🟡 中度注意 / 🔴 高度風險)
* **核心亮點 (Highlights)**：
  1. {{HIGHLIGHT_1}}
  2. {{HIGHLIGHT_2}}
* **主要疑慮與風險 (Key Concerns)**：
  1. {{CONCERN_1}}
  2. {{CONCERN_2}}

---

## 📈 2. 關鍵財務指標總覽 (Key Financial Metrics Dashboard)

| 評估維度 | 當前數值 (Current) | 上季/前期對比 (QoQ/MoM) | VC 行業基準 (Benchmark) | 評價狀態 |
| :--- | :--- | :--- | :--- | :--- |
| **月度可重複營收 (MRR)** | {{CURRENT_MRR}} | {{MRR_GROWTH}} | SaaS 成長階段 > 10% MoM | {{MRR_STATUS}} |
| **毛利率 (Gross Margin %)** | {{GROSS_MARGIN}} | {{GM_CHANGE}} | Enterprise SaaS ≥ 75% | {{GM_STATUS}} |
| **月淨燒錢率 (Net Burn)** | {{NET_BURN}} | {{BURN_CHANGE}} | 視融資規模與 Burn Multiple | {{BURN_STATUS}} |
| **現金續航力 (Runway)** | **{{RUNWAY_MONTHS}} 個月** | {{RUNWAY_TREND}} | 建議維持 ≥ 18 個月 | {{RUNWAY_STATUS}} |
| **淨營收留存率 (NDR)** | {{NDR_VALUE}} | {{NDR_TREND}} | Top Tier ≥ 120% | {{NDR_STATUS}} |

---

## 🔍 3. 專題深度數據分析 (In-Depth Data Analysis & Charts)

### 3.1 營收與費用消長趨勢 (Revenue vs. OpEx)
{{REVENUE_OPEX_ANALYSIS_PARAGRAPH}}

![營收與費用趨勢圖](./charts/financial_trend.png)

### 3.2 現金流與 Runway 斷裂預警 (Cash Runway & Burn Scenario)
{{RUNWAY_ANALYSIS_PARAGRAPH}}

![現金流與 Runway 趨勢圖](./charts/cash_runway_chart.png)

---

## 🚨 4. 財務異常與風險警訊 (Financial Red Flags Audit)

> 💡 *本區塊由 Code Execution 對照 `references/financial-metrics-guide.md` 自動檢測比對。*

- [ ] **毛利異常 (Gross Margin Anomalies)**：{{RED_FLAG_GM}}
- [ ] **費用結構異常 (OpEx Spike Alert)**：{{RED_FLAG_OPEX}}
- [ ] **客戶流失與 CAC 效益 (Churn & CAC Risk)**：{{RED_FLAG_CHURN}}
- [ ] **現金流枯竭警訊 (Runway Depletion Alert)**：{{RED_FLAG_RUNWAY}}

---

## 💡 5. 投資委員會 (IC) 盡調追蹤建議與詢問清單

1. **財務盡調 (FDD) 追蹤項目**：
   - {{FDD_ACTION_1}}
   - {{FDD_ACTION_2}}
2. **IC 會議必問創辦人 3 大關鍵財務題**：
   * ❓ **Q1**：{{FOUNDER_Q1}}
   * ❓ **Q2**：{{FOUNDER_Q2}}
   * ❓ **Q3**：{{FOUNDER_Q3}}

---
*報告由 `VC_Financial_Analyzer` Agent Skill 自動編譯與 Code Execution 繪製產出*
