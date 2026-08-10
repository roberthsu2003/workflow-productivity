# 💼 創投 (VC) 財報數據分析與 Code Execution 自動化實戰

> 🟢 **方案需求**：Free / Pro / Team / Enterprise 方案皆適用 (需開啟 Claude.ai 之 Code Execution / Analysis Tool 功能)  
> 💼 **適用對象**：創投分析師 (VC Analyst / Associate)、財務盡調審查員 (Financial Due Diligence Auditor) 與投資經理 (Investment Manager)。  
> 🎓 **核心技術**：展示 **「零程式基礎的 Code Execution 整合」** 技巧 —— 學員**完全不需要懂任何程式碼**，只需將 Excel 拖入對話框，Skill 就會指引 Claude.ai **在雲端背景自動執行 Python 計算與繪圖**，並產出專業的 IC 盡調報告。

---

## 💡 為什麼非工程師學員也能無痛使用 Code Execution？

很多學員以為 Code Execution (程式碼執行/Code Interpreter) 需要自己寫程式或執行指令，**這是一個誤解**！

在 Claude.ai 中：
1. **AI 負責寫 Code 與跑 Code (80%)**：學員只需上傳 Excel 檔案，Claude.ai 會在**背景自動編寫 Python 代碼、自動讀取試算表、自動計算公式並自動畫出圖表**。
2. **學員負責提問與做決策 (20%)**：學員完全不需要看懂背景的 Python Code，只需點選分析選單，並解讀最終產出的繁體中文報告與視覺化圖表。

---

## 📁 創投 Level 3 Skill 實體目錄結構 (完全免程式)

```text
VC_Financial_Analyzer/
├── README.md                              # 本實戰教學說明文件 (零程式基礎體驗)
├── SKILL.md                               # 主 Skill 檔 (後台 SOP：引導 Claude 背景跑 Python 運算與畫圖)
├── references/                            # 📚 創投專業參考知識庫 (給 Claude 參照的指標庫)
│   ├── financial-metrics-guide.md        # 1. VC 財務指標 (Runway, Burn Rate, NDR, LTV/CAC) 與 Red Flag 警訊
│   └── code-execution-rules.md           # 2. 指引 Claude 背景寫 Python 與繪圖的美感規範
├── templates/                             # 📄 標準 Markdown 輸出樣板
│   └── financial-report-template.md      # 1. 創投 IC 標準財務盡調與營運分析報告樣板
└── examples/                              # 📁 零門檻！學員專用練習檔
    └── sample_startup_financials.xlsx    # 學員可直接下載上傳測試的範例 Excel 財報
```

---

## 🛠️ 1 個 Skill 支援 5 大互動式財務分析模式

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

### 🔍 5 大分析模式詳細介紹

<details>
<summary><b>📊 模式 1：財務健康度與 Cash Runway 深度診斷</b></summary>

- **應用場景**：評估新創公司現金還能撐多久、每月淨燒錢速度是否過快，以及何時達到損益平衡。
- **Claude 背景自動化**：
  - 自動算出每月 Net Burn Rate 與 Runway 剩餘月數。
  - 背景自動繪製期末現金餘額與 6 個月安全警戒線 (Safety Horizon) 趨勢圖。
</details>

<details>
<summary><b>📈 模式 2：營收與成本結構成長趨勢分析</b></summary>

- **應用場景**：分析新創公司的營收成長動力（MRR 增幅）、毛利率變化，以及研發 (R&D) / 行銷 (S&M) / 管理 (G&A) 費用結構是否健康。
- **Claude 背景自動化**：
  - 自動算出 MoM / YoY 營收成長率與 Gross Margin %。
  - 背景自動繪製 Revenue vs. OpEx 雙軸消長圖。
</details>

<details>
<summary><b>🎯 模式 3：SaaS Unit Economics 與客戶動態分析</b></summary>

- **應用場景**：針對 SaaS 或訂閱制標的，評估客戶留存狀況與單一客戶獲利能力。
- **Claude 背景自動化**：
  - 自動運算 ARPU (平均客單價)、Churn Rate (流失率) 與 NDR (淨營收留存率)。
  - 自動對照頂尖 VC 基準 (如 Top-tier NDR ≥ 120%) 輸出評價。
</details>

<details>
<summary><b>🚨 模式 4：財務異常與 Red Flags 風險預警</b></summary>

- **應用場景**：投前財務盡調 (FDD) 快速掃描，尋找報表中隱藏的財務陷阱。
- **Claude 背景自動化**：
  - 比對 `references/financial-metrics-guide.md`，自動標示毛利急降、行銷費用爆增但新客停滯等異常項目。
</details>

<details>
<summary><b>🏆 模式 5：全方位創投 IC 委員會財務盡調簡報 (推薦)</b></summary>

- **應用場景**：需要一份包含完整數據、雙張趨勢圖表、風險預警與創辦人提問清單的完整簡報。
- **Claude 背景自動化**：
  - 綜合執行模式 1~4 之運算，渲染全套視覺化圖表，並套用 `templates/financial-report-template.md` 產出高品質報告。
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

← [返回 Skill 主索引](../README.md)
