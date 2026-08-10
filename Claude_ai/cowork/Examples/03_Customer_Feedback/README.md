# 💬 範例 3：客戶客訴與意見自動分類處置工作流

> 🟢 **適用方案**：Max / Pro / Team / Enterprise (Cowork Beta)  
> 💼 **適用角色**：客服主管、產品經理 (PM)、客戶成功專員 (CSM)、行政營運。  
> 🎯 **核心體驗**：體驗 Cowork 讀取批量客訴表格，自動對照 SOP 進行「緊急程度評級 (🔴 Level 1 ~ 🟢 Level 3)」，自動撰寫專屬回信草稿，並產出產品改進行動清單。

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請先下載並查看本資料夾下的練習檔案：
1. [customer_support_logs.csv](./sample_files/customer_support_logs.csv)：原始客訴與客服單號紀錄（含金流失敗、發票錯誤、系統變慢等真實情境）。
2. [sop_escalation_rules.md](./sample_files/sop_escalation_rules.md)：公司內部客訴風險評級與回應 SLA 規章。

---

## 🤖 Cowork RTCCF 實戰 Prompt

將以下 Prompt 複製至 Cowork 視窗中（並上傳上述兩份練習檔）：

```text
【Role】
你是一名資深客戶成功與服務品質控管主管 (Head of Customer Success)。

【Task】
請讀取上傳的 customer_support_logs.csv 客訴紀錄，並嚴格對照 sop_escalation_rules.md 的評級標準，為每筆單號進行情緒與風險評級（🔴 Level 1 / 🟡 Level 2 / 🟢 Level 3）。針對 🔴 Level 1 的高風險案件，自動撰寫一份安撫客戶並承諾處理的客製化回信草稿；最後整理一份產品改善清單給工程團隊。

【Context】
- 上傳檔案 1：customer_support_logs.csv (5筆測試客訴單號)
- 上傳檔案 2：sop_escalation_rules.md (評級標準與 SOP)

【Constraint】
- 評級必須嚴格遵循 SOP（金流/發票錯誤一律標示 🔴 Level 1）。
- 回信草稿必須展現極高的專業誠意，包含案件編號與承諾回應時間。
- 使用繁體中文輸出。

【Format】
產出包含客訴評級摘要表、Level 1 高風險回信草稿與產品改善建議行動清單。
```

---

## 🚀 學員操作 3 步驟

1. **開啟 Cowork**：登入 [claude.ai](https://claude.ai) 點選切換至 **Cowork** 工作空間。
2. **上傳檔案與貼上 Prompt**：將 `customer_support_logs.csv` 與 `sop_escalation_rules.md` 拖入對話框，貼上上述 RTCCF Prompt。
3. **觀看自動化執行**：Cowork 會自動完成分類、自動產出 Level 1 客戶的完整道歉/說明信草稿，並整理好 PM 專用的產品優化表！

---

← [返回 Cowork 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
