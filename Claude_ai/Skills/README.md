# Claude Skills

> **💡 三種擴充功能快速對照**
>
> | 類型 | 解決什麼 | 比喻 |
> |------|---------|------|
> | **Skills（技能）** | 教 Claude 怎麼把某類任務做好（不連外部服務） | 食譜／SOP |
> | **Connectors（連接器）** | 讓 Claude 能存取資料或操作其他系統 | 對外的插座、橋樑 |
> | **Plugins（外掛）** | 把多種能力打包成一個可安裝單位 | 整套工具箱 |
>
> **Skills** 是給 Claude 一套處理特定任務的「工作流程說明書」——一個資料夾內放 `SKILL.md`（操作指引）加上範本、腳本等檔案。當任務符合時，Claude 會自動讀取並照著做。例如產生 Word 文件、做簡報、填報價單。本身**不連外部服務**。  
> 若需要讀取外部資料請看 [Connectors](../Connectors/README.md)；若要打包整套設定請看 [Plugins](../Plugins/README.md)。

> 🟢 **方案需求**：Free（完全可用，含自訂 SKILL.md）。依官方說明，Free / Pro / Max / Team / Enterprise 皆可建立與使用 Skills。
>
> > [!IMPORTANT]
> > **使用 Skills 的關鍵前提：啟用「程式碼執行 (Code execution)」功能**
> > 
> > 在 Claude 中使用或開發 Skills 時，**必須**啟用「**Cloud code execution and file creation**」（雲端程式碼執行與檔案建立）功能。若未開啟，Skills 將無法正常運作。
> > 
> > ⚙️ **設定路徑**：
> > 1. 點擊左下角個人頭像前往 `Settings`（設定）
> > 2. 選擇左側選單的 `Capabilities`（能力）
> > 3. 將 `Cloud code execution and file creation` 功能切換為**開啟** (On) 狀態
> > 
> > 💡 *提示：這是因為 Skills 在執行任務時，需要依賴 Claude 在伺服器端執行程式碼以及建立/編輯文件、試算表、簡報等檔案的能力。*
> >
> > <details>
> > <summary>⚙️ <b>Settings 設定細節與「找不到 Skills 清單」的常見解惑</b>（點此展開）</summary>
> > <br>
> > 
> > * **Skills 區段在頁面更下方**：  
> >   在 `Capabilities` 設定頁面中，請繼續**往下方捲動**。經過「Allow network egress」與「Domain allowlist」後，才會看到「**Skills**」區段，那裡才會列出您已安裝的 Skills。
> > 
> > * **內建文件 Skills 自動生效**：  
> >   `pptx`、`docx`、`xlsx`、`pdf` 這幾個官方文件 Skills **不會**出現在下方的 Skills 清單中。它們是**直接內建**於 `Cloud code execution and file creation` 功能裡的。只要此開關開啟，這幾項文件處理功能（包含簡報、試算表、Word、PDF 等）就已自動生效，無需也無法手動安裝。
> > 
> > * **下方的 Skills 清單會列出**：  
> >   1. **自訂上傳的 Skills**：例如您上傳的「華梵課程計畫表」、「報價單 (`quotation`)」、「產投課表 (`workforce-training-skill`)」等。
> >   2. **Anthropic 官方提供的範例 Skills**（若有開放瀏覽與安裝）。
> > </details>
> 
> > 📖 **官方參考文案**：
> > - [如何使用 Skills (Use Skills in Claude)](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
> > - [如何建立自訂的 Skills (How to create custom Skills)](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
> > - [官方 Skill 範例庫 (Official Skills Repo)](https://github.com/anthropics/skills) 預設打開`Cloud code execution and file creation`,這些就會自動在雲端掛載

這是一門專為**非程式設計師**設計的職場自動化課程。我們不學寫程式，我們學習如何「訓練」AI 成為您的數位分身。

---

## 🔰 實作練習：Google Workspace Skills

> 這是專注在 **Google Docs、Google Sheets、Google Slides、Gmail** 四個常用辦公室工具的練習。
> 透過實作「使用現有 Skill」主題，幫助您快速上手職場自動化流程。
>
> 👉 [**點此前往 Google Workspace Skills 實作練習（練習 1：使用現有的 Skill）**](./GWorkspace/README.md)

---

## 🚀 自訂 Skills 四階演進路徑與建立方式

您可以透過修改或全新建立自訂 Skills 來打造個人的數位分身。以下是**由淺入深**的四個演進階段，每個階段皆提供**「方式 A（使用內建技能建立）」**與**「方式 B（手動建立）」**兩種實作路徑。

### 🟢 第一階：模仿者 (Imitator) —— 單獨建立 `SKILL.md`
* **核心概念**：學會如何撰寫基礎的 `SKILL.md`（定義 `Role`, `Task`, `Constraint`, `Format` 等指引）。
* **適用場景**：純文字的格式處理、語氣修飾、日常事務摘要等。
* **實戰範例**：👉 [**全能郵件修飾專家**](./Examples/Level1_Email_Polisher/README.md)
* **自訂方式**：
  * **💡 方式 A (使用內建 `/create-skill` 技能)**：
    在 Claude 對話中輸入：
    > 「`請幫我建立一個名為『郵件修飾專家』的 Skill。角色是專業文案，任務是修飾日常郵件語氣，限制是使用繁體中文、格式為 Markdown，請使用 /create-skill 幫我自動產出。`」
    Claude 會呼叫內建工具，在本地自動為您生成 `SKILL.md` 並建立資料夾。
  * **✍️ 方式 B (手動建立檔案)**：
    1. 在電腦中建立一個新資料夾，命名為 `email-polisher`。
    2. 在資料夾中新增一個 `SKILL.md` 檔案。
    3. 在 `SKILL.md` 開頭寫入 YAML 元數據，並編寫指引內容：
       ```markdown
       ---
       name: email-polisher
       description: "修飾電子郵件語氣，使其更加專業且符合商務禮儀。"
       ---
       # 郵件修飾專家
       ## Role ...
       ```
    4. 進入 Claude 設定中的 `Settings` ➔ `Skills` 上傳此資料夾，或將其複製到桌面版本地 Skills 目錄中。
* **延伸工作流**：[01 郵件語氣修飾員](./Examples/Office_Workflow_01_Email_Tone.md)、[02 主管交辦事項整理員](./Examples/Office_Workflow_02_Task_Extractor.md)

### 🔵 第二階：創作者 (Creator) —— `SKILL.md` + `references` & `templates`
* **核心概念**：學習掛載外部參考知識（放置於 `references/`）與套用標準文件範本（放置於 `templates/`），使 Claude 產出特定格式的文件。
* **適用場景**：符合公司特定規範的報價單、遵循特定格式的會議紀錄、參考產品手冊進行預檢等。
* **實戰範例**：👉 [**個人化每日報工助手**](./Examples/Level2_Daily_Report/README.md)
* **自訂方式**：
  * **💡 方式 A (使用內建 `/create-skill` 技能)**：
    先將參考文件 (PDF/Doc) 與範本檔上傳給 Claude，然後下指令：
    > 「`我想建立一個品牌稽核 Skill，請參考我剛才上傳的『品牌手冊.pdf』，並根據『報告樣板.md』的格式，使用 /create-skill 幫我建立包含 references 和 templates 資料夾的 Skill。`」
  * **✍️ 方式 B (手動建立檔案)**：
    1. 在 Skill 資料夾下建立 `references/` 與 `templates/` 兩個子資料夾。
    2. 將參考資料（如 `brand-handbook.pdf`）放入 `references/`；將標準格式範本（如 `daily-report-template.md`）放入 `templates/`。
    3. 在 `SKILL.md` 的 `## Constraint` 中指示 Claude 必須參考與套用該目錄檔案：
       ```markdown
       ## Constraint
       - 請嚴格參考 `references/brand-handbook.pdf` 中的品牌語氣規範。
       - 輸出格式必須完全符合 `templates/daily-report-template.md` 的結構。
       ```
* **延伸工作流**：[03 每日工作日誌產生器](./Examples/Office_Workflow_03_Daily_Report.md)、[04 會議紀錄轉行動計畫助手](./Examples/Office_Workflow_04_Meeting_Action_Plan.md)

### 🟡 第三階：整合者 (Integrator) —— `SKILL.md` + `assets` (Logo 與圖片)
* **核心概念**：在 Skill 中加入 `assets/` 資料夾放置圖片（如公司 Logo、圖表、ICON），並在產出文件時以相對路徑引用，讓 Claude 的輸出直接包含品牌標誌。
* **適用場景**：製作帶有公司商標的合約、簡報封面頁、附有 Logo 的正式報價單等。
* **實戰範例**：👉 [**品牌語氣稽核員**](./Examples/Level3_Brand_Voice/README.md)
* **自訂方式**：
  * **💡 方式 A (使用內建 `/create-skill` 技能)**：
    將您的 Logo 圖片上傳至對話中，並指示：
    > 「`我想建立一個帶有 Logo 的文件產生 Skill。請把這張圖片放入 assets 資料夾，並在 /create-skill 生成的 SKILL.md 中規定：產出的文件開頭必須用相對路徑插入這張 Logo。`」
  * **✍️ 方式 B (手動建立檔案)**：
    1. 在 Skill 資料夾下建立一個名為 `assets/` 的子資料夾。
    2. 將您的 Logo 圖片檔案（例如 `company-logo.png`）放入 `assets/`。
    3. 在 `SKILL.md` 中，使用 Markdown 語法以相對路徑引入該圖片：
       ```markdown
       ## Format
       - 文件第一行必須置中加入公司 Logo：`![公司 Logo](assets/company-logo.png)`
       ```
* **延伸工作流**：[05 請假與代理安排助手](./Examples/Office_Workflow_05_Leave_Handover.md)、[06 採購申請預檢員](./Examples/Office_Workflow_06_Purchase_Checker.md)

### 🔴 第四階：自動化專家 (Automator) —— `SKILL.md` + `scripts` (Python/工具調用)
* **核心概念**：加入 `scripts/` 資料夾放置 Python 腳本或工具宣告定義。結合 Claude 的「程式碼執行 (Code Execution)」，讓 AI 在伺服器端運行腳本，實現資料運算、複雜圖表繪製或自動化處理。
* **適用場景**：自動生成圖表簡報、進行財務數據加總小計、動態更新日程等。
* **實戰範例**：👉 [**智能會議排程秘書**](./Examples/Level4_Meeting_Secretary/README.md)
* **自訂方式**：
  * **💡 方式 A (使用內建 `/create-skill` 技能)**：
    在對話中告知您的自動化邏輯，Claude 會幫您撰寫 Python 腳本並以工具打包：
    > 「`我想建立一個自動排程 Skill，請幫我寫一個計算時間衝突的 Python 腳本放進 scripts 資料夾，並使用 /create-skill 建立此自動化技能。`」
  * **✍️ 方式 B (手動建立檔案)**：
    1. 在 Skill 資料夾下建立 `scripts/` 子資料夾。
    2. 將您寫好的 Python 腳本（例如 `calculate_hours.py`）放入 `scripts/`。
    3. 在 `SKILL.md` 中，指示 Claude 執行該腳本：
       ```markdown
       ## Task
       - 當接收到工時數據後，請使用程式碼執行功能運行 `scripts/calculate_hours.py` 腳本，以計算總工時並產出統計圖表。
       ```
* **延伸工作流**：[07 客戶回覆與 CRM 更新助手](./Examples/Office_Workflow_07_Customer_CRM.md)、[08 週會資料彙整與簡報大綱助手](./Examples/Office_Workflow_08_Weekly_Brief.md)、[09 跨部門簽核追蹤秘書](./Examples/Office_Workflow_09_Approval_Tracker.md)、[10 辦公室營運儀表板代理人](./Examples/Office_Workflow_10_Operations_Dashboard.md)

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

1. **第 1 堂：第一階模仿者 (Imitator) — 範例 1–2**  
   學會建立第一個只含 `SKILL.md` 的基礎 Skill，理解角色、任務與限制。
2. **第 2 堂：第二階創作者 (Creator) — 範例 3–4**  
   學會使用 `templates/` 目錄建立固定輸出樣板與格式，建立基本專案日報。
3. **第 3 堂：第三階整合者 (Integrator) — 範例 5–6**  
   學會使用 `references/` 資料夾掛載外部參考手冊，並在 `assets/` 中配置與引用公司 Logo。
4. **第 4 堂：第三階整合者 (Integrator) — 範例 7–8**  
   進一步學習掛載多個外部參考知識庫資源，處理複雜的欄位審查、風險判定與意圖分類。
5. **第 5 堂：第四階自動化專家 (Automator) — 範例 9–10**  
   學會配置 `scripts/` Python 腳本並搭配工具（Function Tools），實現伺服器端代碼運行與資料加總小計。

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
