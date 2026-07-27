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

1. 先將 [report-template.md](./templates/report-template.md) 檔案上傳至 Claude 對話中。
2. 直接下指令：
   > 「`我想建立一個每日報工 Skill。請參考我剛才上傳的樣板檔案格式，使用 /skill-creator 幫我建立包含 templates 資料夾的 Skill。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
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

