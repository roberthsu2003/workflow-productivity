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
> > - [如何建立自訂的 Skills (How to create custom Skills)](https://support.claude.com/zh-TW/articles/12512198-%E5%A6%82%E4%BD%95%E5%BB%BA%E7%AB%8B%E8%87%AA%E8%A8%82%E6%8A%80%E8%83%BD)
> > - [官方 Skill 範例庫 (Official Skills Repo)](https://github.com/anthropics/skills) 預設打開`Cloud code execution and file creation`,這些就會自動在雲端掛載

這是一門專為**非程式設計師**設計的職場自動化課程。我們不學寫程式，我們學習如何「訓練」AI 成為您的數位分身。

---

## 🔰 內建 Skills 使用與 Google Workspace 實作練習

> 這是專注在 **Google Docs、Google Sheets、Google Slides、Gmail** 四個常用辦公室工具的練習。
> 透過實作「使用內建的現有 Skill」主題，幫助您快速上手職場自動化流程。
>
> 👉 [**點此前往 Google Workspace Skills 實作練習（使用內建的現有 Skill）**](./GWorkspace/README.md)

---

## 🚀 自訂 Skills 四階演進路徑與建立方式

您可以透過修改或全新建立自訂 Skills 來打造個人的數位分身。以下是**由淺入深**的四個演進階段，每個階段皆提供**「方式 A（使用內建技能建立）」**與**「方式 B（手動建立）」**兩種實作路徑。

### 🟢 第一階：模仿者 (Imitator) —— 單獨建立 `SKILL.md`
* **核心概念**：學會如何撰寫基礎的 `SKILL.md`（定義 `Role`, `Task`, `Constraint`, `Format` 等指引）。
* **適用場景**：純文字的格式處理、語氣修飾、日常事務摘要等。
* **實戰範例**：👉 [**全能郵件修飾專家**](./Examples/Level1_Email_Polisher/README.md)
* **延伸實戰練習**：請參閱底部的 [辦公室實戰工作流地圖](#workflow-map)（範例 1 ~ 2）。

### 🔵 第二階：創作者 (Creator) —— `SKILL.md` + `references` & `templates`
* **核心概念**：學習掛載外部參考知識（放置於 `references/`）與套用標準文件範本（放置於 `templates/`），使 Claude 產出特定格式的文件。
* **適用場景**：符合公司特定規範的報價單、遵循特定格式的會議紀錄、參考產品手冊進行預檢等。
* **實戰範例**：👉 [**個人化每日報工助手**](./Examples/Level2_Daily_Report/README.md)
* **延伸實戰練習**：請參閱底部的 [辦公室實戰工作流地圖](#workflow-map)（範例 3 ~ 4）。

### 🟡 第三階：整合者 (Integrator) —— `SKILL.md` + `assets` (Logo 與圖片)
* **核心概念**：在 Skill 中加入 `assets/` 資料夾放置圖片（如公司 Logo、圖表、ICON），並在產出文件時以相對路徑引用，讓 Claude 的輸出直接包含品牌標誌。
* **適用場景**：製作帶有公司商標的合約、簡報封面頁、附有 Logo 的正式報價單等。
* **實戰範例**：👉 [**品牌語氣稽核員**](./Examples/Level3_Brand_Voice/README.md)
* **延伸實戰練習**：請參閱底部的 [辦公室實戰工作流地圖](#workflow-map)（範例 5 ~ 7）。

### 🔴 第四階：自動化專家 (Automator) —— `SKILL.md` + `scripts` (Python/工具調用)
* **核心概念**：加入 `scripts/` 資料夾放置 Python 腳本或工具宣告定義。結合 Claude 的「程式碼執行 (Code Execution)」，讓 AI 在伺服器端運行腳本，實現資料運算、複雜圖表繪製或自動化處理。
* **適用場景**：自動生成圖表簡報、進行財務數據加總小計、動態更新日程等。
* **實戰範例**：👉 [**智能會議排程秘書**](./Examples/Level4_Meeting_Secretary/README.md)
* **延伸實戰練習**：請參閱底部的 [辦公室實戰工作流地圖](#workflow-map)（範例 8 ~ 10）。

---



<div id="workflow-map"></div>

## 🧩 10 個辦公室工作流範例規劃：由簡單到複雜

> **設計原則**：每個範例都以「辦公室真實任務」為場景，從單純文字改寫開始，逐步加入表格、檔案、規則、資料查詢、與跨工具協作。
> 下表與上方自訂 Skills 四階演進路徑互相對應：範例 1–2 對應「第一階：模仿者」，範例 3–4 對應「第二階：創作者」，範例 5–7 對應「第三階：整合者」，範例 8–10 對應「第四階：自動化專家」。

| # | 對應演進階段 | Skill 名稱 | 辦公室場景 | 可形成的工作流 |
| :---: | :--- | :--- | :--- | :--- |
| 1 | 🟢 第一階：模仿者 | [社群貼文文案大師](./Examples/Office_Workflow_01_Copywriter.md) | 有簡單的活動想法，需要快速撰寫成社群推廣文案 | 輸入核心概念 → 選擇平台 → 產出吸睛文案、Hashtags 與 Call-to-Action |
| 2 | 🟢 第一階：模仿者 | [主管交辦事項整理員](./Examples/Office_Workflow_02_Task_Extractor.md) | 會議後收到一堆零散訊息，需要整理成待辦清單 | 貼上對話 → 抽取任務 → 標記負責人、期限、優先級 |
| 3 | 🔵 第二階：創作者 | [每日工作日誌產生器](./Examples/Office_Workflow_03_Daily_Report/README.md) | 下班前要回報今天完成事項與明日計畫 | 輸入零散工作紀錄 → 分類 → 產出日報、週報草稿 |
| 4 | 🔵 第二階：創作者 | [會議紀錄轉行動計畫助手](./Examples/Office_Workflow_04_Meeting_Action_Plan/README.md) | 會議逐字稿太長，主管只想看結論與下一步 | 貼上逐字稿 → 摘要決議 → 產出 Action Items → 寄送前檢查 |
| 5 | 🟡 第三階：整合者 | [請假與代理安排助手](./Examples/Office_Workflow_05_Leave_Handover.md) | 員工請假時，需要整理交接事項與通知信 | 輸入請假日期與工作項目 → 產出交接清單、代理通知、主管摘要 |
| 6 | 🟡 第三階：整合者 | [採購申請預檢員](./Examples/Office_Workflow_06_Purchase_Checker.md) | 行政或 IT 採購前，需要確認品項、預算、理由是否完整 | 貼上採購需求 → 檢查缺漏 → 產出補件問題與申請書草稿 |
| 7 | 🟡 第三階：整合者 | [客戶回覆與 CRM 更新助手](./Examples/Office_Workflow_07_Customer_CRM.md) | 業務收到客戶信件後，要回覆並更新客戶狀態 | 貼上客戶信 → 判斷意圖 → 產出回信 → 產生 CRM 更新摘要 |
| 8 | 🔴 第四階：自動化專家 | [週會資料彙整與簡報大綱助手](./Examples/Office_Workflow_08_Weekly_Brief.md) | 部門週會前，需要從多份進度回報整理重點 | 匯入多份回報 → 合併重複項 → 找風險 → 產出簡報大綱 |
| 9 | 🔴 第四階：自動化專家 | [跨部門簽核追蹤秘書](./Examples/Office_Workflow_09_Approval_Tracker.md) | 文件需要法務、財務、主管多方簽核，容易卡關 | 輸入簽核流程 → 查目前狀態 → 找卡點 → 產出催辦訊息 |
| 10 | 🔴 第四階：自動化專家 | [辦公室營運儀表板代理人](./Examples/Office_Workflow_10_Operations_Dashboard.md) | 主管每天想知道會議、待辦、客訴、採購、簽核的整體狀態 | 讀取多來源資料 → 分析異常 → 產出每日營運摘要 → 建議下一步 |

---


← [返回 Claude_AI 索引](../README.md)
