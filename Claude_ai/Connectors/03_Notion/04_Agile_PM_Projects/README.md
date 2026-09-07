# 🏛️ 實戰 4：打造星橋科技「敏捷專案治理中心」專案

> **所屬章節**：[Notion 連接器實戰](../README.md) ➔ **練習 4 (進階)**  
> **運作模式**：📁 **Claude Projects 專案模式**  
> **預計實作時間**：15 分鐘  
> **所需連接器**：🔹 **Notion**

---

## 🎯 任務目標

學習如何利用 **Claude Projects 專案沙盒** 常駐團隊的敏捷工程規範手冊，並直連 **Notion 連接器**（即時讀取 PRD 需求庫與 Sprint 任務看板），打造全天候自動稽核衝刺進度、診斷 Blocker 瓶頸的「AI 敏捷專案治理總監」。

---

## 📥 專屬測試偽資料庫

| 檔案類型 | 檔案名稱（點擊檢視/下載） | 部署位置 | 說明 |
| :---: | :---| :---: | :---|
| 📑 **Wiki 手冊** | [**星橋科技_工程與設計協作手冊_Engineering_Handbook.md**](./sample_files/星橋科技_工程與設計協作手冊_Engineering_Handbook.md) | **Project Knowledge** | 團隊敏捷規範與 Blocker 處理 SOP。 |
| 📊 **PRD 庫** | [**星橋科技_產品需求規格庫_PRD.csv**](./sample_files/星橋科技_產品需求規格庫_PRD.csv) | **Notion 工作區** | 即時需求資料庫。 |
| 📋 **任務看板** | [**團隊任務與衝刺看板_Sprint_Tasks.csv**](./sample_files/團隊任務與衝刺看板_Sprint_Tasks.csv) | **Notion 工作區** | 即時工程任務看板。 |

---

## 🛠️ 步驟 1：專案建置設定（Claude Projects Setup）

1. 登入 [Claude.ai](https://claude.ai) ➔ 點擊左側 **Projects** ➔ **Create project**。
2. 填入專案基本資料：
   - **Project Name（專案名稱）**：
     ```text
     星橋科技_敏捷專案治理中心
     ```
   - **Project Description（專案描述）**：
     ```text
     結合工程協作手冊與 Notion 連接器，即時監控 Sprint 衝刺健康度、稽核 P0 阻礙事件並自動產出合規 PRD。
     ```
3. 點擊 **Create project** 建立完成。

---

## 📜 步驟 2：設定常駐專案指引（Project Instructions）

進入專案，在右側點擊 **Set Project Instructions**，貼入以下常駐治理規則：

```markdown
## Role
你是「星橋科技敏捷專案管理委員會」的 AI 執行秘書，精通 Scrum 框架、Notion 資料庫關聯治理與技術規格把關。

## Core Mission
每當使用者詢問專案進度、審查需求或查詢任務看板時：
1. 嚴格對照專案知識庫中的《工程與設計協作手冊》，檢驗各項任務是否符合 SLA 時限。
2. 主動穿透 Notion 連接器比對 PRD 與 Task 資料庫，主動揭露卡關超過 24 小時的 P0 隱性風險。
3. 撰寫任何 PRD 或驗收規格時，若未包含量化指標（SLA/TPS/Latency），一律判定為不合規並要求補正。
```

---

## 📥 步驟 3：上傳專案知識庫（Project Knowledge）

在專案頁面右側 **Project Knowledge** 區塊，點選 **Add content** ➔ **Upload files**，上傳：
- [星橋科技_工程與設計協作手冊_Engineering_Handbook.md](./sample_files/星橋科技_工程與設計協作手冊_Engineering_Handbook.md)

---

## 💬 步驟 4：對話實測指令（Prompt）

點選 **Start new chat**，確認該對話已連線 Notion 連接器，貼入以下健康度巡檢指令：

```markdown
請執行每週例行「Sprint 健康度自動巡檢」：
1. 透過 Notion 連接器，掃描當前進行中的 Sprint 所有任務。
2. 列出目前的完成率（Completion Rate）與阻塞率（Blocked Ratio）。
3. 依據協作手冊規範，給出本週的衝刺風險燈號（綠燈/黃燈/紅燈），並列出前三大待辦行動建議。
```

---

## ✅ 成果驗收點

- [ ] **知識庫法規自動套用**：無需額外提醒，Claude 主動將手冊規則與 Notion 任務狀態進行對位。
- [ ] **健康度燈號判定精準**：針對目前 TSK-106 阻塞超時情況，亮出「黃燈警戒（Amber）」或「紅燈（Red）」，並給予精準的資源排解建議。

---

← [上一練習：自動生成標準 PRD](../03_Automated_PRD_Spec/README.md) · [返回主章節](../README.md)
