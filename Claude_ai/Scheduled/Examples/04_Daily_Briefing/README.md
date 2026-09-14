# 🌅 範例 4：每日晨報與行程郵件排程 (Daily Briefing)

> 🔵 **適用方案**：Pro / Max / Team / Enterprise (Scheduled Beta)  
> 💼 **適用角色**：高階主管、產品經理 (PM)、專案負責人、任何需要每日高效開工的知識工作者。  
> 🎯 **核心體驗**：設定「每個工作日 08:00 AM 定時排程」，Claude 會自動讀取你的日曆行程與未讀信件資料，自動比對潛在會議衝突、篩選緊急事項，並在 8 點準時為你備妥一份排版精美的「開工晨報」！

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請確認本目錄下之偽檔案：
1. [mock_calendar_events.json](./sample_files/mock_calendar_events.json)：模擬當日行事曆事件（包含會議名稱、起訖時間、地點與會者，並刻意設計了 14:00 與 14:30 的重疊衝突）。
2. [mock_unread_emails.csv](./sample_files/mock_unread_emails.csv)：模擬早晨收件匣的 4 封不同急迫度的信件（包含客戶緊急憑證過期通知、預算會議出席確認、常規報表等）。
3. [daily_briefing_template.md](./sample_files/daily_briefing_template.md)：每日晨報的標準 Markdown 輸出樣板。

---

## 🤖 Scheduled 排程 Prompt (RTCCF 標準架構)

在建立排程任務時，於 **Instructions** 欄位貼入以下指令：

```markdown
## Role
你是一位頂級**高階幕僚兼行政特助 (Executive Chief of Staff)**，專長是敏銳捕捉日常運作中的關鍵阻礙與會議衝突。

## Task
請讀取 `mock_calendar_events.json`（行事曆事件）與 `mock_unread_emails.csv`（未讀信件），嚴格依據 `daily_briefing_template.md` 樣板格式，產出一份今日晨報。

## Context
- 行程檔案：`mock_calendar_events.json`
- 郵件檔案：`mock_unread_emails.csv`
- 輸出樣板：`daily_briefing_template.md`

## Constraint
1. **行程衝突偵測**：主動比對行事曆中的時間，若發現時間重疊（例如 14:00 與 14:30），必須在「🚨 緊急優先處置事項」與「⚠️ 行程衝突警訊」明確標註警示，並提供協調建議。
2. **緊急郵件前置**：識別帶有 `URGENT` 或涉及客戶障礙的郵件（如 TechCorp 憑證到期），列入第一優先處置事項。
3. **客觀事實依據**：嚴格根據檔案中的與會者、時間、寄件人資料彙整，嚴禁憑空推撰。
4. **輸出語言**：請使用專業繁體中文。

## Format
完全套用 `daily_briefing_template.md` 結構輸出。
```

---

## 🚀 最新介面操作 5 步驟教學

請依照以下最新介面指引完成設定：

```
[左側側欄 Scheduled] 
        ↓
[右上角 New task ˇ] ➔ 選擇 [⚙️ Set up manually]
        ↓
[填寫 Create scheduled task 表單]
  • Name: 每日晨報與行程排程 (Daily Briefing)
  • Instructions: 貼上上方 RTCCF Prompt
  • Work in a project or folder: 選擇放置練習檔的專案或資料夾
  • Default model: 保持預設或選擇 Claude 3.7 Sonnet
  • Frequency: 選擇「Weekdays」並設定時間為 08:00 AM
  • Permissions: 選擇「Manually approve」或「Auto approve」
  • Require this computer: 關閉（使用雲端排程）或 開啟（若使用電腦本機資料夾）
        ↓
[點選 Save] ➔ 任務即建立於 Scheduled tasks 儀表板中！
```

### 💡 實戰小撇步
- **純雲端排程測試**：可先將 `mock_calendar_events.json`、`mock_unread_emails.csv` 與樣板上傳至 Claude 雲端 Project 中，在表單的 `Work in a project or folder` 綁定該 Project。
- **手動立即測試 (Run on demand)**：建立完成後，若不想等到平日早上 8 點，可直接在 Scheduled 列表中點選該任務右側的 **「Run now」**（立即執行一次），驗證生成的晨報效果！

---

← [返回 Scheduled 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
