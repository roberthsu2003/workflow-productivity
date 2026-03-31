# Artifacts（成品／Artifact）

**Artifacts** 是對話中產生的**獨立預覽區塊**（HTML、React、SVG、Mermaid、Markdown 等），可在側欄即時檢視、修改與發佈連結。官方教學指出：在 Artifact 內可**嵌入 Claude 文字完成能力**（無須自行管理 API Key），適合快速做**互動原型**與內部分享。詳見 [Prototype AI-Powered Apps with Claude artifacts](https://www.claude.com/resources/tutorials/prototype-ai-powered-apps-with-claude-artifacts)、[說明中心：Artifacts 介紹](https://support.claude.com/en/articles/9945615-intro-to-artifacts)。

**RTCCF 五段欄位**請對照 [Chats／RTCCF 欄位對照](../Chats/README.md#rtccf-欄位對照複製範本時請五段都填)。

---

## 使用時機

| 適合 | 不適合 |
|------|--------|
| 要**可點、可捲動**的網頁小工具、儀表板、表單原型 | 只要純文字、貼到郵件即可（用一般對話或 Markdown 即可） |
| 要**一鍵分享連結**給同事試用（權限依方案） | 必須正式發佈到自家網站、需後端資料庫（應另做正式系統） |
| 想練習「**內嵌 Claude**」的互動體驗（官方示範如 Compliment Bot） | 需下載 .docx／.xlsx 正式檔（改以 **Skills** 或 [Chats 範例](../Chats/README.md)） |

---

## 官方參考範例（節錄）

Anthropic 在教學中示範用一句話測試 Artifact 內嵌模型是否正常：

> 「Create a simple chatbot that uses Claude. Respond with compliments to every user input.」

並列舉多類靈感：[Language Tutor](https://claude.ai/public/artifacts/2af221b6-367f-4b4f-9fe9-25710f5f8feb)、[One-Page PRD Maker](https://claude.ai/public/artifacts/3d81ba29-d1ad-4e9b-b58e-3e0f46ba8afd)、[5 Whys 分析工具](https://claude.ai/public/artifacts/fc64414e-76db-4876-8531-6e9794e4b1be) 等公開 Artifact（連結見上述教學頁）。

---

## 經典範例（辦公情境）：內部「會議室／請假規則」查詢小工具

### 任務背景

總務想先做一個**可給同仁點選、查閱**的簡易網頁：顯示會議室借用規則與請假流程摘要（內容可事後改），用於內部溝通與教育訓練前預覽，不需正式上線。

### RTCCF Prompt（請複製後修改）

```markdown
## Role

你是一位擅長前端原型的行政／總務承辦人員。

## Task

建立一個**單一 HTML Artifact**（可含內嵌 CSS／JavaScript）：主題為「會議室借用與請假流程快速查詢」。頁面需有清楚標題、分頁或摺疊區塊（會議室規則／請假流程）、以及一個簡單的「常見問題」摺疊清單。

## Context

- 使用對象：公司／機關內部同仁
- **以下為我們實際規定（請貼上或改寫）：**
  - （貼上會議室開放時段、借用方式、請假天數計算方式等）

## Constraint

- 語言：繁體中文；版面清楚、字級夠大，利於螢幕閱讀
- 不連接真實資料庫；按鈕以展示流程為主即可
- 若內容涉及個資或未定案政策，請標註「範例」

## Format

- 產出為 **Artifact**，格式為**單一 HTML**（或 React Artifact，若介面預設支援），可於側欄預覽與互動
- 請在 Format 中註明：完成後我可要求「按鈕加大」「改配色」等迭代
```

---

← [上層：Claude_AI 索引](../README.md) · [Chats 範例庫](../Chats/README.md)
