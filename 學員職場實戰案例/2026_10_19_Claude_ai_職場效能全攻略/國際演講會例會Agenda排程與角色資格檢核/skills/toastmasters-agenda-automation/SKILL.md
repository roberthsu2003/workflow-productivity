---
name: toastmasters-agenda-automation
description: "國際演講會（Toastmasters）例會 Agenda 排程、Pathways 專案轉譯、評審資格審查、歷史輪替防重複與動態時間推算全自動化"
---

# Toastmasters Agenda 排程與資格檢核自動化技能

本技能提供標準化、合規且防呆的國際演講會例會 Agenda 排課作業流程。

## 🎯 核心能力

1. **請假名單剔除**：讀取出席調查，排除標註 Absent 會員。
2. **Pathways 專案轉譯**：將會員教育進度轉譯為標準縮寫格式（如 `PM 4-2`）。
3. **評審資歷門檻檢核**：IE / GE 必須已完成 Level 1（進度在 Level 2 以上或已完成 L1P4）。
4. **近 5 場防重複與公平輪替**：向左比對前 5 場紀錄，落實防重複與最久未任優先原則。
5. **單人單役檢驗**：除固定 SAA/President 外，每人限任 1 職（講者亦算 1 役）。
6. **動態時間滾動推算**：以 19:10 為基準，每個節目加 1 分鐘緩衝累加，超過 21:15 觸發超時預警。
7. **雙成果交付**：輸出出版級三欄位 Agenda 表格與 8 大規則稽核清單。

## 🛠️ 標準調用指令（RTCCF 規格）

當使用者提供 `Signup Sheet.xlsx` 與 `Member Speech Planning.xlsx` 時，請嚴格依照 [**`4-2_AI產出之RTCCF排程與資格檢核提示詞.md`**](../../4-2_AI產出之RTCCF排程與資格檢核提示詞.md) 中規範之終極 RTCCF 規則執行。
