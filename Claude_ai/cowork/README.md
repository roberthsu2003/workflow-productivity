# Claude Cowork：全新 AI 協作與自動化工作空間

> 🔵 **方案需求**：**Max / Pro / Team / Enterprise 付費方案**（目前於 Web 與行動版 Beta 階段提供，優先開放 Max 方案）。  
> 官方參考：[Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)

**Claude Cowork** 是 Anthropic 推出的全新 AI 協作模式。打破傳統「一問一答」的對話限制，Cowork 提供了一個自主性更高、支援背景運算與自動排程的 AI 協作工作空間，讓 Claude 能扮演真正的「數位神隊友」，獨立完成多步驟任務。

---

## 💡 一、什麼是 Claude Cowork？

傳統對話模式（Chat）適合快速發問與單次解答；而 **Claude Cowork** 則專為**複雜工作流程與長任務**而設計。

在 Cowork 工作空間中，您可以為 Claude 設定目標，Claude 會自行規劃執行步驟、調用工具（Connectors、Skills、Plugins）、讀取知識庫（Projects），並在雲端自主完成任務後交付結構化成品。

---

## 📊 二、Cowork vs 一般對話（Chat）比較

| 比較項目 | 一般對話（Chat） 💬 | Claude Cowork 🤝 |
| :--- | :--- | :--- |
| **工作方式** | 單次問答、隨時互動 | 獨立自主執行多步驟工作流 |
| **執行環境** | 前台對話視窗 | 獨立 Cowork Session（支援背景遠端執行） |
| **自動化排程** | 需手動回到對話框下指令 | 支援 Scheduled 雲端定時自動執行 |
| **工具整合** | 需手動傳送檔案與資料 | 整合 Connectors、Skills、Projects 與 Plugins |
| **適用情境** | 靈感發想、單一問答、即時除錯 | 每日新聞彙整、營運週報、多來源數據分析與排程交付 |

---

## 🚀 三、Claude Cowork 核心能力

### 1. 🤖 自主任務執行 (Autonomous Execution)
- 輸入目標後，Claude 會自主拆解步驟、連續調用相關工具，無須人為一步步提示。
- 支援產出 Rich Artifacts（文件、簡報大綱、表單、報告）。

### 2. 🕒 雲端排程任務 (Scheduled Tasks)
- 支援設定「每小時 / 每日 / 每週 / 工作日」定時自動執行。
- 任務在雲端伺服器運行，即使個人電腦關機或瀏覽器關閉也會準時完成。

### 3. 🔌 跨工具與知識庫串接 (Tools & Projects Integration)
- 可同時讀取 **Projects 雲端知識庫** 中的歷史檔案與關注清單。
- 配合 **Connectors** 存取 Google Drive、Gmail、Slack 等服務。
- 自動套用自訂 **Skills**（如語氣修飾、格式樣板）。

---

## 🎓 四、3 大職場自動化實戰範例 (含學員練習檔)

為幫助學員無痛上手 Cowork，本單元提供 3 個真實職場場景的實戰範例，每個範例皆附有可直接下載測試的原始範例檔案 (`sample_files/`)：

| # | 實戰範例名稱 | 職場應用場景 | Cowork 核心能力 | 學員練習檔 (`sample_files/`) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | [**每日產業情報與競品自動彙整**](./Examples/01_Daily_News_Brief/README.md) | 創投、行銷與企劃團隊每日監測產業新聞與趨勢。 | • Web 檢索<br/>• Scheduled 雲端定時排程 | • `industry_keywords.txt`<br/>• `daily_news_template.md` |
| **2** | [**跨來源財務與營運數據對比**](./Examples/02_Financial_Report/README.md) | 財務與風控團隊自動交叉比對多份 CSV 財務與預算。 | • 背景 Code Execution 運算<br/>• 多檔案自動比對與畫圖 | • `q3_financial_raw.csv`<br/>• `crm_sales_target.csv` |
| **3** | [**客戶客訴與意見自動分類處置**](./Examples/03_Customer_Feedback/README.md) | 客服、PM 與營運團隊處理批量客訴，分類評級並草擬回信。 | • 多檔案批量處理<br/>• 自動比對 SOP 風險等級 | • `customer_support_logs.csv`<br/>• `sop_escalation_rules.md` |

---

## 🛠️ 五、快速上手步驟

1. **開啟 Cowork 工作空間**：登入 [claude.ai](https://claude.ai)，從左側功能選單切換至 **Cowork**。
2. **選擇或建立專案**：可直接建立新任務，或結合已有的 **Projects** 知識庫。
3. **明確交付目標 (Task Prompt)**：使用 RTCCF 框架撰寫 Prompt（設定角色、目標、限制與格式）。
4. **掛載工具與技能**：根據需求開啟 Connectors 或掛載對應的自訂 Skill。
5. **啟動執行或設定排程**：
   - 點選執行：Claude 開始自主運算並顯示進度。
   - 點選排程（Schedule）：設定自動觸發的時間與頻率。

---

## 💡 六、教學與使用建議

> [!TIP]
> 1. **非程式背景最佳實用工具**：Cowork 讓不需要程式基礎的學員，也能透過自然語言＋內建工具打造媲美自動化腳本的工作流。
> 2. **與 Scheduled 配合使用**：欲了解如何將 Cowork 任務設定為定時排程，請參考 [Scheduled 排程任務教學](../Scheduled/README.md)。

---

← [返回 Claude_AI 主講義](../README.md) | 🏠 [返回專案總首頁](../../README.md)
