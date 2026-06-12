# Level 4 範例：智能會議排程秘書（第四階：自動化專家）

本階段重點在於結合「程式碼執行 (Code Execution)」，讓 Skill 載入並運行放置在 `scripts/` 目錄底下的自訂腳本（如 Python），以進行高精準度的運算、複雜圖表渲染或文件批量處理。

## 📖 範例說明
當您輸入各專案的名稱與耗費工時後，AI 會自動將資料整理為標準的 JSON 格式，並呼叫內建的程式碼執行工具運行 Python 腳本，繪製出極具視覺效果的工時佔比 ASCII 圖表與總工時加總報告。

## 📁 實體自訂 Skill 結構
此範例在手動建立時，包含以下檔案與資料夾結構：
```text
Level4_Meeting_Secretary/
├── SKILL.md
└── scripts/
    └── calculate_hours.py    # 工時分析統計的 Python 實體腳本
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）
1. 先將 [calculate_hours.py](./scripts/calculate_hours.py) 檔案上傳至 Claude 對話中。
2. 直接下指令：
   > 「`我想建立一個會議秘書 Skill。請幫我把 calculate_hours.py 放入 scripts 資料夾，並使用 /skill-creator 建立包含 scripts 的自訂 Skill。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在電腦中建立新資料夾 `Level4_Meeting_Secretary`，並在其中建立名為 `scripts` 的子資料夾。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 儲存於根目錄；將 [calculate_hours.py](./scripts/calculate_hours.py) 儲存至 `scripts/` 目錄中。
3. 前往 Claude 的 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

## 🧪 測試與驗證

確認 Skill 建立成功後，您可以開啟新對話並使用以下範例 Prompt 來測試其效果：

**測試 Prompt：**
```text
我今天處理了這些事情，幫我產出工時統計報告：
- 撰寫產品規格書花了我 3 小時。
- 跟前端工程師對 API 介面花了 2 小時。
- 修復線上購物車 Bug 花了 4 小時。
- 寫週報跟回覆信件花了 1 小時。
```

**預期效果：**
Claude 將會自動啟用該 Skill，並：
1. 將輸入的資料轉換為 JSON 結構：
   ```json
   [
     {"name": "撰寫產品規格書", "hours": 3},
     {"name": "對 API 介面", "hours": 2},
     {"name": "修復購物車 Bug", "hours": 4},
     {"name": "週報與回信", "hours": 1}
   ]
   ```
2. 透過 Code Execution 執行 `scripts/calculate_hours.py` 腳本，將 JSON 資料寫入腳本。
3. 輸出該腳本產生的 ASCII 百分比長條圖與總工時統計報告。

---

← [返回 Skills 主頁](../../README.md)

