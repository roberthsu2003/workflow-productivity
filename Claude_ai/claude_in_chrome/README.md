# Claude in Chrome 設定與使用教學

> 本文說明 Claude in Chrome 擴充功能是什麼、如何與 Claude Desktop 搭配運作

---

## 一、什麼是 Claude in Chrome？

**Claude in Chrome** 是 Anthropic 推出的 **Chrome 瀏覽器擴充功能**，安裝後可以讓 Claude
直接進入你「目前正在使用、已經登入」的瀏覽器，代替你進行：

- 開啟分頁、切換分頁
- 點擊按鈕、填寫表單
- 讀取頁面內容
- 執行一連串的操作步驟（例如：查詢資料 → 整理 → 回報結果）

因為它操作的是你**真實的瀏覽器環境**，所以能沿用你既有的登入狀態（Cookie、Session），
很適合用在「需要登入才能看到內容」的網站，例如：

- 公司內部系統
- Gmail、Google 日曆等已登入的服務
- 需要帳號密碼的會員網站

---

## 二、安裝位置 vs 管理位置

這是最容易搞混的地方，先釐清觀念：

| 項目 | 說明 |
|---|---|
| **安裝位置** | Chrome 瀏覽器本身，從 Chrome 線上應用程式商店安裝「Claude in Chrome」擴充功能 |
| **管理/設定位置** | 可以在**擴充功能自己的設定頁**改，也可以在 **Claude Desktop 的「Claude in Chrome settings」**頁面改 |

重點：**這兩邊改的是同一份設定，彼此同步**，不是兩個獨立的系統。
Claude Desktop 提供的畫面，其實是一個「遠端管理面板」，讓你不用特地切到 Chrome
也能設定哪些網站允許、哪些網站封鎖。

---

## 三、Claude Desktop 的「Claude in Chrome settings」畫面說明

在 Claude Desktop 左側選單 → **Claude in Chrome**，可以看到以下設定：

### 1. Enable Claude in Chrome（啟用開關）

- 控制 Claude Desktop 是否能**連接**已安裝的 Chrome 擴充功能
- 開啟後，就能直接在 Claude Desktop 的對話框下指令，
  由擴充功能代為執行瀏覽器動作，不需要手動切到 Chrome 側邊欄操作

### 2. Site permissions（網站權限）

- **Default for all sites**：設定預設是「允許所有網站」還是「預設封鎖」
- **Blocked sites**：手動加入不允許 Claude 存取的網站清單

> ⚠️ 這份權限清單同時套用在：
> - Claude in Chrome 擴充功能本身
> - Claude Code Desktop 內建的瀏覽器
>
> 也就是說，不管你從哪個入口操作，都是共用同一份「哪個網站可不可以存取」的規則，
> 不需要重複設定兩次。

---

## 四、Claude Desktop 如何「遠端操作」Chrome？

啟用連接器之後的實際運作方式：

```
你在 Claude Desktop 下指令（例如：「幫我打開 Gmail 看看有沒有新信」）
        ↓
指令透過連接器傳送給 Claude in Chrome 擴充功能
        ↓
擴充功能在你電腦上的 Chrome 實際執行：開分頁、點擊、輸入文字、讀取頁面
        ↓
結果回傳到 Claude Desktop 對話框顯示
```

簡單說：

- **擴充功能** = 實際動手做事的「手腳」
- **Claude Desktop** = 下指令的「介面」，讓整個工作流程可以留在同一個視窗完成

---

## 五、權限審核機制

無論從擴充功能側邊欄操作，或是從 Claude Desktop 下指令，都會套用相同的三種權限模式：

| 模式 | 說明 |
|---|---|
| **Manual（手動核准）** | Claude 每次動作前都會暫停，等你按「允許」或「拒絕」 |
| **Auto（自動核准）** | Claude 持續執行，自行判斷安全性，遇到有風險或不確定的動作才會暫停詢問 |
| **Skip（略過所有審核）** | 完全不暫停詢問，風險最高，建議謹慎使用 |

**建議教學情境**：初次示範時使用 **Manual** 模式，讓學生清楚看到每一步 Claude 打算做什麼動作。

---

## 六、Claude in Chrome vs Playwright MCP（重要觀念比較）

課堂上很常見的疑問：「用 Playwright 爬蟲時，是不是要先開啟 Claude in Chrome？」

**答案：不需要，兩者是完全獨立的工具。**

| 比較項目 | Playwright MCP | Claude in Chrome |
|---|---|---|
| 瀏覽器來源 | 自己啟動一個**全新、乾淨**的瀏覽器 | 直接控制你**現有、已登入**的 Chrome |
| 是否需要安裝擴充功能 | 不需要 | 需要 |
| 登入狀態 / Cookie | 沒有，等於全新環境 | 有，沿用你目前的登入狀態 |
| 適合情境 | 公開資料查詢、不需登入、可重複執行的自動化 | 需要操作已登入帳號的網站 |
| 適合排程無人值守 | 較適合（穩定、不依賴擴充功能連線） | 較不適合（權限允許設定可能無法持久保存，目前仍有已知問題） |

---

## 七、排程自動化時的注意事項

如果之後想把瀏覽器操作設定成「定時自動執行」（Scheduled Task），要特別注意：

1. **本機排程任務**只有在電腦開機、Claude Desktop app 有開啟時才會執行。
2. 建立排程時可設定「always allow（永遠允許）」，但目前 **Claude in Chrome / Playwright 的允許設定，在排程重跑時可能無法穩定保存**，導致任務卡住等待人工核准。
3. 若只是要抓取**公開、免登入**的資料，優先考慮：
   - 該網站是否有開放 API
   - 是否提供可直接下載的 txt / csv / json 檔案連結
   - 用這些方式直接抓資料，完全不需要瀏覽器互動，最適合排程無人值守執行。
4. 只有在網站**必須登入**、且非得靠點擊互動才能取得資料時，才需要用到 Claude in Chrome，
   而這類任務建議安排在「有人在電腦前」的時段執行較為穩定。

---

## 八、重點整理

- Claude in Chrome 是「擴充功能」，安裝在 Chrome 裡；Claude Desktop 的設定頁只是**遠端管理入口**，兩邊設定同步。
- 啟用連接器後，可以直接在 Claude Desktop 下指令操作瀏覽器，不用切換視窗。
- 網站權限清單是共用的，Claude in Chrome 與 Claude Code Desktop 內建瀏覽器都適用。
- Playwright 與 Claude in Chrome 是兩套獨立工具：**不需要登入 → 用 Playwright；需要登入狀態 → 用 Claude in Chrome**。
- 排程自動化情境下，公開資料優先用「直接下載連結／API」，避免依賴瀏覽器互動造成任務卡住。
