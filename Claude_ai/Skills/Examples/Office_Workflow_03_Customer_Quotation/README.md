# 延伸練習 3：客戶報價單產生器（第二階：創作者）

這是第二階的延伸實作練習。本階段的重點在於學會如何使用 Excel 樣板檔案（Templates）來限制 AI 的輸出格式，並產出實體 Excel 檔案供下載。

## 📖 範例說明

這個 Skill 會將您隨手寫下的雜亂客戶專案需求、報價項目與折讓條件，重新進行金額計算，並套用公司標準報價單 Excel 樣板，產出格式嚴謹、專業的商務報價單（`.xlsx`）供下載。

## 🎓 教學：如何將一般 Excel 檔案轉換為 Excel 樣板與預留欄位 (Placeholder)

在職場自動化中，我們常需要 AI 將資料寫入公司既有的 Excel 表單。若要讓 AI 能夠精準填入資料，我們必須先將普通的 Excel 檔案改造為**樣板 (Template)**：

### 1. 什麼是 Excel 樣板？
Excel 樣板就是一個已美化好版面（包含字型、邊框、底色、欄寬與對齊方式等）的普通 `.xlsx` 檔案。我們不需要在檔案中手動輸入具體的客戶名字或金額，而是使用特殊的**標記文字（預留欄位/Placeholder）**來代替。

### 2. 轉換與設計步驟

1. **設計版面與樣式**：
   在 Excel 中繪製好正式的表格。例如，設定字型為「微軟正黑體」、為標題加上背景色彩、設定儲存格的邊框樣式等。
2. **置入大括號佔位符 (Placeholder)**：
   在需要 AI 自動填入資料的儲存格內，直接輸入由大括號包裹的預留字串（如 `{CLIENT_NAME}`、`{DATE}` 等）。
   * 範例樣板 [quotation-template.xlsx](./templates/quotation-template.xlsx) 中使用的預留欄位包含：
     * 客戶與專案：`{CLIENT_NAME}` (客戶名稱)、`{CONTACT_PERSON}` (聯絡窗口)、`{PROJECT_NAME}` (專案名稱)
     * 報價與日期：`{QUOTATION_NO}` (報價單號)、`{DATE}` (報價日期)、`{EXPIRY_DATE}` (有效期限)
     * 交易條款：`{PAYMENT_TERMS}` (付款方式)、`{PROJECT_TIMELINE}` (專案時程)、`{WARRANTY_TERMS}` (保固條款)
     * 金額計算：`{SUBTOTAL}` (合計小計)、`{DISCOUNT}` (折讓優惠)、`{TOTAL}` (總計金額)
   * *💡 提示：預留字串建議一律使用大寫英文與底線（如 `{CLIENT_NAME}`），方便 Python 腳本進行精確的文字取代比對。*
3. **明細列表預設列**：
   報價項目的數量（列數）往往是不固定的。在樣板中，我們通常會預留一行格式好的空白列（例如 Row 11），當 Claude 執行 Python 程式碼時，會自動在該列下方動態插入新列、複製格式並填入資料。
4. **另存新檔**：
   確認所有預留欄位都填寫妥當後，直接儲存為 `.xlsx` 檔案，並放置於 Skill 目錄下的 `templates/` 資料夾內。

## 📁 實體自訂 Skill 結構

此範例在手動建立時，包含以下檔案與資料夾結構：

```
Office_Workflow_03_Customer_Quotation/
├── SKILL.md
└── templates/
    └── quotation-template.xlsx  # 儲存報價單標準 Excel 樣板
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）
1. 先將 [quotation-template.xlsx](./templates/quotation-template.xlsx) 檔案上傳至 Claude 對話中。
2. 直接下指令：

```
我想建立一個客戶報價單 Skill。請參考我剛才上傳的 Excel 樣板檔案格式，使用 /skill-creator 幫我建立包含 templates 資料夾的 Skill。若在填寫時發現有些欄位缺少資料，必須詢問使用者進行確認。
```

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Office_Workflow_03_Customer_Quotation`，並在其中建立名為 `templates` 的子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 內容儲存於根目錄；將 [quotation-template.xlsx](./templates/quotation-template.xlsx) 內容儲存至 `templates/` 目錄中。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

### 💡 方式 C：在終端機中部署（適用於 Claude Code / 終端機代理）
若您是在終端機（如 Claude Code）環境中使用，可以直接將本範例的整個資料夾（包含根目錄的 `SKILL.md` 檔案與相關子目錄）複製或移動到 `/mnt/skills/user/` 下。例如：
```bash
cp -r Office_Workflow_03_Customer_Quotation/ /mnt/skills/user/Office_Workflow_03_Customer_Quotation
```
複製完成後即可在對話中直接使用該自訂技能。

## 🧪 測試與驗證

確認 Skill 建立成功後，您可以開啟新對話並使用以下範例 Prompt 來測試其效果：

**測試 Prompt：**
```text
請幫我產出報價單：
「客戶是創新科技，窗口是王經理。我們要幫他們開發一個簡單的官網，項目包括：首頁設計 15,000 元（1式）、聯絡表單功能開發 5,000 元（1組）、以及 RWD 響應式切版 8,000 元（1式）。專案時程是簽約後一個月內完工。我們額外給他們 10% 的折讓優惠，保固期限是一年。有效期限到這週五。」
```

**預期效果：**
Claude 將會自動啟用該 Skill，並依據 `templates/quotation-template.xlsx` 的結構，呼叫 Python 程式碼將上述內容進行金額與折讓計算後寫入，產出可供下載的專案服務報價單 `.xlsx` 檔案。

---

← [返回 Skills 主頁](../README.md)
