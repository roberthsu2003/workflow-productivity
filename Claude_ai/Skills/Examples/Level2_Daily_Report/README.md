# Level 2 範例：個人化每日報工助手（第二階：創作者）

本階段重點在於學會如何使用樣板檔案（Templates）來限制 AI 的輸出格式。這可使多名同仁使用同一個 Skill 時，產出的日報格式完全一致。

## 📖 範例說明
每天下班前，您只需丟入當天隨手寫下的雜亂工作筆記，AI 就會依照公司標準格式將其重新排版，整理成條列式、分項清楚且專業的日報。

## 📁 實體自訂 Skill 結構
此範例在手動建立時，包含以下檔案與資料夾結構：
```text
Level2_Daily_Report/
├── SKILL.md
└── templates/
    └── report-template.md  # 儲存日報標準 Markdown 樣板
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/create-skill` 技能（自動建立）
1. 先將 [report-template.md](./templates/report-template.md) 檔案上傳至 Claude 對話中。
2. 直接下指令：
   > 「`我想建立一個每日報工 Skill。請參考我剛才上傳的樣板檔案格式，使用 /create-skill 幫我建立包含 templates 資料夾的 Skill。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Level2_Daily_Report`，並在其中建立名為 `templates` 的子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 內容儲存於根目錄；將 [report-template.md](./templates/report-template.md) 內容儲存至 `templates/` 目錄中。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

---

← [返回 Skills 主頁](../../README.md)
