# 延伸練習 3：客戶報價單產生器（第二階：創作者）

這是第二階的延伸實作練習。本階段的重點在於學會如何使用 Excel 樣板檔案（Templates）來限制 AI 的輸出格式，並產出實體 Excel 檔案供下載。

## 📖 範例說明

這個 Skill 會將您隨手寫下的雜亂客戶專案需求、報價項目與折讓條件，重新進行金額計算，並套用公司標準報價單 Excel 樣板，產出格式嚴謹、專業的商務報價單（`.xlsx`）供下載。

## 📁 實體自訂 Skill 結構

此範例在手動建立時，包含以下檔案與資料夾結構：
```text
Office_Workflow_03_Customer_Quotation/
├── SKILL.md
└── templates/
    └── quotation-template.xlsx  # 儲存報價單標準 Excel 樣板
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）
1. 先將 [quotation-template.xlsx](./templates/quotation-template.xlsx) 檔案上傳至 Claude 對話中。
2. 直接下指令：
   > 「`我想建立一個客戶報價單 Skill。請參考我剛才上傳的 Excel 樣板檔案格式，使用 /skill-creator 幫我建立包含 templates 資料夾的 Skill。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Office_Workflow_03_Customer_Quotation`，並在其中建立名為 `templates` 的子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 內容儲存於根目錄；將 [quotation-template.xlsx](./templates/quotation-template.xlsx) 內容儲存至 `templates/` 目錄中。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

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
