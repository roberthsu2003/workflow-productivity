# 🗂️ 範例 1：本機資料夾批次自動整理與報銷總表產出

> 🟢 **難度等級**：**Level 1（入門震撼・本機魔法）**  
> 💻 **適用平台**：Claude Desktop App (macOS / Windows)  
> 💼 **適用角色**：行政特助、財務助理、專案經理 (PM)、自媒體創作者、所有深受「雜亂下載區」困擾的上班族。  
> 🎯 **核心體驗**：
> - 📁 **本機資料夾直接讀寫 (Direct Local File Access)**：告別繁瑣的手動上傳與下載，授權 Claude 直接對硬碟目錄動工。
> - 💻 **本地檔案沙盒操作 (Desktop File Integration)**：自主分析檔案內容、建立分類子目錄、正規化更名並搬移歸檔。
> - 🛡️ **三大安全核准模式 (Manual / Auto / Skip)**：體驗 AI 在碰到磁碟寫入與檔案移動時的安全防護機制。

---

## 🎭 職場痛點劇場：月底的報銷地獄

> *「下班前 30 分鐘，財務部突然發信催收：『同仁請在今天 18:00 前提交 8-9 月所有差旅收據與軟體發票，否則本期不予報銷！』」*  
> *你急忙打開電腦的「下載」資料夾，映入眼簾的是幾百個未命名的 PDF、文字檔、發票截圖、NDA 草案和行銷簡報，混雜在一起。你只能一個個點開看、手動算金額、複製貼上到 Excel……天已經黑了。*

**現在，把這個任務交給 Claude Cowork，只要 20 秒，一鍵見證奇蹟！**

---

## 🔄 執行前後視覺化對比 (Before vs. After)

```
【整理前：雜亂無章的暫存區】
sample_files/
├── expenses_report_template.csv
└── raw_downloads/
    ├── INV_2026_08_GoogleWorkspace.txt   (雲端發票)
    ├── taxi_receipt_20260905.txt         (計程車收據)
    ├── contract_partner_NDA_v1.txt       (保密合約)
    └── Q3_marketing_proposal_draft.txt   (行銷企劃稿)

                ⬇️ 透過 Claude Cowork 一鍵自主執行 ⬇️

【整理後：井然有序的歸檔目錄與報銷總表】
sample_files/
├── 01_財務單據/
│   ├── 財務_20260831_GoogleWorkspace發票.txt
│   └── 財務_20260905_大都會計程車乘車證明.txt
├── 02_法務合約/
│   └── 合約_20260901_合作夥伴保密協議.txt
├── 03_專案企劃/
│   └── 企劃_20260910_Q3品牌推廣企劃草案.txt
├── expenses_report_template.csv (原始空白樣板)
└── expenses_summary_202609.csv  ⭐【自動產出！提取各單據統編與金額總表】
```

---

## 🧠 Cowork 代理執行管線 (Agent Execution Pipeline)

```mermaid
flowchart TD
    Start["📂 選擇本地工作資料夾 (sample_files)"] --> Scan["🔍 讀取 raw_downloads/ 內所有檔案內容"]
    Scan --> Analyze["🧠 辨識檔案語義 (財務 / 法務 / 企劃)"]
    Analyze --> Approval{"🛡️ 安全核准模式檢查"}
    Approval -- Manual 模式 --> PromptUser["跳出 Allow / Deny 請示使用者"]
    Approval -- Auto / Skip 模式 --> AutoPass["即時安全審查無虞，自動放行"]
    PromptUser --> Mkdir["📁 自動建立 3 個分類子目錄"]
    AutoPass --> Mkdir
    Mkdir --> Move["🚚 規範命名 (類別_日期_名稱) 並移動檔案"]
    Move --> Extract["🧾 提取發票日期、廠商、統編與含稅金額"]
    Extract --> CSV["📊 自動寫入並產出 expenses_summary_202609.csv"]
    CSV --> Finish["✅ 交付執行完成報告與總額統計"]
```

---

## 🛡️ 三大安全核准模式 (Approval Modes) 深度演練

在 Claude Cowork 中，涉及到**實體磁碟讀寫**時，右上方可隨時切換安全層級：

| 核准模式 | 介面行為特徵 | 適合場景 | 推薦指數 |
| :--- | :--- | :--- | :---: |
| **Manually approve<br>(Manual 手動核准)** | Claude 準備建立資料夾、移動檔案或寫入 CSV 前，畫面會**彈出確認卡片**（顯示即將執行的路徑），需手動按「Allow」才繼續。 | 首次操作、重要系統磁碟、敏感合約檔案 | ⭐️⭐️⭐️⭐️⭐️<br>(新手必練) |
| **Automatically approve<br>(Auto 自動審查)** | Claude 連續自主作業，背後安全模型即時檢查有無 Prompt Injection 攻擊或資料外洩風險，無異常即順暢推進。 | 日常行政、檔案批次清洗、高效率作業 | ⭐️⭐️⭐️⭐️<br>(日常首選) |
| **Skip all approvals<br>(Skip 跳過核准)** | 完全不審查、不暫停，以最高極速直接完成所有磁碟讀寫。 | 100% 信任的測試沙盒目錄 | ⭐️⭐️<br>(謹慎使用) |

---

## 🖥️ Cowork 擬真執行面板預覽 (What You Will See)

當您送出指令後，Claude Desktop 會展開生動的 Agent 執行進度串流：

```console
🤝 [Claude Cowork] Workspace: ./sample_files/
────────────────────────────────────────────────────────
➜ 🔍 Scanning raw_downloads/ (Found 4 files)...
➜ 📄 Reading INV_2026_08_GoogleWorkspace.txt (Invoice)
➜ 📄 Reading taxi_receipt_20260905.txt (Receipt)
➜ 📄 Reading contract_partner_NDA_v1.txt (Legal)
➜ 📄 Reading Q3_marketing_proposal_draft.txt (Plan)

⚠️ [Manual Approval Required]
Claude wants to create directories:
  • 01_財務單據/  • 02_法務合約/  • 03_專案企劃/
Actions: [ Deny ]  [ Allow ]  <--- 點擊 Allow 繼續

✔ 🚚 Moving and renaming 4 files... Done.
✔ 📊 Parsing amounts and generating summary CSV...
✨ Created: expenses_summary_202609.csv (Total: $1,340)
────────────────────────────────────────────────────────
Status: Task completed successfully.
```

---

## 🤖 Cowork 實戰 Prompt（RTCCF 結構）

請在 **Claude Desktop App** 中，切換至 **Cowork** 模式，工作目錄選取本資料夾中的 `sample_files/`，並輸入以下 Prompt：

```text
【Role】
你是一名高效能企業行政管理專員與財務特助。

【Task】
請檢查當前工作目錄下的 raw_downloads/ 資料夾，讀取裡面的所有檔案內容並執行以下工作：
1. 依據檔案性質建立分類子目錄：
   - 01_財務單據/
   - 02_法務合約/
   - 03_專案企劃/
2. 將 raw_downloads/ 中的檔案正規化重命名（命名格式：[類別]_[日期]_[項目名稱].[副檔名]）並移動至對應的子目錄中。
3. 針對所有屬於「財務單據」的檔案，精確提取其「日期、廠商名稱、發票/收據號碼、含稅金額、費用摘要與報銷人」資訊，參照 expenses_report_template.csv 的欄位規格，在根目錄產出一份名為 expenses_summary_202609.csv 的報銷總表。

【Context】
- 工作目錄：本機 sample_files/
- 報銷樣板：expenses_report_template.csv

【Constraint】
- 移動與更名前請確保原始文字內容完整無損。
- 金額必須準確提取含稅總計（Currency: TWD / USD 請標明）。
- 若單據有統編（如 12345678），請務必抓取填入。
- 使用繁體中文輸出。

【Format】
完成後，產出一份執行成果清單，清晰列出：
1. 檔案搬移紀錄表（原檔名 ➔ 新檔名與存放目錄）
2. 本期報銷金額統計表（個別明細與最終總金額）
3. 提示新檔案 expenses_summary_202609.csv 已儲存成功。
```

---

## 🚀 學員實戰動手做 3 步驟

1. **開啟 Claude Desktop App**：
   - 點擊底部訊息框左下角，由「Chat」切換至 **「Cowork」**。
2. **掛載練習目錄**：
   - 點擊工作目錄選擇按鈕，指定本機的 `Claude_ai/cowork/Examples/01_Local_Folder_Organize/sample_files/`。
3. **選擇核准模式並啟動**：
   - **體驗一（手動安全審查）**：選擇 **Manual** 模式，貼上上方 Prompt 送出。當介面彈出建立目錄和搬移檔案的請示時，點擊 **「Allow」**，親自體驗「人機協同」的安全掌控感！
   - **體驗二（極速自動化）**：復原檔案後改選 **Auto** 模式，再次執行，體驗 15 秒內全自動整理乾淨的極速快感！

---

## 💡 避坑指南與核心收穫 (Tips & Takeaways)

> [!TIP]
> 1. **為什麼要用 Desktop App？**  
>    Web 網頁端因瀏覽器安全沙盒限制，無法直接穿透讀寫硬碟檔案。**直接讀寫本機磁碟**是 Claude Desktop App 獨有的殺手級功能。
> 2. **發票數字容易漏看？**  
>    在 Prompt 中加入 `精確提取含稅金額與統編` 的條件（Constraint），Cowork 會仔細分析文字檔中的每一行關鍵字，準確率達 100%。
> 3. **隨時可復原**：  
>    如果分類不滿意，只要在對話中輸入：「*請幫我將檔案名稱與位置復原回原本的 raw_downloads/ 目錄*」，Claude 就會自主將檔案全部搬回原位！

---

← [返回 Cowork 主頁](../../README.md) ｜ [下一篇：範例 2 客訴分類與原地微調 →](../02_Customer_Feedback/)
