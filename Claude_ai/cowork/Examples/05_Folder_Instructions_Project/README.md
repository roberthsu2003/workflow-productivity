# 🎯 範例 5：資料夾指令 vs 雲端專案規範、日誌自主維護與跨裝置自治中樞

> 🔴 **難度等級**：**Level 5（終極代理・專案自治中樞）**  
> 💻 **適用平台**：Claude 全平台（Desktop / Web / Mobile / Chrome 側邊欄）  
> 💼 **適用角色**：專案總監 (PMO)、產品行銷主管 (PMM)、品牌公關總監、創業團隊負責人。  
> 🎯 **核心體驗**：
> - 🏢 **五大模組分工體系**：解密 Claude 專案右側面板（**Instructions**、**Memory**、**Context**、**Folder**、**Scheduled**）的底層定位。
> - ⚡ **快取機制 (Prompt Caching) vs. 本機直連 (Folder)**：搞懂為什麼雲端 Context 會被快取（靜態唯讀），而本機 Folder 則是動態讀寫、自動原地回寫。
> - 📝 **專案進度日誌自主維護 (Self-Maintaining Project Log)**：**極具自主性的 Agent 特徵！** 任務完成後，Claude 自主開啟並更新硬碟上的 `PROJECT_LOG.md`，自動打勾完成里程碑、記錄時間戳記，**完全零手動**！
> - 🌟 **專案 + 資料夾二合一終極形態 (Project with Folder)**：結合雲端專案的統一規範與本機硬碟的自動化檔案閉環，打造真正的 AI 工作中樞。

---

## 🔍 Cowork 核心解密：解剖專案右側面板的 5 大支柱

在 Claude Desktop 或 Web 介面中進入專案時，右側面板清楚劃分了 5 個核心模組（如下圖所示）：

```
┌────────────────────────────────────────────────────────┐
│ How can I help you today?                              │
│ [＋ Chat] [Cowork]                       Sonnet 5 High │
│                                                        │
│ SmartFlow AI 上線發布專案  Auto                        │
└────────────────────────────────────────────────────────┘
    │
    ▼ 右側專案管理面板 (Project Panel)
┌────────────────────────────────────────────────────────┐
│ Instructions                                         ➕│
│ 定義長效角色語氣、產出規章與排版規範 (所有對話自動繼承)   │
├────────────────────────────────────────────────────────┤
│ Memory                                       🔒Only you│
│ Claude 隨對話次數自主記住的偏好與重要背景              │
├────────────────────────────────────────────────────────┤
│ Context                                              ➕│
│ 雲端靜態參考資料庫（產品白皮書、法規手冊 PDF，享快取折扣）│
├────────────────────────────────────────────────────────┤
│ Folder                                                 │
│ 📁 sample_files                                        │
│ On this computer（本地實體硬碟直連，即時動態讀寫回寫） │
├────────────────────────────────────────────────────────┤
│ Scheduled                                            ➕│
│ 定時自動排程任務（例如每天早上自動巡檢進度並發晨報）     │
└────────────────────────────────────────────────────────┘
```

---

## 🧠 深度剖析：快取機制 (Prompt Caching) 與 Folder 的本質差異

許多學員在實作時常會產生三大靈魂疑問：
1. **只有 Context 會被 Cached，還是 Folder 的內容也會被 Cached？**
2. **更新後的 `PROJECT_LOG.md` 會自動加入還是要手動？**
3. **如果要手動，那為什麼還要有 Folder？**

### 1. 只有 Context 會被快取，Folder 是本機動態讀寫

| 比較維度 | 📄 Context（雲端靜態知識庫） | 📁 Folder（On this computer 本機目錄） |
|:---|:---|:---|
| **本質與儲存** | 上傳至 Anthropic 雲端伺服器的檔案複本 | **您電腦實體硬碟上的真實目錄**（Local Filesystem） |
| **快取機制** | **100% 深度快取 (Prompt Caching)**<br>靜態常駐於前置 System Context，享受 90% 費用折扣與極速回應。 | **動態載入 (Agent Tool Execution)**<br>Claude 不會把整部硬碟預先載入快取，而是需要時才呼叫本地工具即時讀取與寫入。 |
| **可否被 AI 寫入** | ❌ **唯讀 (Read-only)**：Claude 無法透過對話直接修改雲端 Context 裡的檔案。 | ✅ **雙向讀寫 (Read & Write)**：Claude 可直接新增檔案、原地覆寫修改硬碟檔案。 |
| **檔案變更即時性** | 本地檔案修改後，雲端 Context **不會自動同步**。 | **即時反映**！本地檔案一變更，Claude 下次讀取就是最新版。 |

### 2. 更新後的 `PROJECT_LOG.md` 會自動生效，絕不需手動加入！

- 當 Claude Cowork 執行完任務後，是直接呼叫本機檔案工具，**原地修改了您硬碟上的 `sample_files/PROJECT_LOG.md`**。
- 下一次任務啟動時，Claude 直接去資料夾讀取實體檔案，**讀到的就已經是最新打勾 `[x]`、最新時間戳記的內容**。
- ⚠️ **重要避坑警告**：**千萬不要把 `PROJECT_LOG.md` 手動上傳到右側的 Context 裡！**  
  Context 是靜態快取的，若手動放進 Context，雲端就會鎖定 0% 的舊版，導致本機硬碟已是 33%，而雲端 Context 還是 0% 的嚴重認知衝突！

### 3. 為什麼要有 Folder？它解決了哪些痛點？

如果沒有 Folder（純網頁版或純雲端專案），你的工作流程充滿人工折磨：
- ❌ **手動上傳**：每次有新檔案都要手動傳上 Context。
- ❌ **手動複製貼上**：Claude 產出新聞稿或日誌後，只能顯示在畫面上，你得手動複製存回硬碟。
- ❌ **手動維護版本**：日誌更新了，你必須到雲端手動刪除舊檔、重新上傳新版。

**有了 Folder，就是為了徹底實現「零手動」的自動化閉環：**

```mermaid
flowchart LR
    A["💻 電腦硬碟 (Folder)"] -->|1. Cowork 自動即時讀取| B["🧠 Claude 大腦 (依 Instructions 規範)"]
    B -->|2. 撰寫新聞稿 & 自主更新日誌| C["⚡ 成果生成"]
    C -->|3. 直接原地覆寫與新增| A
```

- **讀取零手動**：Claude 自動遍歷本機資料夾。
- **寫入零手動**：成果（`press_release_draft.md`）與進度日誌（`PROJECT_LOG.md`）**直接生成於您的硬碟中**。
- **接續零手動**：下一個任務自動讀取硬碟最新日誌，無縫持續推進！

---

## 📊 專案 (Project) vs. 資料夾 (Folder) 完整規格對照表

| 比較維度 | 📁 連結資料夾 (Folder Mode) | 🗂️ 專案融合資料夾 (Project + Folder ⭐) | ☁️ 純雲端專案 (Cloud-Only Project) |
|:---|:---|:---|:---|
| **底層架構** | 純本機硬碟目錄直連 | **雲端專案規範 + 本機硬碟讀寫（最佳實踐）** | 100% 雲端隔離沙盒 |
| **入口路徑** | `Project or folder` ➜ `+ Add folder` | `+ New project` ➜ 點選 **`+ Use a folder`** | `+ New project`（不選 folder） |
| **長效規範設定** | 目錄下的 `folder-instructions.md` | 右側面板的 **`Instructions`** | 右側面板的 **`Instructions`** |
| **動態作業區** | 本機資料夾（直接讀寫） | **右側 Folder 區塊（直接讀寫實體硬碟）** | 雲端對話框與 Artifact 畫布 |
| **靜態參考資料** | 放在同目錄下的參考檔 | **右側 Context 區塊（享 Prompt Caching）** | 右側 Context 區塊（享 Prompt Caching）|
| **日誌回寫方式** | 原地覆寫本機 `PROJECT_LOG.md` | **原地覆寫本機 `PROJECT_LOG.md`（零手動！）** | 輸出為 Artifact 畫布（需手動存檔）|
| **適用情境** | 本地單機快速任務、程式碼開發 | **企業正式專案、團隊長效標準作業流程** | 外出手機 App 應急、無本機電腦環境 |

---

## 🎭 職場痛點劇場：重複說明的疲憊與版本混亂

> *「每次為了新產品上線發布打開 AI，你都得把同一段話打一次：『我們是 B2B 科技品牌、調性要敏捷專業不可浮誇、章節要有 Owner 和風險評估……』」*  
> *更崩潰的是，一個多星期的專案跑下來，產生了十幾份檔案，你根本記不清哪一份是最新版、哪一項任務已經完成，還得花額外時間手動維護 Excel 專案進度表。*  

**現在，讓 Claude 透過「專案指示」與「本機資料夾連線」，將工作空間升級為「具備長效記憶與自主維護能力的智慧中樞」！**

---

## 📦 快速開始：下載練習素材壓縮檔 (Quick Download)

> [!TIP]
> 💡 **免手動建立！已為您打包完整測試素材壓縮檔**：  
> 本範例已在目錄中預先準備好打包好的壓縮檔：[`sample_files.zip`](./sample_files.zip)  
> - **直接下載**：學員可直接下載此 `sample_files.zip`，解壓縮後即可獲得包含 `sample_files/` 完整測試目錄：
>   - `folder-instructions.md`（定義品牌語氣、四章節排版、自動更新日誌規則）
>   - `product_launch_brief.md`（新產品上線需求書）
>   - `PROJECT_LOG.md`（初始狀態：進度 0%，里程碑皆為 `[ ]`）
> - **一鍵還原環境**：在練習完公關稿撰寫與日誌自動打勾後，若想重新演練，只需再次解壓縮 `sample_files.zip` 覆蓋，即可秒速重置至最乾淨的初始狀態！

---

## 🔄 執行前後視覺化對比 (Before vs. After)

```
【執行前：只有規範與初始需求】
sample_files/
├── folder-instructions.md        (定義品牌語氣、四章節排版、自動更新日誌規則)
├── product_launch_brief.md       (新產品上線需求書)
└── PROJECT_LOG.md                (初始狀態：進度 0%，里程碑皆為 [ ])

            ⬇️ 透過 Claude Cowork 自主理解並執行 ⬇️

【執行後：產出符合規範之公關草案，並自主更新專案日誌】
├── press_release_draft.md        ⭐【新生成！完全符合 4 大章節與專業語氣】
└── PROJECT_LOG.md                ⭐【自動更新！進度提升至 33%，自動勾選已完成】
    ├── 紀錄歷史：新增執行紀錄與產生 press_release_draft.md
    └── 里程碑狀態：
        - [x] 任務一：新聞稿草案撰寫 (由 Claude 自主打勾完成！)
        - [ ] 任務二：社群推廣規劃
        - [ ] 任務三：Sales Battlecard 製作
```

---

## 🧠 Cowork 代理執行管線 (Agent Execution Pipeline)

```mermaid
flowchart TD
    Start["🎯 選擇工作空間 (Project 綁定 sample_files 資料夾)"] --> AutoLoad["🧠 自動載入規範 (Instructions 或 folder-instructions.md)"]
    AutoLoad --> Adopt["🎯 吸收品牌調性 (敏捷/專業) 與排版規範 (Objective/Owner/Milestone/Risks)"]
    Adopt --> ReadBrief["📄 讀取產品需求書 product_launch_brief.md"]
    GenPR["✍️ 撰寫符合規範之正式新聞稿 press_release_draft.md"]
    ReadBrief --> GenPR
    GenPR --> CheckRule{"📜 檢查自動維護進度日誌規則"}
    CheckRule -->|觸發自動維護規範| OpenLog["📖 自主開啟硬碟上的 PROJECT_LOG.md"]
    OpenLog --> UpdateLog["✏️ 原地覆寫時間戳記、將任務一勾選為 [x]、計算進度百分比"]
    UpdateLog --> Deliver["🚀 交付成果（硬碟自動多出新聞稿，日誌自動更新完成）"]
```

---

## 🤖 Cowork 實戰 Prompt（RTCCF 結構）

在 Cowork 模式下連結資料夾或專案後，輸入以下極簡 Prompt——**我們完全不需要在 Prompt 裡重複說明品牌語氣與排版規定，因為規範已全權代勞！**

```markdown
## Role
你是一名**資深科技產品行銷經理 (PMM)** 與**公關策略總監**。

## Task
請讀取 **`product_launch_brief.md`**，並嚴格遵循專案規範執行以下任務：
1. 為 SmartFlow AI 撰寫一份正式對外發布的新聞稿草稿，命名為 **`press_release_draft.md`**。
2. 新聞稿架構與語氣必須百分之百符合專案規範的 4 大核心結構（包含 🎯 Objective、👥 Owner、⏱️ Milestone 與 ⚠️ Risks & Mitigations）。
3. 任務完成後，務必落實自動維護規範：主動開啟並更新 **`PROJECT_LOG.md`**，將 **任務一：新聞稿草案撰寫** 標記為已完成 **`[x]`**，進度更新為 **33%**，並追加一筆包含時間戳記與執行摘要的歷史記錄。

## Context
- 專案需求書：`product_launch_brief.md`
- 專案進度表：`PROJECT_LOG.md`

## Constraint
- 語氣必須精準符合規範規定之 **專業、敏捷、充滿前瞻感，嚴禁浮誇**。
- 必須 **主動落實自動維護進度筆記規則**，更新 `PROJECT_LOG.md`。
- 使用**繁體中文**輸出。

## Format
完成後，交付 **`press_release_draft.md`** 草稿，並展示更新後的 **`PROJECT_LOG.md`** 內容。
```

---

## 🚀 學員實戰動手做：三種玩法實作演練

學員可依使用情境選擇最合適的模式進行演練，**強烈推薦「玩法 ②（專案融合資料夾）」作為正式工作模式**：

### 🌟 玩法 ②：專案融合資料夾模式（Project + Folder・終極最佳實踐 ⭐）

這正是兼具「雲端專案規範 (Instructions)」與「本地硬碟自動回寫 (Folder)」的最高境界：

1. **開啟建立專案視窗**：
   - 在輸入框下方點擊 **`Project or folder`**（預設顯示 `Auto`）。
   - 在彈出面板最下方點擊 **`+ New project`**，彈出 **「Create a project」** 視窗。
2. **填寫專案設定（精準對應介面欄位）**：
   - **What are you working on?**：填入 `SmartFlow AI 上線發布專案`。
   - **What are you trying to achieve?**：填入專案目標與指令規範（可直接將 `sample_files/folder-instructions.md` 內容貼入）。
   - ⭐ **關鍵步驟（`+ Use a folder`）**：
     - 點擊對話框下方的 **`+ Use a folder`** 按鈕。
     - 選取解壓縮後的 **`sample_files`** 資料夾。
     - 點擊 **`Create project`**。
3. **確認專案右側面板狀態**：
   - 進入專案後，右側會出現：
     - **Instructions**：已載入您的品牌與排版規章。
     - **Folder**：顯示 `📁 sample_files` 與 `On this computer` 狀態。
     - **Context**：保持空白即可（**千萬不要把 `PROJECT_LOG.md` 傳上來！**）。
4. **送出 Prompt 執行**：
   - 切換至 **Cowork** 模式，貼上上述 RTCCF Prompt 送出。
5. **見證硬碟自動化奇蹟**：
   - 打開電腦上的 `sample_files/` 資料夾，實體檔案 **`press_release_draft.md`** 已自動誕生！
   - 打開 **`PROJECT_LOG.md`**，任務一已經被 Claude 自動打勾 `[x]`，進度升為 33%！**整個過程完全不需要任何手動上傳或下載！**

---

### 🅰️ 玩法 ①：純本機資料夾模式（Folder Mode Only・單機輕量首選）

如果您只是想在本地快速處理一組檔案，不想在雲端建立專案：

1. **切換 Cowork 並連結資料夾**：
   - 在輸入框切換為 **Cowork** 模式。
   - 點擊輸入框下方的 **`Project or folder`**（顯示 `Auto`）。
   - 在選單最底部點擊 **`+ Add folder`**，選取解壓縮後的 `sample_files` 資料夾。
2. **送出 Prompt**：
   - 貼上上述 RTCCF Prompt 送出。
   - Claude 會直接自動讀取資料夾根目錄的 `folder-instructions.md` 作為規範，並自動修改實體硬碟中的檔案。

---

### ☁️ 玩法 ③：純雲端專案模式（Cloud-Only Project・無電腦手機應急）

當您身處戶外、手邊只有手機或 iPad，電腦沒有開機時：

1. 建立專案時**不點選 `+ Use a folder`**，直接建立純雲端專案。
2. 規範填入 **Instructions**；靜態參考檔案上傳至右側 **Context**。
3. 此時 Claude 產出的公關稿與打勾日誌將會以 **Artifact** 畫布呈現，供您在手機螢幕上即時預覽與檢閱進度。

---

## 💡 避坑指南與核心收穫 (Tips & Takeaways)

> [!IMPORTANT]
> 1. **「Context」與「Folder」該放什麼？**  
>    - **放 Context**：永遠不變的**靜態參考聖經**（如產品規格書 PDF、品牌規章），享受 100% Prompt Caching 快取折扣。
>    - **放 Folder**：需要**動態編輯、產出或打勾維護的實體檔案**（如需求書、草稿、`PROJECT_LOG.md`）。
> 2. **絕對不要把動態日誌上傳到 Context！**  
>    Context 是唯讀靜態的，一旦上傳就會被快取鎖定。動態日誌留在 Folder 才能享受本機原地讀寫、零手動同步的威力！
> 3. **隨時一鍵還原練習環境**：  
>    若演練多次後想重設進度為 0%，只需再次解壓縮目錄內的 [`sample_files.zip`](./sample_files.zip) 覆蓋，即可秒速還原初始狀態！

---

[← 上一篇：範例 4 產業情報監測與定時晨報](../04_Daily_News_Brief/) ｜ [返回 Cowork 主頁](../../README.md)
