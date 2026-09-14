# 📅 範例 6：重要會議前置調查與與會者簡報排程 (Scheduled Meeting Prep)

> 🔵 **適用方案**：Pro / Max / Team / Enterprise (Scheduled Beta)  
> 💼 **適用角色**：商務開發 (BD)、業務顧問、專案經理、企業諮詢顧問。  
> 🎯 **核心體驗**：設定「平日每天 08:00 AM 定時排程」或於會議前定時執行，Claude 會主動比對當日重要客戶會議清單與客戶歷史情報檔案，在會議開始前為你產出一份「關鍵與會者心態分析、提問攻防對策、通關必勝指引」的簡報備忘錄！

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請確認本目錄下之偽檔案：
1. [upcoming_meetings.json](./sample_files/upcoming_meetings.json)：即將召開的重要提案會議資訊（包含客戶名稱、與會代表張副總與李總監各自在乎的關切點、會議目標等）。
2. [client_background_dossier.md](./sample_files/client_background_dossier.md)：客戶歷史背景、歷次交手踩雷經驗、關鍵利害關係人個性特質與技術驗收指標。

---

## 🤖 Scheduled 排程 Prompt (RTCCF 標準架構)

在建立排程任務時，於 **Instructions** 欄位貼入以下指令：

```markdown
## Role
你是一位頂級的**戰略諮詢顧問兼商務幕僚 (Chief Commercial Strategist)**。

## Task
請讀取 `upcoming_meetings.json`（即將召開的會議）與 `client_background_dossier.md`（客戶歷史情報檔案），為今日即將召開的「Apex Logistics 智慧倉儲方案提案會議」生成一份**會議準備戰略簡報 (Meeting Briefing Dossier)**。

## Context
- 會議資訊：`upcoming_meetings.json`
- 客戶歷史檔案：`client_background_dossier.md`

## Constraint
1. **利益關係人精準攻防**：必須針對與會的兩大關鍵人物（IT 副總裁張建國、營運總監李雅婷），分別提煉出「最在意的核心痛點」、「可能提出的質疑或尖銳提問」以及「我方建議的最佳應對說詞」。
2. **禁忌提醒**：從情報檔案中找出絕對不能踩的雷點（例如：避免空洞行銷話術，張副總三年曾遇過跨國延遲痛點）。
3. **推進目標策略**：聚焦在本次會議的核心目標「爭取進入下階段 POC 簽約」，列出 3 項會議收尾必問的成交提問。
4. **輸出語言**：請使用專業繁體中文。

## Format
請分為四大區塊：
一、會議基本情報與核心目標
二、關鍵利害關係人戰略攻防卡片 (Stakeholder Battlecard)
三、預想 Q&A 與應對攻防腳本
四、會議成功通關 Check-list
```

---

## 🚀 最新介面操作 5 步驟教學

```
[左側側欄 Scheduled] 
        ↓
[右上角 New task ˇ] ➔ 選擇 [⚙️ Set up manually]
        ↓
[填寫 Create scheduled task 表單]
  • Name: 重要客戶會議前置簡報排程 (Meeting Prep)
  • Instructions: 貼上上方 RTCCF Prompt
  • Work in a project or folder: 選擇放置練習檔的專案或資料夾
  • Default model: 選擇 Claude 3.7 Sonnet (思考深度與戰略分析更佳)
  • Frequency: 選擇「Weekdays」並設定時間為 08:00 AM
  • Permissions: 選擇「Manually approve」或「Auto approve」
  • Require this computer: 關閉（純雲端執行）
        ↓
[點選 Save] ➔ 完成建立！可點擊「Run now」立刻檢驗戰略簡報產出品質。
```

---

← [返回 Scheduled 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
