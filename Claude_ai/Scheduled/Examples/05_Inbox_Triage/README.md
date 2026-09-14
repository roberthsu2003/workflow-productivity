# 📥 範例 5：收件匣分類與緊急回覆草擬排程 (Scheduled Inbox Triage)

> 🔵 **適用方案**：Pro / Max / Team / Enterprise (Scheduled Beta)  
> 💼 **適用角色**：客戶成功經理 (CSM)、營運特助、技術支援 Lead、業務代表。  
> 🎯 **核心體驗**：設定「平日每天 08:00 AM 定時排程」，自動讀取待處理信件清單，依據優先級矩陣分流（P0 系統中斷、P1 商業商機、P2 客服、P3 反饋），並針對緊急信件直接寫好高質量的回覆草稿！

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請確認本目錄下之偽檔案：
1. [customer_inquiries.csv](./sample_files/customer_inquiries.csv)：模擬收件匣待處理的 4 筆客戶郵件（涵蓋 API 403 阻礙出貨的 P0 緊急事件、50 人企業版詢價 P1、帳號登入問題 P2、產品功能建議 P3）。
2. [triage_rules.md](./sample_files/triage_rules.md)：收件匣分流矩陣與草擬規範規章。

---

## 🤖 Scheduled 排程 Prompt (RTCCF 標準架構)

在建立排程任務時，於 **Instructions** 欄位貼入以下指令：

```markdown
## Role
你是一位經驗豐富的**客戶營運主管 (Customer Operations Manager)**，具備敏銳的事件優先順序判斷與專業商務溝通技巧。

## Task
請讀取 `customer_inquiries.csv` 中的所有信件，依據 `triage_rules.md` 定義的規則進行分流分類，產出一份「收件匣分流處置清單」，並針對 **P0（緊急阻礙）** 與 **P1（商務商機）** 撰寫可直接複製寄送的正式回覆草稿。

## Context
- 郵件清單：`customer_inquiries.csv`
- 分類準則：`triage_rules.md`

## Constraint
1. **分流等級精準**：嚴格依據 `triage_rules.md` 的 P0~P3 定義劃分，不得隨意降級或升級。
2. **生成回覆草稿**：針對 P0（如 MegaRetail Corp 的 API 403 問題）與 P1（如 Global Trade 的 50 人方案諮詢），必須產出完整、得體且具備具體下一步行動的正式回信草稿。
3. **內部轉派指引**：每一筆信件後方需明確指出「建議內部處置人員」（例如：轉發 SRE / 轉發業務團隊 / 客服組處理）。
4. **輸出語言**：請使用專業繁體中文。

## Format
1. **收件匣優先級摘要表**（包含 Ticket ID、寄件人、主旨、優先等級、轉派單位、建議處置期限）。
2. **高優先級回覆草稿專區**（P0 與 P1 的完整 Email 內文範本）。
```

---

## 🚀 最新介面操作 5 步驟教學

```
[左側側欄 Scheduled] 
        ↓
[右上角 New task ˇ] ➔ 選擇 [⚙️ Set up manually]
        ↓
[填寫 Create scheduled task 表單]
  • Name: 每日晨間收件匣分流與草稿排程 (Inbox Triage)
  • Instructions: 貼上上方 RTCCF Prompt
  • Work in a project or folder: 選擇放置練習檔的專案或資料夾
  • Default model: 保持預設或選擇 Claude 3.7 Sonnet
  • Frequency: 選擇「Weekdays」並設定時間為 08:00 AM
  • Permissions: 選擇「Manually approve」或「Auto approve」
  • Require this computer: 關閉（純雲端執行）
        ↓
[點選 Save] ➔ 立即生效！可點選「Run now」手動觸發測試成果。
```

---

← [返回 Scheduled 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
