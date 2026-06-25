# 實作練習：使用現有的 Skill（工程與開發實戰）

> 🟢 **方案需求**：Free（需先在 Settings 開啟 Skills 與程式碼執行）  
> 💻 **開發主軸**：教導 Claude 透過官方的工程與開發 Skills，產出符合現代工程標準、可運行、可自動化測試的程式碼與工具。

本章節介紹如何呼叫官方在工程與開發類別提供的 6 個 Skills：**claude-api、mcp-builder、frontend-design、web-artifacts-builder、webapp-testing、skill-creator**。以下提供每個 Skill 的操作說明與直接複製使用的 RTCCF Prompt。

---

## 🛠️ 前置步驟（只需做一次）

1. 開啟 **Claude Desktop** 或 Web 版的 **Settings**
2. 確認已在 `Capabilities` 開啟 **Code execution and file creation** 
3. 在對話框輸入 `/` 可預覽目前可用的 Skill 清單，確認有相關開發 Skill 已啟用。

---

## 練習 A：使用 `frontend-design` 與 `web-artifacts-builder` 製作互動式儀表板

### 📖 說明
這兩個技能的組合能引導 Claude 避開一般的「AI 生成感」排版，改用 React、Tailwind CSS、更佳的狀態管理 (State Management) 與路由設計 (Routing)，產出具備生產等級 (Production-grade) 的前端網頁。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是一位資深前端 UI 工程師，擅長運用 frontend-design 與 web-artifacts-builder 技能，設計出美觀且具備良好狀態管理的 React 互動式儀表板。

## Task
請幫我開發一個「個人記帳與財務分析儀表板」的單頁應用程式 (SPA)。

## Context
功能需求：
- 記帳功能：可新增、刪除、分類（餐飲、交通、娛樂、其他）消費紀錄，並動態計算總額。
- 圖表分析：以圓餅圖呈現各分類消費佔比，並以長條圖呈現月份消費趨勢。
- 測試數據：預載 3 筆不同分類的消費紀錄以供展示。

## Constraint
- 語言：繁體中文介面
- 技術規範：
  1. 使用 React (可搭配 Lucide Icons) 與 Tailwind CSS 進行排版。
  2. 調用 frontend-design 確保設計細節（如按鈕點擊微動畫、玻璃縮影效果、符合 AAA 無障礙對比度標準）。
  3. 調用 web-artifacts-builder 進行狀態管理，確保新增資料時圖表會即時反應變更。
  4. 畫面必須在 Artifact 中可直接運行並互動。

## Format
- 在 Artifact 中輸出完整的 React 元件程式碼
- 回傳說明在 UI 設計中套用了哪些 frontend-design 無障礙與美學規範
```

---

## 練習 B：使用 `webapp-testing` 撰寫 Playwright E2E 測試

### 📖 說明
`webapp-testing` Skill 讓 Claude 能夠針對前端網頁，自動產生 Playwright 測試程式碼，驗證 UI 互動、表單輸入與狀態變更是否如預期運作，進而大幅提升程式碼品質。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是資深測試工程師 (QA Engineer)，專精於使用 webapp-testing 技能為 React 應用程式撰寫 Robust 的 Playwright 自動化測試。

## Task
請針對上一練習中建立的「個人記帳與財務分析儀表板」，使用 webapp-testing 撰寫一套完整的 Playwright 端對端 (E2E) 測試腳本。

## Context
測試場景需要包含：
1. 首頁載入驗證：確認標題與預載消費紀錄正常顯示。
2. 新增消費功能驗證：模擬填寫金額 $150 元、分類「餐飲」，點擊新增，並確認列表與總金額正確更新。
3. 刪除消費功能驗證：點擊刪除按鈕，確認該筆消費從列表消失。

## Constraint
- 語言：繁體中文註解
- 技術規範：
  1. 呼叫 webapp-testing 規範，使用 Page Object Model (POM) 結構來組織測試程式碼。
  2. 元素選取器優先使用 `getByRole`、`getByText` 等語意化選取器，避免使用脆弱的 CSS class。
  3. 每個測試步驟需附上清晰的預期結果斷言 (Assertions)。

## Format
- 在對話中輸出完整的 `finance-dashboard.spec.js` 測試程式碼
- 簡要說明如何在本機運行此 Playwright 測試與產出 HTML 測試報告
```

---

## 練習 C：使用 `mcp-builder` 規劃 Model Context Protocol 伺服器

### 📖 說明
`mcp-builder` 能夠協助開發者快速規劃、設計並生成符合 Anthropic Model Context Protocol (MCP) 的伺服器架構。透過此 Skill，您能生成包含 Tool 定義與 Schema 的 MCP 範本，打通 AI 與您的資料庫或內部 API。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是系統架構師，擅長運用 mcp-builder 技能設計符合官方標準的 Model Context Protocol 伺服器。

## Task
我需要建立一個自訂的 MCP 伺服器，讓 Claude 可以讀取與更新我的「Notion 待辦清單」。請使用 mcp-builder 為我產生伺服器的 API 規格與基礎程式碼範本。

## Context
伺服器功能需求：
1. Tool A: `list_notion_tasks` -> 查詢 Notion 指定 Database 中的所有待辦任務，參數為 `database_id`。
2. Tool B: `add_notion_task` -> 新增一筆任務，參數為 `title` (字串)、`due_date` (日期)。
3. 使用 Node.js/TypeScript 進行開發。

## Constraint
- 語言：繁體中文說明與英文程式碼
- 規範：
  1. 調用 mcp-builder 規範，輸出完整且符合 TypeScript 規範的 MCP SDK 初始化與 Tool 註冊邏輯。
  2. 詳細列出工具參數的 JSON Schema，確保 Claude 在調用時能正確解析參數。

## Format
- 輸出 MCP 伺服器的核心 `index.ts` 程式碼
- 提供如何將該 MCP 伺服器設定加入 Claude Desktop 中 `mcp_config.json` 的設定檔範本
```

---

## 練習 D：使用 `skill-creator` 引導自訂 Skill 生成

### 📖 說明
`skill-creator` 是官方最特別的 Meta Skill（技能的技能）。啟動後，Claude 會以問答與引導的方式，一步步協助您設計符合官方格式（如 frontmatter 的 YAML 設定、精確的 description 以觸發自動掛載、任務約束與範本）的自訂 Skill。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是 Claude 自訂技能開發專家，擅長運用 skill-creator (Meta Skill) 指引使用者開發符合生產標準的自訂 Skill 資料夾。

## Task
我想要建立一個名為「合約預檢專家 (contract-auditor)」的自訂 Skill。請調用 skill-creator 引導我完成該 Skill 的定義。

## Context
合約預檢專家的需求：
- 角色：法律助理與合約審查專家。
- 任務：檢查上傳的 PDF 合約中是否包含「保密條款」、「終止條款」與「違約金比例」，並找出對我方不利的條款。
- 需要外部參考：我有一份公司標準的「合約範本規約.pdf」。

## Constraint
- 語言：繁體中文
- 規範：
  1. 調用 skill-creator 的引導框架，第一步先與我對話，確認 `contract-auditor` 的 YAML Frontmatter（特別是 `name` 與 `description`，因為這會影響觸發精準度）。
  2. 設計該 Skill 資料夾結構，包含 `SKILL.md`、`references/` 與 `templates/`。
  3. 提供該 Skill 的引導問答，在此階段**不要**直接把整個技能寫完，而是先給我第一步的設計建議與提問。

## Format
- 輸出該 Skill 的初步設計草案（YAML Frontmatter 與結構說明）
- 提出 2 ~ 3 個需要我進一步回答的設計問題以利完善 Skill
```

---

## ✅ 完成後的下一步

練習完這四個開發範例後，您已掌握：
- 如何讓 AI 產出更具架構性、可測試的前端 React 應用。
- 如何透過 MCP 與自訂 Skill 將 Claude 連接到您自己的開發流程中。

**下一步**：前往 [溝通與內容實戰 (Communication)](../Communication/README.md)，學習如何透過 Skills 寫出保留個人風格的長文與製作團隊動態圖文！

---

← [返回 Skills 主頁](../README.md)
