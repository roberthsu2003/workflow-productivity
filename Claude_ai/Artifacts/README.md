# Claude Artifacts（成品）— 2026 新版全面改版

> **一句話理解**：Artifact 是「Claude 幫你做出來、可以拿給別人看的東西」——文件、簡報、設計稿、儀表板、試算表或互動小工具。它會開在對話旁邊，可以繼續修改、隨時回來找，也可以分享給別人。
>
> 🔗 **全域概念對照**：Claude 稱為 **Artifacts**，ChatGPT 稱為 **Canvas 畫布**（詳見 [ChatGPT Canvas 篇](../../chatGPT/03_Canvas/README.md)）。實戰應用請參考 [學員職場實戰案例庫](../../學員職場實戰案例/README.md)。
>
> 📖 **官方來源**（2026/11 查證）：[What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) · [Share artifacts](https://support.claude.com/en/articles/9547008-share-artifacts) · [Claude Pricing](https://claude.com/pricing)

---

## 🆕 這次到底改了什麼？（舊版 vs 新版）

**2026/9/16** 起，Artifacts 從「對話右側的預覽小視窗」升級成**獨立的成品中心**。之前在這天以前做的 Artifact，官方稱為**舊版 Artifact（legacy artifacts）**。

| 項目 | 舊版（2026/9/16 以前） | 🆕 新版 |
| :--- | :--- | :--- |
| 存放位置 | 散落在各個對話裡 | 統一收在左側欄 **Artifacts** 分頁（`claude.ai/artifacts`） |
| 成品種類 | HTML / React / SVG / Mermaid / Markdown / 程式碼 | 以上全部 ➕ **Docs、Slides、Design、Data、Sheets、Whiteboards、Motion** 七種範本 |
| 修改方式 | 只能叫 Claude 改 | 叫 Claude 改、**直接在範本上手動編輯**、在文件中**反白文字按「Edit with Claude」** |
| 分享 | Publish 後產生公開連結 | **預設私人**；可設定「只有你／知道連結的人／指定 Email」，並分成 **檢視 / 留言 / 編輯** 三種權限 |
| 資料儲存 | 20 MB、僅文字，而且一定要先 Publish | 每個 Artifact **100 MB / 25,000 筆**，分「個人資料」與「共用資料」 |
| 匯出 | 複製程式碼或下載 | Docs → Word / PDF / Markdown / Google Docs；Slides → PowerPoint / PDF / Google Slides；Design → .zip / PDF / PowerPoint / HTML |
| 使用裝置 | 網頁版 | 網頁版、Desktop、Claude Code；**iOS / Android 可檢視與編輯** |

> 💡 **教學重點**：舊的 Publish 連結仍然可以開，但新作品請一律使用新版的 **Share** 流程，詳見 [分享、權限與複製再利用 SOP](./Guide/04_Publish_and_Remix_SOP.md)。

---

## 🎯 方案對照：哪些免費？哪些要付費？

| 功能 | 🟢 Free | 🔵 Pro / Max | 🟣 Team / Enterprise |
| :--- | :---: | :---: | :---: |
| 在對話中產生 Artifact（HTML、React、SVG、Mermaid、程式碼、圖表…） | ✓ | ✓ | ✓ |
| 📄 **Docs** 協作文件 | ✓ | ✓ | ✓ |
| 📑 **Slides** 簡報 | ✓ | ✓ | ✓ |
| 🎨 **Design** 設計稿／原型／一頁式網頁 | ✓ | ✓ | ✓ |
| 用「知道連結的人」分享 | ✓ | ✓ | ✓（需管理員開放對外分享） |
| 📊 **Data** 資料儀表板／數據故事 | ✗ | ✓ | ✓ |
| 🧮 **Sheets** 試算表（Beta） | ✗ | ✓ | ✓ |
| 🧠 **Whiteboards** 白板（Beta） | ✗ | ✓ | ✓ |
| 💾 **儲存資料**（Artifact 有記憶力，例如報名表、點餐單） | ✗ | ✓ | ✓ |
| 🔌 **連接外部 App**（Artifact 讀寫 Google Drive、Notion 等） | ✗ | ✓ | ✓ |
| ✉️ 用 Email 邀請特定人（Beta） | ✗ | ✓ | ✓ |
| 🎬 **Motion** 動畫影片，可匯出 MP4（Beta） | ✗ | ✗ | ✓ |
| 依群組分享 | ✗ | ✗ | Enterprise |

> 🧑‍🏫 **課堂建議**：學生用 **Free 帳號**就能完成本單元的 **範例 1～6**（Docs、Slides、Design、互動小工具、流程圖、內建 AI 的小工具）。**範例 7～10** 需要付費方案，建議由講師用 Pro 帳號示範。
>
> ⚠️ Team / Enterprise 的預設值不同：Docs、Slides、Design 在 Team 預設開啟；Sheets、Whiteboards、Motion 在 Enterprise **預設關閉**，要由管理員開啟。

---

## ⚙️ 使用前必做：開啟設定（只要一次）

1. 點左下角頭像 ➔ **Settings（設定）** ➔ **Capabilities（功能）**
2. 開啟 **「Create and edit files」**（舊名稱：Code execution and file creation）
3. （選用）開啟 **「Artifacts that use Claude」**，讓 Artifact 裡面也能呼叫 Claude

> Team / Enterprise 帳號由管理員在 **Organization settings ➔ Capabilities** 統一開啟。

---

## 🚪 三種開始方式

| 方式 | 怎麼做 | 適合時機 |
| :--- | :--- | :--- |
| **① 直接說** | 在任何對話裡說「請幫我做一份…簡報／文件／小工具」 | 最簡單，大部分時候用這個 |
| **② 輸入框選 Output** | 在訊息框點 **Output** ➔ 選範本（Docs / Slides / Design…）再輸入需求 | 想確定做出來的是哪一種範本 |
| **③ 從 Artifacts 分頁開始** | 左側欄 **Artifacts** ➔ 選範本 | 不是從對話開始，而是想直接開新作品 |

做好的作品都會自動存到左側欄的 **Artifacts** 分頁，可以搜尋、篩選類型，不必再翻聊天紀錄。

---

## 💎 為什麼 Artifacts 好用？六大亮點

| # | 亮點 | 說明 | 一般對話做不到的地方 |
| :---: | :--- | :--- | :--- |
| 1 | **成品和討論分開** | 對話在左邊，成品在右邊，改了幾十輪也不會被洗版 | 一般對話的成果會被淹沒在長長的聊天紀錄裡 |
| 2 | **局部修改** | 在 Docs 反白一段文字 ➔ **Edit with Claude**，只改那一段 | 一般對話常常整篇重寫，連改好的地方也跑掉 |
| 3 | **直接匯出 Office 格式** | Docs 可轉 Word/PDF，Slides 可轉 PowerPoint，不必另外排版 | 要自己複製貼上再調格式 |
| 4 | **可以操作的成品** | 做出來的是會動的網頁、計算機、測驗、圖表，長官一點就懂 | 純文字說明很難讓人馬上看懂 |
| 5 | **分享＋權限控管** | 一個連結就能分享，可以設定只能看、可以留言或可以編輯 | 要自己存檔、寄信或上傳雲端 |
| 6 | **集中管理** | 所有作品都在 Artifacts 分頁，手機也能打開 | 關掉對話後很難找回來 |

---

## 🗺️ 使用情境：什麼時候該用 Artifacts？

| 角色 | 情境 | 建議範本 | 方案 |
| :--- | :--- | :--- | :---: |
| 行政／總務 | 會議紀錄、SOP、公告 | Docs | 🟢 Free |
| 業務／講師 | 提案簡報、課程投影片 | Slides | 🟢 Free |
| 行銷／小編 | 活動一頁式網頁、DM、社群圖卡 | Design | 🟢 Free |
| 老師／學生 | 單字測驗、互動教材、計算機 | 自由形式（HTML） | 🟢 Free |
| 專案經理 | 流程圖、系統架構圖 | 自由形式（Mermaid） | 🟢 Free |
| 人資／活動負責人 | 報名表、團購點餐、投票 | 自由形式＋**儲存資料** | 🔵 Pro |
| 主管／分析師 | 銷售儀表板、月報數據 | **Data** | 🔵 Pro |
| 會計／財務 | 預算表、跨工作表公式 | **Sheets** | 🔵 Pro |
| 團隊 | 腦力激盪、專案發想 | **Whiteboards** | 🔵 Pro |
| 訓練／教育部門 | 動畫說明影片 | **Motion** | 🟣 Team |

> 🤔 **判斷原則**：如果這個東西**之後還會改、要給別人看，或要重複使用**，就讓 Claude 做成 Artifact。如果只是問一個問題、要一句答案，留在一般對話即可。

---

# 🧪 實作範例（所有 Prompt 都可直接複製）

> 每個範例都包含：**情境 ➔ 可複製 Prompt ➔ 你會看到什麼 ➔ 追問 Prompt（練習迭代修改）**。Prompt 都採用 [Chats 單元](../Chats/README.md) 的 **RTCCF 框架**（Role / Task / Context / Constraint / Format）。

---

## 範例 1｜📄 Docs：部門會議紀錄 ➔ 匯出 Word　`🟢 Free`

**情境**：開完會手上只有凌亂的筆記，需要整理成正式會議紀錄並寄給全部門。

```markdown
## Role
你是一位細心的行政秘書。

## Task
請用 Docs 範本，把下面的會議筆記整理成正式的「會議紀錄」。

## Context
會議：11/15 行銷部週會，出席：王經理、陳小姐、林先生、張小姐
筆記：
- 雙11活動業績比去年多18%，但退貨率也上升到6%
- 陳負責查退貨原因，下週三前回報
- 年終尾牙預算還沒定，林說廠商報價每桌8000
- 張提議明年改用短影音，王說先試3個月
- 下次開會 11/22 下午2點

## Constraint
- 語氣正式，使用繁體中文
- 待辦事項要有「負責人」和「期限」

## Format
包含：會議資訊、討論重點、決議事項、待辦事項表格（事項／負責人／期限）
```

**你會看到**：右側出現一份排版好的 Docs 文件，待辦事項已整理成表格。

**追問練習**（體驗局部修改）：
1. 在文件中**反白「討論重點」那一段** ➔ 點 **Edit with Claude** ➔ 輸入：
   ```text
   把這段改成條列式，每點不超過 25 個字
   ```
2. 完成後按右上角 **Export ➔ Word**，下載成 .docx 寄出。

---

## 範例 2｜📑 Slides：5 分鐘提案簡報 ➔ 匯出 PowerPoint　`🟢 Free`

**情境**：明天要向主管提案「導入 AI 工具」，只有一個想法，還沒有簡報。

```markdown
## Role
你是一位擅長商業簡報的顧問。

## Task
請用 Slides 範本做一份 7 頁的提案簡報：「在部門導入 Claude 提升文書效率」。

## Context
- 部門 12 人，每人每週約花 6 小時寫報告、會議紀錄、Email
- 預估導入後可省 30% 時間
- 費用：Pro 方案每人每月 20 美元
- 先試辦 3 個月，選 4 位同仁

## Constraint
- 每頁只講一個重點（One message per slide）
- 每頁文字不超過 40 字，多用數字和圖示
- 繁體中文，風格專業簡潔、深藍色系

## Format
封面 ➔ 現況痛點 ➔ 解決方案 ➔ 效益試算 ➔ 費用 ➔ 試辦計畫 ➔ 結論與請求
每頁附上講者備忘稿（speaker notes）
```

**你會看到**：一整套 7 頁投影片，可以點每一頁預覽，也可以直接按 **Present** 全螢幕播放。

**追問練習**：
```text
第 4 頁的效益試算請改成長條圖，比較「導入前」和「導入後」每週總工時
```
完成後按 **Export ➔ PowerPoint**（或 PDF、Google Slides）。

---

## 範例 3｜🎨 Design：活動一頁式報名網頁　`🟢 Free`

**情境**：社團或公司要辦一場講座，需要一個好看的活動介紹頁。

```markdown
## Role
你是一位網頁視覺設計師。

## Task
請用 Design 範本設計一個活動宣傳的一頁式網頁（landing page）。

## Context
- 活動：「AI 辦公室效率工作坊」
- 時間：2026/12/20（六）13:30–16:30
- 地點：台北市信義區某會議中心 3F
- 講師：資深 AI 講師
- 費用：免費，限額 40 人
- 你會學到：AI 寫報告、AI 做簡報、AI 整理 Excel

## Constraint
- 手機版也要好看
- 色系：白底＋橘色重點色，風格活潑但不幼稚
- 繁體中文

## Format
區塊：主視覺標題 ➔ 活動資訊卡 ➔ 三大學習重點（圖示）➔ 講師介紹 ➔ 常見問題 ➔ 報名按鈕
```

**你會看到**：一個完整的網頁設計稿，可在電腦版與手機版預覽之間切換。

**追問練習**：
```text
請再給我兩個不同風格的版本：一個極簡黑白、一個科技感深色，放在一起讓我比較
```
完成後可以 **Export** 成 PDF（當 DM 印出）、PowerPoint 或單一 HTML 檔。

---

## 範例 4｜🧩 自由形式：英文單字互動測驗　`🟢 Free`

**情境**：老師想要一個學生可以在手機上直接玩的單字測驗。

```markdown
## Role
你是一位擅長設計互動教材的英文老師。

## Task
做一個「英文單字選擇題測驗」互動網頁 Artifact。

## Context
單字（英文／中文）：
apple 蘋果、library 圖書館、weather 天氣、journey 旅程、borrow 借入、
improve 改善、schedule 行程表、customer 顧客、deliver 遞送、recommend 推薦

## Constraint
- 每題隨機出 4 個中文選項，答對顯示綠色、答錯顯示紅色並告訴正確答案
- 10 題做完顯示分數和答錯的單字清單，有「再玩一次」按鈕
- 手機好操作，按鈕要大

## Format
單一互動網頁（HTML），直接在右側可以玩
```

**你會看到**：右側就是一個可以玩的測驗，馬上就能測試。

**追問練習**：
```text
加一個「發音」按鈕，按下去會唸出英文單字；再加一個 30 秒倒數計時模式
```
做好後按 **Share ➔ Anyone with the link**，把連結貼到班級 LINE 群組，學生**不需要 Claude 帳號**就能玩。

---

## 範例 5｜🔀 自由形式：工作流程圖（Mermaid）　`🟢 Free`

**情境**：新人總是搞不清楚請購流程，需要一張一看就懂的流程圖。

```markdown
## Role
你是一位擅長流程梳理的專案管理師。

## Task
把以下請購流程畫成一張流程圖 Artifact。

## Context
1. 申請人填請購單
2. 金額 5,000 元以下 ➔ 直屬主管核准即可
3. 金額超過 5,000 元 ➔ 主管核准後還要給財務部審核
4. 超過 50,000 元 ➔ 還要總經理核准
5. 核准後採購部下單 ➔ 驗收 ➔ 會計付款
6. 任何一關退回 ➔ 回到申請人修改

## Constraint
- 用不同顏色區分「申請人／主管／財務／總經理／採購」
- 判斷條件用菱形

## Format
Mermaid 流程圖
```

**追問練習**：
```text
在每個步驟旁邊加上「預估處理天數」，並在最下方算出最快和最慢需要幾天
```

---

## 範例 6｜🤖 內建 AI 的小工具：Email 語氣轉換器　`🟢 Free`

**情境**：做一個小工具，貼上一段草稿，就能自動改寫成不同語氣。Artifact 本身就可以呼叫 Claude，**不需要 API Key**。

```markdown
## Role
你是一位前端工程師，熟悉在 Artifact 中呼叫 Claude。

## Task
做一個「Email 語氣轉換器」互動小工具 Artifact，工具裡面要使用 Claude 改寫文字。

## Context
- 使用者在文字框貼上 Email 草稿
- 選擇語氣：正式商務／親切友善／簡短直接／委婉拒絕
- 按「轉換」後由 Claude 改寫，並顯示結果
- 結果旁有「複製」按鈕

## Constraint
- 繁體中文介面
- 轉換中要顯示「改寫中…」的讀取狀態

## Format
單一互動網頁 Artifact
```

> 💰 **費用說明**：別人使用你分享的 AI 小工具時，要**登入自己的 Claude 帳號**，用量算在**使用者自己的方案額度**，不會用到你的額度。沒登入的連結訪客則**無法使用** AI 功能。
> 需先在 Settings ➔ Capabilities 開啟 **「Artifacts that use Claude」**。

---

## 範例 7｜💾 有記憶的工具：部門團購點餐單　`🔵 Pro 以上`

**情境**：每週五部門訂下午茶，總是要一個人在群組裡收單。改成做一個大家都能填、資料不會消失的點餐單。

```markdown
## Role
你是一位擅長做內部小工具的工程師。

## Task
做一個「部門下午茶團購點餐單」Artifact，要使用「共用儲存空間」，讓所有同仁看到同一份資料。

## Context
- 菜單：珍珠奶茶 55、四季春 35、美式咖啡 60、拿鐵 75、檸檬綠 50
- 每個人選飲料、甜度（全糖/半糖/微糖/無糖）、冰塊（正常/少冰/去冰/熱）
- 自動記錄是誰點的（使用登入帳號名稱）

## Constraint
- 每人只能修改或刪除自己的訂單
- 最下方自動統計：每種飲料杯數、總金額
- 有「匯出 CSV」按鈕給負責訂購的人

## Format
互動網頁 Artifact，資料使用共用儲存
```

**你會看到**：第一次使用共用儲存時，Claude 會跳出確認視窗，因為**共用資料會被所有使用者看到**。把連結分享給同事（建議用 Email 邀請），大家填的資料都會集中在同一個地方。

> 🔐 **個人 vs 共用儲存**：
> - **個人儲存**：每個人只看得到自己的資料（例如個人日記、學習紀錄）
> - **共用儲存**：大家看到同一份資料（例如點餐單、報名表、投票）
> - 輸入敏感資料前，請先確認這個工具用的是哪一種！

---

## 範例 8｜📊 Data：上傳 CSV 做業績儀表板　`🔵 Pro 以上`

**情境**：每月要向主管報告業績，Excel 圖表太陽春，想做一個能互動篩選的儀表板。

先準備一份 CSV（可以請 Claude 先產生練習用資料）：

```text
請幫我產生一份練習用 CSV：2026 年 1–10 月，北中南東 4 區、3 項產品（A/B/C）的月銷售額與訂單數
```

再使用 **Output ➔ Data** 範本，上傳 CSV 並輸入：

```markdown
## Role
你是一位資料分析師。

## Task
用我上傳的銷售 CSV 做一個業績儀表板。

## Constraint
- 最上方 4 張 KPI 卡片：總營收、總訂單、平均客單價、最佳區域
- 月份營收趨勢折線圖、區域比較長條圖、產品占比圖
- 可以用下拉選單篩選「區域」與「產品」
- 最下方用 3 句話寫出本期重點觀察

## Format
Data 儀表板
```

**你會看到**：互動儀表板，每張圖表都會標示資料來源與更新時間。

**追問練習**：
```text
加一個「與上月相比」的漲跌百分比，下跌用紅色標示，並找出下跌最多的區域可能原因
```

---

## 範例 9｜🧮 Sheets：活動預算試算表　`🔵 Pro 以上（Beta）`

**情境**：籌辦尾牙要做預算，需要真的會自動計算的試算表，而不是寫死的數字。

```markdown
## Role
你是一位活動企劃兼會計。

## Task
用 Sheets 範本做一份「2026 公司尾牙預算表」。

## Context
- 參加人數：120 人
- 餐費：每桌 10 人，每桌 8,000 元
- 場地費 30,000、主持人 15,000、抽獎獎品總額 80,000、交通接駁 20,000
- 預備金：總額的 5%

## Constraint
- 工作表 1「明細」：項目、單價、數量、小計（用公式計算）
- 工作表 2「總表」：引用明細的加總，顯示每人平均成本
- 改人數時，桌數要自動用 ROUNDUP 重算

## Format
Sheets 試算表，所有金額都用公式，不能寫死
```

**追問練習**：在表格裡**直接把人數改成 150**，看看桌數、總額是否自動更新；再問：
```text
如果預算上限是 35 萬，請幫我新增一個工作表「刪減方案」，列出三種刪減組合
```

---

## 範例 10｜🧠 Whiteboards：團隊腦力激盪　`🔵 Pro 以上（Beta）`

```markdown
請開一個 Whiteboard，主題是「如何讓新進員工第一個月更快上手」。
請先放上 4 個分類便利貼區：訓練課程、導師制度、工具文件、團隊融入，
每區先放 3 個點子，之後我和同事會一起補充，最後請幫我們整理成投票前 5 名。
```

> 🎬 **Motion（僅 Team / Enterprise，Beta）**：可以做動畫說明、動態圖表或操作導覽，並匯出 **MP4**。例如：「把範例 2 的提案重點做成 60 秒動畫說明影片」。

---

## 🔗 分享與權限

| 分享對象 | 設定 | 方案 |
| :--- | :--- | :---: |
| 只有自己 | **Only you**（預設） | 全部 |
| 任何拿到連結的人 | **Anyone with the link**，多數情況**不需要 Claude 帳號**即可開啟 | 全部（Team/Ent 需管理員開放） |
| 指定的人 | **Email 邀請**（Beta），對方需用該 Email 登入 Claude，每個 Artifact 最多 50 位外部受邀者，邀請 30 天後失效 | Pro 以上 |
| 公司內所有人 | **Anyone at [公司名稱]** | Team / Enterprise |

**三種權限**：

| 權限 | 可以做什麼 |
| :--- | :--- |
| **Can view** | 看成品、看留言 |
| **Commenter** | ＋ 新增留言、下載成品提供的檔案 |
| **Can edit** | ＋ 直接修改內容 |

⚠️ **連結訪客的限制**：沒登入或不在你組織內的訪客，**看不到也不能留言**，而且 Artifact 中**使用 Claude 或連接 App 的功能不能用**。

---

## 📦 匯出格式一覽

| 範本 | 可匯出成 |
| :--- | :--- |
| 📄 Docs | Word (.docx)、PDF、Markdown、Google Docs |
| 📑 Slides | PowerPoint (.pptx)、PDF、可編輯的 Google Slides |
| 🎨 Design | .zip、PDF、PowerPoint、單一 HTML 檔 |
| 🎬 Motion | MP4 影片 |
| 🧩 舊版／自由形式 | 檢視程式碼、複製內容、下載 |

---

## 🛡️ 限制與安全提醒

- **儲存上限**：每個 Artifact 最多 100 MB 或 25,000 筆資料（以先達到者為準）。
- **上傳檔案**：單檔 20 MB（SVG 為 2 MB），最多 5,000 個檔案，總計 1 GB。
- **舊版 Artifact 取消發布 = 資料全刪**：舊版 Artifact 一旦取消發布（Unpublish），就**無法再次發布，而且儲存的資料會永久刪除**。
- **分享前檢查**：不要把密碼、身分證字號、未公開財報等敏感資訊放進公開連結的 Artifact。
- **共用儲存要小心**：使用共用儲存時，所有使用者都看得到彼此輸入的資料。
- **出錯時**：點錯誤訊息旁的 **Try fixing with Claude**，請 Claude 嘗試修正（不保證一定能修好）。
- **原型 vs 正式系統**：Artifact 很適合做內部工具與概念驗證；若要給全公司數百人長期使用，建議交給工程團隊用 Claude API 正式開發。

---

## 💡 進階心法：先討論內容，再產出成品

Docs 雖然可以邊寫邊改，但**正式的大型文件**仍建議採用「人機協作」流程：先用 Markdown／Docs 把內容和數字確認好，再匯出 Word、PPT 或 PDF。詳見 👉 [討論方式的內容生成（Human in the Loop）](../討論方式的內容生成/README.md)。

---

## 📚 延伸範例與深度指南

### 職場實戰範例（自由形式 Artifact，Free 可做）

| 層級 | 範例 | 產出格式 |
| :---: | :--- | :--- |
| 🟢 入門 | [✍️ 產品銷售頁文案守門人](./Examples/02_Marketing_and_Copywriting/README.md) | Markdown |
| 🟢 入門 | [🗂️ 辦公行政小工具](./Examples/01_Office_Administration/README.md) | HTML |
| 🔵 進階 | [💻 工程師的 Python 邏輯函數](./Examples/03_Software_Engineering/README.md) | Python |
| 🔵 進階 | [🧪 學生實作多格式工作坊](./Examples/06_Student_Lab/README.md) | HTML / Mermaid / SVG |
| 🟡 高階 | [📊 雙軸動態營運戰情室](./Examples/04_Business_Intelligence/README.md) | React（新版可改用 **Data** 範本 🔵） |
| 🟡 高階 | [📱 產品經理團隊排程行事曆](./Examples/05_Product_Management/README.md) | React（新版儲存資料需 🔵 Pro） |
| 🔥 企業 | [🌪️ 工研院大型風機 3D 數位分身](./Examples/07_ITRI_Wind_Turbine_3D/README.md) | HTML / Three.js |

### 深度指南

- [05. Artifacts 中心與七大範本全攻略](./Guide/05_Artifacts_Hub_and_Templates.md)（Docs / Slides / Design / Data / Sheets / Whiteboards / Motion）
- [01. 內建 AI 的小工具（Artifacts that use Claude）與費用](./Guide/01_AI_Powered_Artifacts.md)
- [02. 資料儲存：個人 vs 共用](./Guide/02_Persistent_Storage.md)（🔵 Pro；附 Free 的 localStorage 替代方案）
- [03. 外部服務串接（Connectors）](./Guide/03_External_Connectors.md)（對話中讀取 🟢 Free；Artifact 連接 App 🔵 Pro）
- [04. 分享、權限與複製再利用 SOP](./Guide/04_Publish_and_Remix_SOP.md)（含舊版 Publish 說明）

---

## ❓ 常見問題

**Q1：我以前做的 Artifact 還在嗎？**
在。2026/9/16 以前的作品屬於舊版 Artifact，仍然可以開啟與下載，舊的 Publish 連結也還能用。

**Q2：Free 帳號為什麼看不到 Data / Sheets？**
這兩個範本只開放給 Pro 以上方案；Free 可使用 Docs、Slides、Design 和所有自由形式的 Artifact。

**Q3：別人打開我分享的 AI 小工具，會扣我的額度嗎？**
不會。使用者要登入自己的帳號，用量算在他們自己的方案上。

**Q4：手機可以用嗎？**
iOS / Android App 可以檢視與編輯 Artifact，但**分享設定**要到網頁版或 Desktop 調整。

**Q5：做出來的東西出錯怎麼辦？**
點錯誤旁的 **Try fixing with Claude**，或直接在對話中描述問題，例如「按下轉換按鈕沒有反應」。

---

← [返回上層：Claude_AI 索引](../README.md) · [Chats 範例庫](../Chats/README.md) · [Projects 專案沙盒](../Projects/README.md)
