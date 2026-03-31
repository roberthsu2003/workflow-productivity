# Connectors（連接器）

**Connectors** 透過 **MCP（Model Context Protocol）** 將 Claude 連到 **Google 雲端硬碟、Gmail、Google 日曆、GitHub、Slack、Microsoft 365** 等（依方案開放）。設定步驟見官方 [Get started with connectors](https://claude.com/docs/connectors/getting-started)、[Connectors 總覽](https://claude.com/docs/connectors/overview)。各整合能做什麼以該頁為準（例如 **Google Calendar** 多為**讀取**行程、**無法**代為建立／刪除事件，見 [Google Calendar 整合說明](https://claude.com/docs/connectors/google/calendar)）。

**RTCCF 五段欄位**請對照 [Chats／RTCCF 欄位對照](../Chats/README.md#rtccf-欄位對照複製範本時請五段都填)。

---

## 使用時機

| 適合 | 不適合 |
|------|--------|
| 資料在雲端（郵件、檔案、行事曆、Repo），**不想手動複製貼上** | 資料只在純內網、無法授權第三方連線 |
| 希望對話中**帶出處／引用**（官方說明會標示引用來源） | 需要**寫回**行事曆或信箱但該 Connector 僅支援讀取（請改用手動或別的工具） |
| 要在對話裡用 **MCP Apps** 呈現圖表、表單（若已啟用） | 僅需一次性的純文字回答（直接貼上即可） |

---

## 官方操作摘要

1. 登入 **claude.ai** → 左下角頭像 → **Settings** → **Connectors**  
2. 選擇服務（如 Google Calendar）→ **Connect** → 完成 OAuth  
3. 回到對話，**直接用自然語言提問**（例如「我明天有哪些會？」），Claude 會在需要時取用已連結資料。

---

## 經典範例（辦公情境）：查詢本週會議與準備事項

### 任務背景

承辦人已連結 **Google Calendar**（或同組織已授權之日曆），需在週一快速了解**本週已排定的會議**、時段與衝突，並請 Claude 整理成**待辦提醒清單**（不取代正式行程表）。

### RTCCF Prompt（請複製後修改）

```markdown
## Role

你是一位擅長行程整理的行政助理。

## Task

請使用我已連結的 **Google Calendar**（或我指定的日曆），查詢並摘要 **{請填：本週／下周／某日}** 的會議。輸出：日期、時間、標題、地點或線上連結（若有）、與我相關的待準備事項（若標題／說明可推論）。

## Context

- 我的時區：{例如 Asia/Taipei}
- 我關心的關鍵字或專案：{例：預算會議、跨部門協調}
- 若查無資料，請明確說「查無符合行程」

## Constraint

- 僅根據日曆中**實際出現**的資訊回答；不臆造會議內容
- 遵守 Connector 權限：若服務**不支援建立／修改**事件，請不要假裝已代為建立
- 語言：繁體中文

## Format

- 先給一段**本週總覽**，再以**表格或條列**列出每日重點
- 若官方介面有**引用／來源**標示，請保留，讓我知道依據哪些事件
```

> **備註**：實際可查詢的欄位與「讀／寫」範圍以 [Google Calendar 文件](https://claude.com/docs/connectors/google/calendar) 與當時產品為準。

---

← [上層：Claude_AI 索引](../README.md) · [Chats 範例庫](../Chats/README.md)
