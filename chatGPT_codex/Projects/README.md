# Projects（專案與知識來源）

> 🟢 **方案需求**：Free（可建立 project 並連結本機資料夾）。雲端環境與跨裝置執行需 🔵 Plus。

Project 把**相關的 chats、檔案、指示與資料來源收在一起**。當工作跨越多個產出、會持續一段時間、或依賴共用資源時，就該建立 project。

---

## 🆚 三種 Project，先分清楚

Codex 的 Project 比 Claude Projects 多了一個關鍵維度：**它可以綁定你電腦上的真實資料夾**。

| 類型 | 資料在哪 | 能做什麼 | 適合 |
| :--- | :--- | :--- | :--- |
| **ChatGPT project** | 上傳到雲端 Sources | 讀取上傳的檔案，不接觸本機 | 知識庫問答、文件彙整（最接近 Claude Projects） |
| **Local project** | 你電腦上的資料夾 | **讀檔、改檔、執行命令** | 實際的開發與檔案處理工作 |
| **Codex project** | 工作目錄本身即為 project 內容 | 同上，並以該目錄為預設工作路徑 | Git repository |

> **Local project 可以掛多個資料夾**，並指定其中一個為 **primary**（預設工作目錄）。例如同時掛入 `tideflow-portal/`（程式碼）與 `tideflow-docs/`（規格文件），讓 Codex 改程式時能對照規格。

---

## 🌳 三種執行環境

同一個 project，可以在三種環境中跑 task。這是 Codex 最容易搞混、也最重要的觀念。

| 環境 | 適合情境 | 特性 | 方案 |
|---|---|---|---|
| **Local / checkout** | 直接處理目前的工作目錄 | 看得到你未提交的變更；**會直接改你正在編輯的檔案** | 🟢 Free |
| **Worktree** | 同一個 repo 平行跑多個 task | Git worktree 隔離分支與檔案，互不干擾 | 🟢 Free |
| **Cloud** | 遠端執行、背景長時工作、跨裝置 | 需可重現的依賴與環境；secrets 走安全設定 | 🔵 Plus |

### 什麼時候該用 Worktree

> [!WARNING]
> **不要讓兩個 task 同時改同一批檔案。** 這是使用 Codex 最常見的災難來源——兩個代理各自以為自己是唯一的作者，互相覆蓋。

```bash
# 主目錄留給 task A
cd ~/projects/tideflow-portal

# 為 task B 開一個獨立 worktree
git worktree add ../tideflow-portal-feature-b feature/b

# 兩個 task 各自綁定不同目錄，檔案完全隔離
```

完成後清理：

```bash
git worktree remove ../tideflow-portal-feature-b
```

### 什麼時候該用 Cloud

- 工作要跑很久（大規模遷移、批次處理），你想關掉筆電
- 你想從手機交辦並接續（見 [Remote](../Remote/README.md)）
- 需要乾淨、可重現的環境（避免「在我電腦上可以跑」）

> [!IMPORTANT]
> Cloud 環境**看不到你未提交的本機變更**。使用前確認：依賴能安裝、測試能執行、secrets 透過安全設定提供（**不要寫進 prompt 或 repo**）。

---

## 📚 Sources：專案知識來源

每個 project 有一個 **Sources** 區塊，可上傳檔案或連結外部來源，讓該 project 底下**所有 chats 共用**。

| 該放進 Sources | 不該放進 Sources |
| :--- | :--- |
| 品牌語調指南、術語對照表 | 這次會議的逐字稿（放在 task 裡就好） |
| API 規格、資料字典 | 大量原始資料（改用 local project 讀檔） |
| 法遵與合約範本 | 含個資或憑證的檔案 |
| 公司內部術語與縮寫表 | 頻繁變動的資料（會過期） |

> **與 `AGENTS.md` 的分工**：Sources 放**參考資料**（它需要「知道」的），`AGENTS.md` 放**行為規則**（它需要「遵守」的）。

---

## 🧭 Project Instructions

Project instructions 對該 project 底下**所有 chats** 生效，適合放角色設定、語氣與輸出偏好。

```markdown
所有回覆使用繁體中文。
本 project 服務對象是潮汐物流的營運部門，非工程背景。
解釋技術問題時避免術語，必要時用類比。
輸出報表一律用「年／月／日」格式，金額標註幣別 TWD。
```

> [!IMPORTANT]
> **Project instructions vs. `AGENTS.md`——不要重複寫。**
>
> | 內容 | 寫在哪 |
> | :--- | :--- |
> | 語氣、角色、回覆語言 | Project instructions |
> | 建置命令、測試命令、架構邊界 | `AGENTS.md`（跟著 repo 走） |
> | 這次的具體要求 | task 本身 |
>
> 判準：**這條規則換一台電腦、換一個人執行還成立嗎？** 成立就寫進 `AGENTS.md`（因為它在 repo 裡）；只跟你的使用習慣有關，寫 project instructions。

---

## 💬 Chats 與 Project 的關係

- 一個 project 底下有多個 chats，全部共用 Sources 與 instructions。
- **不同產出開不同 chat**，讓每個對話的訊息與結果保持聚焦。
- 需要平行處理程式碼時，除了開不同 chat，還要**搭配不同的 worktree**——否則檔案會打架。

```text
Project: 潮汐物流 Q3 營運改善
├── Sources: 配送 SLA 規範.pdf、區域代碼對照表.csv
├── Instructions: 繁體中文、面向非工程背景讀者
├── Chat 1: 分析 8 月準時率異常          → 只讀
├── Chat 2: 修正結帳頁運費計算            → worktree A
└── Chat 3: 產出月度營運報告              → 只寫 reports/
```

---

## 🏗️ 讓 repo 適合被代理使用

一個「代理友善」的 repo 應該具備：

- [ ] `README.md`：專案用途與快速開始
- [ ] `AGENTS.md`：建置命令、測試命令、架構邊界（見[該章節](../Agent_Configuration/README.md)）
- [ ] 一鍵可跑的安裝與測試命令
- [ ] 明確的驗收方式（測試、型別檢查、lint）
- [ ] `.gitignore` 完整，機密不在 repo 內

> [!WARNING]
> **API key、token 與客戶機密絕對不可提交到 Git。** 即使你事後刪除，Git 歷史仍保留。Codex 讀得到 workspace 內的一切——包含你以為沒人會看的 `.env.backup`。

---

## 📖 教材範例

| 範例 | 情境 | 重點 |
|---|---|---|
| [01. 行政營運](./Examples/01_Office_Administration/README.md) | 會議紀錄、術語對照、內部文件整理 | Sources 的正確用法 |
| [02. 品牌與行銷](./Examples/02_Brand_and_Marketing/README.md) | 麥禾烘焙品牌語調與文案產出 | Project instructions 的威力 |
| [03. 商業情報](./Examples/03_Business_Intelligence/README.md) | 跨季配送數據分析與報表產出 | Local project 直接讀 CSV、**缺漏值處理** |
| [04. 個人學習教練](./Examples/04_Personal_Coach/README.md) | 三個月 Python 學習計畫 | **用 Instructions 設限**，對抗「太好相處」 |
| [05. 盡職調查與稽核](./Examples/05_Due_Diligence/README.md) | 財務預估合理性評估 | **四段式標示防幻覺**、「無法評估」是有效結論 |
| [06. 技術標準查核](./Examples/06_Green_Energy_Standards/README.md) | 儲能建置案逐條法遵查核 | **「有設置 X」≠ 符合**、不推測動機 |

---

## 🔄 與 Claude Projects 的對照

| 面向 | Claude Projects | Codex Projects |
| :--- | :--- | :--- |
| 數量限制 | Free 限 5 個 | 未公告固定上限 |
| 檔案來源 | 上傳到 Project Knowledge | 上傳 **或** 直接綁本機資料夾 |
| 能否改檔 | 否，只能讀 | **可以**（local / worktree / cloud） |
| 自訂指示 | Custom Instructions | Project instructions + `AGENTS.md` |
| 版本控管 | 無 | 綁 Git repo 時完整可追溯 |

---

## 小結

| 決定 | 怎麼選 |
|---|---|
| 只是查資料、不改檔 | ChatGPT project + Sources |
| 要改本機檔案 | Local / Codex project |
| 同時跑多個改檔 task | 每個 task 一個 **worktree** |
| 要跑很久或跨裝置 | Cloud 環境（需 Plus） |
| 規則要跟著 repo 走 | `AGENTS.md` |
| 規則只跟你的習慣有關 | Project instructions |

**官方說明**：[Projects](https://learn.chatgpt.com/docs/projects) · [Environments](https://learn.chatgpt.com/docs/developers)

---

← [返回上層：ChatGPT Codex 索引](../README.md)
