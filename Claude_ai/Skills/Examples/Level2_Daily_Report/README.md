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

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）
> 實際測試-無誤

此方式包含以下兩種自動建立的情境與對話引導：

#### 方案 1：直接提供範本檔案建立
1. **上傳樣板**：先將 [report-template.md](./templates/report-template.md) 檔案上傳至 Claude 對話中。
2. **下指令建立**：直接對 Claude 輸入以下指令：
   > 「`我想建立一個每日報工 Skill。請參考我剛才上傳的樣板檔案格式，使用 /skill-creator 幫我建立包含 templates 資料夾的 Skill。`」
3. **下載與安裝**：
   * Claude 執行完成後，會提供一個自訂技能資料夾的下載包（通常是 ZIP 壓縮檔）。請將其下載並解壓縮。
   * 前往 Claude 網頁左下角個人頭像 ➔ **Settings** ➔ **Skills**。
   * 點擊 **Add Custom Skill** 上傳此解壓縮後的資料夾。

#### 方案 2：先完成任務對話，再打包成技能
1. **上傳樣板與對話測試**：
   * 先將 [report-template.md](./templates/report-template.md) 樣板檔案上傳至對話中。
   * 貼入當天隨手寫下的雜亂工作筆記，請 Claude 協助依樣板排版整理。
   * 檢查 Claude 輸出的日報格式是否符合預期，若有不完美之處可繼續對話修正，直到產出的格式完全滿意。
2. **下指令進行打包**：
   * 當結果完全滿意後，直接輸入指令：
     > 「`請參考剛才我們對話的整理邏輯與格式，使用 /skill-creator 幫我將這個功能打包建立為一個自訂技能。`」
3. **下載與安裝**：
   * Claude 執行完成後，下載其產出的自訂技能資料夾（或 ZIP 檔）並解壓縮。
   * 前往 Claude 網頁左下角個人頭像 ➔ **Settings** ➔ **Skills**。
   * 點擊 **Add Custom Skill** 上傳該解壓縮後的資料夾即可完成安裝。

### ✍️ 方式 B：手動複製檔案（手動建立）
> 實際測試-無誤
1. 在電腦中建立新資料夾 `Level2_Daily_Report`，並在其中建立名為 `templates` 的子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 內容儲存於根目錄；將 [report-template.md](./templates/report-template.md) 內容儲存至 `templates/` 目錄中。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

### 💡 方式 C：在終端機中部署（適用於 Claude Code / 終端機代理）
若您是在終端機（如 Claude Code）環境中使用，可以直接將本範例的整個資料夾（包含根目錄的 `SKILL.md` 檔案與相關子目錄）複製或移動到 `/mnt/skills/user/` 下。例如：
```bash
cp -r Level2_Daily_Report/ /mnt/skills/user/Level2_Daily_Report
```
複製完成後即可在對話中直接使用該自訂技能。

## 🧪 測試與驗證

確認 Skill 建立成功後，您可以開啟新對話並使用以下範例 Prompt 來測試其效果：

**測試 Prompt（雜亂的工作筆記）：**
```text
今天的工作筆記：
- 早上花了三個小時在處理資料庫連線超時的問題，改了 connection pool 的參數後終於正常了，進度 100%。這大概是今天最主要的事情。
- 下午跟 QA 團隊對測試案例，有些關於付費流程的邏輯怪怪的，有跟產品經理提出討論，這件事算完成了。
- 另外，今天也把首頁的 banner 圖片輪播速度調慢了（主管交代的，100% 完成）。
- 還有一個很嚴重的問題：金流串接那邊一直報簽章錯誤（Signature Verification Failed），這部分我試過好幾個 method 都不行，現在卡關了，急需後端資深工程師小明幫忙看，不然明天沒辦法測試（目前進度 30%，卡住了）。
- 明天的話，希望可以先跟小明把金流簽章問題解掉。接著要把購物車的單元測試寫完，下午要開每週例會。
```

**預期效果：**
Claude 將會自動啟用該 Skill，並將上述雜亂的內容，**完全依照** `templates/report-template.md` 的樣板結構，整理成格式一致的專業日報。

---

← [返回 Skills 主頁](../../README.md)

