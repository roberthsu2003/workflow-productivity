# 🎯 範例 5：資料夾指令規範、專案日誌自主維護與原地微調草稿

> 🟢 **適用方案**：Max / Pro / Team / Enterprise (Cowork 全平台支援)  
> 💼 **適用角色**：專案總監 (PMO)、品牌公關主管、產品行銷經理 (PMM)。  
> 🎯 **核心功能示範**：
> - 🎯 **資料夾專屬指令 (Folder Instructions)**：透過設定資料夾層級的規範檔，約束 Claude 的交付格式、品牌語氣，並命令其「自主維護專案進度筆記」。
> - ☁️ **雲端隔離運算 (Sessions in the Cloud) & 跨裝置接續 (Work from Anywhere)**：在辦公室電腦啟動專案，出門在手機 App 檢視進度與給予回饋，回家無縫完成。
> - 📝 **原地反白微調草稿 (Edit Drafts in Place)**：產出新聞稿草案後，直接反白選取段落進行即時修改，無需重寫整篇對話。

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請先查看本資料夾下的練習檔案：
1. [`folder-instructions.md`](./sample_files/folder-instructions.md)：資料夾專屬指令，定義品牌語氣、章節排版規範，以及「每次任務完成後自主更新 `PROJECT_LOG.md`」的自動化規則。
2. [`product_launch_brief.md`](./sample_files/product_launch_brief.md)：新產品 SmartFlow AI 上線發布需求書與待辦里程碑。
3. [`PROJECT_LOG.md`](./sample_files/PROJECT_LOG.md)：專案進度追蹤日誌，作為 Claude 自動維護的專案長效記憶庫。

---

## 🤖 Cowork RTCCF 實戰 Prompt

在 Cowork 模式下開啟此資料夾（或上傳練習檔案），輸入以下 Prompt：

```text
【Role】
你是一名資深科技產品行銷經理 (PMM) 與公關策略總監。

【Task】
請讀取 product_launch_brief.md，並嚴格遵循 folder-instructions.md 中的規範執行以下任務：
1. 為 SmartFlow AI 撰寫一份正式對外新聞稿 (Press Release) 草稿，命名為 press_release_draft.md。
2. 新聞稿架構須符合規範（包含 Objective、Owner、Milestone 與 Risks & Mitigations）。
3. 任務完成後，自主讀取並更新 PROJECT_LOG.md，將第一項里程碑標記為已完成 [x]，並記錄本次操作時間與摘要。

【Context】
- 資料夾指令：folder-instructions.md
- 專案需求書：product_launch_brief.md
- 專案進度表：PROJECT_LOG.md

【Constraint】
- 語氣必須精準符合 folder-instructions.md 規定之「專業、敏捷、充滿前瞻感，嚴禁浮誇」。
- 必須主動落實自動維護進度筆記規則，更新 PROJECT_LOG.md。
- 使用繁體中文輸出。

【Format】
完成後，產出 press_release_draft.md 草稿，並展示更新後的 PROJECT_LOG.md 內容。
```

---

## 🚀 核心功能實戰體驗 3 步驟

### 步驟 1：體驗「Folder Instructions」自動約束與日誌自主維護
- 啟動任務後，觀察 Claude 是否自動讀取了 `folder-instructions.md`。
- 完成後打開 [`PROJECT_LOG.md`](./sample_files/PROJECT_LOG.md)，您會發現 Claude **完全不需要您二次提醒**，就自主更新了執行記錄表格與待辦進度狀態！

### 步驟 2：體驗「原地反白微調草稿 (Edit Drafts in Place)」
- 當 Claude 產出 `press_release_draft.md` 的長篇新聞稿草稿時：
  1. 在畫面上直接用滑鼠**反白選取「引言」或「第三段產品特色」**；
  2. 點擊浮現的 **「Edit with Claude」** 按鈕；
  3. 輸入微調指令（例如：「*將語氣改得更偏向 B2B 企業高管視角，並加入降低營運成本 30% 的預估效益*」）；
  4. 觀察 Claude 直接在原文段落中進行**原地局部修改**，保留其餘段落不動！

### 步驟 3：體驗「雲端隔離運算 & 跨裝置無縫接續」
- 在電腦上啟動此任務後，立即闔上筆電；
- 打開手機上的 Claude App，進入同一筆 Cowork 任務 Session，您會看見雲端伺服器依然在持續執行並已產出檔案；
- 在手機上回覆一則追問或微調指令，回家打開瀏覽器網頁端即可直接下載最終成果！

---

← [返回 Cowork 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
