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

此方式包含以下兩種自動建立的情境與對話引導：

#### 方案 1：直接提供範本檔案建立
1. 先將 [action-plan-template.xlsx](./templates/action-plan-template.xlsx) 檔案上傳至 Claude 對話中。
2. 直接下指令：
   > 「`我想建立一個會議紀錄轉行動計畫 Skill。請參考我剛才上傳的 Excel 樣板檔案格式，使用 /skill-creator 幫我建立包含 templates 資料夾的 Skill。`」

#### 方案 2：先完成任務對話，再打包成技能
1. 在對話中先上傳您的行動計畫樣板並貼上會議記錄，讓 Claude 幫您成功摘要並產出一次符合預期的 Excel 行動計畫表。
2. 隨後直接對 Claude 下指令：
   > 「`請參考剛才我們對話的決議與行動項目整理邏輯，以及 Excel 行動計畫表的填寫格式，使用 /skill-creator 幫我將這個功能打包建立為一個自訂技能。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Office_Workflow_04_Meeting_Action_Plan`，並在其中建立名為 `templates` 的子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 內容儲存於根目錄；將 [action-plan-template.xlsx](./templates/action-plan-template.xlsx) 內容儲存至 `templates/` 目錄中。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

### 💡 方式 C：在終端機中部署（適用於 Claude Code / 終端機代理）
若您是在終端機（如 Claude Code）環境中使用，可以直接將本範例的整個資料夾（包含根目錄的 `SKILL.md` 檔案與相關子目錄）複製或移動到 `/mnt/skills/user/` 下。例如：
```bash
cp -r Office_Workflow_04_Meeting_Action_Plan/ /mnt/skills/user/Office_Workflow_04_Meeting_Action_Plan
```
複製完成後即可在對話中直接使用該自訂技能。

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
