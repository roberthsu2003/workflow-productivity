# 🟡 Level 3 高階實戰：商業數據分析庫（會自動進化的圖表）📊

> **學習階段**：🟡 Level 3（高階數據應用）　|　**預計實作時間**：25 分鐘  
> **核心目標**：多資料源動態合併、免改 Prompt 知識庫自動演進、Artifact 互動式圖表儀表板

---

## 📥 學生課堂實作檔案下載區

在開始前，請點擊下方連結下載本次練習所需的模擬銷售數據（提供 Markdown、CSV 與真實 Excel 三種格式供體驗）：

| 檔案類型 | 檔案名稱（點擊直接下載/檢視） | 檔案說明與用途 | 在專案中的用途 |
| :---: | :---| :---| :---|
| 📄 **Markdown** | [**sales_Q1.md**](./sample_files/sales_Q1.md) | 2026 第一季產品銷售數據（1~3月，營收合計 900 萬元）。 | 📁 基礎篇：階段一上傳至 **Knowledge** |
| 📄 **Markdown** | [**sales_Q2.md**](./sample_files/sales_Q2.md) | 2026 第二季產品銷售數據（4~6月，營收合計 1,520 萬元）。 | 📁 基礎篇：階段二追加上傳至 **Knowledge** |
| 📊 **Excel (3 Sheets)** | [**星橋科技_2026上半年產品銷售數據.xlsx**](./sample_files/星橋科技_2026上半年產品銷售數據.xlsx) | 含 3 個工作表（Q1銷售、Q2銷售、產品毛利對照）。 | 🚀 延伸篇：透過 AI 轉檔瘦身源檔案 |
| 📄 **CSV (已轉檔)** | [**sales_Q1.csv**](./sample_files/sales_Q1.csv) | 從 Excel 拆分出的 Q1 銷售數據（輕量、高效率）。 | 🚀 延伸篇：入庫至 **Knowledge** |
| 📄 **CSV (已轉檔)** | [**sales_Q2.csv**](./sample_files/sales_Q2.csv) | 從 Excel 拆分出的 Q2 銷售數據。 | 🚀 延伸篇：入庫至 **Knowledge** |
| 📄 **CSV (已轉檔)** | [**product_profit_margin.csv**](./sample_files/product_profit_margin.csv) | 從 Excel 拆分出的產品線毛利對照表（用於跨表關聯）。 | 🚀 延伸篇：入庫至 **Knowledge**（跨表 JOIN） |

---

## 📖 情境故事

小美是星橋科技的營運主管。她每季都需要向總經理與董事會匯報銷售趨勢，並附上最新圖表。

過去，每次拿到新一季數據，她都得手動把 Q1、Q2 的數字重新貼進對話框，或重新組合一份巨大的 Excel 再上傳給 AI。到了 Q3、Q4，每次對話都要重新貼一長串歷史數據，費時又容易遺漏。

現在，小美利用 Claude Projects 建立了「商業數據分析庫」：
- 她只要把每季的數據檔案**直接丟進專案 Knowledge**（或透過 Google Drive 連接器自動同步）。
- 之後無論過多久、開幾個新對話，她只需要輸入同一句指令：`繪製銷售趨勢圖`。
- Claude 就會**自動掃描 Knowledge 裡所有的資料表，跨檔合併並自動產出最新圖表**！

---

## 🛠️ Step-by-Step 操作流程

### 第一步：建立新專案
1. 在 Claude 左側點選 **Projects** ➔ 點擊 **New project**。
2. **專案名稱**：`星橋商業數據分析庫`
3. **專案目標**：`自動掃描多季度數據、跨檔合併並繪製動態分析儀表板`
4. 點擊 **Create project**。

### 第二步：配置 Instructions
點選右側 **Instructions** 的 **Edit**，貼入下方內容（亦可查看 [Instructions.md](./Instructions.md)）：

```markdown
## Role
你是星橋科技的「資深商業數據分析師 (BI Analyst)」，具備深厚財務洞察力與前端視覺化能力。

## Task
當收到「分析銷售趨勢並繪製圖表」時，執行：
1. 動態掃描與合併：自動讀取 Knowledge 中所有銷售數據（MD/CSV/Excel），依月份時間軸由遠至近合併。
2. 關鍵指標計算：累計總銷售金額、平均月營收、月複合成長率。
3. 互動視覺化：調用 Artifacts 建立互動式圖表（React + Recharts 或 HTML + Chart.js），繪製長條圖與折線圖。
4. 商業決策洞察：附上 2~3 點精闢的營運策略建言。
```

---

## 🧪 圖表進化實測：見證兩階段演進

### 階段一：僅上傳第一季數據時
1. 在專案 **Project Knowledge** 區塊，僅上傳下載好的 [sales_Q1.md](./sample_files/sales_Q1.md)。
2. 在專案中點擊輸入框開新對話，輸入指令：
```text
請分析銷售趨勢並繪製圖表。
```
**✅ 觀察成果**：
- Claude 讀取 `sales_Q1.md`，計算出第一季總營收 900 萬元。
- 透過 Artifact 生成一張包含 **1月、2月、3月** 的互動圖表。

---

### 階段二：加入第二季數據，見證同一指令自動升級！
1. 回到專案主頁，在 **Project Knowledge** 區塊中點擊 **Add content**，追加上傳 [sales_Q2.md](./sample_files/sales_Q2.md)。
2. 開啟一個**全新的對話 (New Chat)**，輸入**一模一樣的指令**：
```text
請分析銷售趨勢並繪製圖表。
```
**✅ 觀察成果**：
- **Prompt 一個字都沒改！**
- Claude 自動偵測到 Knowledge 中有兩份季報，主動將 1~6 月的數據串接合併。
- 總營收自動累計為 2,420 萬元，生成的 Artifact 圖表自動擴展為 **1 到 6 月的完整上半年成長曲線**！

---

## 🚀 延伸進階實戰：巨型多工作表 Excel 瘦身術（AI 轉 3 個 CSV + 知識庫入庫）

在真實企業日常中，業務或財務部門最常提供**內含多個工作表（Sheets）的 Excel 試算表**。然而，直接將多工作表 Excel 原檔丟進 Projects Knowledge，往往會面臨 Token 暴增與解析混淆的難題。

### ⚠️ 為什麼「不要直接把多工作表 Excel 塞進 Knowledge」？

| 痛點維度 | 直接上傳多工作表 Excel (.xlsx) | 先透過 AI 拆分轉為 CSV (.csv) |
| :--- | :--- | :--- |
| **Token 消耗** | 🔴 **極高**。底層為龐大 XML/ZIP 架構，模型展開需額外解析格式、公式與儲存格樣式，快速耗盡 Prompt Caching 配額。 | 🟢 **極低（節省 70%~90%）**。純文字逗號分隔，只傳遞關鍵數據，大幅減輕模型負擔。 |
| **跨工作表辨識** | 🔴 **容易遺漏或混淆**。大語言模型在讀取單一檔內的多個 Sheets 時，容易只檢索第一頁或產生跨頁欄位錯位。 | 🟢 **語義清晰隔離**。每個 CSV 檔名獨立對應特定資料維度（如 Q1數據、Q2數據、毛利表）。 |
| **關聯運算效率** | 🟡 **較慢**。每次跨頁運算都要全文反覆解碼。 | 🟢 **飛快**。結構標準，支援直接進行 SQL 式跨表 JOIN 與統計運算。 |

---

### 🧪 三步驟延伸操作：AI 拆分 ➔ 知識庫入庫 ➔ 跨表利潤分析

#### 第一步：在一般對話中，請 Claude 執行 Python 將 Excel 拆成 3 個 CSV

1. 打開一個**全新的 Claude 一般對話**（確保支援程式碼執行 / Analysis Tool）。
2. 點擊迴紋針上傳包含 3 個工作表的檔案：[**星橋科技_2026上半年產品銷售數據.xlsx**](./sample_files/星橋科技_2026上半年產品銷售數據.xlsx)。
3. 輸入以下轉檔提示詞（Prompt）：

```text
這是一份包含 3 個工作表（Q1_銷售明細、Q2_銷售明細、產品利潤與負責團隊）的 Excel 檔案。

請啟動 Python 分析環境幫我處理：
1. 讀取每一個工作表的名稱與前兩列預覽。
2. 將這 3 個工作表分別轉存為獨立的 CSV 檔案（UTF-8 編碼，保留標題列）。
3. 檔案分別命名為：
   - sales_Q1.csv
   - sales_Q2.csv
   - product_profit_margin.csv
4. 產生這 3 個 CSV 檔案的直接下載連結給我。
```

> 💡 **AI 執行過程**：  
> Claude 會自動調用 Python (`pandas` / `openpyxl`)，將 3 個 Sheet 逐一匯出為純淨的 CSV，並在對話視窗直接產出 3 個下載按鈕！  
> *(註：若想直接練習後續步驟，本專案已將轉好的 3 個檔案備妥於 sample_files 目錄供您直接點擊下載：[sales_Q1.csv](./sample_files/sales_Q1.csv)、[sales_Q2.csv](./sample_files/sales_Q2.csv)、[product_profit_margin.csv](./sample_files/product_profit_margin.csv))*

---

#### 第二步：將 3 個 CSV 檔案加入專案 Knowledge

1. 回到 **星橋商業數據分析庫** 專案主頁。
2. 在 **Project Knowledge** 區塊，點擊 **Add content**。
3. 一次將以下 3 個精簡後的 CSV 檔案全選上傳：
   - 📄 `sales_Q1.csv`（1~3月銷量與營收）
   - 📄 `sales_Q2.csv`（4~6月銷量與營收）
   - 📄 `product_profit_margin.csv`（產品毛利率 68% 與負責團隊對照）

---

#### 第三步：跨表利潤關聯實測（JOIN 跨表計算 + 互動式 Artifact）

在該專案內開啟新對話，輸入進階商業決策指令：

```text
請結合知識庫中的上半年銷售數據（sales_Q1.csv、sales_Q2.csv）與產品利潤對照表（product_profit_margin.csv）：
1. 跨表比對「智慧客服系統 2.0 (北極星)」的產品毛利率。
2. 計算 1~6 月各月份的「實際毛利金額」（月營收 × 毛利率 68%）。
3. 列出上半年總營收、上半年總毛利、以及平均每月毛利。
4. 使用 Artifact 繪製一個高質感的互動儀表板，同時展示「每月營收長條圖」與「實際毛利趨勢折線圖」。
```

> 🎯 **實測成果見證**：
> 1. **精準跨表關聯 (Cross-table JOIN)**：Claude 能從 `product_profit_margin.csv` 精準抓取 PROD-AI-01 毛利率為 `0.68 (68%)`，並無縫關聯 Q1 與 Q2 的 6 個月份營收。
> 2. **零幻覺準確計算**：
>    - 1月毛利：240 萬 × 0.68 = 163.2 萬元
>    - 6月毛利：600 萬 × 0.68 = 408 萬元
>    - 上半年累計總營收 2,420 萬元，累計毛利達 1,645.6 萬元！
> 3. **高階雙軸 Artifact 儀表板**：直接渲染出營收長條柱與毛利折線圖並存的雙軸圖表，並附上深入的利潤率策略建言。

---

← [返回 Projects 總覽](../../README.md)
