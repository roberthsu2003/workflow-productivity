# Level 1 範例：全能郵件修飾專家（第一階：模仿者）

這是自訂 Skills 的入門範例。本階段的重點是學會如何建立並使用一個最基礎的自訂 Skill。

## 📖 範例說明
這個 Skill 會將您隨手寫下的雜亂資訊，轉化為具備「專業度」與「人情味」的正式商業郵件。

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/skill-creator` 技能（自動建立）
開啟新對話，直接向 Claude 下指令：

```text
請幫我建立一個名為『郵件修飾專家』的 Skill。角色是專業文案，任務是修飾日常郵件語氣，限制是使用繁體中文、格式為 Markdown，請使用 /skill-creater 幫我自動產出。
```

> [!IMPORTANT]
> 建立完成後，請前往 **Customize** ➔ **Skills**，確認列表中是否已成功建立一個新的 Skill（名稱通常為 Email Expert）。

### ✍️ 方式 B：手動在介面新增（Write skill instructions）
1. 點擊 Claude 左下角頭像前往 **Customize** ➔ **Skills**。
2. 點擊右上角的 `+` ➔ **Create skill** ➔ 選擇 **Write skill instructions**。
3. 依照以下內容填寫欄位：
   - **Skill name**: `Email Expert`
   - **Description**: `將簡短訊息轉化為專業且具備商業禮儀的郵件。`
   - **Instructions** (複製並貼上以下內容)：
     ```text
     你是一位具備 10 年經驗的商業溝通專家，擅長撰寫優雅且精確的郵件。

     ## 任務
     當使用者輸入一段簡短或雜亂的訊息時，請將其重寫為正式的商業郵件。

     ## 撰寫規範
     - **語氣**：專業、禮貌且溫暖。
     - **結構**：必須包含主旨、稱謂、正文、結尾祝禱、簽名檔。
     - **語言**：繁體中文。

     ## 使用方式
     請輸入你想傳達的重點，例如：「小王，明天下午三點要開會，記得帶簡報。」
     ```
4. 點擊 **Create** 按鈕完成建立。確認 Skills 列表中是否已成功出現「Email Expert」這個新 Skill。

### 💡 方式 C：在終端機中部署（適用於 Claude Code / 終端機代理）
若您是在終端機（如 Claude Code）環境中使用，可以直接將本範例的整個資料夾（包含根目錄的 `SKILL.md` 檔案與相關子目錄）複製或移動到 `/mnt/skills/user/` 下。例如：
```bash
cp -r Level1_Email_Polisher/ /mnt/skills/user/Level1_Email_Polisher
```
複製完成後即可在對話中直接使用該自訂技能。

## 🧪 測試與驗證

確認 Skill 建立成功後，您可以開啟新對話並使用以下範例 Prompt 來測試其效果：

**測試 Prompt：**
```text
請幫我修飾這段email訊息：
「小明，上週說好要給的行銷企劃書，今天下班前一定要給我，不然下週一跟客戶開會會來不及準備。收到回一下。」
```

**預期效果：**
Claude 將會自動啟用該 Skill，並依據規範將上述較為生硬、簡短的文字，轉化為包含主旨、稱謂、禮貌正文與結尾祝禱的專業商務郵件。

---

← [返回 Skills 主頁](../../README.md)
