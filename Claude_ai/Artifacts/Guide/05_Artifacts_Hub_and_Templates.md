# Artifacts 獨立工作中心與三大原生創作模板（Docs / Slides / Design）

> 深入解析 Anthropic 2026 最新「One Claude」整合架構：從獨立導航中心管理個人與團隊成品資產，以及如何運用 Docs、Slides、Design 三大原生模板實現高效率的雲端協同與多格式匯出。

---

## 🌟 為什麼這是 Artifacts 的里程碑大升級？

過去的 Claude Artifacts 主要定位為**「對話側欄的程式碼與內容渲染畫布」**——只有當你在對話中要求 Claude 產出較長的文章或代碼時，右側才會被動彈出視窗。

最新升級將 Artifacts 昇華為**全功能的 Web-Native 雲端數位資產與創作工作中心（Artifacts Hub / Workspace）**：
1. **Claude Design 正式回歸並常駐**：不再是分立的獨立站點，所有設計專案與簡報原生整合在 Artifacts 體系內。
2. **獨立的導航入口與數位資產庫**：隨時在左側選單進入 Artifacts 首頁，集中管理所有歷史產出、按類型篩選、切換網格與清單檢視。
3. **「Make something new」三大原生創作模板（Beta）**：無需透過空白對話手動撰寫複雜提示詞，直接點擊 **Docs**、**Slides** 或 **Design** 即可快速啟動標準化任務！

```mermaid
graph TD
    subgraph 過去的模式：對話附屬畫布
        O1["💬 空白對話"] --> O2["下達長篇指令"] --> O3["右側被動彈出側欄畫布"]
    end

    subgraph 2026 最新模式：Web-Native 創作與資產中心
        H["🗂️ Artifacts 獨立中心 (Hub)"]
        H --> T1["📄 Claude Docs (Beta)<br/>（協同文件 / 企劃 / 報告）"]
        H --> T2["📑 Claude Slides (Beta)<br/>（簡報 Deck / 線上演練）"]
        H --> T3["📱 Claude Design (Beta)<br/>（UI/UX 原型 / 視覺版型）"]
        H --> T4["💻 經典 Artifacts<br/>（HTML/React/SVG/Mermaid）"]
        
        T1 --> E1["📤 雙向匯出：Word / Google Docs / PDF"]
        T2 --> E2["📤 雙向匯出：PowerPoint (.pptx) / PDF"]
        T3 --> E3["🌐 一鍵發布 Publish / 嵌入網頁"]
    end
```

---

## 🗂️ Artifacts 獨立工作中心（Hub）介面全解

在 Claude 介面點選 **Artifacts**，即可進入專屬資產管理大廳：

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  Artifacts                                                                   │
│  [All]  [Yours]  [Shared with you]                         [🔍] [🔲] [All types ▾]
├──────────────────────────────────────────────────────────────────────────────┤
│  📢 Claude Design lives here now                                             │
│     New Slides and Design projects are created as artifacts.                 │
│     [Visit the standalone homepage ↗]                                        │
├──────────────────────────────────────────────────────────────────────────────┤
│  Make something new                                                          │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐                      │
│  │   📄 Docs    │   │  📑 Slides   │   │  📱 Design   │                      │
│  │    [Beta]    │   │    [Beta]    │   │    [Beta]    │                      │
│  └──────────────┘   └──────────────┘   └──────────────┘                      │
├──────────────────────────────────────────────────────────────────────────────┤
│  我的數位資產庫 (Recent Artifacts) ...                                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 1. 三大分類標籤（Filter Tabs）
- **All（全部）**：匯總所有你擁有編輯權限或瀏覽過的成品。
- **Yours（我建立的）**：專屬個人帳號產出的所有數位作品，便於檢索個人重要企劃或專案。
- **Shared with you（與我共享的）**：在團隊（Team / Enterprise）內部由同事或外部合作夥伴透過連結分享給你的成品庫。

### 2. 強大檢索與檢視工具
- **搜尋框（Search）**：支援成品標題與關鍵字即時模糊比對，數秒內找回數月前做好的報表。
- **檢視模式切換（View Toggle）**：
  - **卡片網格視圖（Grid View）**：以縮圖視覺預覽為導向，最適合挑選簡報、UI 原型與圖表。
  - **清單列表視圖（List View）**：以建立時間、修改時間與檔案類型為導向，最適合快速批次整理公務文件。
- **類型過濾器（`All types` 下拉選單）**：
  - 一鍵篩選：`Docs`、`Slides`、`Design`、`Code`、`Interactive Web Apps` 等。

---

## 📄 專題一：Claude Docs (Beta) 深度實務

### 什麼是 Claude Docs？
Claude Docs 是專為知識工作者設計的「Web-native 雲端原生協同文件」。它徹底改變了過去生成純文字必須手動複製進 Word 的繁瑣步驟。

### 核心特性
1. **所見即所得與劃詞編修**：在右側畫布上，你可以像使用 Notion 或 Google Docs 一樣，直接選取特定段落，要求 Claude「換成更委婉的語氣」、「擴寫這段市場數據」，或是自行手動打字微調。
2. **多方即時協作**：團隊成員可透過分享連結同時進入同一個 Doc，留下評論（Comments）或共同進行校對。
3. **無損格式匯出**：確認完畢後，點擊匯出即可下載為 **Microsoft Word (.docx)**、**Google Docs** 或 **PDF**，格式排版、標題層次完全保留。

### 🎯 實戰 Prompt 範例：跨國產品發佈會新聞稿與執行企劃

```markdown
## Role
你是一位資深科技公關總監（PR Director）與文案專家。

## Task
請在 Claude Docs 中建立一份完整專業的「新一代企業 AI 協同平台發布企劃與新聞稿」。

## Context
- 產品名稱：NexusWork AI 2026
- 主要亮點：整合跨部門知識沙盒、零延遲語音即時決策記錄、端到端機密資料去識別化。
- 目標媒體：數位時代、TechCrunch、彭博商業周刊。

## Format
- 使用 Claude Docs 結構排版：包含發表會時間表、新聞稿主標/副標、公關聯繫資訊、Executive Summary 表格與 FAQ 模組。
```

---

## 📑 專題二：Claude Slides (Beta) 深度實務

### 什麼是 Claude Slides？
以往讓 AI 做 PPT，大多只是吐出大綱文字，或需靠第三方外部外掛轉檔。Claude Slides 讓 Claude 具備了**原生簡報引擎**！

### 核心特性
1. **完整 Deck 自動佈局**：輸入大綱或長篇報告，Claude 會自動將內容拆解成具備合適版面（單欄、對比雙欄、四宮格矩陣、重點數據大字）的完整簡報組。
2. **線上放映模式（Presentation Mode）**：開會時無需下載，直接在瀏覽器點擊全螢幕播放按鈕，透過方向鍵即可切換翻頁，甚至能現場針對長官提問，在簡報旁邊叫 Claude「把第 3 頁的柱狀圖加上 2026 預測值」。
3. **原生 PPTX 匯出**：支援一鍵下載為標準 **Microsoft PowerPoint (.pptx)** 或 **PDF**，下載後的文字與版塊均為向量物件，能在本機 Office 中二次換皮換色。

### 🎯 實戰 Prompt 範例：高階管理層季度業務回顧（QBR Deck）

```markdown
## Role
你是一位頂級管理顧問與商務簡報設計師。

## Task
請使用 Claude Slides 產生一份共 6 頁的「2026 Q3 智慧製造轉型專案階段成果匯報」。

## Content Outline
- Slide 1：封面（專案名稱、報告人、日期）。
- Slide 2：專案執行摘要（Executive Summary，以 3 大 KPI 亮點大字呈現）。
- Slide 3：痛點分析與原先產線瓶頸對照（左邊痛點、右邊解決方案）。
- Slide 4：導入效益指標（良率提升 14.8%、巡檢工時減少 40% 的數據儀表）。
- Slide 5：目前面臨挑戰與風險因應對策表。
- Slide 6：Q4 關鍵里程碑時程規劃（Timeline）。

## Style
- 現代俐落風格、高階商務深藍搭亮金配色、每頁維持簡報少字精確原則。
```

---

## 📱 專題三：Claude Design (Beta) 深度實務

### 什麼是 Claude Design？
Anthropic 於 2026 年春季推出獨立測試的視覺設計工具，現已全面整合入 Artifacts。它能精準理解設計語言（包含間距、排版字級、配色系統與組件狀態），產出極具視覺質感的動態 UI 原型與設計資產。

### 核心特性
1. **自然語言驅動的設計原稿**：輸入「請幫我設計一個支援深色模式的智慧手錶健康監測 App 主畫面」，Claude 能生成高質感的互動元件、自訂圖示與精確排版。
2. **免切換環境**：設計出的成果直接以 Artifact 形式留存於個人的資產庫中，能隨時返回重複精修。
3. **無縫銜接開發**：設計成品同時提供 Design 預覽視圖與底層 Clean Code，工程師可直接複製代碼快速部署。

---

## 🔒 方案權限與環境配置一覽

| 功能項目 | 🟢 Free 方案 | 🔵 Pro / Max 方案 | 🏢 Team / Enterprise 方案 |
| :--- | :---: | :---: | :---: |
| **經典 Artifacts**（HTML/React/SVG/Mermaid） | ✓ 完全免費 | ✓ 高用量上限 | ✓ 組織共用 |
| **Artifacts 獨立管理中心 (Hub)** | ✓ 基礎檢視 | ✓ 完整資產管理 | ✓ 組織權限過濾與搜尋 |
| **Docs 模板 (Beta)** | 預計後續釋出 | ✓ **即刻可用** | ✓（企業管理者後台開啟） |
| **Slides 模板 (Beta)** | 預計後續釋出 | ✓ **即刻可用** | ✓（企業管理者後台開啟） |
| **Design 模板 (Beta)** | 預計後續釋出 | ✓ **即刻可用** | ✓（企業管理者後台開啟） |
| **Office/PPT/PDF 原生匯出** | 支援純程式碼生成 | ✓ **一鍵原生轉出** | ✓ 組織檔案相容 |

> [!IMPORTANT]
> **必要前置設定**：  
> 若要順暢使用 Docs / Slides / Design 以及各種複雜的代碼運算，請確認帳號已開啟代碼執行功能：  
> 前往 **`Settings` ➔ `Capabilities` ➔ 開啟「Code execution and file creation」**。

---

## 💡 總結：新舊工作流的完美融合

有了 Artifacts Hub 與三大原生模板後，你的日常工作流程將更具彈性：
- 想要快速產出報告或簡報？直接進入 **Artifacts Hub** 點選 **Docs** 或 **Slides**。
- 想要討論複雜演算法或內部行政網頁？在 **對話中要求產出 HTML / React / Markdown**。
- 不論哪種方式產出的成品，都會整整齊齊收納在 **Artifacts Hub** 的個人數位資產庫中，再也不怕重要成果被對話洗版淹沒！
