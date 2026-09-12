# Claude Cowork：全新 AI 協作與自主代理工作空間

> 🔵 **方案需求**：**Pro / Max / Team / Enterprise 付費方案**（全平台支援：Desktop / Web / Mobile / Chrome 側邊欄）。  
> 官方參考：
> - [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
> - [Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
> - [Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
> - [Claude Cowork architecture overview](https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview)

**Claude Cowork** 是 Anthropic 將 **Claude Code** 強大的自主代理（Agentic）架構引入「非程式碼知識工作」的全新模式。它打破了傳統「一問一答」的對話限制，**完全無需終端機（Terminal）**，能為職場工作者自主拆解目標、調用工具、存取檔案與排程運行，獨立完成複雜的多步驟長任務。

---

## 💡 一、什麼是 Claude Cowork？

傳統對話模式（Chat）適合快速發問與單次解答；而 **Claude Cowork** 則專為**多步驟長任務、檔案處理與自動化工作流**而設計。

- **與 Chat 共用同一首頁 (Chat and Cowork share one home)**：不必進入完全不同的系統，在對話框左下角就能隨時切換「Chat」與「Cowork」。
- **支援本機資源連動 (Local File & Desktop Integration)**：配合 Claude Desktop App，Claude 可直接讀寫電腦本地資料夾的檔案、操作內建瀏覽器，甚至進行電腦螢幕操作（Computer Use）。（實戰參閱：[範例 1](./Examples/01_Local_Folder_Organize/)）
- **雲端隔離運算 (Sessions in the Cloud)**：任務預設在 Anthropic 雲端伺服器的安全隔離沙盒中執行。即使闔上筆電或關閉瀏覽器，雲端任務依然會持續運行。（實戰參閱：[範例 3](./Examples/03_Financial_Report/)、[範例 4](./Examples/04_Daily_News_Brief/)）
- **跨裝置無縫接續 (Work from Anywhere)**：在辦公室電腦啟動任務，出門時在手機 App 檢視進度與給予回饋，回到家再在另一台裝置下載成品。（實戰參閱：[範例 5](./Examples/05_Folder_Instructions_Project/)）

---

## 📊 二、Cowork vs 一般對話（Chat）比較

| 比較項目 | 一般對話（Chat） 💬 | Claude Cowork 🤝 |
| :--- | :--- | :--- |
| **核心定位** | 單次一問一答、靈感發想、即時諮詢 | 自主代理（Agentic），自主拆解並執行多步驟任務 |
| **操作入口** | 輸入框預設為「Chat」 | 輸入框左下角切換為「Cowork」（Chrome 側邊欄打開即為 Cowork） |
| **執行環境** | 前台對話視窗，依賴即時連線 | 雲端隔離沙盒（Sessions in the cloud），支援背景持續運行 |
| **本地檔案存取** | 需手動上傳檔案（單次對話暫存） | 配合 Desktop App 可直接讀寫本機整份資料夾，免手動上傳下載 |
| **安全核准機制** | 無需核准（單次產出） | 支援 3 種核准模式：**Manual（手動核准）/ Auto（自動審查）/ Skip（跳過核准）** |
| **瀏覽器互動** | 純文字搜尋（Web Search） | 支援內建瀏覽器（Built-in browser），可開啟網頁、點擊、輸入表單 |
| **自動化排程** | 不支援定時執行 | 支援 `/schedule` 雲端自動定時重複執行（定時週報、每日簡報） |
| **成果精細度** | 純文字、Markdown、程式碼 | 專業交付級產出（含 VLOOKUP 公式之 Excel、PowerPoint 簡報、豐富 Artifacts） |
| **額度消耗 (Usage)** | 較低，適合日常問答 | 較高（運算與 Token 密集型），複雜任務建議使用 |

---

## 🚀 三、Claude Cowork 核心能力與架構

### 1. 📁 本機資料夾讀寫 (Direct Local File Access)
- 透過 **Claude Desktop App (macOS / Windows)**，您可以指定工作資料夾。
- Claude 能直接在您的硬碟中讀取、分類、重命名檔案，並直接寫入產出成果（如：整理 Downloads 資料夾、批量將發票產出報銷總表）。
👉 **實戰操作體驗**：請參閱 [範例 1：本機資料夾批次自動整理與報銷總表](./Examples/01_Local_Folder_Organize/)（內附 [`sample_files/`](./Examples/01_Local_Folder_Organize/sample_files/) 偽發票與雜亂檔案）。

### 2. 🛡️ 三大安全核准模式 (Approval Modes)
在任務執行前或過程中，您可隨時調整安全核准模式：
1. **Manually approve (Manual)**（手動核准，前身為 Ask before acting）：Claude 執行每一步動作（存取本機、連網、調用工具）前皆會暫停，由您確認按 Allow（允許）或 Deny（拒絕）。
2. **Automatically approve (Auto)**（自動安全審查）：Claude 連續自主執行，但會在背後即時審查動作安全性（防範 Prompt Injection 提示詞注入與 Data Exfiltration 資料外洩）。若發現風險會自動攔阻或暫停請示您。（*注意：此安全審查會消耗較多 usage 配額*）。
3. **Skip all approvals (Skip)**（跳過所有核准，前身為 Act without asking）：完全不暫停也不進行額外審查，全速推進（僅適用於 100% 信任的內部安全環境）。
👉 **實戰操作體驗**：請參閱 [範例 1：本機資料夾整理與三大核准模式演練](./Examples/01_Local_Folder_Organize/)。

### 3. 📝 原地反白微調草稿 (Edit Drafts in Place)
- 當 Claude 產出長篇 Markdown 報告或草稿時，學員可以直接在畫面上**反白選取欲修改的段落**，點擊「Edit with Claude」輸入微調指令，Claude 即會原地更新該段文字，無需在對話串中費力描述。
👉 **實戰操作體驗**：請參閱 [範例 2：客訴回信草稿原地微調](./Examples/02_Customer_Feedback/) 與 [範例 5：新聞稿草案原地微調](./Examples/05_Folder_Instructions_Project/)。

### 4. 🤖 背景程式碼運算與跨表對帳 (Code Execution & Analytics)
- 處理多份分散的 CSV/Excel 財務與銷售數據時，Claude 會在背景自動編寫 Python 程式碼，執行跨表合併、達成率精算與 Matplotlib 圖表繪製，根除數字幻覺。
👉 **實戰操作體驗**：請參閱 [範例 3：跨來源財務對帳與自動繪圖](./Examples/03_Financial_Report/)。

### 5. 🌐 內建瀏覽器與雲端排程 (Built-in Browser & Scheduled Tasks)
- 處理需要查閱外部網站的任務時，Claude 能自動開啟網頁、閱讀內容、過濾公關廢話。
- 支援輸入 `/schedule` 設定每日/每週定時重複執行。**純雲端任務無須開機**，即使電腦休眠或關機也會準時在雲端執行並交付成果至手機。
👉 **實戰操作體驗**：請參閱 [範例 4：全自動產業情報監測與定時晨報](./Examples/04_Daily_News_Brief/)。

### 6. 🎯 資料夾專屬指令與自主日誌維護 (Folder Instructions & Project Log)
- **Folder instructions**：在工作資料夾中放置 `folder-instructions.md`，為該專案設定永久品牌語氣與交付規範。
- Claude 還能自主維護與更新該資料夾的進度日誌（`PROJECT_LOG.md`），打勾完成里程碑並推播至跨裝置手機。
👉 **實戰操作體驗**：請參閱 [範例 5：資料夾指令規範與專案日誌自主維護](./Examples/05_Folder_Instructions_Project/)。

---

## 💻 四、跨平台裝置功能支援矩陣 (Surfaces)

| 核心功能 | 桌面端 (Desktop App) 🖥️ | 網頁端 (Web) 🌐 | 行動端 (iOS/Android) 📱 | Chrome 側邊欄 🧩 |
| :--- | :---: | :---: | :---: | :---: |
| **發起、引導與審查任務** | ✅ | ✅ | ✅ | ✅（開啟即為 Cowork） |
| **跨裝置接續同一個 Session** | ✅ | ✅ | ✅ | ✅ |
| **雲端排程任務 (Scheduled)** | ✅ | ✅ | ✅ | ✅ |
| **專案知識庫 (Projects)** | ✅ | ✅ | ✅ | ✅ |
| **預覽與下載產出檔案** | ✅ | ✅ | ✅ | ✅ |
| **本機資料夾直接讀寫** | ✅ | ⚠️ 需 Desktop 開啟連線 | ⚠️ 需 Desktop 開啟連線 | ⚠️ 需 Desktop 開啟連線 |
| **內建瀏覽器操作 (Browser Use)** | ✅ | ⚠️ 需 Desktop 開啟連線 | ⚠️ 需 Desktop 開啟連線 | ⚠️ 需 Desktop 開啟連線 |
| **電腦螢幕操作 (Computer Use Beta)**| ✅ | ⚠️ 需 Desktop 開啟連線 | ⚠️ 需 Desktop 開啟連線 | — |

> [!NOTE]
> 標註「⚠️ 需 Desktop 開啟連線」的功能，代表任務雖然在雲端排程或行動端發起，但若需要碰觸您電腦中的**實體檔案**或**本機應用程式**，該台電腦上的 Claude Desktop App 必須維持開啟且聯網。

---

## 🎓 五、5 大職場自動化實戰範例（由淺入深學習階梯）

為幫助學員從「基礎震撼」一路進階到「自主代理」，本單元設計了 5 個由淺入深的職場實戰範例，全部附有可直接演練的練習偽資料資料夾 (`sample_files/`)：

```mermaid
flowchart LR
    L1["<b>Level 1：本機魔法</b><br>混亂下載區自動歸檔<br>& 單據金額匯出總表"] --> L2["<b>Level 2：職場行政</b><br>批量客訴情緒診斷<br>& 原地反白微調回信"]
    L2 --> L3["<b>Level 3：數據對帳</b><br>跨表財務營收交叉對帳<br>& 自動寫程式繪製圖表"]
    L3 --> L4["<b>Level 4：雲端排程</b><br>全自動產業情報監測<br>& 關機定時雲端晨報"]
    L4 --> L5["<b>Level 5：專案自治</b><br>資料夾長效自主記憶<br>& 跨裝置手機無縫接續"]
```

| 難度等級 | 實戰範例資料夾（點選進入） | 職場痛點劇場與核心亮點 | 對應 Cowork 核心能力 | 下載學員練習檔 / 偽檔案 |
| :---: | :--- | :--- | :--- | :--- |
| **Level 1**<br>入門震撼 | [**範例 1：本機資料夾批次自動整理與報銷總表產出**](./Examples/01_Local_Folder_Organize/) | **「救救混亂下載區！」**<br>下載資料夾堆滿雜亂發票與簡報，一鍵自動建目錄分類歸檔，自動辨識單據金額匯出 Excel 總表。 | • 📁 本機資料夾直接讀寫<br/>• 🛡️ 三大安全核准模式 (Manual/Auto/Skip)<br/>• 💻 本機沙盒批次操作 | 📂 [**前往 `sample_files/` 下載**](./Examples/01_Local_Folder_Organize/sample_files/)<br/>• `raw_downloads/` (發票、收據、合約)<br/>• `expenses_report_template.csv` |
| **Level 2**<br>實戰應用 | [**範例 2：客訴情緒診斷、SOP 自動分流與原地微調回信**](./Examples/02_Customer_Feedback/) | **「客訴火燒屁股！」**<br>大促銷後湧入大量負評，自動依內部 SOP 分流評級（Level 1~3），秒生道歉信，並體驗原地反白微調！ | • 📋 SOP 規章自動遵循比對<br/>• 📝 原地反白微調 (Edit Drafts in Place)<br/>• ⚡ 批量文本情緒分析 | 📂 [**前往 `sample_files/` 下載**](./Examples/02_Customer_Feedback/sample_files/)<br/>• `customer_support_logs.csv`<br/>• `sop_escalation_rules.md` |
| **Level 3**<br>進階分析 | [**範例 3：跨來源財務對帳、自動程式運算與營運圖表產出**](./Examples/03_Financial_Report/) | **「月底對帳抓抓樂！」**<br>多個部門 CSV 數字對不起來，Cowork 在背景寫 Python 程式碼自動計算達成率、抓出超支虧損警訊並自動畫圖。 | • 🤖 背景 Code Execution 運算<br/>• 📊 多檔案交叉對比分析<br/>• 📈 自動資料視覺化繪圖 | 📂 [**前往 `sample_files/` 下載**](./Examples/03_Financial_Report/sample_files/)<br/>• `q3_financial_raw.csv`<br/>• `crm_sales_target.csv` |
| **Level 4**<br>情報排程 | [**範例 4：全自動產業情報監測、內建瀏覽器檢索與雲端定時晨報**](./Examples/04_Daily_News_Brief/) | **「週一早會免受苦！」**<br>主管要看競品動態，用內建瀏覽器聯網抓取最新新聞，設定 `/schedule` 雲端排程，筆電關機睡覺，早上手機準時收信！ | • 🌐 內建瀏覽器與 Web 檢索<br/>• 🕒 雲端排程任務 (`/schedule`)<br/>• ☁️ 雲端隔離運算 (關機照跑) | 📂 [**前往 `sample_files/` 下載**](./Examples/04_Daily_News_Brief/sample_files/)<br/>• `industry_keywords.txt`<br/>• `daily_news_template.md` |
| **Level 5**<br>頂級代理 | [**範例 5：資料夾指令規範、專案日誌自主維護與跨裝置無縫接續**](./Examples/05_Folder_Instructions_Project/) | **「自帶靈魂的專案資料夾！」**<br>新產品發布專案，設定資料夾常駐規則，Claude 每次工作自動更新進度日誌，出門用手機無縫審批。 | • 🎯 資料夾專屬指令 (Folder Instructions)<br/>• 📱 跨裝置無縫接續 (Work from Anywhere)<br/>• 📝 專案進度日誌自主追蹤維護 | 📂 [**前往 `sample_files/` 下載**](./Examples/05_Folder_Instructions_Project/sample_files/)<br/>• `folder-instructions.md`<br/>• `product_launch_brief.md`<br/>• `PROJECT_LOG.md` |

---

## 🛠️ 六、快速上手步驟

1. **開啟輸入介面**：
   - 登入 [claude.ai](https://claude.ai)、開啟 Claude Desktop 桌面應用，或打開 Claude in Chrome 側邊欄。
2. **切換為 Cowork 模式**：
   - 在底部訊息輸入框（Message box）的左下角，將選項由「Chat」切換至 **「Cowork」**。
3. **選擇工作空間或關聯知識庫**：
   - **桌面端**：可選擇指定電腦上的本機資料夾（享有直接讀寫權限）。
   - **網頁/行動端**：可關聯已有的 **Projects** 知識庫或掛載雲端 Connectors（Google Drive / Slack）。
4. **設定安全核准模式 (Approval Mode)**：
   - 根據任務重要程度選擇 **Manual**（敏感資料推薦手動核准）、**Auto**（日常流暢推進）或 **Skip**。
5. **輸入目標提示詞 (Task Prompt)**：
   - 清楚告知目標（Objective）、來源資料、格式要求與交付型態。
6. **啟動運算或排程**：
   - **立即執行**：Claude 開始規劃步驟並顯示執行進度面板。
   - **設定排程**：輸入 `/schedule` 或點擊右上方「Schedule」設定每日/每週定時重複執行。

---

## 💡 七、教學與使用建議

> [!TIP]
> 1. **任務分流以節省額度 (Usage Limit 管理)**：
>    Cowork 是高運算密集的 Agentic 流程，消耗的 Token 配額遠大於普通對話。**單次問答、腦力激盪請留在「Chat」模式**；需**讀寫多份檔案、自動化排程、批次數據清洗**的複雜工作才切換至「Cowork」。
> 2. **本機連線 vs 雲端關機提醒**：
>    - 若排程任務**只使用網路搜尋、Google Drive、Slack 等雲端工具**（如範例 4），關閉電腦依然能在雲端準時完成。
>    - 若排程任務**需要存取您筆電內的本機資料夾**（如範例 1），請確保執行當下筆電處於開機且 Claude Desktop 連線狀態。
> 3. **重要任務請善用 Manual 核准模式**：
>    涉及寄送郵件、覆寫重要財務報表或外部 API 調用時，建議保持「Manually approve」模式，先審閱 Claude 的每一步執行計畫。

---

← [返回 Claude_AI 主講義](../README.md) | 🏠 [返回專案總首頁](../../README.md)
