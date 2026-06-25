# Claude Skills 安裝與啟用指南

> **💡 教學觀念先導**
> 
> 在開始使用 Skills 之前，請先釐清一個關鍵點：**「設定清單中沒有顯示任何 Skill 是正常的」**。
> Skills 的安裝與啟用方式，完全取決於您是在**「網頁/桌面版 Claude.ai」**還是**「Claude Code (終端機)」**環境下操作。這是兩條完全不同的路徑。

---

## 💻 一、網頁 / 桌面版 Claude.ai (圖形介面)

在網頁版或桌面應用程式介面中，**不需要（也無法）使用終端機指令安裝**，而是透過 **「上傳自訂 Skill 壓縮檔」** 或 **「直接對話觸發」**。

### 1. 官方內建文件 Skills (無需手動安裝)
* 像 `pptx`、`docx`、`xlsx`、`pdf` 這類官方文件處理技能，在 Pro / Max / Team / Enterprise 方案下已**自動內建在雲端**。
* **使用方式**：只要在對話中直接要求（例如：「*幫我做一份 PowerPoint 簡報*」或「*用 Excel 分析這份資料*」），Claude 就會自動掛載並觸發對應的內建 Skill，**不需要**手動去 GitHub 下載。
* **顯示機制**：這些內建技能**不會**出現在 Settings 的 Skills 清單中，清單只會列出您手動上傳的自訂技能（例如 `skill-creator`）。

### 2. 手動上傳自訂 Skill (用於課堂示範或個人 SOP)
若您想要體驗或向學生示範如何載入自訂的 Skill，請依循以下步驟：
1. 前往官方 GitHub 倉庫 [anthropics/skills](https://github.com/anthropics/skills)。
2. 進入 `skills/` 資料夾，下載您要的技能資料夾（例如 `canvas-design`）。
3. 將該技能資料夾整個**壓縮成 `.zip` 檔**（內部必須包含 `SKILL.md` 指引檔案）。
4. 在 Claude.ai 介面點擊左下角個人頭像 → **Settings** → **Capabilities**。
5. 捲動至下方的 **Skills** 區段，點擊右上角的「**+**」按鈕上傳該 `.zip` 檔。
6. 上傳完成後，將其開關切換為**開啟 (Toggle On)** 即可。

> [!NOTE]
> **方案限制**：使用自訂與上傳 Skills 需要 Claude 訂閱方案（Pro、Max、Team 或 Enterprise），且必須在 Capabilities 頁面中啟用 **Code execution and file creation**（程式碼執行與檔案建立）功能。

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
