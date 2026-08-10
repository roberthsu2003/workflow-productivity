# 💰 範例 3：每週競品價格與促銷變化排程追蹤 (Scheduled Price Monitor)

> 🔵 **適用方案**：Pro / Max / Team / Enterprise (Scheduled Beta)  
> 💼 **適用角色**：電子商務營運經理、訂價策略分析師、產品行銷 (PMM)、採購。  
> 🎯 **核心體驗**：設定「每週一 08:00 雲端定時排程」，Cowork 會自動透過 Code Execution 比對我方商品售價與競品市場價格，計算價差比 (Price Variance %)，並在保障成本底價前提下自動建議跟價或促銷策略！

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請先下載並查看本資料夾下的練習檔案：
1. [our_product_catalog.csv](./sample_files/our_product_catalog.csv)：我方商品目錄（包含 SKU、我方定價、成本底價、最低毛利門檻）。
2. [competitor_market_prices.csv](./sample_files/competitor_market_prices.csv)：最新採集之競品市場價格與促銷活動紀錄。

---

## 🤖 Cowork Scheduled 排程 Prompt (RTCCF)

在 Cowork 的 Scheduled 頁面設定排程時貼入此 Prompt：

```text
【Role】
你是一名資深電商營運與動態訂價策略經理 (Pricing Strategy Manager)。

【Task】
請讀取上傳的 our_product_catalog.csv 與 competitor_market_prices.csv 兩份檔案，透過背景 Code Execution 計算各 SKU 的價差百分比：
$$\text{價差比 (\%)} = \frac{\text{競品售價} - \text{我方售價}}{\text{我方售價}} \times 100\%$$
找出競品售價低於我方超過 10% 的商品，並在「不得低於成本底價」的限制下，給出調價或贈品促銷建議。

【Context】
- 上傳檔案 1：our_product_catalog.csv (我方商品與底價)
- 上傳檔案 2：competitor_market_prices.csv (競品價格與促銷)

【Constraint】
- 算術必須由背景 Code Execution 自動運算。
- 建議售價絕不得低於該商品之成本底價與最低毛利門檻。
- 競品大幅降價項目須標示 🔴 高度關注。
- 使用繁體中文輸出。

【Format】
產出一份包含價差趨勢總覽表、動態跟價建議表與行銷促銷方案的每週報告。
```

---

## 🚀 排程設定 3 步驟 (Cowork Scheduled)

1. **開啟 Scheduled 頁面**：登入 [claude.ai](https://claude.ai)，從左側選單進入 **Scheduled**。
2. **建立新排程**：點選 **New task** ➔ 輸入任務名稱 `每週一競品價格巡檢與跟價建議` ➔ 選擇頻率為 **「Weekly (每週一 08:00)」**。
3. **上傳練習檔與貼上 Prompt**：將 `our_product_catalog.csv` 與 `competitor_market_prices.csv` 附加至任務中，貼上上述 RTCCF Prompt 即可完成定時跟價排程！

---

← [返回 Scheduled 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
