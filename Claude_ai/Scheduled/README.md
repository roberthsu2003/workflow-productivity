# Scheduled（排程任務）：讓 Claude 定時自動幫你工作

> 🔵 **方案需求**：**Pro / Max / Team / Enterprise 付費方案**皆可使用；目前 Claude Cowork 仍在 Web 與行動版 Beta 階段，優先開放 Max 方案，其餘方案陸續開放中。  
> 參考：[Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)

**Scheduled（排程任務）**讓你把重複性工作「說一次、之後自動跑」。不用每次都重新開對話下指令，Claude 會依照你設定的頻率自動執行，並在完成後產出報告、簡報或摘要等成品。

---

## 🕒 排程任務能做什麼

排程任務擁有和一般 Cowork 任務相同的能力，包含已連結的工具（Connectors）、Skills 與已安裝的 Plugins。常見用途：

1. **每日簡報**：彙整過去 24 小時的 Slack 訊息、Email 或行事曆事件
2. **週報彙整**：整合 Google Drive、試算表或其他連線工具的資料成週報
3. **定期研究追蹤**：持續追蹤特定主題、競爭對手或產業新聞
4. **檔案整理**：定期整理、清理或處理指定資料夾中的檔案
5. **團隊更新**：從專案管理工具產生站立會議或狀態摘要

---

## ⚙️ 運作方式

- 建立排程任務時，Claude 會把你的指令存成任務的「執行說明」，並依你設定的頻率自動執行
- 每一次執行都是一個獨立的 Cowork Session，完成後可像一般任務一樣檢視結果
- 排程任務在**雲端遠端執行**，即使電腦休眠或 Claude Desktop 未開啟，也會準時執行
- 點選側欄的「Scheduled」即可檢視所有排程任務的過去與未來執行紀錄

> ⚠️ **限制**：排程任務只能使用內建的排程選項，搭配你的 Connectors 與存放在 Claude 帳號中的檔案；**無法綁定你電腦上的本機資料夾**（若任務需要本機檔案或應用程式，該任務只能在本機執行）。

---

## 🚀 建立排程任務的兩種方式

### 方式一：與 Claude 一起建立

1. 點選左側欄「Scheduled」，進入 **Scheduled tasks** 頁面
2. 點選右上角「New task」，選擇「Create with Claude」
3. Claude 會自動帶入一段提示，詢問你想建立什麼樣的排程任務
4. Claude 可能會用**多選題**方式向你確認細節
5. 確認無誤後，Claude 會列出任務名稱、執行頻率與任務內容，點選「Schedule」即可完成排程

### 方式二：手動設定

1. 點選左側欄「Scheduled」，進入 **Scheduled tasks** 頁面
2. 點選右上角「New task」，選擇「Set up manually」
3. 填寫：任務名稱、任務指令（Prompt）、核准模式、執行頻率（每小時／每日／每週／工作日／手動）、模型選擇（可選）、工作資料夾（可選）
4. 點選「Save」完成建立

---

## 📋 管理排程任務

點選側欄「Scheduled」即可：

- 檢視所有已建立的排程任務
- 檢視過去與未來的執行紀錄
- 進入個別任務，手動編輯指令或頻率
- 暫停 / 恢復任務
- 刪除任務
- 手動立即執行一次任務

---

## 💡 教學提醒

若你的帳號目前尚未看到「Scheduled」功能，通常是因為：

1. 帳號方案尚未包含 Cowork（僅限 Pro / Max / Team / Enterprise）
2. Cowork 仍在 Beta 階段，功能依方案分階段開放

可先參考本章節了解概念與操作邏輯，待帳號開通後即可直接上手。

---

← [返回上層：Claude_AI 索引](../README.md)
