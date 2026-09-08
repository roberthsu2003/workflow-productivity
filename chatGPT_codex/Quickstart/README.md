# Quickstart（快速開始）

> 🟢 **方案需求**：Free（本章全部練習 Free 帳號均可完成）

這一章的目標不是「跑出漂亮結果」，而是讓你在**第一次就建立正確的使用習慣**：先讓 Codex 只讀不寫，確認它真的看懂了，再授權它動手。

> [!IMPORTANT]
> 開始之前，請先完成 [Settings 章節](../Settings/README.md) 的課堂檢查清單，確認權限模式是 **Ask for Approval**。

---

## 🧭 Codex 是什麼（以及不是什麼）

| 它是 | 它不是 |
| :--- | :--- |
| 會讀檔、改檔、執行命令、跑測試的**代理** | 只會回答問題的聊天室 |
| 在**你指定的工作目錄**內做事 | 憑空生成程式碼給你複製貼上 |
| 完成後給你 **diff、測試結果與摘要** | 直接把結果推上線 |

一句話：**Claude Chats 產出「內容」，Codex 產出「已驗證的變更」。**

---

## 📍 四種使用介面，先選一個

| 介面 | 適合 | 方案 |
| :--- | :--- | :---: |
| **ChatGPT 桌面版** | 課堂教學首選。有 diff 檢視、終端機、瀏覽器與成品預覽 | 🟢 Free |
| **Codex CLI** | 終端機工作流、遠端主機、腳本化 | 🟢 Free |
| **IDE extension** | 在 VS Code / JetBrains 內邊寫邊問 | 🟢 Free |
| **Codex cloud / web** | 背景長時工作、跨裝置 | 🔵 Plus |

> 本講義的截圖與操作步驟以 **ChatGPT 桌面版** 為準。CLI 與桌面版共用同一套代理概念，但 UI、登入方式與部分功能不同，請以 [官方 CLI 文件](https://learn.chatgpt.com/docs/cli) 為準。

---

## 🚀 五個步驟跑完第一個 task

### Step 1：建立或選取 project

在 Codex 中加入一個 **saved project**——通常是一個本機資料夾或 Git repository。

> [!WARNING]
> **第一次請不要選你正在工作的重要專案。** 建議先 `git clone` 一個公開範例 repo，或建立一個測試資料夾。Codex 會實際修改檔案。

```bash
# 課堂建議：建一個乾淨的練習專案
mkdir ~/codex-lab && cd ~/codex-lab
git init
echo "# Codex 練習專案" > README.md
git add . && git commit -m "init"
```

### Step 2：先做「只讀偵察」

第一個 task 永遠是**不授權修改**的理解任務。這一步能立刻暴露「Codex 有沒有看懂你的專案」。

```text
請閱讀這個專案的 README.md 與 AGENTS.md（若存在），
整理出：專案用途、啟動方式、目錄結構、以及使用了哪些工具鏈。

限制：不要修改任何檔案，也不要執行安裝命令。
若資訊不足，請直接列出你無法確認的項目，不要猜測。
最後請指出三個最值得補強的文件項目。
```

**驗收重點**：它有沒有老實說「我不知道」？如果它把不存在的東西講得很篤定，代表你的專案缺少可讀的說明，先補 `AGENTS.md`（見[該章節](../Agent_Configuration/README.md)）。

### Step 3：授權一次小範圍修改

第二個 task 才開始改檔，而且**只改一個檔案**。

```text
請替 README.md 新增「快速開始」段落。

範圍：只能修改 README.md，不要新增或刪除其他檔案。
做法：先確認 package.json（或等效設定檔）裡實際可用的安裝與啟動命令，
      不要寫沒有根據的命令。
驗收：完成後檢查所有連結與命令是否與專案現況一致，並摘要你改了什麼。
```

### Step 4：檢查 diff，而不是只看摘要

這是最多人跳過、也最重要的一步。

- 桌面版：切到 **diff 檢視**，逐行看它改了什麼
- CLI：`git diff`
- 有測試的專案：確認它**真的跑了測試**，而不是只說「應該會過」

> [!IMPORTANT]
> **摘要是模型寫的，diff 是事實。** 兩者不一致時以 diff 為準。

### Step 5：接受或還原

```bash
# 滿意 → 提交
git add . && git commit -m "docs: add quickstart section"

# 不滿意 → 一鍵還原
git restore .
```

> 這就是為什麼 Step 1 要先 `git commit`。**Git 是你使用 Codex 時最重要的安全網。**

---

## 🧪 課堂練習：潮汐物流的第一天

用本講義的示範情境走一次完整流程。假設你剛接手 **潮汐物流（TideFlow Logistics）** 的 `tideflow-portal` 專案。

| 階段 | Task | 授權範圍 |
| :--- | :--- | :--- |
| 偵察 | 「整理這個 repo 的結構與啟動方式，列出你不確定的地方」 | 只讀 |
| 補文件 | 「依你剛才的理解，建立 `AGENTS.md`，寫入建置命令與測試命令」 | 只能新增 `AGENTS.md` |
| 小修 | 「README 的安裝步驟與 package.json 不一致，請修正 README」 | 只能改 `README.md` |
| 驗收 | 「執行測試並回報結果；若失敗，只診斷不要修」 | 只讀 + 執行測試 |

**教學重點**：每個階段都明確寫出「可以動什麼」。學員最常犯的錯是第一句話就說「幫我把這個專案整理好」——範圍太大，結果無法驗收。

---

## ❌ 新手最常見的五個錯誤

| 錯誤 | 後果 | 正確做法 |
| :--- | :--- | :--- |
| 第一句就授權大範圍修改 | 改動散落多檔，無法審查 | 先只讀偵察 |
| 沒先 commit 就開始 | 改壞了回不去 | `git commit` 再開始 |
| 只看摘要不看 diff | 相信了沒發生的事 | 逐行看 diff |
| 沒寫驗收方式 | 它自認完成，你不同意 | 每個 task 都寫「怎樣算做完」 |
| 一個 task 塞多個目標 | 上下文混亂、互相干擾 | 不相干的目標拆成不同 task |

---

## 小結

| 步驟 | 一句話 |
|---|---|
| 1. 建 project | 選乾淨的練習專案，先 commit |
| 2. 只讀偵察 | 確認它看懂了，且會誠實說不知道 |
| 3. 小範圍修改 | 明確寫出「只能改哪個檔」 |
| 4. 看 diff | 摘要是說法，diff 是事實 |
| 5. 接受或還原 | `git commit` 或 `git restore` |

**下一步**：[Tasks 章節](../Tasks/README.md)會把 Step 2、3 的提示詞升級成可複製的 **GCSV 框架**範本。

**官方說明**：[Quickstart](https://learn.chatgpt.com/docs/quickstart) · [Prompting](https://learn.chatgpt.com/docs/prompting)

---

← [返回上層：ChatGPT Codex 索引](../README.md)
