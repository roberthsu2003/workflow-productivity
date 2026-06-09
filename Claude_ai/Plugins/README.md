# Plugins（外掛／套件）

> **💡 三種擴充功能快速對照**
>
> | 類型 | 解決什麼 | 比喻 |
> |------|---------|------|
> | **Skills（技能）** | 教 Claude 怎麼把某類任務做好（不連外部服務） | 食譜／SOP |
> | **Connectors（連接器）** | 讓 Claude 能存取資料或操作其他系統 | 對外的插座、橋樑 |
> | **Plugins（外掛）** | 把多種能力打包成一個可安裝單位 | 整套工具箱 |
>
> **Plugins** 偏向打包式的擴充，把一組相關的東西（可能同時包含 Skills、指令、Connector 設定等）整合成一個可安裝的套件，方便一次部署或在團隊間共享。  
> 若需要教 Claude 執行某類工作請看 [Skills](../Skills/README.md)；若需要連外部服務請看 [Connectors](../Connectors/README.md)。

> 🟡 **方案需求**：**Plugins 本身 Free 即可安裝與瀏覽**；但完整的使用環境（**Claude Code** 與 **Cowork**）需 **Pro 方案**。Free 帳號可在一般 claude.ai 聊天中安裝 Plugins，但無法進入 Cowork／Code 流程。  
> **Free 替代方案**：若只是要「同時用一組 Skills + Connectors」，Free 帳號可手動在 Settings 中個別啟用各項 Skills 與 Connectors，效果類似但缺少 slash command 與打包分享。

**Plugins** 將 **MCP Connectors**、**Skills**、**斜線指令（slash commands）**、**子代理（sub-agents）** 等打包成**可安裝、可分享**的能力單元，用於在 **Claude Code**、**Cowork** 等情境一次帶入整套流程。總覽見 [Plugins overview](https://claude.com/docs/plugins/overview)；Anthropic 已開源多個內部使用範例（如 **Productivity**、**Enterprise search**、**Data**、**Legal** 等），可於 [claude.com/plugins](https://claude.com/plugins-for/cowork) 瀏覽（實際入口以官網為準）。Cowork 內安裝方式可參考 [Use plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)。

**RTCCF 五段欄位**請對照 [Chats／RTCCF 欄位對照](../Chats/README.md#rtccf-欄位對照複製範本時請五段都填)。

---

## 使用時機

| 適合 | 不適合 |
|------|--------|
| 使用 **Claude Code**／**Cowork**，希望**一次安裝**「連線＋技能＋指令」 | 僅使用 **claude.ai 網頁一般聊天**、未使用 Code／Cowork（請改用 **Connectors**／**Skills** 單獨設定） |
| 團隊要**共用同一套**工作流程（外掛目錄／自訂上傳） | 需求極簡、不需要打包與版本管理 |
| 需要 **slash command** 觸發固定流程（如 `/sales:…`） | 只要單次 RTCCF 對話（見 [Chats](../Chats/README.md) 即可） |

---

## 官方目錄範例（節錄）

文件中的 **Plugin directory** 表列多類外掛用途，例如：**Productivity**（任務、行事曆、日常流程）、**Data**（查詢與視覺化資料）、**Customer support**（分類與草擬回覆）等；並說明外掛可組合 **Skills**、**MCP connectors**、**slash commands**、**sub-agents**。詳見 [Plugins overview](https://claude.com/docs/plugins/overview) 內表格。

---

## 經典範例（辦公情境）：在 Cowork 用「生產力」類外掛整理一週任務

### 任務背景

使用者已在 **Cowork**（或相容環境）**Customize → Browse plugins** 安裝 **Productivity**（或同類）外掛，希望用**自然語言＋RTCCF**請 Claude 依外掛能力，將雜訊整理成**本週可執行清單**（實際指令名稱以已安裝外掛為準，可輸入 `/` 查看）。

### RTCCF Prompt（請複製後修改）

```markdown
## Role

你是一位擅長任務切割與優先排序的專案行政人員，並可運用我已安裝的 **Productivity／任務管理相關 Plugin**（含其 Skills 與 slash commands）。

## Task

請先確認目前對話中**可用的斜線指令與子流程**（若介面支援，請列出與我相關的 `/` 指令）。接著將我提供的雜事清單，整理成**本週**可執行表：含優先級、預估時間、是否需他人協力。

## Context

- 工作週：{本週日期區間}
- **未整理事項（請貼上）：**
  - （例：週三要交月報、週五前回覆廠商、下週會議需資料）

## Constraint

- 語言：繁體中文
- 不虛構我已完成的進度；不確定處標「待確認」
- 若某步驟需透過 **Connector** 讀取行事曆／郵件，請說明需我先完成授權

## Format

- 輸出為 **Markdown**：含**一週總表**（表格）＋**每日 Top 3**
- 若 Plugin 提供明確 **slash command** 建議（例如建立追蹤項），請在文末**逐條寫出可复制的一行指令**（實際以你偵測到的為準）
```

> **備註**：Plugin 與 Cowork 功能多為**付費方案**且介面可能更新；無法使用時請改以 [Chats](../Chats/README.md) 單獨撰寫 RTCCF，或僅啟用 **Connectors**／**Skills**。

---

← [上層：Claude_AI 索引](../README.md) · [Chats 範例庫](../Chats/README.md)
