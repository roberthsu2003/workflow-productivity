# GWorkspace：用 Plugin 產出真實格式檔案

> 🔵 **方案需求**：Plus 起（Spreadsheets、Presentations、Google Drive、Gmail plugin）。

這一章練的是 **Codex 讀寫真實 Office 格式檔案**的能力——`.xlsx`、`.pptx`、`.docx`、`.png`，而不只是 Markdown。

---

## 🎯 五個次章節

| 次章節 | 用哪個 plugin | 輸入 → 輸出 |
| :--- | :--- | :--- |
| [01. 髒資料任務追蹤表](./01_Sheets_Task_Tracker/README.md) | Spreadsheets | 髒 `.xlsx` → 乾淨的 `.xlsx` |
| [02. 營運回顧簡報](./02_Presentations_Report/README.md) | Presentations | 數據 + 圖 → `.pptx` |
| [03. 會議手記整理](./03_Docs_Meeting_Notes/README.md) | Google Drive / Docs | 凌亂 `.docx` → 正式紀錄 |
| [04. 採購通知草稿](./04_Gmail_Draft_Dispatch/README.md) | Gmail + Spreadsheets | 簽核單 + 明細 → 郵件草稿 |
| [05. Drive 跨檔稽核](./05_Drive_Cross_Analysis/README.md) | Google Drive | 多檔交叉比對 → 稽核報告 |

---

## 📂 示範檔案（真實格式）

| 檔案 | 格式 | 埋了什麼 |
| :--- | :---: | :--- |
| `2026年度各部門待辦事項原始清單.xlsx` | xlsx | **期限欄混用 4 種格式**、優先度中英混雜、狀態有未定義值 |
| `2026_上半年營運回顧_示範簡報.pptx` | pptx | 6 頁，含「資料說明」頁提醒中區 6 月缺漏 |
| `2026_上半年單量趨勢圖.png` | png | 折線圖，供圖片輸入練習 |
| `2026_Q3營運檢討會_會議手記.docx` | docx | **手寫凌亂筆記**，含「待整理」段落 |
| `採購核准單_PO-2026-0915.docx` | docx | 三級簽核完成的正式單據 |
| `採購料件明細表_PO-2026-0915.csv` | csv | 5 項料件，含合計列 |
| `受評標的_財務摘要_2023-2026E.xlsx` | xlsx | 供 [Investing 章節](../Investing/README.md)使用 |

> 這些檔案由 [`tools/generate_office_files.py`](../../tools/README.md) 產生，可重現。

---

## 🔑 核心觀念：Codex 產檔與 Claude 的差異

> [!IMPORTANT]
> | | Claude | Codex |
> | :--- | :--- | :--- |
> | 輸入 | **上傳**檔案到對話 | **直接讀** workspace 裡的檔案 |
> | 產出 | 產生後**下載** | **直接寫進**你的資料夾 |
> | 後續處理 | 要再上傳一次 | 下一個 task 直接接手 |
> | 版本控管 | 無 | **`git diff` 看得到** |
> | 風險 | 低 | **可能覆蓋既有檔案** |
>
> **所以每個 task 都要明確指定輸出路徑，並先 `git commit`。**

---

## ⚠️ 產檔任務的共通限制

把這幾條寫進每個 task 的 `Scope`：

```markdown
## Scope
- **不要修改原始檔案。** 產出寫在 `output/` 目錄。
- 檔案已存在時**不要覆蓋**，改用 `_v2` 後綴並在回報中說明。
- 數字必須與來源完全一致，不可四捨五入後再拿去計算。
- **資料缺漏時標示「資料缺漏」，不可用 0 或推估值填補。**
```

---

## 🔄 與 Claude GWorkspace 章節的對照

| Claude | Codex | 差異 |
| :--- | :--- | :--- |
| `docx` skill | **Google Drive / Docs plugin** | 相近 |
| `xlsx` skill | **Spreadsheets plugin** | 相近 |
| `pptx` skill | **Presentations plugin** | 相近 |
| Gmail Connector | **Gmail plugin** | 相近 |
| — | **檔案直接寫進 workspace** | ➕ 可 `git diff`、可被下一個 task 接手 |

---

← [返回上層：Skills](../README.md) ｜ [返回索引](../../README.md)
