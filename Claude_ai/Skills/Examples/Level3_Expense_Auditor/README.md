# Level 3 範例：差旅與公務費用報銷審核員（第三階：整合者）

> **🎯 本階核心目標**  
> 運用 Claude AI 的「**程式碼執行 (Code Execution)**」能力，讓 Skill 自動執行 Python 腳本！  
> 整合「**外部規章 (references/)**」、「**專業報銷樣板 (templates/)**」與「**企業視覺 (assets/)**」，自動完成發票與收據審核，並將企業 Logo 與 `=SUM()` 加總公式寫入 Excel，產出兼具精準審核與高質感視覺的實體 `.xlsx` 請款單。

---

## 📖 範例運作機制

```mermaid
flowchart LR
    A[同仁輸入報銷清單與發票明細] --> B[讀取 references/<br>expense-policy.md 規章]
    B --> C[逐筆審核統編、限額與事由]
    C --> D[啟用 Code Execution<br>執行 Python openpyxl]
    D --> E[讀取 templates/ 樣板<br>+ 插入 assets/ Logo<br>+ 寫入原生 SUM 公式]
    E --> F[產出高質感商務<br>Excel 請款審核單]
```

### 💡 自動化作業四部曲
1. **規章政策比對**：  
   參照 `references/expense-policy.md` 檢查統一編號（`88888888`）、市區計程車單趟上限（NT$ 500 且需事由）、高鐵限標準車廂、公務用餐單人上限（NT$ 600/人）。
2. **自動化 Python 處理**：  
   AI 自動調用 Code Execution 載入 `templates/expense-report-template.xlsx` 商務樣板。
3. **品牌視覺與公式保留**：  
   呼叫 `openpyxl.drawing.image.Image` 將 `assets/company-logo.jpeg` 插入頂部表頭（Cell A1），並保留總計列的原生加總公式（`=SUM(F9:F18)`）。
4. **實體報表交付**：  
   將申請人資訊、費用明細、稽核狀態（`✅ 合規` / `⚠️ 需補件` / `❌ 超標`）與財務備註填入指定儲存格，生成帶有企業品牌識別的完整實體 Excel 檔供下載。

---

## 📁 資料夾與檔案結構

| 檔案 / 資料夾路徑 | 類型 | 職責與用途 |
| :--- | :---: | :--- |
| 📄 [`SKILL.md`](./SKILL.md) | 主設定檔 | 定義角色、稽核規則與 Python openpyxl 插入圖片及公式的 SOP 指令 |
| 📁 `templates/` | 範本目錄 | 存放高質感報銷樣板 [`expense-report-template.xlsx`](./templates/expense-report-template.xlsx) |
| 📁 `references/` | 參考規範 | 存放企業差旅與公務費用手冊 [`expense-policy.md`](./references/expense-policy.md) |
| 📁 `assets/` | 靜態資產 | 存放企業標準圖檔 [`company-logo.jpeg`](./assets/company-logo.jpeg)（嵌入 Excel 表頭 A1） |

```text
Level3_Expense_Auditor/
├── SKILL.md                             # 核心技能指引（含 Python openpyxl 規範）
├── templates/
│   └── expense-report-template.xlsx     # 高質感專業報銷 Excel 樣板
├── references/
│   └── expense-policy.md                # 差旅與費用報銷規範參考手冊
└── assets/
    └── company-logo.jpeg                # 公司 Logo 圖檔（嵌入表頭 A1）
```

---

## 🛠️ 安裝與建置方式

你可以選擇以下三種方式之一來建立並啟用此技能：

### 💡 方式 A：使用內建 `/skill-creator` 技能（推薦・自動建置）

> [!TIP]
> 請先確認已在 Claude Settings 中開啟 **Code execution and file creation** 功能。

#### 方案 1：直接上傳檔案並下指令建立
1. **上傳檔案**：將以下 3 個檔案同時上傳至 Claude 對話中：
   * 樣板：[`expense-report-template.xlsx`](./templates/expense-report-template.xlsx)
   * 規範：[`expense-policy.md`](./references/expense-policy.md)
   * 圖片：[`company-logo.jpeg`](./assets/company-logo.jpeg)

2. **下達建置指令**：直接複製並貼上以下多行 Prompt：

   ```text
   我想建立一個差旅與公務費用報銷審核員 Skill。
   請參考我上傳的 expense-policy.md 規章、Excel 樣板與 company-logo.jpeg 圖檔，
   使用 /skill-creator 幫我建立包含 references、templates 和 assets 資料夾的 Skill。

   請在 SKILL.md 中明確指定：
   1. 依據 expense-policy.md 逐筆審核發票統編、限額規範與公務事由完整度。
   2. 執行 Python (Code Execution) 寫入 Excel 報銷單時，
      必須使用 openpyxl.drawing.image.Image 將 assets/company-logo.jpeg 
      縮放插入置於試算表頂端表頭 (Cell A1)。
   3. 申請金額欄位必須保留原生加總公式 =SUM(...)，不得寫死數值。
   ```

3. **自動完成與啟用**：
   * Claude 執行完畢後會自動在帳號中安裝並生效此 Skill。
   * *(可選備份)*：可下載 Claude 提供的 ZIP 封裝包保存於本機。

---

#### 方案 2：先完成任務對話，再一鍵打包成技能
1. **實測任務對話**：
   * 將上述 3 個檔案上傳至對話中。
   * 輸入一組同仁日常報銷明細（含計程車、高鐵、公務餐費），請 Claude 先進行合規性審查，並呼叫 Python 填寫 Excel 樣板、寫入 SUM 公式及嵌入 Logo。
   * 下載檢查 Excel 成果，若排版、欄寬或狀態顏色需微調，繼續與 Claude 對話調整至完全滿意。

2. **下一鍵打包指令**：成果滿意後，直接輸入多行 Prompt：

   ```text
   請參考剛才我們對話的審核邏輯、Excel 報銷單輸出格式與公司 Logo 圖片，
   使用 /skill-creator 幫我將這個功能打包建立為包含 references, templates 與 assets 的自訂技能。

   請確保 SKILL.md 中寫入：
   用 openpyxl 將 assets/company-logo.jpeg 嵌入至 Excel 表頭 (Cell A1)，
   並在總計列寫入 =SUM(...) 原生公式的 SOP 流程。
   ```

3. **自動生效**：Claude 打包完成後，此 Skill 即直接於當前帳號中啟用。

---

### ✍️ 方式 B：手動複製檔案（網頁手動上傳）

1. **建立本機目錄**：在電腦中建立 `Level3_Expense_Auditor` 資料夾，並於其下建立 `references`、`templates` 與 `assets` 三個子目錄。
2. **放置對應檔案**：
   * 根目錄：放入 [`SKILL.md`](./SKILL.md)
   * `templates/`：放入 [`expense-report-template.xlsx`](./templates/expense-report-template.xlsx)
   * `references/`：放入 [`expense-policy.md`](./references/expense-policy.md)
   * `assets/`：放入 [`company-logo.jpeg`](./assets/company-logo.jpeg)
3. **上傳至 Claude**：前往 Claude 網頁版 **Settings** ➔ **Capabilities** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

---

### 💻 方式 C：終端機部署（適用於 Claude Code）

若在 Claude Code 終端機環境中，可直接將本專案目錄複製至 Skill 系統路徑：

```bash
cp -r Level3_Expense_Auditor/ /mnt/skills/user/Level3_Expense_Auditor
```

複製完成後，終端機對話環境將自動載入該技能。

---

## 🧪 測試與驗證

安裝完成後，開啟新對話並輸入以下極具辦公室臨場感的測試案例：

### 📥 測試 Prompt（含合規、需補件、超標混合案例）

```text
請幫我審核以下這批同仁上週出差的報銷申請，申請人為「業務部 陳大華 (David Chen)」：

1. 2026/08/20 - 台北市區計程車 - NT$ 380，統編 88888888（事由：攜帶 2 箱重量展示樣品拜訪客戶）
2. 2026/08/21 - 台北前往台中高鐵票 - NT$ 700，統編 88888888（標準車廂對號座）
3. 2026/08/21 - 台中市區 Uber - NT$ 560，統編 88888888（未填寫事由）
4. 2026/08/21 - 客戶商務晚宴 - NT$ 2,800，統編 88888888（事由：招待台中國際開發王總經理 1 人，我方 1 人共 2 人用餐）
5. 2026/08/22 - 個人加班晚餐 - NT$ 850，統編 88888888（備註：個人加班誤餐）

請幫我產出審核結論，並將正式報銷單填寫入樣板，插入公司 Logo 並提供 Excel 下載。
```

---

### 🎯 預期執行成果

Claude 將自動識別並調用本 Skill，完成以下三階段任務：

* **🔍 階段 1・財務合規性逐筆診斷**  
  - 第 1 筆：`✅ 合規`（有攜帶樣品事由，未超額 NT$ 500）。
  - 第 2 筆：`✅ 合規`（標準車廂對號座，統編正確）。
  - 第 3 筆：`⚠️ 需補件 / ❌ 超標`（超過 NT$ 500 上限，且未填寫公務急迫事由，超額 60 元需自負或經主管核准）。
  - 第 4 筆：`✅ 合規`（商務宴客每人限額 NT$ 1,500，2 人上限 NT$ 3,000，申報 NT$ 2,800 合規）。
  - 第 5 筆：`❌ 超標`（個人日常公務餐費上限為 NT$ 600，超額 NT$ 250 列為超標自付）。

* **🐍 階段 2・Python 自動化處理**  
  自動呼叫 Code Execution，以 `openpyxl` 載入 `templates/expense-report-template.xlsx`：
  - 填入申請人姓名「陳大華 (David Chen)」、部門「業務部」。
  - 在 Cell A1 嵌入高清晰 `assets/company-logo.jpeg` 圖檔。
  - 將 5 筆明細寫入試算表，狀態欄搭配顏色標註。
  - 總計列寫入公式 `=SUM(F9:F13)`，金額欄位維持千分號格式。

* **📊 階段 3・產出實體報表檔**  
  輸出文字對話摘要，同時生成具備企業視覺的實體 `.xlsx` 檔案提供即時點擊下載。

---

[← 返回 Skills 主頁](../../README.md)
