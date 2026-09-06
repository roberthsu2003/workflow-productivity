# OAuth 2.0 授權機制與安全控管

> ⚠️ **重要公告**：本文件已全面升級為更完整的深度專題指南！  
> 👉 **請點此閱讀最新版深度指南：[01. OAuth 2.0 授權機制與雲端隱私安全指南](./Guide/01_OAuth_and_Security.md)**

---

## ⚡ 核心精華速覽

在 AI 與雲端服務整合的世界中，**OAuth 2.0** 是最核心的安全標準。它讓 Claude 能夠在「不得知您密碼」的前提下，獲得您的授權來存取特定的資料。

### 🧠 觀念釐清：Connectors vs. Skills

| 特性 | Connectors（連接器） | Skills（技能） |
| :--- | :--- | :--- |
| **核心公式** | **OAuth + Remote MCP** | **Instructions + Resources + (Tools)** |
| **本質** | 基礎設施層（建立安全資料通道） | 行為應用層（封裝專業工作流） |
| **功能呼叫** | 主要由模型自動觸發 API | **可主動調用 Function Calling** |
| **工具整合** | 連接雲端 SaaS (如 Google, Canva, Notion) | **可串接本地 MCP Server 或執行程式碼** |
| **主要角色** | **「資料管道」** | **「調度員 / 專家」** |

---

## 📚 完整深度指南導覽

* 🔐 **[01. OAuth 2.0 授權機制與雲端隱私安全指南](./Guide/01_OAuth_and_Security.md)**
* 🚦 **[02. 工具權限分級（Tool Permissions）與企業級治理架構](./Guide/02_Tool_Permissions_and_Governance.md)**
* 🏗️ **[03. 雲端連接器 (Connectors) vs 本地端 MCP (Local MCP) 架構評估](./Guide/03_Connectors_vs_Local_MCP.md)**

---

← [返回 Connectors 總覽](./README.md)
