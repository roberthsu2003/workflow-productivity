# 📊 範例 1：每週團隊進度與風險排程報告 (Scheduled Weekly Brief)

> 🔵 **適用方案**：Pro / Max / Team / Enterprise (Scheduled Beta)  
> 💼 **適用角色**：專案經理 (PM)、部門主管、團隊 Leader、行政幕僚。  
> 🎯 **核心體驗**：設定「每週五 17:00 雲端定時排程」，Cowork 會自動讀取上傳至專案的同仁週報 CSV，彙整焦點、找出卡點風險，並在電腦休眠狀態下自動完成 Markdown 週會簡報！

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請先下載並查看本資料夾下的練習檔案：
1. [team_weekly_updates.csv](./sample_files/team_weekly_updates.csv)：同仁本週回報進度、卡點風險與下一步預計目標。
2. [weekly_brief_template.md](./sample_files/weekly_brief_template.md)：定時排程產出的標準 Markdown 週會簡報樣板。

---

## 🤖 Cowork Scheduled 排程 Prompt (RTCCF)

在 Cowork 的 Scheduled 頁面設定排程時貼入此 Prompt：

```text
【Role】
你是一名高效的專案營運經理 (Project Operations Manager)。

【Task】
請讀取上傳的 team_weekly_updates.csv 同仁週報數據，自動合併重複或次要進度，重點找出「進度卡點/風險」項目，並將結論填入 weekly_brief_template.md 樣板中，產出一份每週會議簡報。

【Context】
- 上傳檔案 1：team_weekly_updates.csv (同仁進度紀錄)
- 上傳檔案 2：weekly_brief_template.md (簡報樣板)

【Constraint】
- 有卡點或延遲的項目必須標示 🔴 高 或 🟡 中 優先級。
- 人名與部門必須對齊，禁止憑空推撰。
- 使用繁體中文輸出。

【Format】
完全套用 weekly_brief_template.md 樣板格式。
```

---

## 🚀 排程設定 3 步驟 (Cowork Scheduled)

1. **開啟 Scheduled 頁面**：登入 [claude.ai](https://claude.ai)，從左側選單進入 **Scheduled**。
2. **建立新排程**：點選 **New task** ➔ 輸入任務名稱 `每週五團隊簡報排程` ➔ 選擇頻率為 **「Weekly (每週五 17:00)」**。
3. **上傳練習檔與貼上 Prompt**：將 `team_weekly_updates.csv` 與 `weekly_brief_template.md` 附加至任務中，貼上上述 RTCCF Prompt 即可完成雲端自動化排程！

---

← [返回 Scheduled 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
