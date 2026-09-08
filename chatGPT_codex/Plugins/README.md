# Plugins（外掛套件）

> 🔵 **方案需求**：Plus 起（Plus 對部分第一方 plugin 有使用限制）。Business / Enterprise 的管理員可控管可安裝清單。

Plugin 是**可安裝的擴充套件**，把 skills、外部服務整合、MCP server 與選用的 UI 打包成一個單位。安裝來源是 **ChatGPT 與 Codex 共用的通用 plugin 目錄**。

---

## 🧩 Skill、MCP、Plugin：三者的關係

這是最多人搞混的地方。用一句話區分：

> **Skill 是「怎麼做」，MCP 是「連到哪」，Plugin 是「把兩者打包好給你」。**

| 我的需求 | 選擇 | 為什麼 |
| :--- | :--- | :--- |
| 固定的 SOP、規則、範本 | **[Skill](../Skills/README.md)** | 純指示，不需要連外 |
| 連接自有 API 或資料庫 | **[MCP server](../MCP/README.md)** | 需要程式化的工具介面 |
| 打包多個 skills + 整合 + UI 分享出去 | **Plugin** | 可安裝、可分發 |
| 已經有官方或策展好的整合 | **直接裝現成 Plugin** | 不要重造輪子 |

### 組成關係圖

```text
Plugin
├── Skills          （一個或多個 SKILL.md，定義工作流程）
├── App 整合         （OAuth 連接外部服務）
├── MCP server      （選用：程式化的工具介面）
└── UI              （選用：自訂介面元件）
```

---

## 📦 現成的 Plugin 生態

2026 年 6 月起，OpenAI 推出**六個職能導向的官方 plugin**，開箱即連 **62 個常見商務應用**，內建 **110 個現成 skill**。另有 **90+ 個**第三方與社群 plugin。

### 官方職能 Plugin（範例）

| Plugin | 對象 | 串接的工具（例） |
| :--- | :--- | :--- |
| **Data analytics** | 分析師、業務團隊 | Snowflake、Databricks Genie、Hex、Tableau |
| **Creative production** | 行銷與創意團隊 | Figma、Canva、Shutterstock、Picsart、Fal |
| 其餘四個職能 plugin | 依角色而異 | 見官方目錄 |

**Data analytics** 能做的事：回答數據問題、探索產品與營運數據、解釋關鍵指標為什麼變動、產出報表與儀表板。
**Creative production** 能做的事：把 brief 轉成可審查的素材、建立 campaign board、產生與調整廣告變體、產出商品情境照與電商用圖組。

### 值得注意的第三方 Plugin

Atlassian Rovo、CircleCI、CodeRabbit、GitLab Issues、Microsoft Suite、Neon by Databricks、Remotion、Render、Superpowers 等。

> **教學提醒**：plugin 目錄更新非常快，授課前請直接查看 `Settings` → `Plugins` 的實際清單，不要照抄講義中的名單。

---

## 🔍 安裝前的審查清單

> [!WARNING]
> **安裝 plugin 等於授權一段別人寫的程式在你的環境中執行，並代表你存取外部服務。** 這不是「裝個 App」等級的決定。

- [ ] **發布者是誰**？官方、知名廠商、還是不具名個人？
- [ ] **要求哪些權限**？逐項讀 OAuth 範圍，能唯讀就唯讀
- [ ] **資料流向哪裡**？你的程式碼／文件會被送到哪個伺服器？
- [ ] **依賴什麼**？是否包含 MCP server 或會執行的 script？
- [ ] **有沒有維護**？最後更新日期、issue 回應狀況
- [ ] **組織政策允許嗎**？Business / Enterprise 環境請先確認管理員設定

### 第一次使用一律唯讀

```text
請使用剛安裝的 <plugin 名稱>，**只做讀取**：
列出你能存取到的資料範圍，以及你可以呼叫的工具清單。
不要執行任何寫入、修改或發佈動作。
```

看清楚它能碰到什麼，再決定要不要給更多權限。

---

## 🧹 定期清理

> [!IMPORTANT]
> **移除不再使用的 plugin。** 理由有三個：
> 1. **安全**：每個 plugin 都是一條 OAuth 授權，放著就是持續有效的存取權。
> 2. **效能**：plugin 帶進來的 skill 會佔用 skill 清單的 8,000 字元上限（見 [Skills](../Skills/README.md#-漸進式揭露progressive-disclosure)），裝太多會排擠掉你真正常用的。
> 3. **可預測性**：太多重疊的工具會讓 Codex 選錯工具。

建議每季檢視一次 `Settings` → `Plugins`，把三個月沒用過的移除。

---

## 🏗️ 自己做 Plugin

當你想把公司內部的整合分發給全隊時：

1. **建立 MCP server**（若需要連接外部服務）——見 [MCP 章節](../MCP/README.md)
2. **打包 skills**（選用：可透過 ChatGPT UI 設定介面元件）
3. **依提交規範封裝**
4. **透過 plugin 送審與發佈流程上架**

> **先問一句：真的需要 plugin 嗎？** 如果只是團隊內部共用流程，把 skill 放進 `$REPO_ROOT/.agents/skills` 並提交進 Git，就能讓全隊自動取得——不需要做 plugin、不需要送審。**Plugin 是為了跨組織分發而存在的。**

---

## 🏢 組織管控

Business / Enterprise / Edu 的管理員可以：

- 控管哪些 plugin 允許安裝
- 設定 **Allow event-triggered scheduled tasks** 等細部權限
- 檢視稽核日誌
- 透過 RBAC 分派不同角色的權限

> 課堂若在企業環境進行，請先與管理員確認 plugin 安裝政策，避免上課到一半才發現裝不了。

---

## 🔄 與 Claude Plugins 的對照

| 面向 | Claude Plugins | Codex Plugins |
| :--- | :--- | :--- |
| 方案門檻（安裝） | 🟢 Free 可安裝瀏覽 | 🔵 **Plus 起** |
| 方案門檻（使用） | Cowork / Code 需 Pro | Plus 起，部分第一方受限 |
| 包含什麼 | Connectors、Skills、slash commands、sub-agents | Skills、app 整合、MCP server、UI |
| 目錄 | Claude plugin 目錄 | **ChatGPT 與 Codex 共用的通用目錄** |
| 團隊分發替代方案 | Project 分享 | **提交 skill 進 Git**（更輕量） |

---

## 小結

| 情境 | 該做什麼 |
|---|---|
| 想要固定流程 | 做 Skill，不要做 Plugin |
| 想連內部系統 | 做 MCP server |
| 團隊內部共用流程 | Skill 放 `$REPO_ROOT/.agents/skills` 提交進 Git |
| 要跨組織分發 | 才做 Plugin |
| 服務已有現成整合 | 直接裝，不要自己做 |

**官方說明**：[Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins) · [OpenAI Plugins documentation](https://developers.openai.com/plugins)

---

← [返回上層：ChatGPT Codex 索引](../README.md)
