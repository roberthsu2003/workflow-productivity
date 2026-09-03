# Level 3 範例：品牌語氣稽核員（第三階：整合者）

> **🎯 本階核心目標**  
> 運用 Claude AI 的「**程式碼執行 (Code Execution)**」能力，讓 Skill 自動執行 Python 腳本！  
> 整合「**外部規範 (references/)**」、「**報表樣板 (templates/)**」與「**品牌圖片 (assets/)**」，自動完成文案稽核並將品牌 Logo 寫入 Excel，產出可直接交付的實體 `.xlsx` 報告。

---

## 📖 範例運作機制

```mermaid
flowchart LR
    A[使用者輸入宣傳文案] --> B[讀取 references/<br>brand-book.md 規範]
    B --> C[進行語氣與禁忌詞稽核]
    C --> D[啟用 Code Execution<br>執行 Python openpyxl]
    D --> E[讀取 templates/ 樣板<br>+ 插入 assets/ Logo]
    E --> F[產出並下載<br>品牌化 Excel 報告]
```

這個 Skill 的自動化作業流程如下：
1. **規範比對**：參考 `references/brand-book.md` 中的品牌規範，逐句檢驗文案的語氣、風格與禁用詞彙。
2. **自動化處理**：AI 自動執行 Python 程式碼，載入 `templates/brand-voice-audit-template.xlsx` 樣板。
3. **視覺整合**：呼叫 `openpyxl.drawing.image.Image` 將 `assets/company-logo.jpeg` 品牌 Logo 插入至 Excel 頂部表頭（Cell A1）。
4. **產出交付**：將診斷結果、評等與建議改寫文案填入指定欄位，生成帶有企業品牌識別的完整實體 Excel 檔供下載。

---

## 📁 資料夾與檔案結構

| 檔案 / 資料夾路徑 | 類型 | 職責與用途 |
| :--- | :---: | :--- |
| 📄 [`SKILL.md`](./SKILL.md) | 主設定檔 | 定義角色、稽核規則與 Python openpyxl 插入圖片的 SOP 指令 |
| 📁 `templates/` | 範本目錄 | 存放空白的稽核報告樣板 [`brand-voice-audit-template.xlsx`](./templates/brand-voice-audit-template.xlsx) |
| 📁 `references/` | 參考規範 | 存放企業品牌標準手冊 [`brand-book.md`](./references/brand-book.md) |
| 📁 `assets/` | 靜態資產 | 存放企業標準圖檔 [`company-logo.jpeg`](./assets/company-logo.jpeg)（嵌入 Excel 表頭） |

```text
Level3_Brand_Voice/
├── SKILL.md                             # 核心技能指引（含 Python 執行規範）
├── templates/
│   └── brand-voice-audit-template.xlsx  # 稽核報告 Excel 樣板
├── references/
│   └── brand-book.md                    # 品牌規範參考手冊
└── assets/
    └── company-logo.jpeg                 # 公司 Logo 圖檔（嵌入表頭 A1）
```

---

## 🛠️ 安裝與建置方式

你可以選擇以下三種方式之一來建立並啟用此技能：

### 💡 方式 A：使用內建 `/skill-creator` 技能（推薦・自動建置）

> [!TIP]
> 請先確認已在 Claude Settings 中開啟 **Code execution and file creation** 功能。

#### 方案 1：直接上傳檔案並下指令建立
1. **上傳檔案**：將以下 3 個檔案同時上傳至 Claude 對話中：
   * 樣板：[`brand-voice-audit-template.xlsx`](./templates/brand-voice-audit-template.xlsx)
   * 規範：[`brand-book.md`](./references/brand-book.md)
   * 圖片：[`company-logo.jpeg`](./assets/company-logo.jpeg)

2. **下達建置指令**：直接複製並貼上以下 Prompt：

   ```text
   我想建立一個品牌語氣稽核 Skill。
   請參考我剛才上傳的 brand-book.md 規範、Excel 樣板與 company-logo.jpeg 圖檔，
   使用 /skill-creator 幫我建立包含 references、templates 和 assets 資料夾的 Skill。

   請在 SKILL.md 中明確指定：
   執行 Python (Code Execution) 寫入 Excel 報表時，
   必須使用 openpyxl.drawing.image.Image 將 assets/company-logo.jpeg 圖片插入置於 Excel 試算表頂端表頭位置 (Cell A1)。
   ```

3. **自動完成與啟用**：
   * Claude 執行完畢後會自動在帳號中安裝並生效此 Skill。
   * *(可選備份)*：可下載 Claude 提供的 ZIP 封裝包保存於本機。

---

#### 方案 2：先完成任務對話，再一鍵打包成技能
1. **實測任務對話**：
   * 將上述 3 個檔案上傳至對話中。
   * 輸入一段公司宣傳文案，請 Claude 先進行文案稽核，並呼叫 Python 填寫 Excel 樣板及嵌入 Logo。
   * 下載檢查 Excel 成果，若 Logo 位置或欄位需調整，繼續與 Claude 對話微調至完全滿意。

2. **下一鍵打包指令**：成果滿意後，直接輸入：

   ```text
   請參考剛才我們對話的稽核邏輯、Excel 輸出格式與公司 Logo 圖片，
   使用 /skill-creator 幫我將這個功能打包建立為包含 references, templates 與 assets 的自訂技能。

   請確保 SKILL.md 中寫入：
   用 openpyxl 將 assets/company-logo.jpeg 嵌入至 Excel 試算表頂端表頭 (Cell A1) 的 SOP 指令。
   ```

3. **自動生效**：Claude 打包完成後，此 Skill 即直接於當前帳號中啟用。

---

### ✍️ 方式 B：手動複製檔案（網頁手動上傳）

1. **建立本機目錄**：在電腦中建立 `Level3_Brand_Voice` 資料夾，並於其下建立 `references`、`templates` 與 `assets` 三個子目錄。
2. **放置對應檔案**：
   * 根目錄：放入 [`SKILL.md`](./SKILL.md)
   * `templates/`：放入 [`brand-voice-audit-template.xlsx`](./templates/brand-voice-audit-template.xlsx)
   * `references/`：放入 [`brand-book.md`](./references/brand-book.md)
   * `assets/`：放入 [`company-logo.jpeg`](./assets/company-logo.jpeg)
3. **上傳至 Claude**：前往 Claude 網頁版 **Settings** ➔ **Capabilities** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

---

### 💻 方式 C：終端機部署（適用於 Claude Code）

若在 Claude Code 終端機環境中，可直接將本專案目錄複製至 Skill 系統路徑：

```bash
cp -r Level3_Brand_Voice/ /mnt/skills/user/Level3_Brand_Voice
```

複製完成後，終端機對話環境將自動載入該技能。

---

## 🧪 測試與驗證

安裝完成後，開啟新對話並輸入以下測試文案進行驗證：

### 📥 測試 Prompt（含不合格語氣的文案）
```text
請幫我稽核這段文案：
「我們最近推出了全新的 Custom Skills 功能，只要使用我們的 Connectors 就能輕鬆把各種服務串起來！超方便，保證讓你的工作速度飛天，趕快來試用！」
```

---

### 🎯 預期執行成果

Claude 將自動識別並調用本 Skill，完成以下三階段任務：

* **🔍 階段 1・品牌語氣診斷**  
  比對規範後判定：「飛天」、「超方便」等用語過於誇張煽情且不符專業調性；並指出「Custom Skills」與「Connectors」等專有名詞誤用。
* **🐍 階段 2・Python 自動化處理**  
  自動呼叫 Code Execution，以 `openpyxl` 載入 `templates/brand-voice-audit-template.xlsx`，並成功在 Cell A1 嵌入 `assets/company-logo.jpeg` Logo 圖檔。
* **📊 階段 3・產出實體報告檔**  
  填入審核狀態（❌ 需修改）、扣分原因與建議修訂版本，產出具備品牌 Logo 的專屬 `.xlsx` 檔案提供即時點擊下載。

---

[← 返回 Skills 主頁](../../README.md)

