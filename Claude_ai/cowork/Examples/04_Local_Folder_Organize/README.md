# 🗂️ 範例 4：本機資料夾批次自動整理與報銷總表產出

> 🟢 **適用方案**：Max / Pro / Team / Enterprise (Claude Desktop App macOS / Windows)  
> 💼 **適用角色**：行政特助、財務助理、專案經理 (PM)、個人自由工作者。  
> 🎯 **核心功能示範**：
> - 📁 **本機資料夾直接讀寫 (Direct Local File Access)**：無需手動上傳/下載檔案，Claude 能直接讀寫您的本機硬碟資料夾。
> - 💻 **本機資源連動 (Local File & Desktop Integration)**：在本地安全沙盒中批次掃描檔案、建立分類子目錄並移動歸檔。
> - 🛡️ **三大安全核准模式實戰 (Approval Modes: Manual / Auto / Skip)**：體驗檔案移動、新增目錄與寫入時，三種安全層級的行為差異。

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請先查看本資料夾下的練習檔案：
1. [`sample_files/raw_downloads/`](./sample_files/raw_downloads/)：模擬混亂的本機「下載」或「暫存」資料夾，內含 4 份未歸檔的偽檔案：
   - `INV_2026_08_GoogleWorkspace.txt`（8月份 Google Workspace 雲端辦公授權費發票）
   - `taxi_receipt_20260905.txt`（拜訪合作夥伴之計程車乘車證明）
   - `contract_partner_NDA_v1.txt`（法務保密協議草案）
   - `Q3_marketing_proposal_draft.txt`（Q3 行銷推廣企劃投影片文字稿）
2. [`sample_files/expenses_report_template.csv`](./sample_files/expenses_report_template.csv)：公司標準的財務報銷明細樣板。

---

## 🛡️ 三大安全核准模式 (Approval Modes) 實戰演練

本範例最適合用來體驗三種安全模式的差異：

| 核准模式 | 執行本範例時的行為表現 | 適用情境 |
| :--- | :--- | :--- |
| **Manually approve (Manual)** | Claude 每讀取一個檔案、建立新資料夾（如 `01_財務單據/`）、移動檔案前，介面皆會跳出 **「Allow / Deny」** 詢問視窗，由您逐一確認後才動工。 | 處理重要系統磁碟、敏感合約、機密財務帳目時推薦。 |
| **Automatically approve (Auto)** | Claude 連續自主讀取與移動檔案，背後有即時安全模型檢查是否包含注入指令或越權外洩；若無風險則順暢完成。 | 絕大多數日常行政、檔案整理推薦（兼顧效率與安全）。 |
| **Skip all approvals (Skip)** | 完全不審查、不暫停，以最高速度直接將所有檔案分類、重命名與移動完畢。 | 100% 信任的內部測試目錄、大量純文字檔案批次處理。 |

---

## 🤖 Cowork RTCCF 實戰 Prompt

開啟 **Claude Desktop App**，在 Cowork 模式下**選擇此 `sample_files` 資料夾**作為工作目錄，並輸入以下 Prompt：

```text
【Role】
你是一名高效能企業行政管理專員與財務助手。

【Task】
請檢查當前工作目錄下的 raw_downloads/ 資料夾，讀取裡面的所有檔案內容並執行以下工作：
1. 依據檔案性質建立分類子目錄：
   - 01_財務單據/
   - 02_法務合約/
   - 03_專案企劃/
2. 將 raw_downloads/ 中的檔案正規化重命名（格式：[類別]_[日期]_[項目名稱].[副檔名]）並移動至對應的子目錄中。
3. 針對所有屬於「財務單據」的檔案，提取其日期、廠商、金額、摘要與報銷人資訊，填入 expenses_report_template.csv 樣板中，並於同目錄產出 expenses_summary_202609.csv 報銷總表。

【Context】
- 工作目錄：當前指定資料夾
- 樣板路徑：expenses_report_template.csv

【Constraint】
- 移動與更名前請保持原始內容不損壞。
- 金額必須準確提取含稅總計。
- 使用繁體中文輸出執行結果報告。

【Format】
完成後，產出一份執行清單，說明每個檔案的原檔名、新檔名、移動路徑以及報銷總額統計。
```

---

## 🚀 學員操作 3 步驟

1. **開啟 Claude Desktop App**：切換為 **Cowork** 模式。
2. **指定本地工作資料夾**：點擊工作空間路徑，選擇本範例的 `sample_files/` 目錄。
3. **選擇核准模式並執行**：
   - 建議先選擇 **Manual** 模式，觀察 Claude 準備建立子目錄時跳出的審批確認按鈕；
   - 亦可切換為 **Auto** 模式，體驗一氣呵成自動在硬碟中分類檔案並生成報銷總表的流暢感！

---

← [返回 Cowork 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
