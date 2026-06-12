# 延伸練習 3：每日工作日誌產生器（第二階：創作者）

這是第二階的延伸實作練習。本階段的重點在於學會如何使用樣板檔案（Templates）來限制 AI 的輸出格式。

## 📖 範例說明

這個 Skill 會將您一整天隨手寫下的雜亂工作紀錄與零散短句，重新分類整理，並依據公司標準樣板產出結構完整、主管易讀的每日工作日報與三行重點摘要。

## 📁 實體自訂 Skill 結構

此範例在手動建立時，包含以下檔案與資料夾結構：
```text
Office_Workflow_03_Daily_Report/
├── SKILL.md
└── templates/
    └── daily-report-template.md  # 儲存日報標準 Markdown 樣板
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）
1. 先將 [daily-report-template.md](./templates/daily-report-template.md) 檔案上傳至 Claude 對話中。
2. 直接下指令：
   > 「`我想建立一個每日工作日誌 Skill。請參考我剛才上傳的樣板檔案格式，使用 /skill-creator 幫我建立包含 templates 資料夾的 Skill。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Office_Workflow_03_Daily_Report`，並在其中建立名為 `templates` 的子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 內容儲存於根目錄；將 [daily-report-template.md](./templates/daily-report-template.md) 內容儲存至 `templates/` 目錄中。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

## 🧪 測試與驗證

確認 Skill 建立成功後，您可以開啟新對話並使用以下範例 Prompt 來測試其效果：

**測試 Prompt：**
```text
請幫我整理今天的日報：
「早上修了報價單（完成），下午跟設計討論新版頁面（進行中，明天要看設計稿），財務那邊的預算審查一直還沒回，明天要去追合約還有準備週會的資料。」
```

**預期效果：**
Claude 將會自動啟用該 Skill，並依據 `templates/daily-report-template.md` 的結構，將上述內容分類整理為「今日完成」、「進行中」、「阻礙與需求」、「明日計畫」，最後附上「給主管的 3 行摘要」。

---

← [返回 Skills 主頁](../README.md)
