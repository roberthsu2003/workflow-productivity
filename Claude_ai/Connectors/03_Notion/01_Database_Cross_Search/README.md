# 📊 實戰 1：跨資料庫自然語言檢索與關聯比對 (Relational Cross-Search)

> **所屬章節**：[Notion 連接器實戰](../README.md) ➔ **練習 1**  
> **運作模式**：💬 **一般對話模式（Chat Prompts）**  
> **預計實作時間**：10 分鐘  
> **所需連接器**：🔹 **Notion**（確保已授權連線）

---

## 🎯 任務目標

學習如何讓 Claude 穿透 Notion 工作區，跨「PRD 需求庫」與「Sprint 任務看板」兩張獨立資料庫進行跨表關聯查詢，篩選出 Sprint-24 中屬於 P0 級的關鍵需求，並揪出造成上線危機的阻塞任務（Blocker）。

---

## 📥 專屬測試偽資料庫與雙軌實測機制

本練習在專屬目錄中提供兩張標準 CSV 資料庫：

| 檔案類型 | 檔案名稱（點擊檢視/下載） | 說明 |
| :---: | :---| :---|
| 📊 **PRD 庫** | [**星橋科技_產品需求規格庫_PRD.csv**](./sample_files/星橋科技_產品需求規格庫_PRD.csv) | 包含 PRD-01~08 之功能名稱、優先級、Owner 與目標 Sprint。 |
| 📋 **任務看板** | [**團隊任務與衝刺看板_Sprint_Tasks.csv**](./sample_files/團隊任務與衝刺看板_Sprint_Tasks.csv) | 包含 15 項工程任務之狀態、估時、負責人與阻塞原因。 |

---

### ⚡ 方案選擇

* **方案 A（真機 Notion 直連）**：在 Notion 頁面輸入 `/import` 匯入上述兩張 CSV，授權 Claude 連線後實測。
* **方案 B（免匯入快速實測）**：若臨時不想匯入 Notion，直接使用下方方案 B 內建資料的 Prompt，10 秒完成演練！

---

## 📋 複製貼上 Prompt

打開 Claude [一般對話視窗](https://claude.ai)，依您選擇的方案複製貼入：

### 若使用【方案 A：真機 Notion 直連】
```markdown
## Role
你是一位經驗豐富的技術專案經理（Technical PM）。

## Task
請使用 Notion 連接器，檢索我的 Notion 工作區中的「產品需求規格庫（PRD）」與「團隊任務看板（Tasks）」：
1. 找出所有歸屬於「Sprint-24」且優先級為「P0」的需求項目有哪些？
2. 檢查對應的任務中，是否有任何一項目前的狀態為「阻塞中（Blocked）」？
3. 列出該阻塞任務的負責人、截止日期，以及具體的阻塞原因（Blocked Reason）。

## Format
- 使用 Markdown 結構化卡片與警告標記（⚠️）清楚回報。
```

### 若使用【方案 B：免匯入快速實測】
```markdown
## Role
你是一位經驗豐富的技術專案經理（Technical PM）。

## Context（Notion 既有資料庫內容）
- PRD 需求庫：
  * PRD-01 (P1): 即時能耗監控面板 (Sprint-24)
  * PRD-03 (P0): OTA 韌體更新機制 (Sprint-24)
  * PRD-04 (P0): Modbus 異常斷線自動重試 (Sprint-24)
- Sprint Tasks 任務看板：
  * TSK-102: OTA 封包驗證介面 (Owner: 李雅婷, Status: 進行中)
  * TSK-106: Modbus 408 逾時修復 (Owner: 張志偉, Status: 阻塞中, Due: 3/19, Blocked Reason: 等待東京菱光商事提供現場封包日誌)

## Task
1. 篩選 Sprint-24 中優先級為 P0 的項目。
2. 交叉檢查是否有任何任務處於「阻塞中」？
3. 指出該阻塞任務的負責人、時限與具體瓶頸。
```

---

## ✅ 成果驗收點

- [ ] **精準跨庫鎖定**：準確識別出 Sprint-24 中的 P0 項目（OTA 韌體更新、Modbus 斷線自動重試）。
- [ ] **敏銳揪出障礙**：精確指出 `TSK-106`（Modbus-408 逾時排查）處於「阻塞中」。
- [ ] **關鍵責任細節**：完整列出負責人「張志偉」、截止日「3/19」，以及「等待東京菱光商事現場日誌」的核心原因。

---

## 💡 常見問題與除錯

* **Q：Claude 提示找不到 Notion 頁面或資料庫？**  
  * **解法**：請至該 Notion 頁面右上角點擊 `...` ➔ **Connections** ➔ 確認已將 **Claude** 加入連線名單中！

---

← [返回 Notion 主章節](../README.md) · [前往練習 2：阻塞事件升級通報](../02_Blocker_Escalation/README.md)
