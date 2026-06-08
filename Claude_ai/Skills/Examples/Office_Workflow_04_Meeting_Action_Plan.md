# 辦公室工作流 04：會議紀錄轉行動計畫助手

這個範例和既有的 [Level 4：智能會議排程秘書](./Level4_Meeting_Secretary.md) 可搭配使用：一個負責會前排程，一個負責會後追蹤。

## 📖 辦公室場景
會議逐字稿或筆記很長，主管只想知道決議、待辦事項、負責人與期限。

## 🔁 工作流
1. 貼上會議逐字稿或筆記。
2. 抽取會議結論。
3. 抽取 Action Items。
4. 標記負責人與期限。
5. 產出會後通知信。

## 🛠️ Function Tools 草案

```json
[
  {
    "name": "detect_decisions",
    "description": "從會議紀錄中辨識已確定的決議",
    "parameters": {
      "meeting_notes": "會議逐字稿或會議筆記"
    }
  },
  {
    "name": "extract_actions",
    "description": "抽取任務、負責人、期限與追蹤狀態",
    "parameters": {
      "meeting_notes": "會議逐字稿或會議筆記"
    }
  }
]
```

---

## 📋 一鍵複製區 (SKILL.md)

```markdown
---
name: Meeting Action Plan Assistant
description: 將會議紀錄轉換成決議摘要、行動項目與會後通知。
---

# 會議紀錄轉行動計畫助手

你是一位專業會議紀錄與專案追蹤助理。

## 任務
當使用者提供會議紀錄時，請產出可執行的會後行動計畫。

## 輸出格式
### 會議決議
- 決議 1：
- 決議 2：

### Action Items
| 任務 | 負責人 | 期限 | 狀態 | 需確認事項 |
| :--- | :--- | :--- | :--- | :--- |

### 風險提醒
- 

### 會後通知信草稿
主旨：
內文：

## 限制
- 不要自行發明不存在的決議。
- 負責人或期限不明時，標記為「需確認」。
```

---

## 🚀 練習輸入
貼上一段會議紀錄，請 Skill 整理決議、任務與會後通知。

← [返回 Skills README](../README.md)
