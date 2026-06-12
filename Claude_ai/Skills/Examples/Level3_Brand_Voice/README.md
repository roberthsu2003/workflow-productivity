# Level 3 範例：品牌語氣稽核員（第三階：整合者）

本階段重點在於學會掛載「外部知識庫檔案（References）」與「靜態品牌資源（Assets）」。

## 📖 範例說明
這個 Skill 會參考您放置於 `references/` 目錄下的公司品牌指南，稽核您輸入的宣傳文案。若稽核完畢，輸出的報告頂部會透過相對路徑自動帶入放在 `assets/` 目錄下的公司 Logo 圖片。

## 📁 實體自訂 Skill 結構
此範例在手動建立時，包含以下檔案與資料夾結構：
```text
Level3_Brand_Voice/
├── SKILL.md
├── references/
│   └── brand-book.md         # 品牌規範參考手冊
└── assets/
    └── company-logo.png      # 公司的 Logo 圖片檔案
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）
1. 先將 [brand-book.md](./references/brand-book.md) 檔案與 Logo 圖片上傳至 Claude 對話中。
2. 直接下指令：
   > 「`我想建立一個品牌語氣稽核 Skill。請將這張 Logo 圖片放入 assets，並參考我剛才上傳的 brand-book.md 規範內容，使用 /skill-creator 幫我建立包含 references 和 assets 資料夾的 Skill。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Level3_Brand_Voice`，並建立 `references` 與 `assets` 兩個子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 儲存於根目錄；將 [brand-book.md](./references/brand-book.md) 儲存至 `references/` 目錄；將 Logo 圖片儲存為 `assets/company-logo.png`。
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
1. 在稽核報告的最上方置中顯示公司 Logo：`![公司 Logo](assets/company-logo.png)`。
2. 進行品牌語氣分析，判定該文案使用「飛天」、「超方便」等詞彙過於誇大且不夠專業，且誤用了英文專有名詞「Custom Skills」與「Connectors」。
3. 給出「❌ 需修改」的結論，並提供修改與重寫建議（例如將英文專有名詞替換為「自訂技能」與「連接器」）。

---

← [返回 Skills 主頁](../../README.md)

