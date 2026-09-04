# 延伸練習 5：請假與職務代理安排助手（第三階：整合者）

> **🎯 本階核心目標**  
> 運用 Claude AI 的「**多模態視覺辨識 (Vision)**」與「**程式碼執行 (Code Execution)**」能力！  
> 整合「**企業差假規章 (references/)**」、「**專業交接樣板 (templates/)**」與「**企業品牌視覺 (assets/)**」，同仁可直接上傳**人資請假單截圖、就醫證明單**或輸入日常口語，AI 自動進行交接風險評估、撰寫主管知會信與代理人交接清單，並透過 Python 產出包含公司 Logo 的高質感實體 `.xlsx` 請款/交接單。

---

## 📖 範例運作機制

```mermaid
flowchart LR
    A[同仁輸入請假事項或<br>上傳人資假單/就醫截圖] --> B[視覺辨識 + 讀取<br>leave-policy.md 規章]
    B --> C[盤點落於請假期間之任務<br>判定風險: 低/中/高]
    C --> D[啟用 Code Execution<br>執行 Python openpyxl]
    D --> E[載入 templates/ 樣板<br>+ 插入 assets/ Logo]
    E --> F[產出主管信、代理人指南<br>與高質感 Excel 交接單]
```

### 💡 自動化作業四部曲
1. **多模態辨識與規章比對**：  
   支援直接拍照或截圖上傳人資請假申請單、醫院證明，亦可直接輸入文字。參照 `references/leave-policy.md` 檢核請假天數、第一代理人完整度，並嚴格掃描「截止日落在請假期間」的各項任務。
2. **自動化通訊文本生成**：  
   自動生成 3 套專業溝通草稿：
   - ✉️ **主管知會核備信**（條列請假事由、代理安排與緊急聯絡方式）。
   - 🤝 **代理人交接指南**（清晰步驟、檔案存放路徑與客戶窗口）。
   - 🌐 **Out of Office (OOO) 外部自動回覆信**。
3. **品牌視覺與 Python 整合**：  
   呼叫 `openpyxl.drawing.image.Image` 將 `assets/company-logo.jpeg` 動態縮放插入頂部表頭（Cell A1:B3），並讀取內建企業 Footer 的樣板。
4. **實體報表交付**：  
   將請假人資訊、任務清單、風險等級（`🟢 低風險` / `🟡 中風險` / `🔴 高風險`）與簽核欄位填入指定儲存格，生成完整實體 Excel 檔供下載。

---

## 📁 資料夾與檔案結構

### 1. 核心 Skill 設定架構（安裝 Skill 時所需之標準結構）
| 檔案 / 資料夾路徑 | 類型 | 職責與用途 |
| :--- | :---: | :--- |
| 📄 [`SKILL.md`](./SKILL.md) | 主設定檔 | 定義角色、文字/圖片多模態辨識、交接風險規則與 Python openpyxl SOP 指令 |
| 📁 `templates/` | 範本目錄 | 存放高質感職務交接樣板 [`leave-handover-template.xlsx`](./templates/leave-handover-template.xlsx) |
| 📁 `references/` | 參考規範 | 存放企業請假與職務代理人作業手冊 [`leave-policy.md`](./references/leave-policy.md) |
| 📁 `assets/` | 靜態資產 | 存放企業標準圖檔 [`company-logo.jpeg`](./assets/company-logo.jpeg)（嵌入 Excel 表頭 A1） |

### 2. 課堂實測教材（獨立測試資料夾，供學生上傳練習）
| 檔案 / 資料夾路徑 | 類型 | 職責與用途 |
| :--- | :---: | :--- |
| 📁 [`sample_materials/`](./sample_materials/) | 測試單據 | 存放符合企業常見規格之模擬人資假單與就醫證明圖檔（供圖片上傳測試） |

```text
Office_Workflow_05_Leave_Handover/
├── SKILL.md                             # 核心技能指引（含多模態辨識與 Python openpyxl 規範）
├── templates/
│   └── leave-handover-template.xlsx     # 高質感專業請假交接 Excel 樣板
├── references/
│   └── leave-policy.md                  # 企業請假與職務代理人作業手冊
├── assets/
│   └── company-logo.jpeg                # 公司 Logo 圖檔（嵌入表頭 A1）
│
└── sample_materials/                    # 🧾 獨立課堂測試資料夾
    ├── 01_hr_leave_request_slip.png     # 企業人資 Portal 請假單截圖
    └── 02_medical_certificate_slip.png  # 醫院門診證明與就醫收據截圖
```

---

## 🛠️ 安裝與建置方式

你可以選擇以下三種方式之一來建立並啟用此技能：

### 💡 方式 A：使用內建 `/skill-creator` 技能（推薦・自動建置）

> [!TIP]
> 請先確認已在 Claude Settings 中開啟 **Code execution and file creation** 功能。

#### 方案 1：直接上傳檔案並下指令建立
1. **上傳檔案**：將以下 3 個檔案同時上傳至 Claude 對話中：
   * 樣板：[`leave-handover-template.xlsx`](./templates/leave-handover-template.xlsx)
   * 規範：[`leave-policy.md`](./references/leave-policy.md)
   * 圖片：[`company-logo.jpeg`](./assets/company-logo.jpeg)

2. **下達建置指令**：直接複製並貼上以下多行 Prompt：

   ```text
   我想建立一個請假與職務代理安排助手 Skill。
   請參考我上傳的 leave-policy.md 規章、Excel 樣板與 company-logo.jpeg 圖檔，
   使用 /skill-creator 幫我建立包含 references、templates 和 assets 資料夾的 Skill。

   請在 SKILL.md 中明確指定：
   1. 支援使用者輸入純文字或上傳假單截圖，自動提取請假期間與待辦清單。
   2. 比對 leave-policy.md，特別掃描截止日落在請假期間之任務並標註 🔴 高風險。
   3. 自動撰寫主管核備信、代理人交接指南與中英文 Out of Office 自動回覆。
   4. 執行 Python (Code Execution) 讀取 Excel 樣板並使用 openpyxl.drawing.image.Image 
      將 assets/company-logo.jpeg 插入頂部表頭 (Cell A1)。
   ```

3. **自動完成與啟用**：Claude 執行完畢後會自動在帳號中安裝並生效此 Skill。

---

### ✍️ 方式 B：手動複製檔案（網頁手動上傳）

1. **建立本機目錄**：在電腦中建立 `Office_Workflow_05_Leave_Handover` 資料夾，並建立 `references`、`templates` 與 `assets` 三個子目錄。
2. **放置對應檔案**：放入對應之 [`SKILL.md`](./SKILL.md)、樣板、規範手冊與公司 Logo。
3. **上傳至 Claude**：前往 Claude 網頁版 **Settings** ➔ **Capabilities** ➔ **Skills** ➔ 點擊 **Add Custom Skill** 上傳此資料夾。

---

### 💻 方式 C：終端機部署（適用於 Claude Code）

```bash
cp -r Office_Workflow_05_Leave_Handover/ /mnt/skills/user/Office_Workflow_05_Leave_Handover
```

---

## 🧪 測試與驗證（三種實測情境）

為滿足不同課堂環境與教學層次需求，本技能設計了 **3 種由淺入深的測試模式**：

---

### 📝 測試情境一：純文字快速審核（無圖・日常口語）

適合學員快速演練。直接複製以下同仁隨手寫下的雜亂請假文字清單：

#### 📥 測試 Prompt（純文字）：
```text
我下週要請特休，申請人為「產品研發部 林家豪 (Kevin Lin)」：
- 請假日期：2026/09/10 (四) 到 2026/09/15 (二)，共 4 天工作日
- 職務代理人：張雅晴 (Amy Chang, 分機 #3812)
- 緊急聯絡電話：0928-112-889
- 手上進行中的工作：
  1. 官網改版 V2.0 上線驗收（預計 9/11 週五下午驗收，需要送交主管簽核）
  2. 與行銷部每週例行對焦會議（9/14 週一 10:00，需有人代為出席紀錄）
  3. 核心 API 伺服器安全性憑證更新（已於 9/8 提前完成）
  4. 新進工程師 Code Review 指引（9/18 前完成即可）

請幫我檢查交接風險，產出主管通知信、給 Amy 的交接訊息、外部 OOO 回信，
並幫我將交接清單填寫進 Excel 樣板，產出正式的 Excel 請假交接單供我下載。
```

---

### 📸 測試情境二：全單據圖片多模態辨識（純圖片・人資系統截圖）

從 [`sample_materials/`](./sample_materials/) 目錄上傳企業人資系統的請假申請截圖：

| 單據圖檔名稱 | 單據類型 | 關鍵欄位內容 | 預期審核結果 |
| :--- | :--- | :--- | :--- |
| [`01_hr_leave_request_slip.png`](./sample_materials/01_hr_leave_request_slip.png) | 人資系統請假申請單截圖 | 林家豪 9/10~9/15 特休 4 天、代理人 Amy、待辦含 9/11 驗收 | 辨識完整，標註 9/11 上線為 `🔴 高風險` |
| [`02_medical_certificate_slip.png`](./sample_materials/02_medical_certificate_slip.png) | 醫院門診證明與就醫收據 | 張雅晴 9/4 急性扁桃腺高燒、醫囑居家休養 3 天 | 突發病假，缺少代理人，觸發停止煞車詢問 |

#### 📥 測試步驟與 Prompt（純圖片）：
1. 將 [`01_hr_leave_request_slip.png`](./sample_materials/01_hr_leave_request_slip.png) 拖曳上傳至對話框。
2. 輸入以下指令：

```text
這是我剛在公司人資系統填寫並經主管初審的請假申請單截圖。
請幫我辨識請假起訖日、代理人與各項工作任務，依公司規章分析交接風險，
產出主管核備信、代理人交接指南與 OOO 信件，並產出一份正式的 Excel 交接單。
```

---

### 🔀 測試情境三：圖片與文字多模態整合（混合模式・最貼近真實辦公室）

**最貼近日常辦公室的突發狀況**：同仁因急病突發請假，附上醫院就診證明單據，但文字訊息補充代理與緊急交接事項！

#### 📥 測試步驟與 Prompt（圖文整合）：
1. **上傳 1 張圖片**：[`02_medical_certificate_slip.png`](./sample_materials/02_medical_certificate_slip.png)（台安醫院診斷證明，需休養至 9/6）。
2. **在輸入框貼入以下圖文整合 Prompt**：

```text
不好意思主管，我今天突發高燒去醫院掛急診，附件附上台安醫院的就醫收據與診斷證明單。
我需要申請 2026/09/04 到 2026/09/06 共 3 天病假。

【緊急交接補充】：
- 職務代理人：陳大華 (David Chen, 分機 #3102)
- 緊急聯絡：我的手機 0912-345-678
- 進行中緊急任務：
  1. 今天 (9/4) 下午 14:00 有一場合約審查線上會議，需要 David 幫忙上線旁聽並記錄。
  2. 明天 (9/5) 下午 17:00 需交 Q3 行銷專案結案報告，檔案在雲端共享資料夾「Q3-Report-Draft」，內容已完成 90%，請 David 幫忙做最後排版確認送出。

請幫我依據證明單與文字進行整合審核，產生請病假主管通知信、給 David 的緊急交接清單，
並調用 Python 將交接單填入 Excel 樣板，產出正式的 Excel 交接單！
```

---

### 🎯 預期執行成果（智慧稽核與停止條件機制）

無論採取哪一種測試情境，Claude 皆會展現專業的「**安全煞車與主動補件（Human-in-the-Loop）**」機制：

* **🔍 階段 1・交接風險診斷與安全煞車判定**  
  - 檢核 9/11「官網改版 V2.0 上線驗收」截止日落在休假期間 ➔ 標記為 `🔴 高風險`。
  - 主動提示：「由於 9/11 驗收涉及跨部門簽核，若代理人 Amy 尚未取得授權，建議於休假前或指派專責代理同仁」。
* **🚨 階段 2・安全煞車與主動詢問（Human-in-the-Loop）**  
  若缺少代理人或緊急電話，AI 不會自行捏造，而是立即停下提出補件請求；若資訊完整，則生成清晰的主管通知、代理人指南與中英文 OOO 自動回覆。
* **🐍 階段 3・Python 自動化處理與報表交付**  
  呼叫 Code Execution，以 `openpyxl` 載入 `templates/leave-handover-template.xlsx`：
  - 填入請假同仁、部門、代理人與起訖日期。
  - 在 Cell A1 嵌入高清晰 `assets/company-logo.jpeg` 圖檔。
  - 將各筆任務、截止日、進度與風險等級（`🟢 低` / `🔴 高`）寫入試算表。
  - 產出實體 `.xlsx` 檔案提供即時點擊下載。

---

[← 返回 Skills 主頁](../../README.md)
