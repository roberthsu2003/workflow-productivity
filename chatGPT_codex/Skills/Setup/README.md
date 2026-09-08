# Skills 與 Plugins 安裝啟用指南

> 🟢 **方案需求**：自訂 Skill 為 Free；**Plugins 需 Plus 起**。

> [!IMPORTANT]
> ### 🚀 課堂第一步：3 分鐘環境探測
>
> 班上同學的帳號會混雜 **Free / Go / Plus / Pro**，各方案能用的功能差很多。上課開始時先讓全班一起跑兩個探測，立刻釐清每個人的環境狀態。

---

## 🧪 實驗一：探測目前載入了哪些 Skill

開啟新對話，直接送出：

```markdown
請報告目前這個工作階段中可用的 skills 與 plugins：

1. 系統內建（隨 Codex 附帶）的 skill 有哪些？
2. 我的個人 skill（`$HOME/.agents/skills`）有幾個？請列出名稱。
3. 目前 repo 的 skill（`.agents/skills`）有幾個？請列出名稱。
4. 已安裝的 plugin 有哪些？各自帶進了哪些 skill？

限制：
- 只做查詢與回報，不要執行任何 skill。
- **找不到就說找不到，不要推測可能有什麼。**
```

### 預期結果與判讀

| 你看到的 | 代表 | 該做什麼 |
| :--- | :--- | :--- |
| 列出內建 skill，個人／repo 為 0 | ✅ 正常，還沒建立自訂 skill | 繼續實驗二 |
| Plugin 清單為空 | 你可能是 Free / Go 方案 | Plugins 需 Plus 起 |
| 完全查不到 skill 機制 | 版本較舊或介面不同 | 檢查 Codex 版本 |
| 它「推測」你可能有哪些 skill | ⚠️ 它在編造 | 重下 prompt 強調不可推測 |

---

## 🧪 實驗二：驗證 skill 真的會被觸發

建立一個**故意很好認**的 skill，確認觸發機制運作。

```bash
mkdir -p ~/.agents/skills/hello-codex
cat > ~/.agents/skills/hello-codex/SKILL.md <<'EOF'
---
name: hello-codex
description: 課堂測試用。當使用者說「執行課堂測試」時觸發，回報 skill 機制正常運作。不要用於其他任何情況。
---

# Hello Codex

當被觸發時，回覆以下三項：
1. 「✅ Skill 機制正常運作」
2. 你是從哪個路徑載入這個 skill 的
3. 目前的日期時間
EOF
```

然後在對話中輸入：

| 介面 | 輸入 |
| :--- | :--- |
| ChatGPT | `@hello-codex 執行課堂測試` |
| Codex | `$hello-codex 執行課堂測試` |

**看到 ✅ 就代表環境沒問題。**

> [!WARNING]
> 若沒反應，依序檢查：
> 1. 路徑是否正確（`~/.agents/skills/hello-codex/SKILL.md`，不是 `.claude` 也不是 `.codex`）
> 2. frontmatter 的 `---` 是否完整成對
> 3. **是否需要重新開啟對話**——skill 通常在新對話或新 CLI session 開始時載入

---

## 📍 安裝位置速查

| 作用域 | 路徑 | 優先權 | 用途 |
| :--- | :--- | :---: | :--- |
| REPO（目前目錄） | `$CWD/.agents/skills` | 最高 | 這個資料夾專用 |
| REPO（上層） | `$CWD/../.agents/skills` | ↑ | 巢狀 repo |
| REPO（根目錄） | `$REPO_ROOT/.agents/skills` | ↑ | **全隊共用** |
| USER | `$HOME/.agents/skills` | ↑ | 個人跨專案 |
| ADMIN | `/etc/codex/skills` | ↑ | 系統預設 |
| SYSTEM | Codex 內建 | 最低 | 官方隨附 |

```bash
# 個人 skill
mkdir -p ~/.agents/skills/<skill-name>

# 團隊 skill（提交進 Git，全隊自動取得）
mkdir -p <repo>/.agents/skills/<skill-name>
cd <repo> && git add .agents && git commit -m "feat(skills): 新增 <skill-name>"
```

---

## 🔌 安裝 Plugin

> 🔵 需 Plus 起。Business / Enterprise 由管理員控管可安裝清單。

1. `Settings` → `Plugins`
2. 瀏覽通用 plugin 目錄（**ChatGPT 與 Codex 共用**）
3. 檢查發布者、權限、依賴、資料去向
4. 安裝並完成 OAuth 授權
5. **開啟新對話或新 CLI session**——plugin 帶的 skill 要新 session 才會載入

### 第一方 plugin

| Plugin | 做什麼 | 需授權 |
| :--- | :--- | :---: |
| **Spreadsheets** | 建立與編輯試算表檔案 | — |
| **Presentations** | 建立與編輯簡報 | — |
| **Google Drive** | 跨 Drive、Docs、Sheets、Slides 作業 | ✓ OAuth |
| **Gmail** | 讀取與管理 Gmail | ✓ OAuth |
| **Google Calendar** | 管理行事曆事件與排程 | ✓ OAuth |
| **GitHub** | 分流 PR、Issue、CI 與發布流程 | ✓ OAuth |
| **Slack** | 讀取與管理 Slack | ✓ OAuth |
| **Notion** | 規格、研究、會議與知識庫流程 | ✓ OAuth |
| **Chrome** | 用 Codex 控制 Chrome | 本機權限 |
| **Computer Use** | 從 Codex 控制 Mac 應用程式 | 本機權限 |
| **Apple Messages** | 讀取／搜尋訊息、從 macOS 傳送 | macOS 權限 |

### 六大職能 plugin（2026-06-02 推出）

| Plugin | 對象 | 串接的工具（例） |
| :--- | :--- | :--- |
| **Data Analytics** | 分析師、業務團隊 | Snowflake、Databricks Genie、Hex、Tableau |
| **Creative Production** | 行銷與創意 | Figma、Canva、Shutterstock、Picsart、Fal |
| **Sales** | 業務 | Salesforce、HubSpot、Slack、Outreach、Rox |
| **Product Design** | 產品設計 | 設計工具鏈 |
| **Public Equity Investing** | 投資研究 | 研究與分析工作流 |
| **Investment Banking** | 投行 | 財務模型、盡職調查 |

合計串接 **62 個應用**、內建 **110 個自動化 skill**，另有 **90+** 第三方 plugin。

> 目錄更新很快，授課前請直接看 `Settings` → `Plugins` 的實際清單，不要照抄講義名單。

---

## ⚠️ 安裝前必檢查

> [!WARNING]
> **安裝 plugin = 授權一段別人寫的程式在你的環境執行，並代表你存取外部服務。**

- [ ] 發布者是誰？官方、知名廠商、還是不具名個人？
- [ ] OAuth 權限範圍是什麼？能唯讀就唯讀
- [ ] 你的程式碼／文件會被送到哪個伺服器？
- [ ] 是否包含 MCP server 或會執行的 script？
- [ ] 最後更新日期？有在維護嗎？
- [ ] 組織政策允許嗎？

### 第一次一律唯讀

```text
請使用剛安裝的 <plugin 名稱>，**只做讀取**：
列出你能存取到的資料範圍，以及可呼叫的工具清單。
不要執行任何寫入、修改或發佈動作。
```

---

## 🧹 定期清理（建議每季）

> [!IMPORTANT]
> 移除不用的 plugin 有三個理由：
> 1. **安全**：每個授權都是持續有效的存取權
> 2. **效能**：plugin 帶的 skill 佔用 **8,000 字元**的 skill 清單上限，裝太多會排擠你常用的
> 3. **可預測性**：太多重疊的工具會讓 Codex 選錯

---

## 🔄 與 Claude 的安裝差異

| 面向 | Claude | Codex |
| :--- | :--- | :--- |
| 探測路徑 | `/mnt/skills/{public,examples,user}/` | `.agents/skills` 六層作用域 |
| 前置開關 | Settings → Capabilities → Code execution | **不需要開關**，但 plugin 需 Plus |
| 觸發 | 背景自動識別 | `@name`（ChatGPT）／ `$name`（Codex）或自動 |
| 團隊分享 | 介面分享 | **`git commit`** |
| 生效時機 | 即時 | **plugin 需新開對話／session** |

---

**官方說明**：[Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins) · [Build skills](https://learn.chatgpt.com/docs/build-skills) · [Plugins](https://learn.chatgpt.com/docs/plugins)

---

← [返回上層：Skills](../README.md) ｜ [返回索引](../../README.md)
