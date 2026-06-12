# 延伸練習 4：會議紀錄轉行動計畫助手（第二階：創作者）

這是第二階的延伸實作練習。本階段的重點在於學會如何使用 Excel 樣板檔案（Templates）來限制 AI 的輸出格式，並產出實體 Excel 檔案供下載。

## 📖 範例說明

這個 Skill 可以將長篇會議逐字稿、會議摘要或討論隨記，快速整理出會議決議、負責人、期限、風險提示，並套用標準 Excel 樣板，產出格式美觀的行動計畫試算表（`.xlsx`）供下載。

## 📁 實體自訂 Skill 結構

此範例在手動建立時，包含以下檔案與資料夾結構：
```text
Office_Workflow_04_Meeting_Action_Plan/
├── SKILL.md
└── templates/
    └── action-plan-template.xlsx  # 儲存行動計畫標準 Excel 樣板
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）
1. 先將 [action-plan-template.xlsx](./templates/action-plan-template.xlsx) 檔案上傳至 Claude 對話中。
2. 直接下指令：
   > 「`我想建立一個會議紀錄轉行動計畫 Skill。請參考我剛才上傳的 Excel 樣板檔案格式，使用 /skill-creator 幫我建立包含 templates 資料夾的 Skill。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Office_Workflow_04_Meeting_Action_Plan`，並在其中建立名為 `templates` 的子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 內容儲存於根目錄；將 [action-plan-template.xlsx](./templates/action-plan-template.xlsx) 內容儲存至 `templates/` 目錄中。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

## 🧪 測試與驗證

確認 Skill 建立成功後，您可以開啟新對話並使用以下範例 Prompt 來測試其效果：

**測試 Prompt：**
```text
請幫我將這段會議對話整理成行動計畫：
「大家下午好。今天主要討論新產品上線的準備。行銷部分，小美提到下週二前要完成新聞稿初稿。技術部分，大雄說購物車的功能基本上測完了，但金流 API 還有點問題，需要他在這週五下班前跟金流廠商確認。另外，我們一致決定下週五早上 10 點進行最後上線審查會議，這部分需要小美幫忙訂會議室和發通知。」
```

**預期效果：**
Claude 將會自動啟用該 Skill，並依據 `templates/action-plan-template.xlsx` 的格式，自動呼叫 Python 程式碼，將對話內容整理並寫入成可供下載的 `.xlsx` 檔案，其中包含會議決議、負責人任務與期限、風險提醒。

---

← [返回 Skills 主頁](../README.md)
