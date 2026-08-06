# 🎯 創投 (VC) 專屬 Skill 與 Playwright MCP 自動化實戰

> 🟢 **方案需求**：Free / Pro 方案皆適用（搭配 Claude Desktop 本地 Playwright MCP 伺服器）  
> 💼 **產業目標**：針對創投（Venture Capital）產業的核心工作（Deal Sourcing、Due Diligence、Market Mapping、Portfolio Management），將 **Playwright MCP 瀏覽器自動化** 與 **創投商業分析框架** 結合，打造高效率的模组化 Agent Skills。

---

## 💡 為什麼創投產業需要 Playwright MCP + Custom Skill？

創投經理與分析師（VC Associates / Analysts）每天需處理海量的公開與非公開數據，常見痛點包括：
- **動態網頁難以直接擷取**：許多新創官網、Pricing 價格頁面、Changelog 或 Product Launch 平台採用 SPA（Single Page Application）或動態渲染。
- **反覆人工爬查極度耗時**：比對 5–10 家競品的 Pricing、最新 Feature 或創辦人背景時需頻繁切換分頁與複製貼上。
- **資料缺乏標準化結構**：散落於不同網站的非結構化資訊，難以直接輸入至創投 IC（Investment Committee，投資委員會）會議簡報或投資備忘錄 (Investment Memo)。

透過 **Playwright MCP**（操控本機真實瀏覽器）+ **Claude Custom Skill**（封裝創投分析邏輯 SOP），即可實現從「網頁動態點擊擷取」到「專業商業報告產出」的全自動化！

---

## 🚀 創投 4 大專屬 Skill 主題與實操架構

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                創投 4 大專屬 Skill 自動化矩陣                             │
├──────────────────────────┬──────────────────────────┬───────────────────────────────────┤
│ Skill 主題               │ Playwright MCP 任務      │ 技能產出結果                      │
├──────────────────────────┼──────────────────────────┼───────────────────────────────────┤
│ 1. 競品動態與市場地圖    │ 自動連線競品官網/Pricing  │ 競品矩陣（定位、商業模式、優劣勢） │
│ 2. 創辦團隊背景研判      │ 爬取工商登記/新聞/論壇   │ 數位足跡與背景風險評估報告        │
│ 3. 新創趨勢與 Deal Source│ 追蹤 Product Hunt/YC/GitHub│ 每週 Deal Sourcing 預警簡報        │
│ 4. 投後營運健康度追蹤    │ 抓取 App 評分/Careers 職缺│ 營運成長/預警訊號報告             │
└──────────────────────────┴──────────────────────────┴───────────────────────────────────┘
```

### 1. 競品動態與市場地圖生成器 (Market Mapping & Competitor Intel Skill)
- **應用場景**：分析特定賽道（如 AI DevTools、FinTech、Enterprise SaaS）時，快速掃描目標公司與 5–10 家競品的產品定位、價格架構、最新 Feature 與客群。
- **Playwright MCP 角色**：自動連線至競品官網、`/pricing` 頁面、`/changelog` 或更新日誌頁面，動態擷取最新文案與畫面結構。
- **技能產出**：競品對照矩陣（包含：核心定位、商業模式、收費機制、功能特點、目標客群、SWOT 分析）。

### 2. 初創團隊與創辦人背景研判 Skill (Founder & Startup Background Check Skill)
- **應用場景**：收到 Pitch Deck 或發現潛在項目時，進行快速背景研判與數位足跡核實。
- **Playwright MCP 角色**：前往公開商業登記（如公司登記查詢網站）、新聞搜尋引擎、社群/論壇（GitHub Trending、Product Hunt、LinkedIn 公開頁面）、創辦人採訪或 Podcast 逐字稿。
- **技能產出**：團隊數位足跡與背景風險評估報告，標示公開新聞紀錄、技術社群聲量、專利發明與公司異動歷程。

### 3. 新創趨勢與 Deal Sourcing 偵測 Skill (Deal Sourcing & Product Launch Tracker)
- **應用場景**：主動發現早期潛在投資標的，降低錯失好項目的風險（FOMO）。
- **Playwright MCP 角色**：自動造訪與爬取 Product Hunt、YC Launch 頁面、GitHub Trending、Hacker News Launch 貼文或垂直產業論壇。
- **技能產出**：依據自訂條件（如 AI 應用、High Upvotes、特定 Tech Stack、SaaS 訂閱制）過濾優質項目，生成「每週 Deal Sourcing 預警與初審簡報」。

### 4. 投後公司營運狀況自動追蹤器 (Portfolio Company Health Checker)
- **應用場景**：定期關注已投 Portfolio 公司或重點觀望 (Watchlist) 名單的運作狀態。
- **Playwright MCP 角色**：連線至 App Store / Google Play 擷取最新評分與用戶負評、進入官網 Careers（招募頁面）統計職缺數量變動、前往 Blog / Newsroom 觀察產品更新頻率。
- **技能產出**：營運訊號健康報告（例如組織擴張訊號：技術與業務職缺爆發；營運警訊：評分下滑或長達數月無更新）。

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

## 📋 課堂可以直接複製使用的 Prompt（RTCCF 格式）

上課示範時，若無上傳 `.md` 設定檔，學員可以直接複製以下 RTCCF Prompt 在對話框中發起任務：

```markdown
## Role
你是一位資深創投分析師 (VC Investment Associate)，精通運用 Playwright MCP 操控瀏覽器進行自動化盡職調查與市場調研。

## Task
請針對目標新創公司網站（例如：https://example-startup.com），進行網頁資料抓取、競品分析並產出一份「VC 初步盡職調查報告 (Preliminary VC Due Diligence Report)」。

## Context
你需要分析該項目的產品商業模式、價格策略、團隊擴張狀況，並自動搜尋網路上 2 家主要競品進行比較。

## Constraint
- 必須使用 Playwright MCP 造訪目標網站的首頁、/pricing 頁面與 /careers 頁面。
- 使用搜尋引擎尋找競品，並使用 Playwright 開啟前 2 家競品官網。
- 報告須使用繁體中文輸出。
- 遇 DOM 動態載入時，需等待元件載入完成（wait_for_selector）再擷取內容。

## Format
請輸出標準 Markdown 格式報告，包含：
1. 執行摘要 (Executive Summary)
2. 商業模式與價格機制 (Business Model & Pricing)
3. 競品分析矩陣 (Competitor Comparison Table)
4. 團隊與招募訊號 (Hiring & Growth Signals)
5. 創辦人面談建議問題 (Top 3 Questions for Founders)
```

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
