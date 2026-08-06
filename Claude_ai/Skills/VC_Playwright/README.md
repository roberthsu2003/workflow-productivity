# 🎯 創投 (VC) 專屬 Skill 與 Playwright MCP 自動化實戰

> 🟢 **方案需求**：Free / Pro 方案皆適用（搭配 Claude Desktop 本地 Playwright MCP 伺服器）  
> 💼 **產業目標**：針對創投（Venture Capital）產業的核心工作（Deal Sourcing、Due Diligence、Market Mapping、Portfolio Management），將 **Playwright MCP 瀏覽器自動化** 與 **創投商業分析框架** 結合，打造高效率的模組化 Agent Skills。  
> 🎓 **講師提示**：本文件專為非創投背景講師設計，提供 **真實可測試網址**、**可以直接複製的示範指令** 以及 **VC 創投商業背景小知識**，方便課堂上順暢示範。

---

## 🎓 講師專屬：4 大實戰演練案例庫（含真實測試網址）

為了讓非創投背景的講師能直接在課堂上對著畫面示範，以下精選 4 個國際知名新創公司的真實網址與課堂操作腳本：

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                創投 4 大實戰案例網址與示範主題                                     │
├──────────────────────────┬──────────────────────────────────────┬───────────────────────────────┤
│ 演練主題                 │ 真實測試網址 (Target URLs)           │ 創投商業關注點 (VC Metrics)   │
├──────────────────────────┼──────────────────────────────────────┼───────────────────────────────┤
│ 案例 1：開發者工具與競品 │ Supabase (https://supabase.com)      │ 定價機制 (Freemium/Usage)、   │
│          調研 (DD)       │ vs Firebase (https://firebase.google)│ 開源社群影響力 vs 競品壁壘    │
├──────────────────────────┼──────────────────────────────────────┼───────────────────────────────┤
│ 案例 2：AI 向量資料庫    │ Pinecone (https://www.pinecone.io)   │ 賽道成長潛力、收費模式、      │
│          市場地圖        │ vs Qdrant (https://qdrant.tech)      │ 全託管 (Managed) vs 自建      │
├──────────────────────────┼──────────────────────────────────────┼───────────────────────────────┤
│ 案例 3：新創標的發現     │ Product Hunt (https://producthunt.com)│ Upvote 聲量、產品創新度、     │
│          (Deal Source)   │ YC Companies (https://ycombinator.com)│ 早期趨勢與關鍵字篩選          │
├──────────────────────────┼──────────────────────────────────────┼───────────────────────────────┤
│ 案例 4：投後營運與擴張   │ Resend (https://resend.com/careers)  │ 招募規模變動 (Hiring Blitz)、 │
│          健康度追蹤      │ Changelog (https://resend.com/changelog)│ 產品疊代頻率 (Release Velocity)│
└──────────────────────────┴──────────────────────────────────────┴───────────────────────────────┘
```

---

### 📌 案例 1：新創盡職調查與競品比對 (Due Diligence & Competitor Intel)

- **目標新創**：**Supabase**（知名開源資料庫新創）
  - 官網首頁：`https://supabase.com`
  - 價格頁面：`https://supabase.com/pricing`
  - 招募頁面：`https://supabase.com/careers`
- **對照競品**：**Firebase** (`https://firebase.google.com`)
- **💡 創投背景小知識（講師口播備忘）**：
  > 「Supabase 是主打替代 Google Firebase 的開源新創。VC 在做盡職調查 (DD) 時，極度看重這類 SaaS 公司的 **Pricing 模型（免費額度 Freemium 能否轉化為付費客戶）** 以及 **招募頁面（工程與業務團隊是否快速膨脹）**。」

#### 📋 講師課堂示範指令（直接複製發送給 Claude）：
```markdown
請使用 Playwright MCP 連接至 Supabase 官網 (https://supabase.com) 與價格頁面 (https://supabase.com/pricing)，擷取其核心產品訴求與付費方案。接著開啟競品 Firebase (https://firebase.google.com)，幫我產出一份「Supabase vs Firebase 競品分析報告」，包含：核心價值主張、計費方式（Usage-based 或月費）、目標客群差異。
```

---

### 📌 案例 2：AI 賽道競品對照與市場地圖 (Market Mapping)

- **目標新創**：**Pinecone**（知名 AI 向量資料庫新創）
  - 官網與 Pricing：`https://www.pinecone.io/pricing`
- **對照競品**：**Qdrant** (`https://qdrant.tech`)
- **💡 創投背景小知識（講師口播備忘）**：
  > 「AI 大模型暴紅後，『向量資料庫 (Vector Database)』成為 VC 最瘋狂競相投資的基礎設施賽道。VC 做 Market Mapping 時，需要快速比對誰提供 Serverless 隨用隨付、誰提供開源自架版本。」

#### 📋 講師課堂示範指令（直接複製發送給 Claude）：
```markdown
請使用 Playwright MCP 造訪 Pinecone (https://www.pinecone.io/pricing) 與 Qdrant (https://qdrant.tech)，比較這兩家 AI 向量資料庫新創。請擷取兩家的：1. 核心產品定位 2. 收費機制 3. 是否提供開源版，並產出 Markdown 競品對照矩陣。
```

---

### 📌 案例 3：早期新創標的搜尋 (Deal Sourcing Tracker)

- **目標網站**：**Product Hunt** (`https://www.producthunt.com`)
- **💡 創投背景小知識（講師口播備忘）**：
  > 「Deal Sourcing 是創投分析師最重要的基本功。分析師每天早上都要上 Product Hunt 看有哪些新工具獲得高 Upvote（社群投票讚數），搶在其他創投之前聯絡創辦人發出投資邀約。」

#### 📋 講師課堂示範指令（直接複製發送給 Claude）：
```markdown
請使用 Playwright MCP 造訪 Product Hunt 首頁 (https://www.producthunt.com)，抓取今天熱門發布 (Featured Products) 前 5 個項目。請整理出：產品名稱、一句話摘要、獲得的 Upvote 票數、官網連結，並分析哪些項目屬於 AI 應用。
```

---

### 📌 案例 4：投後公司營運健康度追蹤 (Portfolio Health Check)

- **目標新創**：**Resend**（知名郵件 API 新創，成長速度極快）
  - 招募頁面：`https://resend.com/careers`
  - 更新日誌：`https://resend.com/changelog`
- **💡 創投背景小知識（講師口播備忘）**：
  > 「投後管理 (Portfolio Management) 時，VC 不需要天天問創辦人進度。觀察公司的 **Careers 頁面職缺數**（代表資金是否充沛、正大規模擴張）與 **Changelog 產品更新頻率**（代表團隊開發執行力），就能精準評估公司的健康狀態。」

#### 📋 講師課堂示範指令（直接複製發送給 Claude）：
```markdown
請使用 Playwright MCP 造訪 Resend 的招募頁 (https://resend.com/careers) 與 Changelog 頁 (https://resend.com/changelog)，統計該公司目前開放的職缺數量與類別，以及最近一個月的產品更新次數，產出一份「Resend 營運成長與擴張訊號報告」。
```

---

## 🛠️ 實作範例：打造「新創盡職調查與競品分析 Skill」

將這套流程標準化為符合 Claude 規範的 `SKILL.md` 範本，可直接放置於 `.claude/skills/vc-due-diligence/SKILL.md` 或在對話中作為指令：

```yaml
---
name: vc-due-diligence-analyzer
description: 當使用者提供新創公司 URL 時，結合 Playwright MCP 自動進行官網導覽、競品搜尋並產出 VC 創投盡職調查與競品對照報告。
---

# VC Due Diligence & Competitor Analyst Skill

## 任務目標
協助創投分析師針對指定新創公司 URL，進行自動化網站數據擷取、市場競品調研，並生成專業的投資前評估報告。

## 執行流程 SOP

### 第一階段：Playwright 動態擷取 (Target Startup)
1. 使用 Playwright MCP 開啟使用者指定的目標網站 URL。
2. 擷取首頁的核心價值主張 (Value Proposition) 與主要產品訴求。
3. 導覽至網站中的選單，自動尋找並進入以下子頁面擷取內容：
   - `/pricing` 或 `/plans` (價格機制)
   - `/about` 或 `/company` (團隊背景與願景)
   - `/customers` 或 `/case-studies` (標竿客戶與應用場景)
   - `/careers` 或 `/jobs` (招募狀態與團隊擴張規模)

### 第二階段：競品搜尋與比對 (Competitor Intel)
1. 透過搜尋引擎查詢 `"Alternative to [目標公司名稱]"` 或 `"[目標公司名稱] vs"`。
2. 挑選前 2-3 家主要競品，使用 Playwright 造訪其官網首頁與 Pricing 頁面。

### 第三階段：商業分析與報告產出
綜合以上擷取之數據，輸出符合以下格式的 Markdown 報告：

1. **Executive Summary（執行摘要）**：100 字極簡說明產品定位與解決痛點。
2. **Business Model & Pricing Analysis（商業模式與訂閱機制）**：分析收費模式（SaaS, Marketplace, Usage-based, Freemium 等）。
3. **Competitor Comparison Matrix（競品分析矩陣）**：以 Markdown 表格比較目標公司 vs 主要競品（定位、客群、價格、核心功能優勢）。
4. **Traction & Growth Signals（成長與營運訊號）**：由 Careers 與 Customers 頁面評估其目前發展階段。
5. **Key Questions for Founders（創辦人面談建議問答）**：提出 3–5 個針對防禦壁壘 (Moat)、Unit Economics、客戶獲取成本 (CAC) 與擴張瓶頸的關鍵問題。
```

---

## 📚 非創投背景講師：VC 核心術語與講義備忘手冊

上課時如果學員問起創投術語，可以參考以下簡明解說表：

| 創投術語 (Term) | 全名 / 中文 | 講師秒懂解釋（課堂口播法） |
| :--- | :--- | :--- |
| **Deal Sourcing** | 標的尋找 / 案源發掘 | 「像探星獵人一樣，主動在網路上尋找剛起步、有潛力的新創公司。」 |
| **Due Diligence (DD)** | 盡職調查 | 「買房前的驗屋！在掏錢投資前，把目標公司的產品、財務、法務與競品查個水落石出。」 |
| **Market Mapping** | 市場地圖 / 賽道掃描 | 「繪製產業地圖，把市面上的主要玩家（目標公司 + 競品）依照定位與價格排成對照表格。」 |
| **Portfolio Management**| 投後管理 | 「投資後的售後服務與健康追蹤，定期關注已投公司有沒有在好好招募與做產品更新。」 |
| **Freemium / Usage-based**| 免費增值 / 按用量計費| 「SaaS 新創常見的收費模式：基礎功能免費吸引用戶，用量變大（如資料量、API 呼叫數）才收費。」 |
| **Changelog** | 產品更新日誌 | 「新創公司的開發成績單。看 Changelog 就能知道這家公司的工程師有沒有在認真寫程式發佈新功能。」 |

---

## 💡 課程設計與教學進階建議

### 1. 教導「處理動態阻擋與結構化提取」
- **元件載入與動態等待**：創投常研究的科技新創網站多採用動態前端（React/Vue/Next.js），教導學員如何在 Playwright 指令中加入「等待元件載入完成（`wait_for_selector`）」或「等待網路空閒（`wait_for_load_state`）」，避免擷取到空白頁面。
- **非結構化 HTML 轉結構化 JSON/Markdown**：引導學員理解 Playwright MCP 負責「抓取 raw 內容」，而 Claude 則負責將龐大的 DOM 結構自動清理並轉換為結構化的 JSON 欄位或 Markdown 比對表格。

### 2. 結合多 MCP 打造完整自動化 Workflow (Playwright + FileSystem / Notion / Slack)
串聯多個 MCP 伺服器，實現資料從「抓取 ➔ 分析 ➔ 存檔 ➔ 通報」的一站式工作流：

```
┌─────────────────┐     ┌──────────────────┐     ┌───────────────────┐     ┌─────────────────────┐
│  Playwright MCP │ ──> │ Claude DD Skill  │ ──> │   FileSystem MCP  │ ──> │ Notion / Slack MCP  │
│ (自動抓取官網/競品) │     │ (創投商業框架分析) │     │ (儲存為 .md 投資報告) │     │ (自動同步至 IC 數據庫) │
└─────────────────┘     └──────────────────┘     └───────────────────┘     └─────────────────────┘
```

1. **Playwright MCP**：本機操控瀏覽器前往新創官網與競品網頁，抓取動態內容。
2. **Claude Custom Skill**：輸入網頁資料並套用 VC 商業分析模組進行歸納收斂。
3. **FileSystem MCP**：將產出的報告自動儲存至團隊的 `/Investment_Reports/2026/` 目錄中。
4. **Notion / Slack Connector (Remote MCP)**：自動將重點摘要同步張貼至團隊的 Slack `#deal-flow` 頻道或更新至 Notion 投資案資料庫中。

---

← [返回 Skills 主頁](../README.md) | [返回專案首頁](../../README.md)
