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
- **雲端隔離運算 (Sessions in the Cloud)**：任務預設在 Anthropic 雲端伺服器的安全隔離沙盒中執行。即使闔上筆電或關閉瀏覽器，雲端任務依然會持續運行。
- **支援本機資源連動 (Local File & Desktop Integration)**：配合 Claude Desktop App，Claude 可直接讀寫電腦本地資料夾的檔案、操作內建瀏覽器，甚至進行電腦螢幕操作（Computer Use）。
- **跨裝置無縫接續 (Work from Anywhere)**：在辦公室電腦啟動任務，出門時在手機 App 檢視進度與給予回饋，回到家再在另一台裝置下載成品。

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

### 1. 🤖 自主任務執行與子代理協同 (Sub-agent Coordination)
- 給定目標後，Claude 會自主制定計畫、將任務拆解為子任務（Sub-agents），並視情況**並行處理**多條工作流程，大幅縮短執行時間。
- 具備記憶延續性（Shared Memory with Chat），能自動調用您過往在 Chat 中的偏好與對話記憶。

### 2. 🛡️ 三大安全核准模式 (Approval Modes)
在任務執行前或過程中，您可隨時調整安全核准模式：
1. **Manually approve (Manual)**（手動核准，前身為 Ask before acting）：Claude 執行每一步動作（存取本機、連網、調用工具）前皆會暫停，由您確認按 Allow（允許）或 Deny（拒絕）。
2. **Automatically approve (Auto)**（自動安全審查）：Claude 連續自主執行，但會在背後即時審查動作安全性（防範 Prompt Injection 提示詞注入與 Data Exfiltration 資料外洩）。若發現風險會自動攔阻或暫停請示您。（*注意：此安全審查會消耗較多 usage 配額*）。
3. **Skip all approvals (Skip)**（跳過所有核准，前身為 Act without asking）：完全不暫停也不進行額外審查，全速推進（僅適用於 100% 信任的內部安全環境）。

### 3. 📁 本機資料夾讀寫 (Direct Local File Access)
- 透過 **Claude Desktop App (macOS / Windows)**，您可以指定工作資料夾。
- Claude 能直接在您的硬碟中讀取、分類、重命名檔案，並直接寫入產出成果（如：整理 Downloads 資料夾、批量將發票產出報銷總表）。

### 4. 🌐 內建瀏覽器與網路操作 (Built-in Browser & Chrome)
- 處理需要查閱外部網站的任務時，Claude 能自動開啟網頁、閱讀內容、點擊按鈕與填寫表單。
- 桌面版具備免安裝的**內建瀏覽器 (Built-in browser)**，亦可選擇直接連動您的 **Chrome 瀏覽器 (Claude in Chrome)**。

### 5. 🕒 雲端排程任務 (Scheduled Tasks)
- 支援在任務中直接輸入 `/schedule`，或從左側側邊欄點選「Scheduled」管理排程。
- 支援「每小時 / 每日 / 每週 / 工作日」自動執行。
- **純雲端任務無須開機**：使用網路搜尋、雲端檔案或 Connectors 的排程任務，即使電腦休眠或關機也會準時在雲端執行並交付成果。

### 6. 📝 原地反白微調草稿 (Edit Drafts in Place)
- 當 Claude 產出長篇 Markdown 報告或草稿時，學員可以直接在畫面上**反白選取欲修改的段落**，點擊「Edit with Claude」輸入微調指令，Claude 即會原地更新該段文字，無需在對話串中費力描述。

### 7. 🎯 全域與資料夾指令 (Global & Folder Instructions)
- **Global instructions**：在 `Settings > Cowork` 設定常駐指令（如您的工作職稱、公司產品線、偏好語氣與交付格式），自動套用於每次 Cowork 任務。
- **Folder instructions**：在桌面版為指定資料夾設定專屬指令，Claude 在處理專案期間還能自主維護與更新該資料夾的進度筆記。

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
| **內建瀏覽器操作 (Browser Use)** | ✅ | ⚠️ 需 Desktop 開啟連線 | ⚠️ 需 Desktop 開啟連線 | ✅（可讀取當前分頁） |
| **電腦螢幕操作 (Computer Use Beta)**| ✅ | ⚠️ 需 Desktop 開啟連線 | ⚠️ 需 Desktop 開啟連線 | — |

> [!NOTE]
> 標註「⚠️ 需 Desktop 開啟連線」的功能，代表任務雖然在雲端排程或行動端發起，但若需要碰觸您電腦中的**實體檔案**或**本機應用程式**，該台電腦上的 Claude Desktop App 必須維持開啟且聯網。

---

## 🎓 五、3 大職場自動化實戰範例 (含學員練習檔)

為幫助學員無痛上手 Cowork，本單元提供 3 個真實職場場景的實戰範例，每個範例皆附有可直接下載測試的原始範例檔案 (`sample_files/`)：

| # | 實戰範例名稱 | 職場應用場景 | Cowork 核心能力 | 學員練習檔 (`sample_files/`) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | [**每日產業情報與競品自動彙整**](./Examples/01_Daily_News_Brief/README.md) | 創投、行銷與企劃團隊每日監測產業新聞與趨勢。 | • 內建瀏覽器與 Web 檢索<br/>• Scheduled 雲端定時排程 | • `industry_keywords.txt`<br/>• `daily_news_template.md` |
| **2** | [**跨來源財務與營運數據對比**](./Examples/02_Financial_Report/README.md) | 財務與風控團隊自動交叉比對多份 CSV 財務與預算。 | • 背景運算與多檔案交叉分析<br/>• 產出含公式之 Excel 活頁簿 | • `q3_financial_raw.csv`<br/>• `crm_sales_target.csv` |
| **3** | [**客戶客訴與意見自動分類處置**](./Examples/03_Customer_Feedback/README.md) | 客服、PM 與營運團隊處理批量客訴，分類評級並草擬回信。 | • 多檔案批量處理與比對<br/>• 原地劃記微調 (Edit in Place) | • `customer_support_logs.csv`<br/>• `sop_escalation_rules.md` |

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
>    - 若排程任務**只使用網路搜尋、Google Drive、Slack 等雲端工具**，關閉電腦依然能在雲端準時完成。
>    - 若排程任務**需要存取您筆電內的本機資料夾**，請確保執行當下筆電處於開機且 Claude Desktop 連線狀態。
> 3. **重要任務請善用 Manual 核准模式**：
>    涉及寄送郵件、覆寫重要財務報表或外部 API 調用時，建議保持「Manually approve」模式，先審閱 Claude 的每一步執行計畫。

---

← [返回 Claude_AI 主講義](../README.md) | 🏠 [返回專案總首頁](../../README.md)

