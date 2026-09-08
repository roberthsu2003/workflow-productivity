# Skills（技能）

> 🟢 **方案需求**：Free（建立、安裝與使用自訂 skill 全方案可用）

Skill 是一個含 `SKILL.md` 的資料夾，用來**封裝可重複的專業流程**。Codex 依 skill 的名稱與描述判斷何時該載入，再依需要讀取裡面的 references、templates、scripts 或 assets。

> **一句話定位**：`AGENTS.md` 是「每次都要遵守的規則」，Skill 是「**某種工作出現時才啟動的完整流程**」。

---

## 🎯 什麼時候該做 Skill

| 徵兆 | 該做 Skill 嗎 |
| :--- | :---: |
| 你第三次貼上同一段冗長的 prompt | ✅ 該做了 |
| 這個流程有固定步驟、固定輸出格式 | ✅ |
| 需要搭配範本檔（.xlsx 範本、品牌色票） | ✅ |
| 團隊裡不同人做同一件事，結果品質不一 | ✅ |
| 只用過一次的臨時需求 | ❌ 寫在 task 裡 |
| 每個 task 都要遵守的規則 | ❌ 寫在 `AGENTS.md` |
| 需要連接外部服務的 API | ❌ 那是 [MCP](../MCP/README.md) 或 [Plugin](../Plugins/README.md) |

---

## 📂 資料夾結構

```text
my-skill/
├── SKILL.md              # 必要：名稱、描述、流程指示
├── scripts/              # 選用：可執行的程式
├── references/           # 選用：參考文件、規範、schema
├── assets/               # 選用：範本、圖檔、色票
└── agents/
    └── openai.yaml       # 選用：UI 設定與依賴宣告
```

---

## 📄 `SKILL.md` 規格

### Frontmatter（YAML）

| 欄位 | 必要 | 說明 |
| :--- | :---: | :--- |
| `name` | ✓ | skill 識別名稱（kebab-case） |
| `description` | ✓ | **明確說明何時該觸發、何時不該觸發** |

其餘欄位可依需要自行加入作為 metadata。

> [!IMPORTANT]
> ### `description` 是整個 skill 最重要的一行
> Codex 用它來決定要不要載入這個 skill。寫得模糊，它該用的時候不會用、不該用的時候亂用。
>
> | ❌ 模糊 | ✅ 精確 |
> | :--- | :--- |
> | 「處理會議相關的事」 | 「將會議逐字稿整理成決議、負責人、期限與待確認事項。**不要用於**即時會議摘要或行事曆安排。」 |
> | 「做報表」 | 「依配送績效 CSV 產出月度營運報告 .xlsx。**僅適用於**潮汐物流的配送資料格式。」 |

### 最小可用範例

```markdown
---
name: meeting-action-items
description: 將會議逐字稿整理成決議、負責人、期限與待確認事項。適用於已結束會議的文字紀錄；不要用於即時摘要、行事曆安排或會議邀請撰寫。
---

# Meeting Action Items

## 流程
1. 通讀逐字稿，標記出所有「決定了什麼」與「誰要做什麼」。
2. 區分「已定案的決議」與「討論中但未拍板的方向」。
3. 找出有明確負責人與期限的行動項目。
4. 把缺負責人或缺期限的項目歸入「待確認」。

## 輸出格式
- **摘要**：3 句話以內
- **決議事項**：條列，每項註明拍板者
- **行動項目**：表格（項目 / 負責人 / 期限）
- **待確認問題**：條列

## 限制
- **不得補造未在逐字稿中出現的負責人或期限。**
- 逐字稿中若以暱稱或代稱出現，保留原稱呼，不要自行對應到全名。
- 語氣中立，不加入評價。
```

---

## 📍 安裝位置

Codex 依下列順序尋找 skill，**越上面優先權越高**：

| 作用域 | 路徑 | 用途 |
| :--- | :--- | :--- |
| REPO（目前目錄） | `$CWD/.agents/skills` | 這個資料夾專用的流程 |
| REPO（上層目錄） | `$CWD/../.agents/skills` | 巢狀 repo 共用 |
| REPO（根目錄） | `$REPO_ROOT/.agents/skills` | **全隊共用，隨 repo 分發** |
| USER | `$HOME/.agents/skills` | 你的個人 skill，跨所有專案 |
| ADMIN | `/etc/codex/skills` | 系統層預設值 |
| SYSTEM | Codex 內建 | 官方隨附 skill |

```bash
# 個人 skill：跨專案可用
mkdir -p ~/.agents/skills/meeting-action-items

# 團隊 skill：提交進 Git，全隊自動取得
mkdir -p ~/projects/tideflow-portal/.agents/skills/monthly-ops-report
```

> **教學重點**：把 skill 放進 `$REPO_ROOT/.agents/skills` 並提交，等於**把團隊的 SOP 變成程式碼的一部分**——會被 review、有版本歷史、新人 clone 下來就有。

---

## 🔍 漸進式揭露（Progressive Disclosure）

Codex 不會把所有 skill 的完整內容都塞進上下文。它先看一份精簡清單（僅 `name` + `description`），選中之後才載入完整的 `SKILL.md`。

| 限制 | 值 |
| :--- | :--- |
| 初始 skill 清單上限 | **8,000 字元** 或 **上下文視窗的 2%**（取較小者） |
| 完整 `SKILL.md` | 僅在被選中時載入 |

> [!WARNING]
> **這個上限意味著：skill 裝太多，有些會擠不進清單而永遠不被觸發。** 定期清掉不用的 skill，並讓 `description` 精簡有力——它要在 8,000 字元的競爭中被選中。

---

## ▶️ 怎麼呼叫

| 介面 | 語法 |
| :--- | :--- |
| ChatGPT | `@skill-name` |
| Codex | `$skill-name` |

也可以不明確呼叫——當你的請求符合某個 skill 的 `description` 時，Codex 會**自動載入**。

```text
$meeting-action-items 請處理 notes/2026-08-15_營運週會.txt
```

---

## 🛠️ 三種製作方式

### 方式一：`@skill-creator` / `$skill-creator`（推薦入門）

用對話描述你的流程，讓 Codex 幫你產生 `SKILL.md`。

```text
$skill-creator

我想做一個 skill，用途是：把潮汐物流的月度配送 CSV 轉成主管會議用的 .xlsx 報告。

流程：
1. 讀取 CSV（欄位：日期、區域、單量、準時率、平均配送時數、異常件數）
2. 產出三個工作表：明細（原始資料，首列凍結）、摘要（各區彙總並依準時率排序）、異常（僅列準時率 < 95%）
3. 空值標註「資料缺漏」，不可用 0 代替

限制：不可修改原始 CSV；數字必須與來源一致，不可推估。
輸出：`reports/YYYY-MM_配送績效報告.xlsx`

請產生 SKILL.md，並幫我想一個精確的 description，說清楚何時該用、何時不該用。
```

### 方式二：Record & Replay

**示範一次流程，讓系統自動轉成可重複使用的 skill**——不必手寫指示。適合流程步驟多、但你講不清楚的情況。

### 方式三：手寫

需要精細控制、要搭配 scripts 或 templates 時，直接手寫最可靠。本章的四階範例採用這個方式。

---

## 📖 本章的完整教材

### 入門

| 章節 | 內容 | 方案 |
|---|---|:---:|
| [Setup：安裝與啟用指南](./Setup/README.md) | 3 分鐘環境探測、安裝位置、plugin 清單與審查 | 🟢 Free |
| [Examples：四階實作範例](./Examples/README.md) | L1 模仿者 → L4 自動化專家，含可安裝的 `SKILL.md` | 🟢 Free |

### 使用現成 Plugin

| 章節 | 用哪些 plugin | 對應 Claude |
|---|---|---|
| [Communication：溝通與協作](./Communication/README.md) | Gmail、Slack、Notion | `doc-coauthoring`、`internal-comms` |
| [Design：設計與品牌](./Design/README.md) | Creative Production、Product Design | `brand-guidelines`、`theme-factory` |
| [Development：工程與開發](./Development/README.md) | GitHub、Chrome、Computer Use、`$skill-creator` | `frontend-design`、`webapp-testing` |
| [GWorkspace：產出真實格式檔案](./GWorkspace/README.md) | Spreadsheets、Presentations、Drive、Gmail | GWorkspace 章節 |

### 特別專題

| 專題 | 內容 | 對應 Claude |
|---|---|---|
| 💼 [投資研究與盡職調查](./Investing/README.md) | Public Equity Investing、Investment Banking plugin | `VC_Creator`、`VC_Financial_Analyzer` |
| 🌐 [Browser 自動化與資料擷取](./Browser_Automation/README.md) | 內建 Browser，**不需要 Playwright MCP** | `VC_Playwright` |

---

## 🪜 四階範例：從模仿者到自動化專家

> **📂 完整可安裝的範例、教學順序與課堂設計：[Skills/Examples](./Examples/README.md)**

對應 `Claude_ai` 講義的四階設計，但改用 Codex 的路徑與語法。

| 階段 | 名稱 | 新增能力 | 資料夾內容 |
| :---: | :--- | :--- | :--- |
| **L1** | [模仿者<br>`email-polisher`](./Examples/Level1_Email_Polisher/SKILL.md) | 只有指示，沒有附加檔案 | `SKILL.md` |
| **L2** | [創作者<br>`daily-ops-brief`](./Examples/Level2_Daily_Ops_Brief/SKILL.md) | 加入 `templates/` 範本，輸出格式固定 | `SKILL.md` + `templates/` |
| **L3** | [整合者<br>`expense-auditor`](./Examples/Level3_Expense_Auditor/SKILL.md) | 加入 `references/` 規範，能做判斷與比對 | `SKILL.md` + `references/` + `templates/` |
| **L4** | [自動化專家<br>`meeting-secretary`](./Examples/Level4_Meeting_Secretary/SKILL.md) | 加入 `scripts/`，能執行實際運算 | 全部 |

### L1 範例：`email-polisher`

```markdown
---
name: email-polisher
description: 把口語或草稿式的中文郵件改寫成正式商務郵件。適用於對外客戶、供應商與跨部門溝通；不要用於內部即時訊息、公告或需要法務審閱的正式函文。
---

# Email Polisher

## 流程
1. 判讀原始草稿的核心訴求與收件對象層級。
2. 重寫為：主旨 → 稱謂 → 背景一句 → 訴求 → 具體待辦與期限 → 結尾。
3. 保留所有事實性資訊（日期、金額、單號），一字不改。

## 限制
- **不可新增草稿中沒有的承諾、日期或金額。**
- 不確定收件人職稱時，用「您好」，不要猜測。
- 語氣專業但不卑微；避免「不好意思打擾了」這類冗詞。

## 輸出
先給主旨，再給信件全文。最後用一行列出你**刪掉或改寫**的模糊處，供我確認。
```

### L4 範例的關鍵：`scripts/`

L4 skill 可以放實際會被執行的程式：

```text
meeting-secretary/
├── SKILL.md
├── references/
│   ├── 會議類型與必要欄位.md
│   └── 測試用逐字稿_含時間戳記.md
└── scripts/
    └── calculate_hours.py     # 統計各與會者發言時數
```

在 `SKILL.md` 中明確指出何時執行它：

```markdown
## 流程
...
4. 若逐字稿含時間戳記，執行 `scripts/calculate_hours.py` 統計發言時數，
   並把結果填入紀錄的「議程時間分配」欄位。
   若無時間戳記，跳過此步驟並在報告中註明「無時間資料」。
```

> [!WARNING]
> **`scripts/` 裡的程式會被實際執行。** 安裝來源不明的 skill 前，務必先讀過 `scripts/` 的內容。這是 skill 生態系最主要的風險面。

---

## ✅ 撰寫檢查清單

- [ ] `description` 同時寫了「**何時該用**」與「**何時不該用**」
- [ ] 流程是編號步驟，不是一段散文
- [ ] 明確寫出**不可以做什麼**（不可捏造、不可修改原始檔）
- [ ] 輸出格式具體到可以驗收
- [ ] 沒有把單次任務的細節寫進去
- [ ] `scripts/` 內的程式已人工審閱過
- [ ] 用三個真實案例測過，包含一個**不該觸發**的案例

---

## 🔄 與 Claude Skills 的對照

| 面向 | Claude Skills | Codex Skills |
| :--- | :--- | :--- |
| 檔名 | `SKILL.md` | `SKILL.md`（相同） |
| Frontmatter | `name`、`description` | `name`、`description`（相同） |
| 安裝位置 | 帳號 / Project 層級（雲端） | **檔案系統路徑**，六層作用域 |
| 團隊分享 | 透過介面分享 | **提交進 Git** |
| 呼叫語法 | 自動觸發為主 | `@name`（ChatGPT）／`$name`（Codex） |
| 快速產生 | 對話描述 | `$skill-creator` 或 **Record & Replay** |

> **遷移提示**：`Claude_ai/Skills/Examples` 底下的純文字流程內容**可以直接參考沿用**，但安裝路徑、工具名稱、權限模型與 UI 操作必須改成 Codex 版本。

---

## 小結

| 需求 | 用什麼 |
|---|---|
| 每次都要遵守的規則 | [`AGENTS.md`](../Agent_Configuration/README.md) |
| 特定工作的完整流程 | **Skill** |
| 連接外部 API 或資料庫 | [MCP](../MCP/README.md) |
| 打包多個 skill + 整合 + UI | [Plugin](../Plugins/README.md) |
| 這一次的臨時需求 | 寫在 [task](../Tasks/README.md) 裡 |

**官方說明**：[Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins) · [Build skills](https://learn.chatgpt.com/docs/build-skills)

---

← [返回上層：ChatGPT Codex 索引](../README.md)
