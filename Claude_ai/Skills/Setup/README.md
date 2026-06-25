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
* **其他非文件技能的原理**：例如 `brand-guidelines`、`theme-factory` 或 `skill-creator` 等，它們是純系統提示詞指令（無對應標準 Python 庫），若帳號中沒有安裝，Claude 就無法以官方標準運作。

為了讓學生清楚了解自己帳號目前到底擁有多少技能，請引導學生使用以下兩種方式進行檢查：

### 方法一：輸入 `/`（斜線鍵）進行選單檢查（最直覺）
1. 請學生在對話框中輸入一個半形斜線 `/`。
2. 觀察對話框上方是否會跳出 **「可用指令與技能清單」**。
3. **對照清單**：清單中列出的（如 `/pptx`、`/theme-factory`、`/skill-creator`）即為當前已安裝並啟用的 Skills。如果沒有出現您需要的技能，代表免費版需要手動去 GitHub 下載並上傳 `.zip` 檔安裝。

### 方法二：貼上「自我診斷 Prompt」讓 Claude 報告
開啟一個新對話，請學生複製並發送以下提示詞，讓 Claude 盤點其當前擁有的技能：

> 💬 **診斷提示詞**：
> *「請檢查目前此對話中，你是否有載入任何系統 Skills（技能），或可以使用哪些斜線指令（如 `/pptx`、`/theme-factory` 等）？如果沒有，當我要求你產生 PPT 或 Word 檔案時，你是透過執行 Python 程式碼來完成的嗎？請簡要說明。」*

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
