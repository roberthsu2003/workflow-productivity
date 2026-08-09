# Level 3 範例：品牌語氣稽核員（第三階：整合者）

本階段重點在於學會掛載「外部知識庫檔案（References）」與「Excel 樣板（Templates）」，並透過「程式碼執行 (Code Execution)」產出實體 `.xlsx` 檔案供使用者下載。

## 📖 範例說明
這個 Skill 會參考您放置於 `references/` 目錄下的公司品牌指南，稽核您輸入的宣傳文案。稽核完畢後，AI 會透過 Python 程式碼載入 `templates/` 資料夾底下的 Excel 樣板，將稽核結果寫入，**並自動將 `assets/company-logo.png` 品牌 Logo 嵌入至試算表頂部**，最終輸出一個具備公司品牌識別的實體 Excel 檔（`.xlsx`）供下載。

## 📁 實體自訂 Skill 結構
此範例在手動建立時，包含以下檔案與資料夾結構：
```text
Level3_Brand_Voice/
├── SKILL.md                             # 採用 RTCCF 提示詞架構的主 Skill 檔
├── templates/
│   └── brand-voice-audit-template.xlsx  # 儲存稽核報告 Excel 樣板
├── references/
│   └── brand-book.md                    # 品牌規範參考手冊
└── assets/
    └── company-logo.png                 # 公司的 Logo 圖片檔案（將嵌入 Excel 表頭）
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）

此方式包含以下兩種自動建立的情境與對話引導：

#### 方案 1：直接提供範本檔案與參考文件建立
1. **上傳檔案**：先將 [brand-voice-audit-template.xlsx](./templates/brand-voice-audit-template.xlsx) 樣板與 [brand-book.md](./references/brand-book.md) 檔案上傳至 Claude 對話中。
2. **下指令建立**：直接對 Claude 輸入以下指令：
   > 「`我想建立一個品牌語氣稽核 Skill。請參考我剛才上傳的 brand-book.md 規範與 Excel 樣板，使用 /skill-creator 幫我建立包含 references 和 templates 資料夾的 Skill。`」
3. **下載與安裝**：
   * Claude 執行完成後，會提供一個自訂技能資料夾的下載包（通常是 ZIP 壓縮檔）。請將其下載並解壓縮。
   * 前往 Claude 網頁左下角個人頭像 ➔ **Settings** ➔ **Skills**。
   * 點擊 **Add Custom Skill** 上傳此解壓縮後的資料夾。

#### 方案 2：先完成任務對話，再打包成技能
1. **上傳相關資源與對話測試**：
   * 先將 [brand-voice-audit-template.xlsx](./templates/brand-voice-audit-template.xlsx) 樣板與 [brand-book.md](./references/brand-book.md) 檔案上傳至對話中。
   * 輸入一段公司宣傳文案，請 Claude 依據上傳的品牌指引進行語氣與禁忌詞稽核，並呼叫 Python 寫入 Excel 樣板中。
   * 檢查 Claude 產出下載的 Excel 內容是否符合預期，若需要微調可以繼續對話，直到產出的格式完全滿意。
2. **下指令進行打包**：
   * 當結果完全滿意後，直接輸入指令：
     > 「`請參考剛才我們對話的稽核邏輯與 Excel 輸出格式，使用 /skill-creator 幫我將這個功能打包建立為一個自訂技能。`」
3. **下載與安裝**：
   * Claude 執行完成後，下載其產出的自訂技能資料夾（或 ZIP 檔）並解壓縮。
   * 前往 Claude 網頁左下角個人頭像 ➔ **Settings** ➔ **Skills**。
   * 點擊 **Add Custom Skill** 上傳該解壓縮後的資料夾即可完成安裝。

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Level3_Brand_Voice`，並建立 `references`、`templates` 與 `assets` 三個子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 儲存於根目錄；將 [brand-voice-audit-template.xlsx](./templates/brand-voice-audit-template.xlsx) 儲存至 `templates/` 目錄；將 [brand-book.md](./references/brand-book.md) 儲存至 `references/` 目錄；將 Logo 圖片儲存為 `assets/company-logo.png`。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

### 💡 方式 C：在終端機中部署（適用於 Claude Code / 終端機代理）
若您是在終端機（如 Claude Code）環境中使用，可以直接將本範例的整個資料夾（包含根目錄的 `SKILL.md` 檔案與相關子目錄）複製或移動到 `/mnt/skills/user/` 下。例如：
```bash
cp -r Level3_Brand_Voice/ /mnt/skills/user/Level3_Brand_Voice
```
複製完成後即可在對話中直接使用該自訂技能。

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
2. 自動呼叫程式碼執行功能，利用 Python 的 `openpyxl` 庫讀取 `templates/brand-voice-audit-template.xlsx` 樣板，並使用 `openpyxl.drawing.image.Image` 將 `assets/company-logo.png` 品牌 Logo 寫入表頭區域。
3. 將稽核狀態（❌ 需修改）、稽核細節與建議修正文案填入 Excel，產出一份附帶品牌 Logo 的 `.xlsx` 檔案供下載。

---

← [返回 Skills 主頁](../../README.md)
