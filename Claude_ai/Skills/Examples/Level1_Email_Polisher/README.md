# Level 1 範例：全能郵件修飾專家（第一階：模仿者）

這是自訂 Skills 的入門範例。本階段的重點是學會如何建立並使用一個最基礎的、僅包含單一 `SKILL.md` 的 Skill。

## 📖 範例說明
這個 Skill 會將您隨手寫下的雜亂資訊，轉化為具備「專業度」與「人情味」的正式商業郵件。

## 📁 實體自訂 Skill 結構
此範例在手動建立時，其資料夾結構非常單純，僅有一個核心描述檔：
```text
Level1_Email_Polisher/
└── SKILL.md
```

## 🛠️ 安裝與使用方式

### 💡 方式 A：使用內建 `/create-skill` 技能（自動建立）
開啟新對話，直接向 Claude 下指令：
> 「`請幫我建立一個名為『郵件修飾專家』的 Skill。角色是專業文案，任務是修飾日常郵件語氣，限制是使用繁體中文、格式為 Markdown，請使用 /create-skill 幫我自動產出。`」

### ✍️ 方式 B：手動複製檔案（手動建立）
1. 在您的電腦中建立新資料夾 `Level1_Email_Polisher`。
2. 複製此資料夾下的 [SKILL.md](./SKILL.md) 內容，並將其儲存於該資料夾中。
3. 點擊 Claude 左下角頭像前往 **Settings** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

---

← [返回 Skills 主頁](../../README.md)
