# Claude Skills：從模仿到大師（14 小時完整教案）

> 🟢 **方案需求**：Free（完全可用，含自訂 SKILL.md）。依官方說明，Free / Pro / Max / Team / Enterprise 皆可建立與使用 Skills，惟需先在 Settings 中啟用 **Skills** 與 **程式碼執行** 兩項功能。  
> 參考：[Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

這是一門專為**非程式設計師**設計的職場自動化課程。我們不學寫程式，我們學習如何「訓練」AI 成為您的數位分身。

---

## 🚀 Skills 四階進化路徑與實戰範例

### 🟢 第一階：模仿者 (Imitator) —— 「先複製，再體驗」
- **實戰範例**：👉 [**全能郵件修飾專家**](./Examples/Level1_Email_Polisher.md)
- **核心**：學會如何建立第一個 `SKILL.md` 並使用它。
- **延伸工作流**：[01 郵件語氣修飾員](./Examples/Office_Workflow_01_Email_Tone.md)、[02 主管交辦事項整理員](./Examples/Office_Workflow_02_Task_Extractor.md)

### 🔵 第二階：創作者 (Creator) —— 「寫出您的工作魂」
- **實戰範例**：👉 [**個人化每日報工助手**](./Examples/Level2_Daily_Report.md)
- **核心**：學會根據個人習慣設計輸出格式與結構。
- **延伸工作流**：[03 每日工作日誌產生器](./Examples/Office_Workflow_03_Daily_Report.md)、[04 會議紀錄轉行動計畫助手](./Examples/Office_Workflow_04_Meeting_Action_Plan.md)

### 🟡 第三階：整合者 (Integrator) —— 「給 AI 一本書」
- **實戰範例**：👉 [**品牌語氣稽核員**](./Examples/Level3_Brand_Voice.md)
- **核心**：學會將 Skill 與外部知識資源（Resources）進行掛載。
- **延伸工作流**：[05 請假與代理安排助手](./Examples/Office_Workflow_05_Leave_Handover.md)、[06 採購申請預檢員](./Examples/Office_Workflow_06_Purchase_Checker.md)

### 🔴 第四階：自動化專家 (Automator) —— 「讓 AI 動起來」
- **實戰範例**：👉 [**智能會議排程秘書**](./Examples/Level4_Meeting_Secretary.md)
- **核心**：學會透過工具調用（Tools）實現真正的自動化行動。
- **延伸工作流**：[07 客戶回覆與 CRM 更新助手](./Examples/Office_Workflow_07_Customer_CRM.md)、[08 週會資料彙整與簡報大綱助手](./Examples/Office_Workflow_08_Weekly_Brief.md)、[09 跨部門簽核追蹤秘書](./Examples/Office_Workflow_09_Approval_Tracker.md)、[10 辦公室營運儀表板代理人](./Examples/Office_Workflow_10_Operations_Dashboard.md)

---

## 🧩 10 個辦公室工作流範例規劃：由簡單到複雜

> **設計原則**：每個範例都以「辦公室真實任務」為場景，從單純文字改寫開始，逐步加入表格、檔案、規則、資料查詢、跨工具協作，最後進入「自己定義 function tools」的自動化工作流。
> 下表與上方四階範例互相對應：範例 1–2 對應「模仿者」，範例 3–4 對應「創作者」，範例 5–6 對應「整合者」，範例 7–10 對應「自動化專家」。

| # | 難度 | Skill 名稱 | 辦公室場景 | 可形成的工作流 | 自訂 Function Tools 概念 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 入門 | [郵件語氣修飾員](./Examples/Office_Workflow_01_Email_Tone.md) | 同事寫好草稿，但語氣太直接或不夠專業 | 貼上草稿 → 判斷對象 → 產出正式版、友善版、簡短版 | `classify_recipient()`、`rewrite_email()` |
| 2 | 入門 | [主管交辦事項整理員](./Examples/Office_Workflow_02_Task_Extractor.md) | 會議後收到一堆零散訊息，需要整理成待辦清單 | 貼上對話 → 抽取任務 → 標記負責人、期限、優先級 | `extract_tasks()`、`prioritize_tasks()` |
| 3 | 初階 | [每日工作日誌產生器](./Examples/Office_Workflow_03_Daily_Report.md) | 下班前要回報今天完成事項與明日計畫 | 輸入零散工作紀錄 → 分類 → 產出日報、週報草稿 | `format_report()` |
| 4 | 初階 | [會議紀錄轉行動計畫助手](./Examples/Office_Workflow_04_Meeting_Action_Plan.md) | 會議逐字稿太長，主管只想看結論與下一步 | 貼上逐字稿 → 摘要決議 → 產出 Action Items → 寄送前檢查 | `extract_actions()`、`detect_decisions()` |
| 5 | 中階 | [請假與代理安排助手](./Examples/Office_Workflow_05_Leave_Handover.md) | 員工請假時，需要整理交接事項與通知信 | 輸入請假日期與工作項目 → 產出交接清單、代理通知、主管摘要 | `check_leave_overlap()`、`create_handover_plan()` |
| 6 | 中階 | [採購申請預檢員](./Examples/Office_Workflow_06_Purchase_Checker.md) | 行政或 IT 採購前，需要確認品項、預算、理由是否完整 | 貼上採購需求 → 檢查缺漏 → 產出補件問題與申請書草稿 | `validate_purchase_request()` |
| 7 | 中高階 | [客戶回覆與 CRM 更新助手](./Examples/Office_Workflow_07_Customer_CRM.md) | 業務收到客戶信件後，要回覆並更新客戶狀態 | 貼上客戶信 → 判斷意圖 → 產出回信 → 產生 CRM 更新摘要 | `classify_customer_intent()`、`generate_crm_note()` |
| 8 | 高階 | [週會資料彙整與簡報大綱助手](./Examples/Office_Workflow_08_Weekly_Brief.md) | 部門週會前，需要從多份進度回報整理重點 | 匯入多份回報 → 合併重複項 → 找風險 → 產出簡報大綱 | `merge_status_updates()`、`risk_score()` |
| 9 | 高階 | [跨部門簽核追蹤秘書](./Examples/Office_Workflow_09_Approval_Tracker.md) | 文件需要法務、財務、主管多方簽核，容易卡關 | 輸入簽核流程 → 查目前狀態 → 找卡點 → 產出催辦訊息 | `get_approval_status()`、`draft_followup_message()` |
| 10 | 進階整合 | [辦公室營運儀表板代理人](./Examples/Office_Workflow_10_Operations_Dashboard.md) | 主管每天想知道會議、待辦、客訴、採購、簽核的整體狀態 | 讀取多來源資料 → 分析異常 → 產出每日營運摘要 → 建議下一步 | `fetch_calendar()`、`fetch_tasks()`、`fetch_tickets()`、`summarize_operations()` |

---

## 🛠️ Function Tools 設計範例

> **教學提醒**：前 1–2 個範例以 `SKILL.md` 操作為主，function tools 先作為概念草案。第 3 個範例開始讓學生設計固定輸出工具，第 5 個範例後再逐步加入檢查、查詢與整合型 function tools。重點不是馬上寫程式，而是學會把工作拆成可被工具執行的步驟。

### 範例 A：每日工作日誌 `format_report()`

```json
{
  "name": "format_report",
  "description": "將零散工作紀錄整理成公司指定的日報格式",
  "parameters": {
    "date": "2026-06-08",
    "completed": ["完成客戶報價單", "更新專案時程"],
    "blocked": ["等待財務確認預算"],
    "tomorrow_plan": ["追蹤合約回簽", "整理週會資料"]
  }
}
```

### 範例 B：採購申請預檢 `validate_purchase_request()`

```json
{
  "name": "validate_purchase_request",
  "description": "檢查採購申請是否包含品項、數量、金額、用途、預算來源與核准人",
  "parameters": {
    "item": "27 吋螢幕",
    "quantity": 3,
    "amount": 18000,
    "purpose": "新進同仁設備",
    "budget_code": "IT-2026-Q2",
    "approver": "行政主管"
  }
}
```

### 範例 C：簽核追蹤 `get_approval_status()`

```json
{
  "name": "get_approval_status",
  "description": "查詢文件目前卡在哪一位簽核人，並回傳等待天數與建議催辦方式",
  "parameters": {
    "document_id": "PO-2026-0612",
    "workflow": ["申請人", "部門主管", "財務", "法務", "總經理"]
  }
}
```

---

## 🗺️ 建議教學順序

1. **第 1 堂：範例 1–2**  
   建立第一個 Skill，學會描述角色、任務、限制與輸出格式。
2. **第 2 堂：範例 3–4**  
   練習把零散資訊整理成固定格式，開始理解「工作流」的概念。
3. **第 3 堂：範例 5–6**  
   加入欄位檢查、條件判斷與缺漏追問，讓 Skill 更像辦公室助理。
4. **第 4 堂：範例 7–8**  
   處理多來源資料、分類、風險判斷與摘要輸出。
5. **第 5 堂：範例 9–10**  
   設計 function tools，將 Skill 從「會寫」升級為「會查、會判斷、會追蹤」。

---

## 💡 Skills 與 Projects 的協作藝術 🔵 Pro 進階

> **提醒**：本小節示範的是 Skills + **Projects** 雙劍合璧的進階用法。  
> **Projects 需 Pro 方案**，Free 帳號可改在一般 Chats 內反覆呼叫 Skill 達到類似效果（僅缺乏專屬知識庫與長期記憶）。

在教學中，強烈建議將 Skills 放在 **Projects** 的框架下使用，這能實現最強大的「自動化沙盒」：

1.  **專案即測試場 (Project as Sandbox)**：
    - 建立一個名為「Skill 開發實驗室」的 Project。在裡面反覆測試 `SKILL.md` 的邏輯，不會干擾到其他的日常對話。
2.  **資源互補 (Resource Sharing)**：
    - 將大型參考文件（如 200 頁的手冊）上傳到 **Project Knowledge**。
    - 在 **Skill** 中下令：「請參考本專案知識庫中的手冊第 5 章，來執行審查任務」。
3.  **能力封裝**：
    - 您可以為每個 Project 設定專屬的 **Connectors**，而 Skill 則負責「調度」這些連線獲取的資料。

---


← [返回 Claude_AI 索引](../README.md)
