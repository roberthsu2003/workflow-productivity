# Dispatch（Beta）：手機下指令，電腦幫你做

> 🟣 **方案需求**：**Pro 或 Max 方案專屬（Beta）**，需同時安裝最新版 **Claude Desktop app** 與 **Claude 手機 App**（iOS / Android）。  
> 參考：[Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)

**Dispatch** 讓你在手機上傳訊息給 Claude，Claude 就會在你的**電腦桌面**上實際執行任務——使用本機檔案、Connectors、Plugins 與應用程式，完成後把成品回傳給你。可以把它想成「手機是遙控器，電腦是實際幹活的機器人」。

---

## 🔑 使用需求

1. 電腦端安裝最新版 **Claude Desktop app**（macOS、Windows x64 或 Linux），且電腦必須保持**開機、未休眠**，Claude Desktop 需維持開啟狀態
2. 手機端安裝最新版 **Claude App**（iOS / Android）
3. 帳號需為 **Pro 或 Max 方案**
4. 兩端裝置都需要**穩定的網路連線**

> 💡 與雲端 Session（如 Scheduled）不同：Dispatch 是在**你的電腦上**執行任務，電腦關機或 Claude Desktop 關閉時任務就無法進行；若希望電腦關機也能繼續工作，應改用雲端 Cowork Session。

---

## 🧵 運作邏輯：一條不會重置的對話串

Dispatch 的核心概念是「**單一持續對話**」：

- 不論你從手機或電腦開啟，看到的都是**同一條對話**、**同一份記憶**
- 上班途中用手機交辦任務，坐到電腦前可以直接接續，不需要重新說明背景
- 當你交辦任務後，Claude 會判斷任務類型並自動啟動對應的 Session：**開發類任務**會在 Claude Code 執行，**知識工作類任務**會在 Cowork 執行，兩者分別出現在各自的側欄
- Claude 完成後會直接把結果（試算表、備忘錄、比較表、Pull Request 等）傳訊息給你，而不是逐步展示過程；完成或需要你確認時會推播通知到手機

---

## 🚀 開始使用

1. 下載或更新 **Claude Desktop**
2. 下載或更新 **Claude iOS / Android App**
3. 在手機或電腦任一端開啟 Cowork
4. 點選左側欄「Dispatch」
5. 進入功能說明頁後，點選「Get started」
6. 依畫面提示，開啟「存取本機檔案」與「保持電腦喚醒」等權限
7. 點選「Finish setup」完成設定，即可在「Dispatch」區塊開始與 Claude 對話

---

## 📌 你可以用 Dispatch 做什麼

- 請 Claude 從本機試算表擷取資料並彙整成報告
- 請 Claude 搜尋 Slack 訊息與 Email，草擬簡報文件
- 請 Claude 根據 Google Drive 中的檔案，產出格式化簡報
- 請 Claude 整理或處理電腦上特定資料夾的檔案

Dispatch 會沿用你在 Cowork 中已設定好的 Connectors、Plugins 與檔案存取權限，**不需要另外重新設定**。

延伸功能：
- **排程任務**：可請 Claude 每天早上檢查信箱、每週彙整指標、固定產出週報，詳見 [Scheduled 章節](../Scheduled/README.md)
- **Computer Use**：Claude 可直接操作電腦上的應用程式（如更新 Excel 試算表、瀏覽內部系統），但 **Linux Beta 版尚不支援 Computer Use**，僅能使用檔案、Connectors 與 Plugins

---

## ⚠️ 安全性提醒

Dispatch 讓手機端可以透過 Claude 存取電腦上的所有資源，包含檔案、Connectors、已安裝的 Plugins，以及透過 Computer Use 操作的應用程式。這形成一條「手機指令 → 電腦實際動作」的鏈路，代表：

- 錯誤指令、非預期指令，或是路徑中出現的惡意內容（例如釣魚連結），都可能造成難以復原的實際後果

啟用前請確認：

1. 你信任這條鏈路中的**每一個應用程式與服務**
2. 你清楚知道 Claude 能存取哪些檔案與帳號
3. 你知道如何**快速中斷或撤銷存取權限**

只在你能接受 Claude「可能做到的事」（而不只是你「打算讓它做的事」）時，才啟用跨裝置連動。

---

## 📎 目前限制

- **電腦必須保持運作**：Dispatch 依賴桌面本機的檔案與應用程式，電腦需保持開機、Claude Desktop 需保持開啟
- **Computer Use 的安全性質不同於其他 Cowork 工具**：Claude 直接點擊、輸入、操作畫面，而非透過 Connectors 或權限管控的檔案存取
- **僅有單一持續對話串**：目前無法另開新對話或管理多條對話，所有訊息都在同一條對話中
- **Linux 版本不支援 Computer Use**：檔案、Connectors、Plugins 相關任務仍可正常使用

---

## 💡 教學提醒

若你目前在 Claude Desktop 側欄看不到「Dispatch」，通常代表：

1. 帳號方案未達 Pro / Max（Dispatch 目前僅開放 Pro 與 Max）
2. 尚未安裝或更新到支援此功能的最新版 App

可先參考本章節了解概念，未來帳號升級或功能開放後即可直接上手。

---

← [返回上層：Claude_AI 索引](../README.md)
