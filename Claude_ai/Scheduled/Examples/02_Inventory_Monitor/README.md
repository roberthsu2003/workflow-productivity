# 📦 範例 2：每日庫存與供應鏈異常定時巡檢 (Scheduled Inventory Monitor)

> 🔵 **適用方案**：Pro / Max / Team / Enterprise (Scheduled Beta)  
> 💼 **適用角色**：資材主管、倉管經理、供應鏈營運專員、採購人員。  
> 🎯 **核心體驗**：設定「每日 09:00 雲端定時排程」，Claude 會自動透過 Code Execution 讀取每日庫存 CSV、計算安全庫存天數 (DOI)，並在斷貨風險發生前自動發出紅黃燈補貨警訊！

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請先下載並查看本資料夾下的練習檔案：
1. [daily_inventory_status.csv](./sample_files/daily_inventory_status.csv)：每日庫存現況數據（含 SKU、當前庫存量、日消耗量、供應商交期）。
2. [reorder_threshold_rules.md](./sample_files/reorder_threshold_rules.md)：安全庫存 DOI 天數計算公式與紅黃燈判定 SOP 規章。

---

## 🤖 排程 Prompt (RTCCF)

在對話中建立排程時貼入此 Prompt（開頭加上「請幫我設定排程：」及執行頻率即可）：

```markdown
## Role
你是一名資深**供應鏈風控**與**資材管理經理 (Supply Chain Manager)**。

## Task
請讀取每日上傳更新的 `daily_inventory_status.csv` 數據，透過背景 **Code Execution** 運算每項商品的 **DOI 可用天數**（當前庫存數 ÷ 日平均消耗數）。然後對照 `reorder_threshold_rules.md` 的判定標準，找出面臨斷貨風險的商品，產出一份**每日庫存巡檢與採購警訊報告**。

## Context
- 上傳檔案 1：`daily_inventory_status.csv`（每日庫存檔）
- 上傳檔案 2：`reorder_threshold_rules.md`（補貨 SOP 規章）

## Constraint
- DOI 可用天數必須 **100% 由背景 Code Execution 計算**。
- 若 DOI 剩餘天數低於交期天數+2天，必須標示 **🔴 缺貨極高風險**，並計算**建議急採購量**。
- 使用**繁體中文**輸出。

## Format
產出一份包含**風險警戒統計**、**急需採購清單表**與**資材控管建議**的 Markdown 報告。
```

---

## 🚀 排程設定 3 步骤 

1. **開新對話**：登入 [claude.ai](https://claude.ai) 開一個新對話（或從左側 **Scheduled** 頁面的 **New task** 手動建立）。
2. **說明排程**：告訴 Claude 任務名稱 `每日庫存巡檢與採購預警` 與頻率 **「Daily (每日 09:00)」**。
3. **上傳練習檔與貼上 Prompt**：將 `daily_inventory_status.csv` 與 `reorder_threshold_rules.md` 附加至任務中，貼上上述 RTCCF Prompt 即可開啟定時自動巡檢！

---

← [返回 Scheduled 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
