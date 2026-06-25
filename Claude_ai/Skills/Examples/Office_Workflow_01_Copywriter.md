# 延伸練習 1：社群貼文文案大師（第一階：模仿者）

這是第一階的延伸實作練習。本階段的重點是學會如何透過介面建立最基礎的自訂 Skill。

## 📖 範例說明
這個 Skill 會將您簡單的主題想法，擴寫為吸引人、具備高互動率的社群媒體貼文（Facebook/Instagram/LinkedIn）。

## 🛠️ 建立方式（使用 Write skill instructions）
請依照以下步驟在 Claude 介面中手動新增：

1. 點擊 Claude 左下角頭像前往 **Customize** ➔ **Skills**。
2. 點擊右上角的 `+` ➔ **Create skill** ➔ 選擇 **Write skill instructions**。
3. 依照以下內容填寫欄位：
   - **Skill name**: `social-media-expert`
   - **Description**: `將簡單的主題想法，擴寫為吸引人的社群媒體貼文。`
   - **Instructions** (複製並貼上以下內容)：
     ```text
     你是一位資深的社群媒體文案專家，擅長撰寫吸引點擊、具備高互動率的貼文。

     ## 任務
     當使用者輸入一段簡單的想法或文章大綱時，請將其擴寫為符合社群平台特性的文案。

     ## 撰寫規範
     - **語氣**：活潑、親切且具吸引力。
     - **結構**：必須包含吸引人的標題、分點正文、Hashtags、以及呼籲行動 (CTA)。
     - **語言**：繁體中文。

     ## 使用方式
     請輸入你想撰寫的主題，例如：「我想寫一篇關於時間管理工具的推薦貼文。」
     ```
4. 點擊 **Create** 按鈕完成建立。確認 Skills 列表中是否已成功出現「Social Media Expert」這個新 Skill。


### 💡 方式 B：在終端機中部署（適用於 Claude Code / 終端機代理）
1. 在您的專案或 CLI 系統的 `/mnt/skills/user/` 目錄下建立一個自訂技能資料夾（名稱例如 `social-media-expert`）。
2. 在該資料夾內建立 `SKILL.md` 檔案。
3. 複製下方「一鍵複製區 (SKILL.md)」中的所有內容並貼入 `SKILL.md` 存檔即可。

## 🧪 測試與驗證

確認 Skill 建立成功後，您可以開啟新對話並使用以下範例 Prompt 來測試其效果：

**測試 Prompt：**
```text
請幫我撰寫社群貼文：
「今天推薦一款我們團隊在用的番茄鐘工作法 App。用了之後大家工作專注度提升 30%，而且免費。幫我寫一篇適合發在 Facebook 的貼文，語氣要活潑。」
```

**預期效果：**
Claude 將會自動啟用該 Skill，並依據規範將上述簡單的概念，轉化為帶有吸睛標題、分點介紹、Hashtags 與呼籲行動（CTA）的活潑 Facebook 貼文。

---

← [返回 Skills 主頁](../README.md)
