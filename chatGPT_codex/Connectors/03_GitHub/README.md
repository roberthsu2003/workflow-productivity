# 03. GitHub 工程協作

> 🔵 **方案需求**：Plus 起（雲端整合含 GitHub code review 從 Plus 開始）。

這是 **Codex 相對於 Claude 最有優勢的章節**——Claude 的對應章節是 Notion 知識庫，而 Codex 原生就是工程代理，GitHub 整合是它的主場。

用 **潮汐物流** 的 `tideflow-portal` 專案，練習 Issue 分流、PR 審查與 Release note 產生。

---

## 🎯 這一章要練的三件事

| 次章節 | 情境 | 核心能力 |
| :--- | :--- | :--- |
| [01. Issue 分流](./01_Issue_Triage/README.md) | 12 個未分類 Issue，排出處理順序 | 優先度判準、**留言數 ≠ 重要性** |
| [02. PR 自動審查](./02_PR_Review/README.md) | 依 `AGENTS.md` 的 review rules 審查 PR | 規則落地、**只留意見不動手** |
| [03. Release Note 產生](./03_Release_Notes/README.md) | 從 commit 歷史產出對外版本說明 | 面向使用者的改寫、資訊取捨 |

---

## 🔐 授權範圍建議

> [!WARNING]
> **課堂請用你自己建立的測試 repo，不要授權公司的私有 repo。**

| 範圍 | 建議 | 說明 |
| :--- | :---: | :--- |
| `public_repo` | ✅ | 只能存取公開 repo，課堂足夠 |
| `repo` | ⚠️ | 私有 repo 的**完整讀寫**，包含刪除 |
| `workflow` | ⚠️ | 可修改 CI 設定，風險高 |
| `delete_repo` | ❌ | 絕不授權 |

---

## 🚫 三條不可跨越的紅線

本章所有練習都遵守：

```markdown
## Boundaries（建議寫進 AGENTS.md）
- **不要 approve 或 merge 任何 PR。** 審查意見可以留，決定權在人。
- **不要 push 到 main 或任何受保護分支。**
- **不要關閉 Issue。** 可以建議關閉並說明理由。
```

> **為什麼**：這三個動作在協作情境中影響的不只是你。誤 merge 一個 PR 可能觸發部署；誤關 Issue 會讓回報者以為被忽視。

---

## 📂 示範資料

| 檔案 | 用於 | 說明 |
| :--- | :--- | :--- |
| [`tideflow_issue_backlog.csv`](./01_Issue_Triage/sample_files/tideflow_issue_backlog.csv) | 01 | 12 個 Issue，含留言數與現有優先度 |
| [`AGENTS_code_review_rules.md`](./02_PR_Review/sample_files/AGENTS_code_review_rules.md) | 02 | 團隊的 code review 規則 |
| [`tideflow_commit_log.md`](./03_Release_Notes/sample_files/tideflow_commit_log.md) | 03 | 兩週的 commit 歷史 |

---

## 🔄 與 Claude Notion 章節的對照

`Claude_ai` 講義的第三個 Connector 是 Notion（知識庫）。這裡換成 GitHub，理由：

| | Claude / Notion | Codex / GitHub |
| :--- | :--- | :--- |
| 章節定位 | 知識庫跨資料庫搜尋 | **工程協作** |
| 為什麼換 | Notion 偏向文件整理 | Codex 的核心能力就是讀程式碼、改程式碼 |
| 共通的教學點 | 跨來源交叉比對、優先度判斷、SOP 落地 | 相同 |

> 若你的課程對象是非工程背景，可以只教 [01. Issue 分流](./01_Issue_Triage/README.md)（純粹的優先度判斷練習，不需讀程式碼）。

---

← [返回上層：Connectors](../README.md) ｜ [返回索引](../../README.md)
