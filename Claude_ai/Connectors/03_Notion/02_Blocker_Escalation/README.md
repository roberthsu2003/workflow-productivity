# 🚨 實戰 2：依據內部手冊進行阻塞事件升級 (Eskalation Protocol)

> **所屬章節**：[Notion 連接器實戰](../README.md) ➔ **練習 2**  
> **運作模式**：💬 **一般對話模式（Chat Prompts）**  
> **預計實作時間**：10 分鐘  
> **所需連接器**：🔹 **Notion**

---

## 🎯 任務目標

學習如何讓 Claude 調用 Notion 連接器檢索內部 Wiki（工程與設計協作手冊），核對 P0 級任務阻塞之處置規範，並針對 TSK-106 阻塞事件自動起草高警示之 Slack 通報訊息。

---

## 📥 專屬測試偽資料庫

| 檔案類型 | 檔案名稱（點擊檢視/下載） | 說明 |
| :---: | :---| :---|
| 📑 **Wiki 手冊** | [**星橋科技_工程與設計協作手冊_Engineering_Handbook.md**](./sample_files/星橋科技_工程與設計協作手冊_Engineering_Handbook.md) | 包含敏捷協議、P0~P3 定義與 Blocker 升級 SOP。 |
| 🚨 **阻塞案例** | [**Sprint-24_嚴重阻塞任務通報案例.md**](./sample_files/Sprint-24_嚴重阻塞任務通報案例.md) | TSK-106 具體超時細節與現場回報。 |

---

## 📋 複製貼上 Prompt

打開 Claude [一般對話視窗](https://claude.ai)，依您選擇的方案複製貼入：

### 若使用【方案 A：真機 Notion 直連】
```markdown
## Role
你是一位注重專案節奏與危機處理的資深 Scrum Master。

## Task
請檢索 Notion 中的《星橋科技 工程與設計協作手冊》：
1. 依據手冊規範，當「P0 級任務處於阻塞中（Blocked）」時，團隊標準的處置協議（Protocol）與升級時限為何？
2. 針對剛才發現的 TSK-106 阻塞事件，請幫我起草一份發在 Slack #product-alert 頻道的緊急警示訊息，督促相關窗口立刻跟進。

## Constraints
- Slack 訊息需包含：任務代碼、受影響客戶、阻塞時限倒數、具體呼叫對象（@張志偉、@海外業務窗口）。
```

### 若使用【方案 B：免匯入快速實測】
```markdown
## Role
你是一位注重專案節奏與危機處理的資深 Scrum Master。

## Context（工程手冊規範條文）
- 手冊規範：凡 P0 級任務處於 Blocked 狀態超過 24 小時，負責人必須通報；若超過 48 小時，Scrum Master 需立即啟動跨組 Eskalation，並於 Slack #product-alert 頻道發布緊急公告，指派代理人或協調外部資源。

## Task
針對 TSK-106（Modbus 408 逾時修復，負責人：張志偉，卡在等待日本菱光商事日誌，距離截止日僅剩 48 小時）起草一份 Slack #product-alert 緊急公告。
```

---

## ✅ 成果驗收點

- [ ] **法規條文準確引用**：指出「阻塞超 48 小時需啟動跨組 Eskalation」之核心協議。
- [ ] **Slack 通報高情境化**：清晰列出任務編號、影響範圍與具體點名的負責人窗口。

---

← [上一練習：跨資料庫檢索](../01_Database_Cross_Search/README.md) · [返回主章節](../README.md) · [前往練習 3：自動生成標準 PRD](../03_Automated_PRD_Spec/README.md)
