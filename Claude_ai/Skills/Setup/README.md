# Claude Skills 安裝與啟用指南

> [!IMPORTANT]
> **🚀 課堂第一步：3 秒鐘快速實驗（確認你的帳號方案與技能狀態）**
> 
> 由於班上同學的帳號包含 **Free 免費版** 與 **Pro/Team 專業版**，且不同方案對 Skills 的支援度與設定不同。請在授課開始時，請全班同學一起進行以下「快速實驗」，即可立刻釐清每位學生的環境狀態！
> 
> **🧪 實驗步驟**：
> 1. 確認已在個人 Settings → **Capabilities** 中將 **Code execution and file creation** 功能切換為**開啟 (On)**。
> 2. 開啟一個新對話，直接複製並貼上以下指令發送給 Claude：
>    > *「請用內建的 PPTX Skill 幫我規劃一份只有 2 頁的簡報大綱，並直接匯出成 .pptx 簡報檔案供我下載。」*
> 3. **根據 Claude 的回覆，對照下方結果**：
> 
> | 實驗結果 | 帳號狀態 | 該生適用的 Skills 學習路徑 |
> | :--- | :--- | :--- |
> | **A. 順利產生實體簡報檔並提供下載連結** 🎉 | 帳號為 **Pro/Team** 或已獲得代碼執行額度的 **Free（免費版）** | 內建文件技能已自動在雲端生效，**不需手動下載或安裝**即可直接呼叫使用。免費版唯一的區別是**每日有代碼執行額度上限 (Daily Limit)**。 |
> | **B. 出現「您的帳號方案目前不支援」或提示升級** ⚠️ | 尚未獲得代碼執行權限的 **Free（免費版）** | 此時無法使用雲端代碼執行產生實體檔案。教學重點請引導該生走 **「手動建立/下載自訂 Skill (內含 SKILL.md)，並點擊『+』上傳 .zip 檔」** 的自訂技能路線（免費版仍支援此功能）。 |
> | **C. 僅回覆文字大綱，說無法建立實體檔（無方案提示）** ⚙️ | 忘記開啟 **Code execution** | 請引導該生至 Settings → Capabilities 確認將 **Code execution and file creation** 切換為開啟 (On) 後重新測試。 |

---

## 🔍 課堂實作：如何檢查目前對話中有沒有這些 Skills？

當您進行完上述實驗時，可能會發現：**「有些免費版帳號沒有手動安裝，卻一樣能產出 PPTX 或 Excel 檔案！」**
這是因為：
* **文件類技能的原理**：當您在 Capabilities 中開啟了 **Code execution**（代碼執行），即便帳號中沒有安裝正式的 `pptx` 或 `xlsx` 技能，Claude 也能在雲端沙盒中**直接撰寫 Python 程式碼**（利用內建的 `python-pptx`、`pandas` 等庫）來為您生成與下載實體檔案。
* **其他非文件技能的原理**：如 `brand-guidelines`、`theme-factory` 等，免費版在未手動上傳時通常沒有預載，故需要走手動上傳 `.zip` 檔安裝。

為了讓學生清楚了解自己帳號目前到底載入了哪些技能，我們需要進行實際檢查。

> [!WARNING]
> **⚠️ 釐清斜線指令（Slash command）的迷思**
> 
> 在網頁版或桌面版 **claude.ai** 中，輸入 `/` **並不會**像終端機一樣彈出 `/pptx` 或 `/theme-factory` 這類的斜線技能選單！Skills 在圖形介面中是**自動偵測並在背景隱性觸發的**，不需也無法手動輸入斜線指令。

因此，在實際操作上，若要檢查對話中載入了哪些技能，唯一的檢查方法是**在對話中直接貼上「自我診斷 Prompt」讓 Claude 報告**：

### 📋 檢查方法：貼上「自我診斷 Prompt」讓 Claude 報告

請開啟一個全新對話，複製並發送以下提示詞，請 Claude 盤點其當前已載入的技能：

> 💬 **診斷提示詞**：
> *「請檢查目前此對話中，你是否有載入任何系統 Skills（技能）？如果是透過執行 Python 程式碼來產生 PPT、Excel 或 Word 檔案，請告訴我你載入了哪些 Skills（如 docx, pptx, xlsx, frontend-design, skill-creator 等），並簡要說明你的產出檔案流程與使用的庫。」*

---

### 💡 深入底層：Claude.ai 內建 Skills 的「雙層結構」架構

根據對 Claude 沙盒環境的實測，Claude.ai 在背景掛載的 Skills 其實是由**「自動啟用的核心技能」**與**「磁碟上的範例參考技能」**所組成的雙層磁碟結構（通常位於 `/mnt/skills/` 目錄下）：

---

#### 1. 📂 `/mnt/skills/public/`（自動啟用的核心 Skills）
這些技能被列在 Claude 系統提示詞的 `<available_skills>` 區塊中。這代表每次對話開始時，Claude **預設就已經「知道」它們的存在**，只要遇到相關指令，它就會**自動觸發**，不需手動上傳或在對話中特別提醒。

##### 📋 `public/` 自動觸發系統 Skills 對照表（共 9 個）
| 技能名稱 (Skill) | 類別 | 用途說明 | 運作庫 / 資源 |
| :--- | :--- | :--- | :--- |
| **`pptx`** | 文件製作 | 建立或編輯 PowerPoint 簡報（.pptx） | `python-pptx` |
| **`docx`** | 文件製作 | 建立、編輯、讀取 Word 文件（.docx） | `python-docx` |
| **`xlsx`** | 文件製作 | 建立或編輯 Excel 試算表（.xlsx） | `openpyxl`、`pandas` |
| **`pdf`** | 文件製作 | 處理 PDF：讀取、合併、分割、建立等 | `pypdf`、`PyPDF2` |
| **`frontend-design`** | 工程開發 | 現代前端 UI 設計、無障礙設計與元件生成 | React, Tailwind, Lucide |
| **`skill-creator`** | 工程開發 | 逐步引導設計、建立或優化自訂技能 | 官方技能模板 |
| **`file-reading`** | 核心讀取 | 讀取與解析上傳的各類檔案內容 | 系統底層 parser |
| **`pdf-reading`** | 核心讀取 | 專門讀取與解析 PDF 內容與表格 | pdfminer 等 |
| **`product-self-knowledge`** | 核心知識 | Anthropic 產品知識與說明文件查詢 | 官方知識庫 |

---

#### 2. 📂 `/mnt/skills/examples/`（範例 Skills，共 24 個）
這些是存放在沙盒磁碟上的範本檔案（預設並未寫入系統提示詞中，因此 Claude 預設「不知道」它們的存在）。但因為檔案確實存在於磁碟上，**只要您在對話中明確指名、或它主動用工具去檢索**，Claude 就會前往該目錄讀取 `SKILL.md`，並完全遵循該範本的規範來執行任務！

##### 📋 `examples/` 磁碟範例 Skills 清單（部分精選）
| 技能名稱 (Skill) | 用途說明 | 課堂實戰應用 |
| :--- | :--- | :--- |
| **`theme-factory`** | 主題樣式配色生成工具 | 可幫 PPT 或 HTML Artifact 一鍵套用 10 種專業主題樣式。 |
| **`canvas-design`** | 2D 畫布與圖層排版設計 | 提供海報、資訊圖表等視覺區塊的比例間距定位。 |
| **`algorithmic-art`** | p5.js 程序與演算法藝術 | 用於生成參數化幾何圖案或網頁互動特效背景。 |
| **`web-artifacts-builder`** | 單頁 Web 應用（SPA）建置 | 專用於 React + shadcn/ui 等高難度網頁應用的程式碼架構。 |
| **`mcp-builder`** | MCP 伺服器規格與對接建置 | 自動設計 Model Context Protocol 伺服器程式碼與 JSON Schema。 |
| **`doc-coauthoring`** | 文件共同撰寫與潤飾 | 協作撰寫長文，重點在於「給予編輯建議而非完全改寫」，保留作者筆調。 |
| **`internal-comms`** | 企業內部高效溝通公告 | 提供 TL;DR、時間線、責任分配等商務通知格式。 |
| *… 還有更多* | *包含財務計算、活動規劃、費用申報、表單處理等共 24 個範例模板。* | - |

---

#### 💡 核心觀念對照：自動觸發（Public） vs. 需指名調用（Examples）
為了方便向學生說明，老師可以使用以下的「員工入職比喻」：

| 比較維度 | 📂 `public/`（自動觸發） | 📂 `examples/`（需明確使用） |
| :--- | :--- | :--- |
| **生動比喻** | 公司給你的**正式工作手冊**（一入職就發在桌上） | 放在**公司檔案室裡的歷史參考檔案**（要自己去查或被交代才看） |
| **Claude 的認知** | 預設就知道（寫在系統提示詞中） | 預設不知道（但可用磁碟讀取工具讀取） |
| **是否需提醒？** | **不需要**，直接說「幫我做一個簡報」即可觸發 | **需要**，必須在對話中明確說「使用 `theme-factory` 技能」 |
| **主要功能** | 生成簡報、試算表、Word 等實體檔案 | 主題套用、畫布排版、MCP 伺服器代碼結構等 |

---

#### 📋 如何在對話中調用 `/examples` 技能？（實戰 Prompt 範例）
如果您想要在對話中調用像是 `theme-factory` 這樣的範例技能，您可以直接用這樣的對話方式：

> **💬 對話範例（直接指定主題）**：
> *「請幫我製作一份關於『AI 趨勢』的 5 頁簡報，並**使用 theme-factory 範例技能裡的 Midnight Galaxy 主題**來為我設計簡報的配色與字型風格。」*
> 
> *註：此時 Claude 就會去讀取 `/mnt/skills/examples/theme-factory/SKILL.md`，並按照裡面的步驟：(1) 顯示 10 種主題的 theme-showcase，(2) 讓您選擇，(3) 讀取對應 HEX 配色並套用到您的 PPT 檔案中。*

---

#### ⚙️ 產生簡報與文件的背景執行流程：
1. **讀取規範**：Claude 讀取系統內建掛載的 `SKILL.md`（自動或手動指名）。
2. **撰寫與執行代碼**：在雲端沙盒容器內以 Python（搭配對應的函式庫如 `python-pptx`, `python-docx`, `openpyxl` 等）撰寫並執行程式碼。
3. **儲存輸出**：將產出的實體檔案存至系統路徑 `/mnt/user-data/outputs/`。
4. **呈現檔案**：調用內建的 `present_files` 工具，在對話右側產生下載連結提供給您。

---

## 💡 教學觀念先導

在開始使用 Skills 之前，請先釐清一個關鍵點：**「設定清單中沒有顯示任何 Skill 是正常的」**。
Skills 的安裝與啟用方式，完全取決於您是在**「網頁/桌面版 Claude.ai」**還是**「Claude Code (終端機)」**環境下操作。這是兩條完全不同的路徑。

---

## 💻 一、網頁 / 桌面版 Claude.ai (圖形介面)

在網頁版或桌面應用程式介面中，**不需要（也無法）使用終端機指令安裝**，而是透過 **「上傳自訂 Skill 壓縮檔」** 或 **「直接對話觸發」**。

### 1. 官方內建文件 Skills (無需手動安裝)
* 像 `pptx`、`docx`、`xlsx`、`pdf` 這類官方文件處理技能，不論是 **Free（免費版）** 還是 **Pro/Team（付費版）**，只要開啟了 **Code execution and file creation**，系統就會自動內建在雲端中。
* **使用方式**：只要在對話中直接要求（例如：「*幫我做一份 PowerPoint 簡報*」或「*用 Excel 分析這份資料*」），Claude 就會自動掛載並觸發對應的內建 Skill，**不需要**手動去 GitHub 下載。
* **顯示機制**：這些內建技能**不會**出現在 Settings 的 Skills 清單中，清單只會列出您手動上傳的自訂技能（例如 `skill-creator`）。
* **特別注意**：免費版在執行這些需要代碼執行 (Code execution) 的技能時，會有每日使用額度上限，用完後將需要等待重置或升級 Pro。

### 2. 手動上傳自訂 Skill (用於課堂示範或個人 SOP)
若您想要體驗或向學生示範如何載入自訂的 Skill，請依循以下步驟：
1. 前往官方 GitHub 倉庫 [anthropics/skills](https://github.com/anthropics/skills)。
2. 進入 `skills/` 資料夾，下載您要的技能資料夾（例如 `canvas-design`）。
3. 將該技能資料夾整個**壓縮成 `.zip` 檔**（內部必須包含 `SKILL.md` 指引檔案）。
4. 在 Claude.ai 介面點擊左下角個人頭像 → **Settings** → **Capabilities**。
5. 捲動至下方的 **Skills** 區段，點擊右上角的「**+**」按鈕上傳該 `.zip` 檔。
6. 上傳完成後，將其開關切換為**開啟 (Toggle On)** 即可。

### 3. 如何在對話中直接向 Claude 查詢可用 Skills 與範例？

其實不需要到 GitHub 去找文件，只要在對話中開啟「Code execution」後，您可以直接透過以下對話 Prompt 詢問 Claude 本身，它就會自動列表報告目前已經為您載入的所有 Skills，甚至提供對應的 Prompt 範例！

#### 📋 一鍵查詢 Skills 魔法 Prompt（直接複製使用）

```markdown
## Role
你是 Claude 系統大師，對目前已載入、可用的 Skills (技能) 系統瞭若指掌。

## Task
請幫我查詢並報告目前此對話中，已經為我載入或可用的所有 Skills 清單。並針對每一個可用的 Skill，提供一個具體的、可直接複製使用的應用範例提示詞 (Prompt)。

## Constraint
- 語言：繁體中文。
- 若有內建的 pdf, docx, xlsx, pptx 等文件 Skills，也請一併列出。
- 格式：以表格呈現 Skill 名稱與核心功能，並在表格下方以程式碼區塊 (Code block) 條列式提供每一個 Skill 的應用 Prompt 範例。
```

> [!NOTE]
> **方案限制**：使用自訂與上傳 Skills 需要啟用 **Code execution and file creation**（程式碼執行與檔案建立）功能。

---

## ⌨️ 二、Claude Code (終端機 / 開發者專用 CLI)

如果您是工程師或習慣使用終端機的開發者，在 **Claude Code** 環境下，Skills 是以 **Plugin (外掛)** 的形式被安裝與管理的。

### 1. 註冊官方 Marketplace 插件庫
在終端機對話中輸入以下指令，將官方倉庫註冊為套件市場來源：
```bash
/plugin marketplace add anthropics/skills
```

### 2. 安裝官方 Skill 插件包
依需求安裝對應的技能外掛：
```bash
# 安裝文件處理類技能包 (pdf, docx, xlsx, pptx 等)
/plugin install document-skills@anthropic-agent-skills

# 安裝範例類技能包 (例如 theme-factory, brand-guidelines 等)
/plugin install example-skills@anthropic-agent-skills
```

### 3. 本機手動複製安裝
您也可以直接下載官方技能資料夾，手動放入您個人或專案的本機技能目錄下，Claude Code 啟動時會自動載入：
* **個人全域路徑**：`~/.claude/skills/`
* **專案專屬路徑**：`./.claude/skills/`（位於您的專案根目錄）

---

## 👩‍🏫 教師授課建議 (身為老師您需要知道的事)

### 💡 建議 1：先別急著上傳，直接用對話測試
在教授 Google Workspace 實戰或簡報產生時，請先請學生開啟一個新對話，直接輸入：
> *「幫我用 pptx 做一份 5 頁的簡報大綱，並匯出成 .pptx 檔供我下載。」*
確認內建的 PPTX 技能是否會自動執行。多數情況下，內建技能會直接運作，無需進行任何安裝步驟。

### 💡 建議 2：以「+ 上傳 zip」示範自訂技能
在課堂上要介紹「數位分身」或「SOP 流程自動化」的概念時，使用**「網頁版 + 上傳 .zip」**的流程是最直覺且視覺化的示範方式，能讓非程式設計背景的學生快速理解「技能就是一套 SOP 包」的概念。

### ⚠️ 安全提醒：嚴格審查未知來源的 Skills
由於 Skills 能在 Claude 的雲端沙盒中運行任意程式碼（如 Python），**請務必提醒學生只安裝來自官方或可信賴來源的 Skill**。對於社群分享的 Skill 壓縮檔，在上傳前應如同審查開源程式碼般，先解壓並檢查其中的 `SKILL.md` 與腳本內容，以防止惡意程式碼執行。

---

← [返回 Skills 主頁](../README.md)
