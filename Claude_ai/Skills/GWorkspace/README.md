# 實作練習：Google Workspace Skills

> 以下三個練習專注在 **Google Docs、Google Sheets、Google Slides、Gmail** 四個工具，  
> 透過「先用現有 Skill → 再改造成自己的 Skill」兩步驟，讓學生快速上手。  
> 需先在 Settings 開啟 **Skills** 與 **程式碼執行**，並透過 [Connectors](../../Connectors/README.md) 完成 Google Drive 與 Gmail 授權。

---

### 👉 [練習 0：使用現有的 Skill（Google Workspace 四合一範例）](./GWorkspace_00_Use_Existing_Skills.md)

> **建議第一個做這個**。不需要自己建立 Skill，直接呼叫現有 Skill，  
> 分別產出 Google Docs 會議紀錄、Google Sheets 任務追蹤表、Google Slides 簡報、Gmail 郵件。  
> 每個練習附有可直接複製的完整 RTCCF Prompt。

---

### 練習 1：使用現有的 Skill

> **目標**：學會從 Skill 目錄找到合適的 Skill，直接呼叫並產出 Google Workspace 文件。  
> **前置**：已安裝 Claude Desktop 或在 claude.ai 的 Settings → Skills 中啟用對應 Skill。

| 任務 | 呼叫的 Skill | 說明 |
|------|------------|------|
| 產出 Google Docs 會議紀錄 | `Meeting Notes → Google Doc` | 輸入逐字稿或要點，Skill 自動整理並建立 Doc |
| 建立 Google Sheets 追蹤表 | `Task Tracker → Google Sheet` | 輸入任務清單，Skill 自動建立含狀態欄的試算表 |
| 製作 Google Slides 簡報大綱 | `Presentation Builder → Google Slides` | 輸入主題與要點，Skill 自動建立投影片結構 |
| 草擬並寄送 Gmail | `Email Drafter → Gmail` | 輸入收件人與重點，Skill 草擬郵件並可一鍵寄出 |

**RTCCF 呼叫範例（Google Sheets 追蹤表）**

```markdown
## Role
你是辦公室行政助手，擅長使用 Google Sheets 建立追蹤表。

## Task
請用「Task Tracker」Skill，將下列任務清單建立成 Google Sheets，
欄位包含：任務名稱、負責人、截止日、狀態（待處理／進行中／完成）。

## Context
任務清單：
- 採購新螢幕（負責人：小明，截止：2026-06-20）
- 更新員工手冊（負責人：小華，截止：2026-06-30）
- 安排季度會議（負責人：小美，截止：2026-06-15）

## Constraint
- 語言：繁體中文
- 狀態欄預設值為「待處理」
- 試算表名稱：「2026-06 任務追蹤表」

## Format
建立完成後回傳 Google Sheets 連結，並列出已建立的欄位清單。
```

---

### 練習 2：修改現有的 Skill

> **目標**：學會開啟現有 `SKILL.md`，針對自己的需求調整角色、輸出格式或規則，  
> 打造屬於自己的 Google Workspace 工作流。

**修改步驟**

1. 在 Claude Settings → Skills 找到目標 Skill，點擊「Edit」
2. 開啟 `SKILL.md`，找到要修改的段落
3. 依下表調整後儲存，重新呼叫測試

| 修改目標 | 原始 Skill 設定 | 建議改法 |
|---------|--------------|---------|
| **Google Docs** 會議紀錄改成符合公司格式 | 通用標題與段落結構 | 在 `## Format` 加入公司抬頭、部門、與會人員欄位 |
| **Google Sheets** 追蹤表加入顏色規則說明 | 純文字欄位 | 在 `## Constraint` 加入「狀態為『逾期』時請在備註欄標記 ⚠️」 |
| **Google Slides** 簡報改成 5 頁固定結構 | 依內容自動決定頁數 | 在 `## Format` 指定：封面、問題、解法、數據、結論各一頁 |
| **Gmail** 草稿改成部門專屬簽名檔 | 通用結尾 | 在 `## Format` 加入固定簽名格式（職稱、分機、部門） |

**修改範例：為 Gmail Skill 加入部門簽名檔**

在原始 `SKILL.md` 的 `## Format` 區塊末尾加入：

```markdown
郵件結尾必須附上以下簽名（固定格式，勿更動）：

---
{姓名}
{職稱} ｜ 行政管理部
分機：{分機號碼}
信箱：{email}
```

> **測試方式**：修改後在 Claude 輸入「/gmail 幫我寫一封詢問採購進度的信給小明」，  
> 確認產出的草稿結尾是否出現您設定的簽名格式。

---

← [返回 Skills 主頁](../README.md)
