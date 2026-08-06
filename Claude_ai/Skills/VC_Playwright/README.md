# 🎯 創投 (VC) 專屬 Skill 與 Playwright MCP 自動化實戰（台灣在地案例篇）

> 🟢 **方案需求**：Free / Pro 方案皆適用（搭配 Claude Desktop 本地 Playwright MCP 伺服器）  
> 💼 **產業目標**：針對創投（Venture Capital）產業的核心工作（Deal Sourcing、Due Diligence、Market Mapping、Portfolio Management），將 **Playwright MCP 瀏覽器自動化** 與 **創投商業分析框架** 結合，打造高效率的模組化 Agent Skills。  
> 🇹🇼 **台灣在地化專章**：本文件精選 **台灣無人機 (Drone)**、**矽光子與邊緣 AI 晶片 (Silicon Photonics & Edge AI)**、**工業 AI / 智慧製造** 以及 **台灣熱門新創** 作為實作範例，讓講師能在課堂上使用在地學員高度共鳴的真實網址進行示範。

---

## 🎓 台灣在地 4 大實戰演練案例庫（含真實測試網址）

以下精選台灣目前最熱門的深科技（DeepTech）與 AI 新創公司網址，供講師在課堂上對著畫面實機操作示範：

| 演練主題 | 台灣在地測試網址 (Taiwan Target URLs) | 創投商業關注點 (VC Metrics) |
| :--- | :--- | :--- |
| **案例 1：無人機國家隊盡職調查 (DD)** | • 智飛科技 ([taiwan-uav.com](https://www.taiwan-uav.com)) <br>• 經緯航太 ([geosat.com.tw](https://www.geosat.com.tw)) | 非紅供應鏈、軍規光電/飛控技術自研率、災防與防衛標案營收 |
| **案例 2：矽光子與邊緣 AI 晶片市場地圖** | • 創鑫智慧 ([neuchips.ai](https://www.neuchips.ai)) <br>• 耐能智慧 ([kneron.com](https://www.kneron.com)) | 算力能效比 (TOPS/W)、地端生成式 AI 晶片 vs CPO 封裝 |
| **案例 3：台灣新創標的發現 (Deal Source)** | • 創業小聚 ([meet.bnext.com.tw](https://meet.bnext.com.tw)) <br>• FINDIT 平台 ([findit.org.tw](https://findit.org.tw)) | 台灣 Meet Neo Star 評選熱門、早期募資訊號、垂直賽道潛力 |
| **案例 4：工業 AI 投後營運與擴張追蹤** | • 杰倫智能招募 ([profetai.com/careers](https://www.profetai.com/careers)) <br>• 杰倫智能官網 ([profetai.com](https://www.profetai.com)) | 製造業 SaaS 落地速度、海外拓展（日本/東南亞）招募 |

---

### 📌 案例 1：台灣無人機 (Drone / Defense Tech) 盡職調查與競品比對

- **目標新創 1**：**智飛科技 (Skyline Dynamics)**
  - 官網首頁：`https://www.taiwan-uav.com`
- **目標新創 2**：**經緯航太 (GEOSAT)**
  - 官網首頁：`https://www.geosat.com.tw`
- **💡 創投背景小知識（台灣講師口播備忘）**：
  > 「台灣無人機與國防科技（Defense Tech）是近年政府與創投（如國發基金、台杉投資）極力扶植的重點。VC 在評估無人機新創時，重點在於 **『非紅供應鏈』自主研發比例**、**自研飛控電腦**、**軍規酬載整合能力** 以及 **政府災防/國防標案落地能力**。」

#### 📋 講師課堂示範指令（直接複製發送給 Claude）：
```markdown
請使用 Playwright MCP 造訪台灣無人機廠商智飛科技官網 (https://www.taiwan-uav.com) 與經緯航太官網 (https://www.geosat.com.tw)，擷取兩家公司的核心技術訴求。幫我產出一份「台灣無人機產業競品分析報告」，包含：核心產品類別（如垂直起降 VTOL、災防/軍規）、自研飛控能力與應用場景對照表。
```

---

### 📌 案例 2：矽光子與邊緣 AI 晶片 (Silicon Photonics & Edge AI) 市場地圖

- **目標新創 1**：**創鑫智慧 (NEUCHIPS)**（專注於 AI 推論晶片與 GenAI 解決方案）
  - 官網首頁：`https://www.neuchips.ai`
- **目標新創 2**：**耐能智慧 (Kneron)**（全球領先的邊緣 AI NPU 晶片廠商）
  - 官網首頁：`https://www.kneron.com`
- **💡 創投背景小知識（台灣講師口播備忘）**：
  > 「隨著台積電推動矽光子 (Silicon Photonics / CPO) 聯盟，台灣半導體 AI 晶片新創成為全球 VC 焦點。VC 做市場地圖時，會比較哪家晶片提供更高能效比 (TOPS/W)、是否支援地端 LLM 運行，以及能否整合至台灣優勢的高階封裝供應鏈。」

#### 📋 講師課堂示範指令（直接複製發送給 Claude）：
```markdown
請使用 Playwright MCP 造訪台灣 AI 晶片新創創鑫智慧 (https://www.neuchips.ai) 與耐能智慧 (https://www.kneron.com)，比較兩家的產品與技術定位。請擷取兩家的：1. 核心 AI 晶片架構與訴求 2. 目標應用場景（伺服器加速 vs 邊緣終端）3. 能效與算力優勢，並整理成 Markdown 競品對照矩陣。
```

---

### 📌 案例 3：台灣標的發現與新創生態圈 (Deal Sourcing Tracker)

- **目標網站**：**創業小聚 Meet** (`https://meet.bnext.com.tw`) 或 **FINDIT 台灣新創平台** (`https://findit.org.tw`)
- **💡 創投背景小知識（台灣講師口播備忘）**：
  > 「在台灣做 Deal Sourcing，創投分析師最常關注『創業小聚 (Meet Startup)』與『FINDIT 平台』的報導。從 Meet Neo Star 評選或最新的募資新聞中，挑選出具備外銷潛力或 AI 轉型能力的台灣早期團隊。」

#### 📋 講師課堂示範指令（直接複製發送給 Claude）：
```markdown
請使用 Playwright MCP 造訪台灣創業小聚網站 (https://meet.bnext.com.tw)，瀏覽最新報導與新創新聞，挑選 3 家近期受到關注的台灣新創公司。請整理出：公司名稱、所屬賽道（如 AI、醫療、綠能、物聯網）、核心解決方案與官網連結。
```

---

### 📌 案例 4：台灣工業 AI / SaaS 投後營運與擴張追蹤 (Portfolio Health Check)

- **目標新創**：**Profet AI 杰倫智能**（台灣製造業 AI AutoML SaaS 領導廠商）
  - 官網首頁：`https://www.profetai.com`
  - 招募頁面：`https://www.profetai.com/careers`（若網址變更請從首頁選單點擊導覽）
- **💡 創投背景小知識（台灣講師口播備忘）**：
  > 「Profet AI 是台灣工業 AI 的代表性新創，協助半導體與 PCB 製造廠實現 AI 智動化。VC 進行投後管理時，會觀察該公司是否正在擴招『海外市場（日本、東南亞）業務團隊』，以此驗證其產品海外複製的成長動能。」

#### 📋 講師課堂示範指令（直接複製發送給 Claude）：
```markdown
請使用 Playwright MCP 造訪台灣工業 AI 新創 Profet AI 官網 (https://www.profetai.com)，導覽至其產品介紹頁與招募頁面。統計該公司主打的製造業 AI 應用場景，以及目前招募的職缺類型，產出一份「Profet AI 產品定位與海外擴張訊號報告」。
```

---

## 🛠️ 實作範例：打造「台灣硬體與 AI 新創盡職調查 Skill」

將這套流程標準化為符合 Claude 規範的 `SKILL.md` 範本，可直接放置於 `.claude/skills/taiwan-tech-dd/SKILL.md`：

```yaml
---
name: taiwan-tech-due-diligence
description: 當使用者提供台灣硬體（無人機、矽光子/AI晶片）或 AI 新創官網 URL 時，結合 Playwright MCP 自動進行台灣產業特性檢視與競品對照報告。
---

# 台灣 DeepTech & AI 新創盡職調查 Skill

## 任務目標
針對台灣在地新創（無人機、矽光子/半導體、工業 AI 等），結合 Playwright MCP 進行官網動態擷取、供應鏈與技術特點分析，產出投資前評估報告。

## 執行流程 SOP

### 第一階段：Playwright 動態擷取 (Target Taiwan Startup)
1. 使用 Playwright MCP 開啟指定之台灣新創官網 URL。
2. 擷取首頁之核心技術價值主張 (Value Proposition) 與產品規格。
3. 自動導覽至網站中的 `/products` (產品)、`/solutions` (解決方案)、`/about` (團隊背景) 與 `/careers` (招募狀態) 頁面。

### 第二階段：台灣產業鏈特色分析
1. 檢視產品是否符合「非紅供應鏈」或「半導體/矽光子生態系整合」。
2. 透過搜尋引擎查詢其主要台灣或國際競品，使用 Playwright 開啟競品官網。

### 第三階段：商業分析與報告產出
綜合以上擷取之數據，輸出符合以下格式的 Markdown 報告：

1. **Executive Summary（執行摘要）**：100 字極簡說明產品技術與市場切入點。
2. **Technical & Supply Chain Advantages（技術與供應鏈優勢）**：分析其在台灣半導體/硬體製造鏈中的優勢與壁壘。
3. **Competitor Comparison Matrix（競品分析矩陣）**：以 Markdown 表格比較目標公司 vs 主要競品。
4. **Hiring & Market Expansion Signals（招募與市場擴張訊號）**：分析其團隊擴張與海外落地進度。
5. **Key Questions for Founder（創辦人訪談關鍵問題）**：針對專利壁壘、客戶驗證 (PoC) 進度與毛利率提出 3–5 個建議問題。
```

---

## 📚 非創投背景講師：VC 核心術語與台灣產業講義備忘手冊

上課時如果學員問起創投術語，可以參考以下簡明解說表：

| 創投術語 (Term) | 講師秒懂解釋（課堂口播法） | 台灣產業實例說明 |
| :--- | :--- | :--- |
| **Deal Sourcing** | 「像探星獵人一樣，主動在網路上尋找剛起步、有潛力的新創公司。」 | 在創業小聚或 Meet Neo Star 清單中發掘潛在投資標的。 |
| **Due Diligence (DD)** | 「買房前的驗屋！掏錢投資前，把產品技術、專利、團隊與競品查個水落石出。」 | 使用 Playwright MCP 前往無人機新創官網檢查自研飛控與專利宣告。 |
| **Market Mapping** | 「繪製產業地圖，把市面上的主要玩家依照技術定位與價格排成對照表格。」 | 比對台灣創鑫智慧 (Neuchips) 與耐能 (Kneron) 的邊緣 AI 晶片定位。 |
| **Portfolio Management**| 「投資後的售後服務與健康追蹤，定期關注已投公司有沒有在好好招募與做產品更新。」 | 進入 Profet AI 官網觀察是否有開出日本或東南亞市場的業務職缺。 |
| **DeepTech (深科技)**| 「以硬科技、半導體、矽光子、生醫為核心，技術門檻極高、研發週期較長的新創。」 | 如矽光子 CPO 封裝、邊緣 AI NPU 晶片、軍規無人機系統等。 |
| **PoC (Proof of Concept)**| 「概念驗證。新創要把產品拿到客戶工廠或真實環境試跑，證明技術可行。」 | 台灣工業 AI 新創在半導體廠進行 AI 瑕疵檢測的 PoC 驗證。 |

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
3. **FileSystem MCP**：將產出的報告自動儲存至團隊的 `/Investment_Reports/Taiwan_Startups/` 目錄中。
4. **Notion / Slack Connector (Remote MCP)**：自動將重點摘要同步張貼至團隊的 Slack `#deal-flow` 頻道或更新至 Notion 投資案資料庫中。

---

← [返回 Skills 主頁](../README.md) | [返回專案首頁](../../README.md)
