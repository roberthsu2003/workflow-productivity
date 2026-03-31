# Skills（技能）

**Skills** 是含 **SKILL.md**（與選用的腳本、參考檔）的資料夾，Claude 依**描述**在需要時**動態載入**，用於可重複的工作流（如品牌規範、文件產出格式）。官方教學見 [Creating custom skills](https://claude.com/docs/skills/how-to)；**範例技能原始碼**見 [github.com/anthropics/skills](https://github.com/anthropics/skills/tree/main/skills)（含 **brand-guidelines** 等可參考結構）。通常需 **Pro／Max／Team／Enterprise** 等方案，並可能需開啟**程式碼執行**。

**RTCCF 五段欄位**請對照 [Chats／RTCCF 欄位對照](../Chats/README.md#rtccf-欄位對照複製範本時請五段都填)。

---

## 使用時機

| 適合 | 不適合 |
|------|--------|
| **重複性高**、格式固定的產出（簡報、試算表、依品牌規範撰寫） | 一次性、無需封裝成「技能」的臨時提問 |
| 願意維護 **SKILL.md**（與選用腳本）並在設定中**啟用** | 只想貼靜態長文脈絡（用 **Projects** 較單純） |
| 需與 **MCP** 搭配的外部工具流程（技能內可說明何時呼叫） | 完全不能執行任何程式碼的環境（功能可能受限） |

---

## 官方結構範例（節錄）

文件中的 **brand-guidelines** 示範：`SKILL.md` 前綴 YAML 含 `name`、`description`，內文寫色彩、字型、Logo 規範與**何時套用**。上傳為 ZIP、於 **Settings → Capabilities** 啟用後，以自然語言觸發相關任務即可載入。完整欄位與打包方式見 [Creating custom skills](https://claude.com/docs/skills/how-to)。

---

## 經典範例（辦公情境）：依「機關／公司品牌規範」產出對外新聞稿

### 任務背景

組織已將 **品牌與對外發言規範** 製成自訂 **Skill**（內容可改寫自官方 `brand-guidelines` 範本）。承辦人需就一則**活動訊息**產出**符合標語、抬頭、禁用詞**的新聞稿草稿。

### RTCCF Prompt（請複製後修改；須已啟用對應 Skill）

```markdown
## Role

你是一位遵循組織對外發言規範的發言人或承辦人員。

## Task

請**啟用並遵循**我已上傳的 **{品牌／公文撰寫}** Skill，將下列活動資訊改寫成**對外新聞稿**（一段標題＋導言＋本文＋聯絡方式占位）。

## Context

- 活動名稱：{ }
- 時間地點：{ }
- 主辦／協辦：{ }
- **關鍵事實（請貼上，勿虛構）：**
  - （背景、人數、法源依據摘要等）

## Constraint

- 嚴格遵守 Skill 中的**禁用詞、稱謂、數字寫法**；若與事實衝突，以事實為準並註明「與範本用語不一致處」
- 語言：繁體中文
- 長度：全文約 500～800 字（可依需要調整）

## Format

- 先列**建議標題 2～3 個**供選擇，再給完整本文（Markdown）
- 若 Skill 要求特定檔案類型（如 .docx），請一併依 [Chats 文件範例](../Chats/README.md) 嘗試產出可下載檔
```

---

← [上層：Claude_AI 索引](../README.md) · [Chats 範例庫](../Chats/README.md)
