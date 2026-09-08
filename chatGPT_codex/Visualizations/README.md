# Visualizations、Sites 與成品呈現

> 🔵 **方案需求**：Visualizations 與 Image generation 需 **Plus** 起（Free／Go 有限）；**Sites** 為 public beta，需 Plus / Pro / Business / Enterprise / Edu。workspace 檔案產出 🟢 Free 可用。

Claude 的 **Artifacts** 在 Codex 沒有一對一的同名功能。它被拆成**四個不同的出口**，各有適用場景。這一章的重點就是：**幫你選對出口。**

---

## 🚪 四個出口，怎麼選

| 出口 | 產出什麼 | 互動 | 可分享網址 | 資料持久 | 方案 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Workspace 檔案** | `.md` / `.docx` / `.xlsx` / `.pptx` / `.pdf` / 程式碼 | ✗ | ✗ | — | 🟢 Free |
| **Visualizations** | 互動圖表、地圖、模擬器、計算機 | ✓ | ✗ | ✗ | 🔵 Plus |
| **Sites** | 可發佈的網站、web app、遊戲 | ✓ | ✓ | ✓ | 🔵 Plus |
| **Image generation** | 圖片 | ✗ | ✓ | — | 🔵 Plus |

### 決策流程

```text
我要的成品……
├─ 是要存檔、寄出、簽核的文件？        → Workspace 檔案
├─ 是要在對話裡「玩看看」的解說或圖表？  → Visualizations
├─ 是要給別人開網址看的東西？           → Sites
└─ 是一張圖？                          → Image generation
```

> [!IMPORTANT]
> **最常見的錯誤是用 Sites 做只該是 Visualization 的東西。** Sites 有部署流程、有網址、有資料庫；如果你只是想看一張可以拖拉的圖表，用 `@Visualize` 快得多。官方建議：**用能達成目的的最小格式。**

---

## 📊 Visualizations

把問題與資料轉成**互動式的視覺解說**——圖表、地圖、流程圖、計算機、模擬器——直接顯示在對話中，可以調整輸入即時看變化。

### 怎麼建立

| 介面 | 方式 |
| :--- | :--- |
| ChatGPT 網頁版 / Work | 在訊息中標記 `@Visualize` 並描述需求 |
| ChatGPT 桌面版 | 在輸入框輸入 `@`，在 Plugins 中搜尋 **Visualize** |
| 自動 | 情境適合時，ChatGPT 也會主動產生 |

> [!WARNING]
> **Codex CLI 與 IDE extension 不支援 visualization 的畫面呈現。** 課堂如果用 CLI 教學，這一節請切換到桌面版或網頁版。

### 適合的形式

| 你要表達 | 用什麼 |
| :--- | :--- |
| 流程與標記過的關係 | 圖解 / 流程圖 |
| 數值比較 | 圖表 |
| 地理分布 | 地圖 |
| 「調整參數看看會怎樣」 | 互動工具 |

### 範例：麥禾烘焙的季度營收

```text
@Visualize

讀取 sample_files/maiho_quarterly_sales.csv，建立可互動的季度營收視覺化。

需求：
- 可切換「全部門市 / 單一門市」
- 同時顯示營收與毛利率（雙軸）
- 滑鼠移上去顯示該季的單店數與客單價
- 下方附三點洞察，每點須指出是從哪個數字看出來的

限制：
- **不要更動原始 CSV。**
- 缺漏的月份請留空並在圖上標示，不要內插補值。
- 幣別標註 TWD，數字用千分位。
```

### 驗收重點

- [ ] 每個數字都能追溯回原始資料
- [ ] 單位與幣別標示清楚
- [ ] **空值的處理方式有明說**（留空？補 0？內插？）
- [ ] 座標軸從 0 開始，或有明確標註為什麼不從 0
- [ ] 對比度足夠、可鍵盤操作、尊重「減少動態效果」偏好
- [ ] 公開分享前已移除敏感資料

---

## 🌐 Sites

Sites 讓你**建立、託管、修改與分享網站、web app 與小遊戲**，不需要自己管部署。

### 建立與發佈

1. 在對話中提到「website」或標記 `@Sites`
2. 描述**受眾、用途、需要的功能與資料**
3. ChatGPT 產生初版 → 你逐輪修改
4. **兩階段發佈**：先建立可審查的版本，確認後才部署到正式環境

> **這個兩階段設計很重要**：你永遠有機會在上線前看到實際的樣子。

### 網址與網域

- 每個 Site 自動取得一個 ChatGPT 託管的網址
- 在支援的情況下，擁有者**可以更改網址而不需重新部署**，舊網址會轉址到新的
- 可透過 DNS 記錄接自訂網域

### 隱私與分享

新建立的 Site **預設只有擁有者可見**。分享選項（依帳號類型與管理員設定而異）：

| 範圍 | 說明 |
| :--- | :--- |
| 僅自己 | 預設 |
| 工作區成員 | 同 workspace 的人 |
| 受邀的外部訪客 | 逐一邀請 |
| 整個工作區 | 全員可見 |
| 公開網際網路 | 任何人 |

也可選擇加上 **Sign in with ChatGPT**，做身分感知的功能。

### 限制與規格

| 項目 | 值 |
| :--- | :--- |
| 每個 Site 的 D1 資料庫 | 10 GB |
| R2 物件儲存 | 無上限 |
| 分析 | 自動提供訪客數與頁面瀏覽數 |
| 資料落地 | 目前不支援 |

> [!WARNING]
> ### Sites 明確禁止的用途
> - 受保護的健康資訊（PHI）
> - 支付卡處理與金融交易
> - 13 歲以下兒童相關服務
> - 惡意程式散布
>
> 課堂示範請避開這些主題。

### 範例：潮汐物流的內部查詢頁

```text
@Sites

建立一個內部用的配送區域查詢頁。

受眾：潮汐物流客服人員，非工程背景，用桌機操作。
功能：
- 輸入郵遞區號 → 顯示所屬配送區、預估工作天、是否支援當日配
- 資料來源：`data/delivery_zones.csv`
- 查無資料時明確顯示「非服務範圍」，不要顯示空白

限制：
- 不需要登入，但**不可公開發佈**，只分享給工作區成員。
- 不儲存任何查詢紀錄。
- 介面繁體中文，字級不小於 16px。

先建立可審查的版本給我看，確認後我再決定要不要部署。
```

---

## 📄 Workspace 檔案產出

最常被忽略、但也最常用的出口：**直接在 workspace 產生檔案**。

```text
依 data/2026-08_配送績效.csv 產出月度報告。

輸出：`reports/2026-08_配送績效報告.xlsx`
- 「明細」工作表：原始資料，首列凍結
- 「摘要」工作表：各區彙總，依準時率排序
- 「異常」工作表：僅列準時率 < 95% 的區域

限制：不要修改原始 CSV；數字須與來源完全一致。
```

> **與 Claude 的關鍵差異**：Claude 產生檔案後你要**下載**；Codex 直接**寫進你的資料夾**。這代表：
> - 好處：可以立刻 `git diff`、可以被下一個 task 接手處理
> - 風險：**它可能覆蓋既有檔案**。永遠在 Scope 明確指定輸出路徑，並先 commit。

---

## 🖼️ Image generation

適合產品概念圖、前端設計稿、模型草圖與遊戲素材。

```text
替麥禾烘焙的「蜜香紅茶生吐司」產生一張商品情境照。
風格：自然光、木質桌面、暖色調、俯視 45 度。
不要出現文字、logo 或人物臉部。
尺寸：正方形，供 Instagram 使用。
```

> 圖片生成的用量消耗較快（依模型約為文字的 3～5 倍），課堂示範請節制。

---

## 🔄 與 Claude Artifacts 的對照

| Claude Artifacts 的用法 | Codex 對應 |
| :--- | :--- |
| 側欄顯示 HTML / React 小工具 | **Visualizations**（不可分享）或 **Sites**（可分享） |
| Mermaid 流程圖 | Visualizations |
| 產生可下載的 .docx / .xlsx | **直接寫進 workspace** |
| 發佈與 Remix | **Sites**（有正式的發佈與權限模型） |
| SVG 圖示 | Image generation 或 workspace 檔案 |

> **心智模型轉換**：Claude Artifacts 是「對話的附屬產出」；Codex 這四個出口各自是**獨立的產品線**，有各自的權限、方案門檻與生命週期。

---

## 📖 教材範例

| 範例 | 用哪個出口 | 教學重點 |
|---|---|---|
| [01. 配送績效互動儀表板](./Examples/01_Delivery_Dashboard/README.md) | Visualization | 缺漏值不可畫成 0、離群值造成的 Y 軸壓縮、色盲友善 |
| [02. 門市銷售查詢 Site](./Examples/02_Brand_Sales_Site/README.md) | Sites | 「未上市」≠「銷售 0」、兩階段發佈、**分享範圍設定** |

---

## 📘 進階指南

| 指南 | 內容 |
|---|---|
| [01. 選對出口](./Guide/01_Choosing_The_Right_Output.md) | 四個出口的完整比較、決策樹、三個常見誤判 |
| [02. 資料的誠實呈現](./Guide/02_Data_Honesty.md) | **四種視覺化謊言**、無障礙雙重編碼、可寫進 `AGENTS.md` 的原則 |
| [03. 發佈與分享 SOP](./Guide/03_Publish_and_Sharing_SOP.md) | 分享範圍決策、發佈前四類檢查、Git 洩漏風險 |

---

## 小結

| 我要的東西 | 用哪個 | 方案 |
|---|---|---|
| 存檔、寄出、簽核的文件 | Workspace 檔案 | 🟢 Free |
| 對話裡的互動圖表與解說 | Visualizations | 🔵 Plus |
| 給別人開網址看的頁面 | Sites | 🔵 Plus |
| 一張圖 | Image generation | 🔵 Plus |

**官方說明**：[Visualizations](https://learn.chatgpt.com/docs/visualizations) · [Sites](https://learn.chatgpt.com/docs/sites) · [File handling](https://learn.chatgpt.com/docs/features)

---

← [返回上層：ChatGPT Codex 索引](../README.md)
