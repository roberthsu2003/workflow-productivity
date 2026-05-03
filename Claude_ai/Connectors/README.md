# Connectors（連接器）

**Connectors** 是 Claude 的擴充功能，主要透過 **OAuth 2.0** 協定完成身分驗證，並基於 **MCP（Model Context Protocol）** 開放標準，將 Claude 安全地連接到 **Google 雲端硬碟、Gmail、Google 日曆、GitHub、Slack、Microsoft 365** 等外部服務。

這讓 Claude 能夠在您的授權下，直接讀取、檢索或摘要您的個人與組織資料，無需手動複製貼上。

---

## 核心機制：OAuth 與 MCP

### 1. OAuth 2.0 驗證（正確資訊確認）
您的資訊完全正確：**Connectors 確實使用 OAuth 進行授權**。
- **核心原理**：請參閱專門的 [**OAuth 2.0 授權機制詳解**](./OAuth.md) 了解代客泊車比喻與技術細節。
- **安全性**：Claude 不會看到或儲存您的帳號密碼，而是透過 OAuth 取得限時、限縮權限的「存取權杖（Access Token）」。
- **授權範圍 (Scopes)**：您可以清楚看到 Claude 申請了哪些權限（例如：僅限讀取日曆，或包含編輯文件）。
- **隨時撤銷**：您隨時可以在 Google、GitHub 等服務的安全性設定中撤銷授權。

### 2. MCP (Model Context Protocol) 傳輸
- Connectors 的底層運作是基於 Anthropic 推出的 MCP 協議。
- 它定義了模型如何向外部資料源請求資料，並將資料以結構化的方式餵給 Claude 的上下文。

---

## 使用時機

| 適合情境 | 限制與不適用 |
| :--- | :--- |
| **自動化資料存取**：資料在雲端（郵件、Repo），想直接在對話中分析。 | **內網與離線資料**：資料若在純內網且無法提供公網 OAuth 回調連結，則無法連線。 |
| **精準引用來源**：對話中會標示資料來源（如：根據哪一封郵件），增加可信度。 | **寫回權限限制**：多數官方 Connector 目前以「讀取」為主（如 Google Calendar），無法直接代為建立事件。 |
| **跨工具協作**：同時分析 GitHub 的代碼與 Slack 的討論記錄。 | **隱私敏感度極高**：若組織政策不允許 AI 接取任何雲端 SaaS 資料。 |

---

## 操作流程

1. **進入設定**：登入 **claude.ai** → 點擊左下角頭像 → **Settings** → **Connectors**。
2. **連線授權**：選擇目標服務（如 GitHub）→ 點擊 **Connect** → 導向該平台完成 **OAuth 登入與授權**。
3. **自然提問**：回到對話框，直接以自然語言互動（如：「摘要我上週在 GitHub 的 Pull Requests」），Claude 會視需求自動觸發連線。

---

## 經典範例：本週會議摘要與行動建議

### 任務背景
使用者已連結 **Google Calendar**，需要快速整理本週行程並產生對應的準備清單。

### RTCCF Prompt 範本
> **RTCCF 提醒**：請對照 [Chats／RTCCF 欄位對照](../Chats/README.md#rtccf-欄位對照複製範本時請五段都填) 確保五段內容完整。

```markdown
## Role
你是一位資深的行政效率專家與行程分析師。

## Task
請讀取我已連結的 **Google Calendar** 行事曆，檢索 **{請填：本週／下週}** 的所有會議資訊。
請為我產出一份「行程概覽與行動建議」，內容需包含：
1. 每日重點會議（時間、主題、地點/連結）。
2. 行程衝突警告（若有重疊時段）。
3. 具體的行動建議（例如：某會議前需準備哪些文件、某時段建議留白產出報告）。

## Context
- 我的時區：{例如 Asia/Taipei}。
- 專注專案：{例如 A 產品上市、Q2 預算審核}。
- 若無資料，請明確告知「查無此時段行程」。

## Constraint
- 資訊準確性：僅根據日曆實際內容回答，不可自行推測或虛構行程。
- 權限限制：若服務不支援「寫入/建立」，請勿在回答中暗示已幫我排定會議。
- 語言：繁體中文。

## Format
- 格式：使用 Markdown 表格列出行程。
- 標示引用：請保留 Connector 的來源引用標記，讓我能點擊確認。
```

---

## 延伸閱讀與資源
- [官方文件：Get started with connectors](https://claude.com/docs/connectors/getting-started)
- [官方文件：Connectors 總覽](https://claude.com/docs/connectors/overview)
- [Google Calendar 整合限制說明](https://claude.com/docs/connectors/google/calendar)

---

← [上層：Claude_AI 索引](../README.md) · [Chats 範例庫](../Chats/README.md)
**‌**