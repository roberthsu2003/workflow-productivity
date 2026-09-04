# 延伸練習 7：客戶回覆與 CRM 更新助手（第三階：整合者）

> **🎯 本階核心目標**  
> 運用 Claude AI 的「**多模態視覺辨識 (Vision)**」與「**程式碼執行 (Code Execution)**」能力！  
> 整合「**企業客戶應對手冊 (references/)**」、「**標準 CRM 試算表樣板 (templates/)**」與「**企業視覺 (assets/)**」，業務或客服人員可直接上傳**客戶來信截圖（客訴信、詢價信）**或輸入信件文字，AI 自動完成客戶意圖與情緒判定、撰寫高 EQ 回信草稿與 CRM Note，並透過 Python 呼叫 `openpyxl` 寫入企業 Logo 與 `=SUM()` 商機加總公式，產出高質感的實體 `.xlsx` CRM 互動紀錄單。

---

## 📖 範例運作機制

```mermaid
flowchart LR
    A[業務輸入客戶信件或<br>上傳客戶來信截圖] --> B[視覺辨識 + 讀取<br>crm-guidelines.md 準則]
    B --> C[分析客戶意圖與情緒指數<br>評估潛在商機金額與風險]
    C --> D[啟用 Code Execution<br>執行 Python openpyxl]
    D --> E[載入 templates/ 樣板<br>+ 插入 assets/ Logo<br>+ 寫入 SUM 公式]
    E --> F[產出高EQ回信草稿、<br>CRM Note與實體Excel紀錄單]
```

### 💡 自動化作業四部曲
1. **多模態辨識與意圖情緒診斷**：  
   支援直接拍照或截圖上傳客戶 Email 郵件。參照 `references/crm-guidelines.md` 判定客戶核心意圖（詢價擴充/客訴抱怨/會議邀約/流失風險）與情緒指數（`🟢 正向` / `🟡 中性` / `🔴 負面焦慮`）。
2. **高 EQ 專業回信草稿生成**：  
   依據應對黃金準則，先同理致歉、說明排障行動計畫、附帶明確會議時間選項（CTA），文字得體專業。
3. **品牌視覺與公式保留**：  
   呼叫 `openpyxl.drawing.image.Image` 將 `assets/company-logo.jpeg` 插入頂部表頭（Cell A1），並保留潛在商機金額的原生加總公式（`=SUM(F11:F20)`）。
4. **實體報表交付**：  
   將客戶名稱、窗口、痛點、跟進策略與預估商機填入指定儲存格，生成帶有企業品牌識別的完整實體 Excel 檔供下載。

---

## 📁 資料夾與檔案結構

### 1. 核心 Skill 設定架構（安裝 Skill 時所需之標準結構）
| 檔案 / 資料夾路徑 | 類型 | 職責與用途 |
| :--- | :---: | :--- |
| 📄 [`SKILL.md`](./SKILL.md) | 主設定檔 | 定義角色、Email多模態辨識、CRM準則與 Python openpyxl SOP 指令 |
| 📁 `templates/` | 範本目錄 | 存放高質感 CRM 互動樣板 [`crm-activity-template.xlsx`](./templates/crm-activity-template.xlsx) |
| 📁 `references/` | 參考規範 | 存放企業客戶關係管理與溝通手冊 [`crm-guidelines.md`](./references/crm-guidelines.md) |
| 📁 `assets/` | 靜態資產 | 存放企業標準圖檔 [`company-logo.jpeg`](./assets/company-logo.jpeg)（嵌入 Excel 表頭 A1） |

### 2. 課堂實測教材（獨立測試資料夾，供學生上傳練習）
| 檔案 / 資料夾路徑 | 類型 | 職責與用途 |
| :--- | :---: | :--- |
| 📁 [`sample_materials/`](./sample_materials/) | 測試單據 | 存放符合企業真實情境之客戶來信郵件截圖（供圖片上傳測試） |

```text
Office_Workflow_07_Customer_CRM/
├── SKILL.md                             # 核心技能指引（含多模態辨識與 Python openpyxl 規範）
├── templates/
│   └── crm-activity-template.xlsx       # 高質感專業 CRM 互動紀錄 Excel 樣板
├── references/
│   └── crm-guidelines.md                # 企業客戶溝通與 CRM 準則手冊
├── assets/
│   └── company-logo.jpeg                # 公司 Logo 圖檔（嵌入表頭 A1）
│
└── sample_materials/                    # 🧾 獨立課堂測試資料夾
    ├── 01_customer_complaint_email.png  # 客戶高急迫客訴來信截圖 (API延遲+續約流失警訊)
    └── 02_customer_expansion_inquiry.png# 客戶採購加購詢價信截圖 (45萬擴充商機+Demo預約)
```

---

## 🛠️ 安裝與建置方式

你可以選擇以下三種方式之一來建立並啟用此技能：

### 💡 方式 A：使用內建 `/skill-creator` 技能（推薦・自動建置）

> [!TIP]
> 請先確認已在 Claude Settings 中開啟 **Code execution and file creation** 功能。

#### 方案 1：直接上傳檔案並下指令建立
1. **上傳檔案**：將以下 3 個檔案同時上傳至 Claude 對話中：
   * 樣板：[`crm-activity-template.xlsx`](./templates/crm-activity-template.xlsx)
   * 規範：[`crm-guidelines.md`](./references/crm-guidelines.md)
   * 圖片：[`company-logo.jpeg`](./assets/company-logo.jpeg)

2. **下達建置指令**：直接複製並貼上以下多行 Prompt：

   ```text
   我想建立一個客戶回覆與 CRM 更新助手 Skill。
   請參考我上傳的 crm-guidelines.md 規章、Excel 樣板與 company-logo.jpeg 圖檔，
   使用 /skill-creator 幫我建立包含 references、templates 和 assets 資料夾的 Skill。

   請在 SKILL.md 中明確指定：
   1. 支援純文字貼入或上傳客戶信件圖檔，自動診斷意圖、情緒指數與商機金額。
   2. 依據 crm-guidelines.md 產出同理心專業回信與標準化 CRM Note。
   3. 遇重大客訴與流失風險時啟動安全煞車，不得擅自承諾賠償，提示內部升級。
   4. 執行 Python (Code Execution) 讀取 Excel 樣板並使用 openpyxl 
      在 Cell A1 嵌入 assets/company-logo.jpeg，保留商機總計列 =SUM(...) 原生公式。
   ```

3. **自動完成與啟用**：Claude 執行完畢後會自動在帳號中安裝並生效此 Skill。

---

### ✍️ 方式 B：手動複製檔案（網頁手動上傳）

1. **建立本機目錄**：在電腦中建立 `Office_Workflow_07_Customer_CRM` 資料夾，並建立 `references`、`templates` 與 `assets` 三個子目錄。
2. **放置對應檔案**：放入對應之 [`SKILL.md`](./SKILL.md)、樣板、規範手冊與公司 Logo。
3. **上傳至 Claude**：前往 Claude 網頁版 **Settings** ➔ **Capabilities** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

---

### 💻 方式 C：終端機部署（適用於 Claude Code）

```bash
cp -r Office_Workflow_07_Customer_CRM/ /mnt/skills/user/Office_Workflow_07_Customer_CRM
```

---

## 🧪 測試與驗證（三種實測情境）

為滿足不同課堂環境與教學層次需求，本技能設計了 **3 種由淺入深的測試模式**：

---

### 📝 測試情境一：純文字快速審核（無圖・日常口語）

適合學員快速演練。直接複製以下業務同仁收到的客戶真實詢價信件：

#### 📥 測試 Prompt（純文字）：
```text
我剛剛收到大客戶「元大金控 數位創新部 李協理」寄來的信，內容如下：
「David 您好：我們上週試用了貴司的企業 AI 工作流平台，同仁反饋非常好。目前我們正在評估下季度的採購預算，預計採購全公司 80 席年約授權，內部預估預算約 NT$ 650,000。想請問下週四 (9/10) 下午 15:00 是否方便安排一次正式的線上會議，討論系統資安合規性並提供正式報價單？」

請幫我分析客戶意圖與情緒，寫一封熱情專業的回信草稿（確認會議時間並附帶議程），
整理 CRM 系統 Note，並調用 Python 將這筆商機填入 Excel 樣板，產出正式的 Excel 紀錄單！
```

---

### 📸 測試情境二：全單據圖片多模態辨識（純圖片・高急迫客訴來信截圖）

從 [`sample_materials/`](./sample_materials/) 目錄上傳客戶來信截圖：

| 單據圖檔名稱 | 單據類型 | 關鍵欄位內容 | 預期審核結果 |
| :--- | :--- | :--- | :--- |
| [`01_customer_complaint_email.png`](./sample_materials/01_customer_complaint_email.png) | Outlook 客戶客訴郵件截圖 | 富邦科技王總監、API 延遲 8.4秒、威脅影響 36 萬續約 | 判定為 `🔴 高度負面/流失風險`，觸發安全煞車 |
| [`02_customer_expansion_inquiry.png`](./sample_materials/02_customer_expansion_inquiry.png) | 採購擴充詢價郵件截圖 | 國泰物流蔡經理、加購 40 輛車隊模組、45 萬商機預算 | 判定為 `🟢 高價值商機`，產出 Demo 邀約回信 |

#### 📥 測試步驟與 Prompt（純圖片）：
1. 將 [`01_customer_complaint_email.png`](./sample_materials/01_customer_complaint_email.png) 拖入對話框中。
2. 輸入以下指令：

```text
這是客戶剛寄來的緊急信件截圖，情緒非常焦慮不滿，負責業務為「業務部 陳大華 (David Chen)」。
請幫我辨識信件內容，判定客戶的核心訴求與情緒指標，
幫我寫一封具備高度同理心與明確修復時程的回覆信草稿，
並產出可貼入 CRM 的追蹤 Note，以及正式的 Excel 客戶互動紀錄單。
```

---

### 🔀 測試情境三：圖片與文字多模態整合（混合模式・最貼近真實辦公室）

**最貼近日常辦公室的真實情況**：同仁手邊有客戶詢價信件圖片，但剛好電話中與客戶聊到了額外需求與預算！

#### 📥 測試步驟與 Prompt（圖文整合）：
1. **上傳 1 張圖片**：[`02_customer_expansion_inquiry.png`](./sample_materials/02_customer_expansion_inquiry.png)（國泰智慧物流加購 45 萬詢價）。
2. **在輸入框貼入以下圖文整合 Prompt**：

```text
請幫我整合審查以下客戶最新商機進展，負責業務為「業務部 陳大華 (David Chen)」：

【附件圖片部分】：
已上傳國泰智慧物流蔡佩琪經理的加購諮詢信（預算 NT$ 450,000），請自動辨識其核心訴求。

【剛才電話通聯文字補充】：
剛剛與蔡經理通完電話，蔡經理補充：「若能在 9/15 前完成系統 POC 測試，他們願意在 Q4 額外追加全台 2 個物流分部的資料整合授權（預估追加預算 NT$ 200,000），總專案商機預估達到 NT$ 650,000」。會議時間確認定於下週三 9/9 下午 14:00。

請幫我合併分析這筆高價值商機，撰寫正式的確認回信草稿、更新 CRM 摘要與商機金額，
並將 2 筆模組明細填入 Excel 樣板，在表頭插入公司 Logo，產出實體 Excel CRM 紀錄單供我下載！
```

---

### 🎯 預期執行成果（智慧稽核與停止條件機制）

無論採取哪一種測試情境，Claude 皆會展現專業的「**安全煞車與主動補件（Human-in-the-Loop）**」機制：

* **🔍 階段 1・客戶意圖與情緒診斷**  
  - 面對富邦科技客訴：精準診斷意圖為 `客訴/流失警訊`，情緒指數判定為 `🔴 負面焦慮`，優先級列為 `最高 (High)`。
  - 面對國泰物流加購：精準提煉 2 大採購模組與商機預算 NT$ 450,000 ~ 650,000。
* **🚨 階段 2・安全煞車與高 EQ 回信（Human-in-the-Loop）**  
  面對客戶威脅解約或索賠，AI 展現高 EQ 同理心，先致歉並提供 19:00 前的排障說明，**嚴格遵守安全邊界，絕不私自答應賠償金額**，並主動建議業務主管知悉介入。
* **🐍 階段 3・Python 自動化處理與報表交付**  
  呼叫 Code Execution，以 `openpyxl` 載入 `templates/crm-activity-template.xlsx`：
  - 填入客戶公司名稱、窗口、負責業務。
  - 在 Cell A1 嵌入高清晰 `assets/company-logo.jpeg` 圖檔。
  - 將各筆互動訴求、建議策略與商機金額寫入試算表。
  - 潛在商機金額總計自動保留原生公式 `=SUM(F11:F20)`。
  - 產出實體 `.xlsx` 檔案提供即時點擊下載。

---

[← 返回 Skills 主頁](../../README.md)
