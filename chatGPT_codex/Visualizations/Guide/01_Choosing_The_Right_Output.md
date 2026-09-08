# 進階指南 01：選對出口

> 對應 `Claude_ai/Artifacts/Guide/01_AI_Powered_Artifacts.md`。

Claude 的 Artifacts 是**一個**功能。Codex 把同樣的需求拆成**四個獨立產品線**，各有方案門檻、權限模型與生命週期。

**選錯出口的代價**：多花三倍時間做出一個不需要部署的東西，或做了一個沒人能打開的東西。

---

## 🚪 四個出口的完整比較

| | Workspace 檔案 | Visualizations | Sites | Image generation |
| :--- | :---: | :---: | :---: | :---: |
| **方案** | 🟢 Free | 🔵 Plus | 🔵 Plus（beta） | 🔵 Plus |
| 互動 | ✗ | ✅ | ✅ | ✗ |
| 可分享網址 | ✗ | ✗ | ✅ | ✅ |
| 資料持久 | 檔案本身 | ✗ | ✅（D1 10GB） | ✗ |
| 建立速度 | 快 | **最快** | 慢（有部署流程） | 快 |
| 可版控 | ✅ | ✗ | ✗ | ✗ |
| 可被下個 task 接手 | ✅ | ✗ | ✗ | ✗ |
| CLI / IDE 支援 | ✅ | ❌ | ❌ | ❌ |
| 適合 | 交付文件 | 會議上探索 | 給別人開網址 | 視覺素材 |

---

## 🧭 決策樹

```text
這個成品的「讀者」是誰、怎麼看到它？

├─ 只有我，而且要存檔／寄出／簽核
│   → Workspace 檔案（.md / .docx / .xlsx / .pptx / .pdf）
│
├─ 會議上大家一起看，我會操作，看完就結束
│   → Visualizations
│
├─ 別人自己去看，可能看很多次，要有網址
│   → Sites
│
└─ 是一張圖，要放進簡報／社群／網頁
    → Image generation
```

### 三個常見的誤判

| 誤判 | 症狀 | 正解 |
| :--- | :--- | :--- |
| **用 Sites 做該是 Visualization 的東西** | 為了一次會議建了一個網站、設定分享權限、走部署流程 | 用 `@Visualize`，快十倍 |
| **用 Visualization 做該是 Sites 的東西** | 每次別人要看都要你重跑一次對話 | 升級成 Sites |
| **用 Visualization 做該是檔案的東西** | 主管要的是可簽核的報表，你給他一個互動圖 | 產 `.xlsx` |

---

## 📄 Workspace 檔案：最被低估的出口

> [!IMPORTANT]
> **這是唯一 Free 可用、唯一可版控、唯一能被下一個 task 接手的出口。**

```markdown
## Goal
依 `data/2026-08_配送績效.csv` 產出月度報告。

## Scope
- **不要修改原始 CSV。**
- 輸出 `reports/2026-08_配送績效報告.xlsx`
- **檔案已存在時不要覆蓋**，改用 `_v2` 並在回報中說明。

## Verification
三個工作表：明細（首列凍結）／各區彙總／異常月份
數字與來源完全一致。
```

### 與 Claude 的關鍵差異

| | Claude | Codex |
| :--- | :--- | :--- |
| 產出後 | **下載** | **直接寫進資料夾** |
| 要再處理 | 重新上傳 | 下一個 task 直接讀 |
| 版本 | 無 | **`git diff`** |
| 風險 | 低 | **可能覆蓋既有檔案** |

**所以每個產檔 task 都要**：明確指定輸出路徑 + 禁止覆蓋 + 事先 `git commit`。

---

## 📊 Visualizations：探索用，不是交付用

**建立**：ChatGPT 網頁版／Work 標記 `@Visualize`；桌面版輸入 `@` 搜尋 Visualize。

> [!WARNING]
> **Codex CLI 與 IDE extension 不支援 visualization 呈現。** 用 CLI 教學時這一節請切到桌面版。

### 它的三個限制

1. **沒有可分享的網址**——別人看不到，除非你截圖
2. **資料不持久**——關掉對話就沒了
3. **無法版控**——下次要重做

**這三個限制決定了它的定位：探索與討論的工具，不是交付物。**

---

## 🌐 Sites：有部署流程，別當玩具用

Sites 是**兩階段發佈**：先建立可審查版本 → 確認後才部署。

### 什麼時候值得

- [ ] 至少 3 個人會看
- [ ] 會看不只一次
- [ ] 需要網址而不是截圖
- [ ] 資料需要持久（有查詢紀錄、有狀態）

**四項有三項成立，才值得用 Sites。**

### 規格與限制

| 項目 | 值 |
| :--- | :--- |
| D1 資料庫 | 10 GB／每個 Site |
| R2 物件儲存 | 無上限 |
| 分析 | 自動提供訪客數與頁面瀏覽數 |
| 網址 | 自動配發，可更改且舊網址轉址 |
| 自訂網域 | 可透過 DNS 連接 |
| **資料落地** | **目前不支援** |

> [!WARNING]
> **Sites 明確禁止**：受保護的健康資訊（PHI）、支付卡處理與金融交易、13 歲以下兒童相關服務、惡意程式散布。

---

## 🖼️ Image generation

適合產品概念圖、前端設計稿、模型草圖、遊戲素材。

> **用量消耗較快**（依模型約為文字的 3～5 倍），課堂示範請節制。

**不適合**：需要精確數字的圖表（用 Visualizations）、需要文字正確的圖（生成模型的文字經常出錯）。

---

## 🔄 與 Claude Artifacts 的完整對照

| Claude Artifacts 用法 | Codex 對應 | 注意 |
| :--- | :--- | :--- |
| 側欄的 HTML / React 小工具 | Visualizations（不可分享）或 Sites（可分享） | **先問要不要分享** |
| Mermaid 流程圖 | Visualizations | |
| 可下載的 .docx / .xlsx | **直接寫進 workspace** | 要防覆蓋 |
| 發佈與 Remix | **Sites** | 有正式的權限模型 |
| SVG 圖示 | Image generation 或直接產 SVG 檔 | 要精確就產檔 |

> **心智模型轉換**：Claude Artifacts 是「對話的附屬產出」；
> Codex 這四個出口**各自是獨立的產品線**。

---

**相關**：[Visualizations 主章節](../README.md) · [02. 資料誠實呈現](./02_Data_Honesty.md) · [03. 發佈與權限 SOP](./03_Publish_and_Sharing_SOP.md)

---

← [返回上層：Visualizations](../README.md) ｜ [返回索引](../../README.md)
