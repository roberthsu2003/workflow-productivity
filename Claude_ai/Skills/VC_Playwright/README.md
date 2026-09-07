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
| **案例 3：台灣新創標的發現 (Deal Sourcing)** | • 創業小聚 ([meet.bnext.com.tw](https://meet.bnext.com.tw)) <br>• FINDIT 平台 ([findit.org.tw](https://findit.org.tw)) | 台灣 Meet Neo Star 評選熱門、早期募資訊號、垂直賽道潛力 |
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
## Task
請使用 Playwright MCP 造訪台灣無人機廠商：
1. 智飛科技官網：https://www.taiwan-uav.com
2. 經緯航太官網：https://www.geosat.com.tw

擷取兩家公司的核心技術訴求，幫我產出一份「台灣無人機產業競品分析報告」。

## Format (Optional)
包含：
- 核心產品類別（如垂直起降 VTOL、災防/軍規）
- 自研飛控能力
- 應用場景對照表（Markdown 表格）
```

---

### 📌 案例 2：矽光子與邊緣 AI 晶片 (Silicon Photonics & Edge AI) 市場地圖

- **目標新創 1**：**創鑫智慧 (NEUCHIPS)**（專注於 AI 推論晶片與 GenAI 解決方案）
  - 官網首頁：`https://www.neuchips.ai`
- **目標新創 2**：**耐能智慧 (Kneron)**（全球領先的邊緣 AI NPU 晶片廠商）
  - 官網首頁：`https://www.kneron.com`
- **💡 創投背景小知識（台灣講師口播備忘）**：
  > 「隨著台積電推動矽光子 (Silicon Photonics / CPO) 聯盟，台灣半導體 AI 晶片新創成為全球 VC 焦點。VC 做市場地圖時，會比較哪家晶片提供更高能效比 (TOPS/W)、是否支援地端 LLM 運行，以及能否整合至台灣優勢的高階封裝供應鏈。」

#### 📋 示範指令（直接複製發送給 Claude）：
```markdown
## Task
請使用 Playwright MCP 造訪台灣 AI 晶片新創：
1. 創鑫智慧：https://www.neuchips.ai
2. 耐能智慧：https://www.kneron.com

比較兩家的產品與技術定位。

## Format (Optional)
請擷取兩家的：
1. 核心 AI 晶片架構與訴求
2. 目標應用場景（伺服器加速 vs 邊緣終端）
3. 能效與算力優勢
並整理成 Markdown 競品對照矩陣。
```

---

### 📌 案例 3：台灣標的發現與新創生態圈 (Deal Sourcing Tracker)

- **目標網站**：**創業小聚 Meet** (`https://meet.bnext.com.tw`) 或 **FINDIT 台灣新創平台** (`https://findit.org.tw`)
- **💡 創投背景小知識（台灣講師口播備忘）**：
  > 「在台灣做 Deal Sourcing，創投分析師最常關注『創業小聚 (Meet Startup)』與『FINDIT 平台』的報導。從 Meet Neo Star 評選或最新的募資新聞中，挑選出具備外銷潛力或 AI 轉型能力的台灣早期團隊。」

#### 📋 示範指令（直接複製發送給 Claude）：
```markdown
## Task
請使用 Playwright MCP 造訪台灣創業小聚網站 (https://meet.bnext.com.tw)，
瀏覽最新報導與新創新聞，挑選 3 家近期受到關注的台灣新創公司。

## Format (Optional)
請整理出 Markdown 表格，包含：
- 公司名稱
- 所屬賽道（如 AI、醫療、綠能、物聯網）
- 核心解決方案
- 官網連結
```

---

### 📌 案例 4：台灣工業 AI / SaaS 投後營運與擴張追蹤 (Portfolio Health Check)

- **目標新創**：**Profet AI 杰倫智能**（台灣製造業 AI AutoML SaaS 領導廠商）
  - 官網首頁：`https://www.profetai.com`
  - 招募頁面：`https://www.profetai.com/careers`（若網址變更請從首頁選單點擊導覽）
- **💡 創投背景小知識（台灣講師口播備忘）**：
  > 「Profet AI 是台灣工業 AI 的代表性新創，協助半導體與 PCB 製造廠實現 AI 智動化。VC 進行投後管理時，會觀察該公司是否正在擴招『海外市場（日本、東南亞）業務團隊』，以此驗證其產品海外複製的成長動能。」

#### 📋 示範指令（直接複製發送給 Claude）：
```markdown
## Task
請使用 Playwright MCP 造訪台灣工業 AI 新創 Profet AI 官網 (https://www.profetai.com)，
導覽至其產品介紹頁與招募頁面。

## Format (Optional)
統計該公司主打的製造業 AI 應用場景，以及目前招募的職缺類型，
產出一份「Profet AI 產品定位與海外擴張訊號報告」。
```

---

## 🛠️ 實作範例：打造「台灣硬體與 AI 新創盡職調查 Skill」

將這套流程標準化為符合 Claude 規範的 `SKILL.md` 範本，可直接放置於 `.claude/skills/taiwan-tech-dd/SKILL.md`：

```yaml
---
name: taiwan-tech-due-diligence
description: >-
  當使用者提供台灣硬體（無人機、矽光子/AI晶片）或 AI 新創官網 URL 時，
  結合 Playwright MCP 自動進行台灣產業特性檢視與競品對照報告。
---

# 台灣 DeepTech & AI 新創盡職調查 Skill

## 提示詞與執行 SOP（RTCCF 架構）

- **Role (角色)**：創投資深 DeepTech 投資分析師與台灣半導體/硬體產業研究員。
- **Task (任務)**：結合 Playwright MCP 自動導覽台灣硬體與 AI 新創官網，擷取核心產品技術規格、供應鏈定位與招募訊號，並產出投資前初審評估報告。
- **Context (背景與資源)**：
  1. 第一階段（Playwright 動態擷取）：開啟指定 URL，導覽首頁、`/products`、`/solutions`、`/about` 及 `/careers` 頁面擷取價值主張與招募訊號。
  2. 第二階段（台灣產業鏈對照）：檢視產品是否符合「非紅供應鏈」或「半導體/矽光子生態系整合」，並透過搜尋開啟主要競品官網。
- **Constraint (限制與規範)**：
  1. 數據必須來自官網與公開搜尋之真實資訊，不得臆測捏造。
  2. 若網頁載入失敗或有動態 DOM，必須等待元件載入完成 (`wait_for_selector`) 後再擷取。
  3. 創辦人提問單須聚焦專利壁壘、客戶 PoC 進度與毛利率。
- **Format (輸出格式)**：產出包含以下 5 大章節的 Markdown 報告：
  1. **Executive Summary（執行摘要）**：100 字極簡說明產品技術與市場切入點。
  2. **Technical & Supply Chain Advantages（技術與供應鏈優勢）**：分析其在台灣半導體/硬體製造鏈中的優勢與壁壘。
  3. **Competitor Comparison Matrix（競品分析矩陣）**：以 Markdown 表格比較目標公司 vs 主要競品。
  4. **Hiring & Market Expansion Signals（招募與市場擴張訊號）**：分析其團隊擴張與海外落地進度。
  5. **Key Questions for Founder（創辦人訪談關鍵問題）**：針對專利壁壘、客戶驗證 (PoC) 進度與毛利率提出 3–5 個建議問題。
```
---
## 📝 學員課後自主練習：台灣智慧醫療 AI (MedTech) 投資前初審 Skill

### 🎯 練習目標
請學員運用上課所學的 **Playwright MCP 網頁自動化** 與 **Claude Custom Skill 寫作語法**，打造一個專為創投分析師設計的 **「台灣智慧醫療 AI (MedTech) 標的極速評估 Skill」**。

---

### 📋 練習題目需求

- **目標新創**：**雲象科技 (aetherAI)**（台灣 AI 數位病理與醫療影像領導廠商）
  - 測試網址：`https://aetherai.com`
- **評估情境**：身為創投分析師，你收到雲象科技的案源，需要快速了解其在 AI 數位病理的技術壁壘、醫療器材認證（TFDA / FDA）與合作醫院落地狀況，並產出投資委員會 (IC) 的「MedTech 案源初審報告」。

---

### 💡 給學員的解題提示與指引 (Student Hints & Workflow Guide)

> 💡 **提示 1：創投商業思維 (VC Business Focus)**  
> 醫療 AI (MedTech) 與一般 SaaS 新創不同，VC 最關注的 3 大關鍵指標為：
> 1. **醫療器材許可證 (SaMD)**：是否取得 TFDA (台灣) 或 FDA (美國) 認證？
> 2. **臨床驗證與標竿醫院**：合作的醫學中心有哪些（如台大、榮總、長庚）？
> 3. **AI 模型數據源與專利**：病理切片標註資料量與影像辨識準確率訴求。

> 💡 **提示 2：Playwright MCP 網頁導覽技巧 (Playwright Navigation Rules)**  
> 在撰寫 `SKILL.md` 的 SOP 時，請務必提示 Claude 執行以下步驟：
> 1. 使用 Playwright MCP 開啟 `https://aetherai.com`。
> 2. 導覽至選單中的 `/solutions` (解決方案) 或 `/news` (最新消息)，擷取認證與醫院合作資訊。
> 3. 遇 DOM 動態選單時，設定「等待元件載入完成 (wait_for_selector)」，確保不會抓取到空白頁面。

> 💡 **提示 3：Skill YAML 與 SOP 定義參考 (SKILL.md Template - RTCCF 架構)**  
> 學員可在 `.claude/skills/medtech-ai-dd/SKILL.md` 中嘗試撰寫以下結構：

```yaml
---
name: medtech-ai-evaluator
description: >-
  當輸入醫療 AI 新創官網時，利用 Playwright MCP 擷取 TFDA/FDA 認證、
  臨床合作醫院並生成 MedTech 投資評估報告。
---

# 智慧醫療 AI 標的評估 SOP（RTCCF 架構）

- **Role (角色)**：創投智慧醫療 (MedTech) 領域投資經理與醫療器材監管分析師。
- **Task (任務)**：造訪醫療 AI 新創官網，擷取醫療器材認證 (SaMD)、臨床合作醫院實績與 AI 病理/影像技術壁壘，生成投資委員會 (IC) 案源初審報告。
- **Context (背景與資源)**：
  1. 開啟目標官網（如 `https://aetherai.com`），導覽至 `/solutions` 或 `/news` 頁面。
  2. 擷取 TFDA (台灣) / FDA (美國) 醫療器材許可證與專利標示。
  3. 統計合作之醫院與醫學中心名單以驗證臨床落地能力。
- **Constraint (限制與規範)**：
  1. 嚴格區分「已取得認證」與「臨床進行中/申請中」狀態，不可混淆。
  2. 遇到 DOM 動態選單時，須等待元件載入完成再進行擷取，避免抓取空白頁。
  3. 著重評估 SaMD 法規壁壘、醫院通路與模型數據源。
- **Format (輸出格式)**：輸出包含「法規壁壘與認證狀態」、「臨床驗證與標竿醫院」、「技術與數據壁壘」、「創投評估建議與提問單」之 Markdown 報告。
```

---

### 🏆 驗收標準 (Completion Criteria)
- [ ] 成功使用 Playwright MCP 造訪 `https://aetherai.com` 並動態擷取產品與合作夥伴頁面。
- [ ] 報告中需明確列出該公司獲得的 **TFDA/FDA 認證狀態** 或 **臨床醫院落地實績**。
- [ ] 產出一份符合創投 IC 會議標準的 Markdown 「MedTech 案源初審報告」。

---

← [返回 Skills 主頁](../README.md) | [返回專案首頁](../../README.md)
