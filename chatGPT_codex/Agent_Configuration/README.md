# Agent Configuration：用 `AGENTS.md` 設定代理

> 🟢 **方案需求**：Free（全方案可用）

`AGENTS.md` 是 Codex 版的 Custom Instructions，但比 Claude 的專案指示強大得多：它**依目錄作用域層層疊加與覆寫**，而且是純文字檔，可以提交進 Git、隨 repo 分發給全隊。

> **一句話定位**：[Tasks](../Tasks/README.md) 管「這一次要做什麼」，`AGENTS.md` 管「**每一次都要遵守什麼**」。

---

## 🎯 為什麼這是最高 CP 值的一章

觀察學員的 prompt，你會發現同樣的句子一直重複出現：

```text
...請用 pnpm 不要用 npm...
...測試指令是 pnpm test:unit...
...不要動 src/legacy/ 底下的東西...
...修 bug 時要補回歸測試...
```

這些話**寫一次就好**。搬進 `AGENTS.md` 之後，你的 task 從 30 行變成 8 行，而且不會因為某次忘了寫而出事。

---

## 📂 作用域與優先序

Codex 從兩個層級尋找指示檔：

### 1. 全域（Global）

位於 Codex home 目錄，預設 `~/.codex/`：

```text
~/.codex/AGENTS.override.md   ← 優先讀取
~/.codex/AGENTS.md            ← 沒有 override 才讀這個
```

適合放**跨所有專案的個人偏好**：回覆語言、你習慣的溝通方式、你個人的安全底線。

### 2. 專案（Project）

從 Git repo 根目錄，一路往下到你目前的工作目錄，**每一層目錄各檢查一次**：

```text
repo-root/AGENTS.md                       ← 先讀
repo-root/services/AGENTS.md              ← 再讀，覆寫上面
repo-root/services/payments/AGENTS.override.md  ← 最後讀，優先權最高
```

### 合併規則

> [!IMPORTANT]
> **從 repo 根目錄往下合併，越接近目前目錄的檔案優先權越高。**
> 官方說明：*"Files closer to your current directory override earlier guidance because they appear later in the combined prompt."*
>
> 每一層目錄**最多讀一個檔案**：同層若同時有 `AGENTS.override.md` 與 `AGENTS.md`，只讀 `override` 那個。

### 完整層級示意

```text
~/.codex/AGENTS.md                      # 全域：我的個人偏好
└── tideflow-portal/
    ├── AGENTS.md                       # repo 全域：技術棧、測試、風格
    ├── services/
    │   └── payments/
    │       └── AGENTS.override.md      # 金流服務的特殊規範（法遵、稽核）
    └── src/legacy/
        └── AGENTS.md                   # 舊程式碼區：只修不重構
```

---

## 📏 大小限制

| 項目 | 值 |
| :--- | :--- |
| 預設讀取上限 | **32 KiB**（`project_doc_max_bytes`） |
| 空檔案 | 直接略過 |
| 超過上限 | 拆分到子目錄，或在 `config.toml` 調高上限 |

```toml
# ~/.codex/config.toml
project_doc_max_bytes = 65536   # 調高到 64 KiB（不建議，先考慮拆分）
```

> **實務建議**：一份 `AGENTS.md` 控制在 **100 行以內**。超過通常代表你把「文件」寫進了「規則」——把背景說明搬去 `docs/`，`AGENTS.md` 只留可執行的指令。

---

## 🧱 建議的章節結構

### 完整範例：`tideflow-portal/AGENTS.md`

```markdown
# AGENTS.md — 潮汐物流 Portal

## Project
- Node.js 22 + TypeScript 5.6，套件管理器一律用 **pnpm**（不要用 npm 或 yarn）。
- 原始碼在 `src/`，測試在 `tests/`，資料庫遷移在 `migrations/`。
- 前端 Next.js App Router；後端 API 在 `src/api/`。

## Commands
- 安裝：`pnpm install --frozen-lockfile`
- 開發：`pnpm dev`
- 單元測試：`pnpm test:unit`
- 端對端測試：`pnpm test:e2e`（需先啟動 `pnpm dev`）
- 型別檢查：`pnpm typecheck`
- Lint：`pnpm lint --fix`

## Working agreements
- 修 bug 時**必須**補上對應的回歸測試。
- 不修改公開 API 的輸入／輸出型別，除非任務明確要求。
- 不引入新的執行期依賴；需要時先在對話中提出並說明理由。
- 提交前必須通過 `pnpm typecheck` 與 `pnpm test:unit`。

## Boundaries
- `src/legacy/`：只修正 bug，**不要重構、不要改風格**。
- `migrations/`：只能新增檔案，**絕不修改或刪除既有 migration**。
- 不要提交 `.env`、`*.pem`、`secrets/` 底下任何檔案。

## Code review rules
- 標記出未處理的 Promise rejection。
- 標記出直接字串拼接的 SQL。
- 金額一律用整數（分）計算，發現浮點數金額請標記。

## Style
- 繁體中文撰寫 commit message 與 PR 說明；程式碼註解用英文。
- 錯誤訊息面向使用者時用繁體中文，面向開發者的 log 用英文。
```

### 子目錄覆寫範例：`services/payments/AGENTS.override.md`

```markdown
# 金流服務特別規範

> 本檔覆寫 repo 根目錄的 AGENTS.md。

## 額外限制
- 這個目錄涉及支付法遵，**任何變更都必須同時更新 `CHANGELOG.md`**。
- 不可寫入任何日誌包含完整卡號、CVV 或持卡人姓名。
- 對外 API 的錯誤碼不可變更語意，只能新增。

## Verification
- 除了 repo 預設測試，額外執行 `pnpm test:payments --coverage`，覆蓋率不得低於 90%。
```

---

## ✍️ 寫得好 vs. 寫不好

| ❌ 沒用的寫法 | ✅ 可執行的寫法 |
| :--- | :--- |
| 「請寫出高品質的程式碼」 | 「提交前必須通過 `pnpm typecheck` 與 `pnpm test:unit`」 |
| 「注意安全性」 | 「標記出直接字串拼接的 SQL；金額一律用整數（分）計算」 |
| 「遵循專案慣例」 | 「套件管理器一律用 pnpm；測試檔命名為 `*.test.ts` 放在 `tests/`」 |
| 「這次幫我把登入頁改成深色」 | （這是單次任務，寫在 task 裡，不要寫進 `AGENTS.md`） |
| 「架構請參考微服務最佳實踐」 | 「`src/api/` 不可直接 import `src/ui/`；跨層呼叫走 `src/lib/`」 |

> [!WARNING]
> **不要把單次任務的細節永久寫進 `AGENTS.md`。** 它會在往後每一個 task 都生效，久了會累積成一堆互相矛盾的過期規則。判準很簡單：**這條規則三個月後還成立嗎？** 不成立就寫在 task 裡。

---

## 🔄 與 Claude Custom Instructions 的對照

| 面向 | Claude Projects Custom Instructions | Codex `AGENTS.md` |
| :--- | :--- | :--- |
| 儲存位置 | 雲端，綁在 Project 上 | **repo 內的純文字檔** |
| 分享方式 | 邀請成員加入 Project | `git push`，全隊自動生效 |
| 作用域 | 整個 Project 一份 | **可依目錄層層覆寫** |
| 版本控管 | 無 | Git 完整歷史 |
| 大小上限 | 依介面 | 32 KiB（可調） |
| 適合放 | 角色設定、語氣、輸出格式 | 建置命令、架構邊界、驗收要求 |

> **教學提醒**：這是 Claude 使用者轉換到 Codex 時最大的心智模型轉變——**專案規則不再是「設定」，而是「程式碼的一部分」**。它會被 review、會有 diff、會有人問「這條規則為什麼加的」。

---

## 🧪 課堂練習

1. 用 [Quickstart](../Quickstart/README.md) 的練習 repo，執行一個只讀 task：
   ```text
   請閱讀這個 repo，然後**只產生一份 AGENTS.md 草稿**。
   內容只能包含你從 repo 實際讀到的事實（套件管理器、測試命令、目錄結構）。
   任何你無法確認的項目，請用「TODO：待補」標示，不要猜測。
   不要修改其他檔案。
   ```
2. 人工審查草稿，把 `TODO` 補完、把猜測刪掉。
3. 再跑一個修改型 task，觀察它**是否自動遵守**你剛寫的規則——不要在 task 裡重複那些規則。
4. 在 `src/` 底下新增一個 `AGENTS.md`，寫一條與根目錄衝突的規則，觀察哪一條生效（答案：子目錄的）。

---

## 小結

| 要點 | 說明 |
|---|---|
| 位置 | 全域 `~/.codex/AGENTS.md`；專案從 repo root 逐層往下 |
| 優先序 | 越靠近目前目錄，優先權越高；`AGENTS.override.md` 勝過 `AGENTS.md` |
| 上限 | 32 KiB，建議控制在 100 行內 |
| 該寫 | 命令、邊界、驗收要求、code review 規則 |
| 不該寫 | 單次任務細節、空泛形容詞、背景文件 |

**官方說明**：[Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

---

← [返回上層：ChatGPT Codex 索引](../README.md)
