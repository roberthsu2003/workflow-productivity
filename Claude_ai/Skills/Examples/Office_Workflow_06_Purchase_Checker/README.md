# 延伸練習 6：採購申請預檢員（第三階：整合者）

> **🎯 本階核心目標**  
> 運用 Claude AI 的「**多模態視覺辨識 (Vision)**」與「**程式碼執行 (Code Execution)**」能力！  
> 整合「**企業採購規章 (references/)**」、「**標準請購樣板 (templates/)**」與「**企業視覺 (assets/)**」，同仁可直接上傳**廠商報價單、電商比價截圖**或輸入日常採購清單，AI 自動核算金額級距、防退件預檢，並透過 Python 呼叫 `openpyxl` 寫入企業 Logo 與 `=SUM()` 加總公式，產出高質感的實體 `.xlsx` 採購請購單。

---

## 📖 範例運作機制

```mermaid
flowchart LR
    A[同仁輸入採購需求或<br>上傳廠商報價單/比價圖] --> B[視覺辨識 + 讀取<br>purchase-policy.md 規章]
    B --> C[比對金額級距與比價家數<br>預檢預算代碼與合規度]
    C --> D[啟用 Code Execution<br>執行 Python openpyxl]
    D --> E[載入 templates/ 樣板<br>+ 插入 assets/ Logo<br>+ 寫入 SUM 公式]
    E --> F[產出採購理由說帖草稿<br>與實體 Excel 請購單]
```

### 💡 自動化作業四部曲
1. **多模態辨識與規章比對**：  
   支援直接拍照或截圖上傳廠商報價單或電商網頁查價截圖。參照 `references/purchase-policy.md` 檢查金額級距（1萬~5萬需 2 家比價）、明確規格與預算科目代碼完整性。
2. **防退件說帖草稿生成**：  
   自動提煉商業效益，產出「採購理由與業務必要性說帖草稿」，方便同仁直接向主管呈報。
3. **品牌視覺與公式保留**：  
   呼叫 `openpyxl.drawing.image.Image` 將 `assets/company-logo.jpeg` 插入頂部表頭（Cell A1），並保留總額的原生加總公式（`=SUM(E11:E20)`）。
4. **實體報表交付**：  
   將申請人、部門、品項規格、單價、比價狀態填入指定儲存格，生成帶有企業品牌識別的完整實體 Excel 檔供下載。

---

## 📁 資料夾與檔案結構

### 1. 核心 Skill 設定架構（安裝 Skill 時所需之標準結構）
| 檔案 / 資料夾路徑 | 類型 | 職責與用途 |
| :--- | :---: | :--- |
| 📄 [`SKILL.md`](./SKILL.md) | 主設定檔 | 定義角色、報價單多模態辨識、防退件規則與 Python openpyxl SOP 指令 |
| 📁 `templates/` | 範本目錄 | 存放高質感請購審查樣板 [`purchase-request-template.xlsx`](./templates/purchase-request-template.xlsx) |
| 📁 `references/` | 參考規範 | 存放企業採購請購作業手冊 [`purchase-policy.md`](./references/purchase-policy.md) |
| 📁 `assets/` | 靜態資產 | 存放企業標準圖檔 [`company-logo.jpeg`](./assets/company-logo.jpeg)（嵌入 Excel 表頭 A1） |

### 2. 課堂實測教材（獨立測試資料夾，供學生上傳練習）
| 檔案 / 資料夾路徑 | 類型 | 職責與用途 |
| :--- | :---: | :--- |
| 📁 [`sample_materials/`](./sample_materials/) | 測試單據 | 存放符合企業常見規格之模擬報價單與比價圖檔（供圖片上傳測試） |

```text
Office_Workflow_06_Purchase_Checker/
├── SKILL.md                             # 核心技能指引（含多模態辨識與 Python openpyxl 規範）
├── templates/
│   └── purchase-request-template.xlsx   # 高質感專業採購請購 Excel 樣板
├── references/
│   └── purchase-policy.md               # 企業採購請購作業手冊
├── assets/
│   └── company-logo.jpeg                # 公司 Logo 圖檔（嵌入表頭 A1）
│
└── sample_materials/                    # 🧾 獨立課堂測試資料夾
    ├── 01_dell_monitor_quotation.png    # 廠商正式報價單 (聯強經銷 DELL 螢幕 3台)
    └── 02_ecom_price_comparison.png     # 電商通路比價截圖 (PChome 查價對照)
```

---

## 🛠️ 安裝與建置方式

你可以選擇以下三種方式之一來建立並啟用此技能：

### 💡 方式 A：使用內建 `/skill-creator` 技能（推薦・自動建置）

> [!TIP]
> 請先確認已在 Claude Settings 中開啟 **Code execution and file creation** 功能。

#### 方案 1：直接上傳檔案並下指令建立
1. **上傳檔案**：將以下 3 個檔案同時上傳至 Claude 對話中：
   * 樣板：[`purchase-request-template.xlsx`](./templates/purchase-request-template.xlsx)
   * 規範：[`purchase-policy.md`](./references/purchase-policy.md)
   * 圖片：[`company-logo.jpeg`](./assets/company-logo.jpeg)

2. **下達建置指令**：直接複製並貼上以下多行 Prompt：

   ```text
   我想建立一個採購申請預檢員 Skill。
   請參考我上傳的 purchase-policy.md 規章、Excel 樣板與 company-logo.jpeg 圖檔，
   使用 /skill-creator 幫我建立包含 references、templates 和 assets 資料夾的 Skill。

   請在 SKILL.md 中明確指定：
   1. 支援純文字或上傳廠商報價單圖檔，自動提取品項規格、數量、單價與總額。
   2. 依據 purchase-policy.md 檢查金額級距（1萬~5萬需 2 家比價）與預算代碼。
   3. 自動產出防退件建議與主管呈報採購理由說帖草稿。
   4. 執行 Python (Code Execution) 讀取 Excel 樣板並使用 openpyxl 
      在 Cell A1 嵌入 assets/company-logo.jpeg，保留合計列 =SUM(...) 原生公式。
   ```

3. **自動完成與啟用**：Claude 執行完畢後會自動在帳號中安裝並生效此 Skill。

---

### ✍️ 方式 B：手動複製檔案（網頁手動上傳）

1. **建立本機目錄**：在電腦中建立 `Office_Workflow_06_Purchase_Checker` 資料夾，並建立 `references`、`templates` 與 `assets` 三個子目錄。
2. **放置對應檔案**：放入對應之 [`SKILL.md`](./SKILL.md)、樣板、規範手冊與公司 Logo。
3. **上傳至 Claude**：前往 Claude 網頁版 **Settings** ➔ **Capabilities** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

---

### 💻 方式 C：終端機部署（適用於 Claude Code）

```bash
cp -r Office_Workflow_06_Purchase_Checker/ /mnt/skills/user/Office_Workflow_06_Purchase_Checker
```

---

## 🧪 測試與驗證（三種實測情境）

為滿足不同課堂環境與教學層次需求，本技能設計了 **3 種由淺入深的測試模式**：

---

### 📝 測試情境一：純文字快速審核（無圖・日常口語）

適合學員快速演練。直接複製以下同仁隨手寫下的雜亂採購文字需求：

#### 📥 測試 Prompt（純文字）：
```text
我們部門下個月有 2 位新進同仁報到，需要採購辦公設備，請購人為「資訊部 陳大華 (David Chen)」：
1. DELL 27吋 4K 護眼專業螢幕 (U2723QE) - 2 台，單價預估 NT$ 16,500，總價 NT$ 33,000
2. 羅技 MX Keys 無線人體工學鍵鼠組 - 2 組，單價預估 NT$ 3,800，總價 NT$ 7,600
3. 人體工學多段可調金屬螢幕支架 - 2 組，單價預估 NT$ 1,500，總價 NT$ 3,000
4. 預算科目代碼：IT-2026-CAPEX
5. 廠商來源：聯強國際經銷商報價

請幫我檢查有沒有符合採購法規？有沒有退件風險？請產出呈報主管的採購理由說帖，
並調用 Python 將採購審查單寫入 Excel 樣板，產出正式的 Excel 請購單供我下載！
```

---

### 📸 測試情境二：全單據圖片多模態辨識（純圖片・廠商正式報價單）

從 [`sample_materials/`](./sample_materials/) 目錄上傳廠商正式報價單與比價圖檔：

| 單據圖檔名稱 | 單據類型 | 關鍵欄位內容 | 預期審核結果 |
| :--- | :--- | :--- | :--- |
| [`01_dell_monitor_quotation.png`](./sample_materials/01_dell_monitor_quotation.png) | 聯強國際正式報價單 | DELL 螢幕 3台、單價 16,500、總計 NT$ 49,500 | 辨識完整，總額達 4.95 萬，提示需檢附第 2 家比價 |
| [`02_ecom_price_comparison.png`](./sample_materials/02_ecom_price_comparison.png) | PChome 24h 比價截圖 | 單台 17,900、3台 53,700，節省 4,200 | 比價合格，符合優先採購最低價標準 |

#### 📥 測試步驟與 Prompt（純圖片）：
1. 將上述 **2 張圖片同時拖入對話框**。
2. 輸入以下指令：

```text
這是我向經銷商索取的螢幕報價單與電商平台的比價存查截圖，請購人為「資訊部 陳大華 (David Chen)」。
預算代碼為「IT-2026-CAPEX」，用途為「研發處新進同仁工作站配發」。
請幫我進行多模態辨識與採購合規預檢，告訴我有沒有退件風險，
產出給主管的採購理由說帖草稿，並產出正式的 Excel 採購申請審查單。
```

---

### 🔀 測試情境三：圖片與文字多模態整合（混合模式・最貼近真實辦公室）

**最貼近日常辦公室的真實情況**：同仁手邊有大額硬體的廠商報價單圖片，但軟體授權與配件只有文字補充！

#### 📥 測試步驟與 Prompt（圖文整合）：
1. **上傳 1 張圖片**：[`01_dell_monitor_quotation.png`](./sample_materials/01_dell_monitor_quotation.png)（聯強報價單 NT$ 49,500）。
2. **在輸入框貼入以下圖文整合 Prompt**：

```text
請幫我整合審查以下硬體與軟體合併採購申請，請購人為「資訊部 陳大華 (David Chen)」：

【附件圖片部分】：
已上傳聯強經銷商的 3 台 4K 螢幕報價單（總額 NT$ 49,500），請自動辨識其規格與金額。

【純文字補充部分（軟體與配件採購）】：
1. JetBrains All Products Pack 開發工具一年授權 - 2 套，單價 NT$ 8,500，總計 NT$ 17,000（官網原廠刷卡採購）
2. 預算科目代碼：軟體部分為「IT-2026-OPEX」，硬體部分為「IT-2026-CAPEX」
3. 需求到貨日期：2026/09/20

請幫我檢查整體採購案有無違規或缺漏，產出呈報主管的採購說帖，
並將全部品項整合寫入 Excel 樣板，在表頭插入公司 Logo，產出實體 Excel 審查單供下載！
```

---

### 🎯 預期執行成果（智慧稽核與停止條件機制）

無論採取哪一種測試情境，Claude 皆會展現專業的「**安全煞車與主動補件（Human-in-the-Loop）**」機制：

* **🔍 階段 1・採購金額級距與防退件診斷**  
  - 核算總額：4.95 萬屬於中額採購（1萬~5萬級距），主動核對是否具備 2 家報價比價。
  - 若同仁未檢附比價圖，立即發出提示：`⚠️ 需補第 2 家比價單，否則採購處將退件`。
* **🚨 階段 2・安全煞車與主動詢問（Human-in-the-Loop）**  
  若同仁未輸入預算代碼或用途過於模糊，AI 絕不自行腦補捏造，而是主動向同仁發出補件清單，並詢問是否立即補充。
* **🐍 階段 3・Python 自動化處理與報表交付**  
  呼叫 Code Execution，以 `openpyxl` 載入 `templates/purchase-request-template.xlsx`：
  - 填入請購人資訊、預算代碼、需求日期。
  - 在 Cell A1 嵌入高清晰 `assets/company-logo.jpeg` 圖檔。
  - 將各筆品項明細寫入試算表，金額套用 `#,##0` 貨幣格式。
  - 合計列自動保留原生公式 `=SUM(E11:E20)`。
  - 產出實體 `.xlsx` 檔案提供即時點擊下載。

---

[← 返回 Skills 主頁](../../README.md)
