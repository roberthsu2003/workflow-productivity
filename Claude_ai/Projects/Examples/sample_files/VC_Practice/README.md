# 🎓 創投盡職調查 (VC Due Diligence) 學生實務練習指引

本資料夾包含了專為 **Claude Projects 知識庫 (RAG) 實作課程** 設計的測試檔案。
學生可以透過將這些檔案上傳至 Claude Project 知識庫，親身體驗「免改 Prompt，僅靠 Knowledge 擴充即實現跨檔案偵探抓包」的震撼效果。

---

## 📂 本資料夾練習檔案清單 (Practice Files)

### 🔴 第一部分：WeWork 2019 美股 IPO 爆雷案 (全球經典案例)

1. 📄 **`WeWork_2019_SEC_S1_Registration_Statement.md`**
   * **檔案類型**：招股說明書摘要 (對應 PDF 格式)
   * **內容重點**：包含 2019 年向美國 SEC 提交之 S-1 登記聲明、長租合約負債（470 億美元）與自創的 Non-GAAP 會計指標「Community Adjusted EBITDA」。
2. 📊 **`WeWork_2018_2019_Financial_Breakdown_BurnRate.csv`**
   * **檔案類型**：財務拆解與燒錢率表 (可用 Excel 點開並上傳)
   * **內容重點**：2018 年營收 18.2 億美元、淨虧損 19.3 億美元（每賺 $1 燒掉 $1.06 美元），以及各營運據點之現金流。
3. 📝 **`Adam_Neumann_Corporate_Governance_and_Trademark_Agreement.md`**
   * **檔案類型**：公司治理與條款合約 (對應 Word 格式)
   * **內容重點**：創辦人 Adam Neumann 擁有 20:1 雙重股權投票權、將個人房產出租給公司，以及將「We」商標作價 590 萬美元賣回給公司。
4. 📝 **`創投投審會_合夥人歷史質疑與退件庫.md`**
   * **檔案類型**：VC 內部評審紀錄 (對應 Word 格式)
   * **內容重點**：合夥人歷史退件的 3 大死穴：估值過高 (EV/Sales >10x)、創辦人專制集權、商業模式長短租期限錯配。

---

### 🛵 第二部分：Gogoro 睿能創意赴美 SPAC 上市與產發署審查案 (台灣在地真實案例)

5. 📄 **`Gogoro_Poema_SPAC_F4_Registration_Statement.md`**
   * **檔案類型**：SPAC 上市說明書 (對應 PDF 格式)
   * **內容重點**：赴美 Poema Global SPAC 上市 F-4 登記聲明，包含全台 GoStation 電池交換站之 CAPEX 折舊與現金流支出。
6. 📊 **`Gogoro_車輛毛利與補助依存度.csv`**
   * **檔案類型**：毛利與補助精算表 (可用 Excel 點開並上傳)
   * **內容重點**：每台電動機車售價、電池月租收入、經濟部產發署/地方政府補助金額（每台 7,000 ~ 10,000 元）與扣除補助後的真實毛利率。
7. 📝 **`經濟部產發署_睿能馬達國產化審查意見書.md`**
   * **檔案類型**：政府調查與合規公文 (對應 Word 格式)
   * **內容重點**：經濟部產發署關於馬達控制器供應商填報異動、1.85 億元售後保固安心方案成本與國產化補助資格審議結論。

---

## 🧪 學生課堂操作三步驟

### Step 1：建立 Claude Project
* 在 Claude 中建立一個名為 `創投盡調與風控練習` 的專案。
* 貼入上層 Examples 文件（`VC_Due_Diligence.md` 或 `Taiwan_VC_Gogoro.md`）中的 System Prompt (Instructions)。

### Step 2：將上述檔案上傳至專案 Knowledge
* 可先嘗試僅上傳部分檔案，觀察 AI 輸出的粗估回應。
* 隨後將全部 PDF/CSV/MD 檔案上傳，見證 AI 自動進行「跨檔案數據抓包與矛盾檢視」。

### Step 3：在專案開新對話測試
* 輸入：`請評估此案是否適合送投審會 (IC)？`
* 觀察 AI 如何精確指出創辦人吹牛、財務指標造假與政府補助依賴風險！
