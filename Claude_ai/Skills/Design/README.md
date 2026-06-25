# 實作練習：使用現有的 Skill（設計與品牌實戰）

> 🟢 **方案需求**：Free（需先在 Settings 開啟 Skills 與程式碼執行）  
> 🎨 **設計主軸**：教導 Claude 透過官方的設計與品牌 Skills 確保輸出具有高度的一致性與專業視覺美感。

本章節介紹如何呼叫官方在設計與品牌類別提供的 4 個 Skills：**brand-guidelines、canvas-design、theme-factory、algorithmic-art**。以下提供每個 Skill 的操作說明與直接複製使用的 RTCCF Prompt。

---

## 🛠️ 前置步驟（只需做一次）

1. 開啟 **Claude Desktop** 或 Web 版的 **Settings**
2. 確認已在 `Capabilities` 開啟 **Cloud code execution and file creation** 
3. 在 `Skills` 區段確認已掛載或啟用設計類相關 Skill。
4. 在對話框輸入 `/` 可預覽目前可用的 Skill 清單。

---

## 練習 A：使用 `brand-guidelines` 建立品牌化產品介紹

### 📖 說明
當您需要讓 Claude 的回答或產出的 Artifacts 符合特定企業識別時，`brand-guidelines` 會自動帶入標準色彩（例如 Orange `#d97757`、Blue `#6a9bcc` 等）與字型（Poppins、Lora），讓產出的文件具有一致的品牌質感，而不是單調的預設排版。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是一位資深品牌視覺規劃師，擅長運用 brand-guidelines 技能，將零散的產品特色轉化為符合品牌視覺規範的精美網頁介紹。

## Task
請幫我將下方提供的新產品資訊，整理成一份精美的產品介紹頁面。請先使用 Artifacts 預覽，並調用 brand-guidelines 確保配色、字型與間距完全符合企業視覺標準。

## Context
新產品資訊：
- 產品名稱：Zenith 智能手錶
- 核心賣點：極致省電（30天續航）、AI 睡眠追蹤、航太級鈦金屬錶殼
- 產品定位：高端商務與戶外運動愛好者
- 定價：$8,990 元

## Constraint
- 語言：繁體中文
- 排版樣式：
  1. 頂部必須有明顯的 Hero Section（大圖配標題）
  2. 產品賣點需使用並排卡片（Cards）呈現
  3. **調用規定**：請主動套用 brand-guidelines 中的配色規範（使用定義的橘色與藍色作為主要/次要色調），並使用 Poppins 作為標題字型，Lora 作為內文字型。

## Format
- 以 HTML/CSS 的 Artifact 呈現精美的單頁產品介紹
- 完成後回傳說明你套用了哪些 brand-guidelines 視覺規範
```

---

## 練習 B：使用 `canvas-design` 規劃社群貼文視覺排版

### 📖 說明
`canvas-design` Skill 讓 Claude 能夠理解 2D 畫布、圖層、字型大小與排版間距的概念。您可以透過此技能讓 Claude 輸出具有層次感的社群媒體貼文、海報或資訊圖表的佈局設計。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是社群媒體視覺設計師，擅長使用 canvas-design 技能在 2D 畫布上精準配置圖文資訊。

## Task
請幫我設計一張用於 Facebook 推廣「AI 自動化工作坊」課程的宣傳海報版面佈局。

## Context
活動資訊：
- 主題：AI 職場自動化實戰班
- 時間：7/18 (六) 14:00 - 17:00
- 亮點：0 基礎也能學會、手把手打造數位分身
- 行動呼籲：限額 30 名，掃碼報名！

## Constraint
- 語言：繁體中文
- 畫布規格與排版邏輯：
  1. 尺寸：1200 x 630 像素（標準 FB 貼文尺寸）
  2. 調用 canvas-design 技能規劃至少三個圖層（背景層、圖形元素層、文字資訊層）
  3. 主標題字級需為副標題的 2.5 倍，確保視覺焦點
  4. 邊距（Padding）需至少保留 60 像素，避免元素過於擁擠

## Format
- 在 Artifact 中以 SVG 或 HTML 呈現海報的視覺佈局草圖
- 詳細列出您在 canvas-design 中所設定的各圖層位置、尺寸、字型大小與色彩數值
```

---

## 練習 C：使用 `theme-factory` 生成專業配色方案

### 📖 說明
`theme-factory` 內建了 10 組精心挑選的專業色彩與字型組合（例如「Ocean Depths」、「Modern Minimalist」、「Tech Innovation」等）。您只要指定風格，它就能為您產生一套完整的配色與元件庫主題。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是前端 UI 設計工程師，擅長運用 theme-factory 快速產出符合特定風格的主題樣式與元件規範。

## Task
我正在開發一個「心理諮商預約平台」的網頁，需要一套讓人感到平靜、信任且優雅的配色與字型主題。請使用 theme-factory 為我產生對應的主題，並展示範例元件。

## Context
平台調性：溫暖、平靜、專業、放誠、療癒。

## Constraint
- 語言：繁體中文
- 主題規定：
  1. 請調用 theme-factory 中的「Teal Trust」（青綠/海泡綠/薄荷綠）或「Sage Calm」（鼠尾草綠/尤加利綠/石板灰）配色主題。
  2. 配色必須包含：主色、輔助色、背景色、文字深色、文字淺色。
  3. 元件展示：在頁面中必須展示該主題下的「按鈕狀態（主、次、Hover）」、「輸入框」與「卡片元件」。

## Format
- 使用 HTML/CSS 建立一個互動式主題展示頁面（Artifact）
- 回傳調用 theme-factory 輸出的配色代碼（HEX）與字型設定說明
```

---

## 練習 D：使用 `algorithmic-art` 產生程序化幾何視覺

### 📖 說明
`algorithmic-art` 能夠利用 p5.js 或 canvas 程式碼，透過演算法動態生成幾何藝術、動態粒子或數據視覺化作品。這適合用於製作炫目的網頁背景或互動式視覺藝術。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是創意程式設計師 (Creative Coder)，擅長運用 algorithmic-art 與 p5.js 創加入互動幾何視覺藝術。

## Task
請幫我創作一個以「宇宙引力與星軌」為主題的互動式程序化藝術作品。

## Constraint
- 語言：繁體中文說明
- 技術要求：
  1. 使用 p5.js 框架與 canvas 技術。
  2. 調用 algorithmic-art 動態計算多個粒子圍繞中心引力點旋轉的軌跡。
  3. 必須支援互動：滑鼠移動時，引力點位置隨滑鼠改變，且粒子旋轉軌跡產生波動。
  4. 漸層配色：使用深邃的星空黑為背景，粒子使用螢光藍與霓虹紫的漸層。

## Format
- 在 Artifact 中輸出完整的 p5.js 程式碼，使其能直接在瀏覽器中渲染與互動
- 簡要說明粒子運動的物理演算法公式（如萬有引力公式之模擬）
```

---

## ✅ 完成後的下一步

練習完這四個設計範例後，您已掌握：
- 如何讓 AI 的輸出不再是「千篇一律的機器感」，而是套用專業品牌設計。
- 活用 2D 畫布佈局、主題工廠與動態程序藝術。

**下一步**：前往 [工程與開發實戰 (Development)](../Development/README.md)，學習如何讓 Claude 撰寫更強大、可測試的前端 UI 與自訂工具！

---

← [返回 Skills 主頁](../README.md)
