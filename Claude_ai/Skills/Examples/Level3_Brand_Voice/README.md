# Level 3 範例：品牌語氣稽核員（第三階：整合者）

本階段重點在於學會掛載「外部知識庫檔案（References）」與「Excel 樣板（Templates）」，並透過「程式碼執行 (Code Execution)」產出實體 `.xlsx` 檔案供使用者下載。

## 📖 範例說明
這個 Skill 會參考您放置於 `references/` 目錄下的公司品牌指南，稽核您輸入的宣傳文案。若稽核完畢，AI 會呼叫 Python 程式碼載入 `templates/` 資料夾底下的 Excel 樣板，將稽核結果寫入，並輸出一個實體 Excel 檔（`.xlsx`）供下載。

## 📁 實體自訂 Skill 結構
此範例在手動建立時，包含以下檔案與資料夾結構：
```text
Level3_Brand_Voice/
├── SKILL.md
├── templates/
│   └── brand-voice-audit-template.xlsx  # 儲存稽核報告 Excel 樣板
├── references/
│   └── brand-book.md                    # 品牌規範參考手冊
└── assets/
    └── company-logo.png                 # 公司的 Logo 圖片檔案
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）
1. 先將 [brand-voice-audit-template.xlsx](./templates/brand-voice-audit-template.xlsx) 樣板與 [brand-book.md](./references/brand-book.md) 檔案上傳至 Claude 對話中。
2. 直接下指令：
   > 「`我想建立一個品牌語氣稽核 Skill。請參考我剛才上傳的 brand-book.md 規範與 Excel 樣板，使用 /skill-creator 幫我建立包含 references 和 templates 資料夾的 Skill。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Level3_Brand_Voice`，並建立 `references`、`templates` 與 `assets` 三個子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 儲存於根目錄；將 [brand-voice-audit-template.xlsx](./templates/brand-voice-audit-template.xlsx) 儲存至 `templates/` 目錄；將 [brand-book.md](./references/brand-book.md) 儲存至 `references/` 目錄；將 Logo 圖片儲存為 `assets/company-logo.png`。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

## 🧪 測試與驗證

確認 Skill 建立成功後，您可以開啟新對話並使用以下範例 Prompt 來測試其效果：

**測試 Prompt（不合規範的文案）：**
```text
請幫我稽核這段文案：
「我們最近推出了全新的 Custom Skills 功能，只要使用我們的 Connectors 就能輕鬆把各種服務串起來！超方便，保證讓你的工作速度飛天，趕快來試用！」
```

**預期效果：**
Claude 將會自動啟用該 Skill，並：
1. 進行品牌語氣分析，判定該文案使用「飛天」、「超方便」等詞彙過於誇大且不夠專業，且誤用了英文專有名詞「Custom Skills」與「Connectors」。
2. 自動呼叫程式碼執行功能，利用 Python 的 `openpyxl` 庫載入並讀取 `templates/brand-voice-audit-template.xlsx`。
3. 將稽核狀態（❌ 需修改）、稽核細節與建議修正文案填入 Excel，並產出一個包含完整稽核資料的 `.xlsx` 檔案供使用者點擊下載。

---

← [返回 Skills 主頁](../../README.md)
