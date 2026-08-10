# 📈 範例 2：跨來源財務與營運數據自動對比工作流

> 🟢 **適用方案**：Max / Pro / Team / Enterprise (Cowork Beta)  
> 💼 **適用角色**：財務分析師、營運經理、創投風控員、高階幕僚。  
> 🎯 **核心體驗**：體驗 Cowork 背景自動寫 Python 程式碼讀取多個 CSV/Excel 檔案，交叉比對「實際營收/費用」與「目標預算」，自動找出超支與毛利衰退警訊，並繪製對比圖表。

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請先下載並查看本資料夾下的練習檔案：
1. [q3_financial_raw.csv](./sample_files/q3_financial_raw.csv)：Q3 實際財務數據（含各月份 SaaS 與硬體部門營收、費用、現金餘額）。
2. [crm_sales_target.csv](./sample_files/crm_sales_target.csv)：CRM 系統登載的 Q3 營運目標與預算上限。

---

## 🤖 Cowork RTCCF 實戰 Prompt

將以下 Prompt 複製至 Cowork 視窗中（並上傳上述兩份練習檔）：

```text
【Role】
你是一名資深企業財務分析師與營運風控專員 (Financial Controller)。

【Task】
請讀取上傳的 q3_financial_raw.csv 與 crm_sales_target.csv 兩份檔案，透過背景 Code Execution 執行交叉比對，計算各部門（SaaS訂閱 vs 硬體設備）的「目標達成率 (%)」、「費用超支金額」與「期末 Cash Runway 營運月數」，並產出一份 Q3 營運對比分析報告與圖表。

【Context】
- 上傳檔案 1：q3_financial_raw.csv (實際財務數據)
- 上傳檔案 2：crm_sales_target.csv (預算與營運目標)

【Constraint】
- 數字必須 100% 經由背景 Code Execution 自動運算，嚴禁推算。
- 若硬體部門連續出現淨虧損，須標示 🔴 高度警訊。
- 背景自動繪製一張「實際營收 vs 目標營收對比圖」嵌入報告中。
- 使用繁體中文輸出。

【Format】
產出包含執行摘要表、部門對比分析、圖表與 3 大財務改善建議的 Markdown 報告。
```

---

## 🚀 學員操作 3 步驟

1. **開啟 Cowork**：登入 [claude.ai](https://claude.ai) 點選切換至 **Cowork** 工作空間。
2. **上傳檔案與貼上 Prompt**：將 `q3_financial_raw.csv` 與 `crm_sales_target.csv` 拖入對話框，貼上上述 RTCCF Prompt。
3. **觀看自動化執行**：Cowork 會在背景自動寫 Python 程式碼、自動運算與自動畫圖，並輸出高品質的對比報告！

---

← [返回 Cowork 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
