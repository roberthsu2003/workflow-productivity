# 實作練習：使用現有的 Skill（Google Workspace 實戰）

> 🟢 **方案需求**：Free（需先在 Settings 開啟 Skills 與程式碼執行）  
> 🔗 **前置準備**：在 Settings → Connectors 完成 Google Drive 與 Gmail 授權

這是學習 Skills 的**第一步**：不需要自己建立，先學會找到合適的現有 Skill 並直接呼叫。  
以下四個練習對應 **Google Docs、Google Sheets、Google Slides、Gmail**，每個都附有可直接複製使用的 RTCCF Prompt。

---

## 🛠️ 前置步驟（只需做一次）

1. 開啟 **Claude Desktop** → **Settings** → **Capabilities**（能力）
2. 確認已將 **Code execution and file creation**（程式碼執行與檔案建立）切換為**開啟** (On) 狀態（此功能是呼叫 Skills 的關鍵前提）
3. 前往 **Settings** → **Connectors** → 連接 **Google Drive** 與 **Gmail**（Docs 與 Sheets 不需要單獨授權，只需授權 Google Drive 即可）
4. 完成後即可直接在對話中以 Prompt 觸發 Skill（網頁版介面無斜線 `/` 指令選單，Skills 會在背景自動識別並觸發執行）

---

## 練習 A：用現有 Skill 建立 Google Docs 會議紀錄

> 使用artifacts,測試無誤

### 📖 說明
輸入會議的零散要點或逐字稿，Claude 會先在 Artifacts 呈現草稿與你討論。確認無誤後，再透過 Google Workspace Skill 自動建立 Google Doc，並將其存放至 Google Drive 的「上課用」資料夾中，回傳可分享的連結。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是辦公室行政助手，擅長整理會議紀錄，並能運用 Google Workspace Skill 管理雲端檔案。

## Task
請將我提供的會議要點，整理成一份正式的會議紀錄，先與我討論確認後，再使用 Google Docs Skill 將其建立並儲存至 Google Drive 中名為「上課用」的資料夾。

## Context
會議資訊：
- 會議名稱：2026 年第二季業務檢討會
- 日期：2026-06-09
- 與會人員：王小明（主持）、李小華、陳小美
- 討論要點：
  - Q1 業績達成率 87%，Q2 目標上調 10%
  - 新客戶開發：本季新增 3 家，需加強中南部區域
  - 下次會議排定 6/23，小華負責準備競品分析

## Constraint
- 語言：繁體中文
- 文件結構：會議基本資訊 → 討論摘要 → 決議事項 → 行動清單（含負責人與期限）
- 行動清單格式：| 任務 | 負責人 | 截止日 |
- **工作流程限制**：
  1. **第一步（討論階段）**：請先使用 Claude Artifacts 功能，以 Markdown 格式呈現會議紀錄草稿。
  2. **第二步（討論階段）**：詢問我是否需要修改，在此時**不要**呼叫 Google Workspace Skill 建立文件。
  3. **第三步（存檔階段）**：待我確認「可以建立」後，呼叫 Google Docs Skill 建立文件。
  4. **第四步（資料夾歸檔）**：請將該會議紀錄存放在 Google Drive 根目錄下的 **「上課用」** 資料夾中（若「上課用」資料夾不存在，請先建立該資料夾再將文件移入）。

## Format
- 建立 Google Docs 文件，命名為「{日期} {會議名稱} 會議紀錄」
- 完成後回傳 Google Docs 的文件連結
```

---

## 練習 B：用現有 Skill 建立 Google Sheets 任務追蹤表

> 使用artifacts,測試無誤

### 📖 說明
輸入任務清單，Claude 會先在 Artifacts 呈現試算表結構與草稿。確認無誤後，再透過 Google Workspace Skill 自動建立 Google Sheets，並將其存放至 Google Drive 的「上課用」資料夾中，回傳可分享的連結。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是辦公室行政助手，擅長使用 Google Sheets 建立任務追蹤表，並能運用 Google Workspace Skill 管理雲端檔案。

## Task
請將我提供的任務清單，整理成一份任務追蹤表，先與我討論確認後，再使用 Google Sheets Skill 將其建立並儲存至 Google Drive 中名為「上課用」的資料夾。

## Context
任務清單：
- 採購 3 台 27 吋螢幕（負責人：王小明，截止：2026-06-20）
- 更新員工手冊 2026 版（負責人：李小華，截止：2026-06-30）
- 安排 Q2 部門聚餐（負責人：陳小美，截止：2026-06-15）
- 整理客戶合約歸檔（負責人：王小明，截止：2026-07-05）

## Constraint
- 語言：繁體中文
- 欄位：任務名稱、負責人、截止日、狀態（預設：待處理）、備註
- 依截止日由近到遠排序
- 試算表名稱：「2026-06 任務追蹤表」
- **工作流程限制**：
  1. **第一步（討論階段）**：請先使用 Claude Artifacts 功能，以 Markdown 表格呈現任務追蹤表草稿。
  2. **第二步（討論階段）**：詢問我是否需要修改，在此時**不要**呼叫 Google Workspace Skill 建立檔案。
  3. **第三步（存檔階段）**：待我確認「可以建立」後，呼叫 Google Sheets Skill 建立檔案。
  4. **第四步（資料夾歸檔）**：請將該試算表存放在 Google Drive 根目錄下的 **「上課用」** 資料夾中（若「上課用」資料夾不存在，請先建立該資料夾再將檔案移入）。

## Format
- 建立 Google Sheets 試算表
- 完成後回傳連結，並列出已建立的欄位清單
```

---

## 練習 C1：使用 Anthropic PPTX Skill 製作簡報 (.pptx)

> ⚠️ **注意**：必需先關閉 Canva 的 Connector  
> 💡 *這也是內建於「Code execution and file creation」功能中的工具。*

### 📖 說明
輸入簡報主題與要點，Claude 會先在 Artifacts 呈現簡報大綱與投影片結構。確認大綱無誤後，再透過內建的 **PPTX Skill**（已內建於 `Code execution and file creation` 功能中）在雲端自動產生實體 PowerPoint 簡報檔案 (.pptx)，並提供下載連結。

> 🎨 **設計配色指南**：
> 內建的 PPTX Skill 支援自訂配色主題。請參考 [Anthropic PPTX 官方設計指南](https://github.com/anthropics/skills/tree/main/skills/pptx) 的說明，您可以直接在 Prompt 裡的 `Constraint` 指定下方其中一組主題：
> 
> * **Midnight Executive** (`1E2761` / `CADCFC` / `FFFFFF`) - 深藍/冰藍/白（適合正式商務報告）
> * **Forest & Moss** (`2C5F2D` / `97BC62` / `F5F5F5`) - 森林綠/苔綠/乳白（適合永續、環保或自然主題）
> * **Coral Energy** (`F96167` / `F9E795` / `2F3C7E`) - 珊瑚紅/金黃/深藍（適合活力、創新或科技主題）
> * **Warm Terracotta** (`B85042` / `E7E8D1` / `A7BEAE`) - 磚紅/沙褐/鼠尾草綠（適合溫暖、人文質感主題）
> * **Ocean Gradient** (`065A82` / `1C7293` / `21295C`) - 深藍/湖水藍/子夜藍（適合專業、嚴謹或科技主題）
> * **Charcoal Minimal** (`36454F` / `F2F2F2` / `212121`) - 炭灰/灰白/純黑（極簡商務風格）
> * **Teal Trust** (`028090` / `00A896` / `02C39A`) - 青綠/海泡綠/薄荷綠（適合醫療、信任與新創主題）
> * **Berry & Cream** (`6D2E46` / `A26769` / `ECE2D0`) - 莓紫/玫瑰粉/奶油白（適合生活、美妝或優雅主題）
> * **Sage Calm** (`84B59F` / `69A297` / `50808E`) - 鼠尾草綠/尤加利綠/石板灰（適合安靜、極簡或療癒主題）
> * **Cherry Bold** (`990011` / `FCF6F5` / `2F3C7E`) - 櫻桃紅/暖白/深藍（強烈對比，適合發表會與焦點發表）

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是簡報設計助手，擅長將要點轉化為結構清晰的簡報大綱，並能運用 PPTX Skill 產生 PowerPoint 簡報檔案。

## Task
請依我提供的主題與要點，規劃一份簡報大綱與投影片結構，先與我討論確認後，再使用 PPTX Skill 將其製作成 PowerPoint 簡報檔案 (.pptx) 供我下載。

## Context
簡報資訊：
- 主題：2026 Q2 業務成果報告
- 對象：部門主管
- 要點：
  - Q2 業績達成率 94%，超越目標 4%
  - 新客戶 5 家，集中在北部科技業
  - 下半年策略：深耕現有客戶 + 開拓中南部市場
  - 預計 Q3 目標：業績成長 15%

## Constraint
- 語言：繁體中文
- 簡報設計配色：指定使用「Midnight Executive」配色方案（深藍/冰藍/白），營造專業且清晰的商務視覺。
- 固定 5 頁結構：封面 → 本期成果 → 重點發現 → 下半年策略 → 結語與目標
- 每頁要點不超過 4 條
- **工作流程限制**：
  1. **第一步（討論階段）**：請先使用 Claude Artifacts 功能，呈現每頁投影片的標題與大綱草稿。
  2. **第二步（討論階段）**：詢問我是否需要修改，在此時**不要**呼叫 PPTX 產生工具。
  3. **第三步（製作階段）**：待我確認大綱「可以製作」後，呼叫內建的 PPTX Skill 將此大綱內容製作成實體 PPTX 簡報檔案。

## Format
- 使用內建 PPTX Skill 建立並套用指定配色，匯出 PowerPoint 簡報檔案 (.pptx)
- 完成後提供簡報檔案下載連結，並列出每頁的標題與大綱摘要
```

---

## 練習 C2：使用 Canva Connector 製作簡報

> ⚠️ **注意**：必需開啟 Canva 的 Connector  
> 使用artifacts,測試無誤

### 📖 說明
輸入簡報主題與要點，Claude 會先在 Artifacts 呈現簡報大綱與投影片結構。確認大綱無誤後，再透過 **Canva Connector** 於 Canva 雲端平台自動建立精美簡報，回傳簡報的編輯或檢視連結。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是簡報設計助手，擅長將要點轉化為結構清晰的簡報大綱，並能運用 Canva Connector 製作精美的簡報。

## Task
請依我提供的主題與要點，規劃一份簡報大綱與投影片結構，先與我討論確認後，再使用 Canva Connector 將其製作成簡報檔案。

## Context
簡報資訊：
- 主題：2026 Q2 業務成果報告
- 對象：部門主管
- 要點：
  - Q2 業績達成率 94%，超越目標 4%
  - 新客戶 5 家，集中在北部科技業
  - 下半年策略：深耕現有客戶 + 開拓中南部市場
  - 預計 Q3 目標：業績成長 15%

## Constraint
- 語言：繁體中文
- 固定 5 頁結構：封面 → 本期成果 → 重點發現 → 下半年策略 → 結語與目標
- 每頁要點不超過 4 條
- **工作流程限制**：
  1. **第一步（討論階段）**：請先使用 Claude Artifacts 功能，呈現每頁投影片的標題與大綱草稿。
  2. **第二步（討論階段）**：詢問我是否需要修改，在此時**不要**呼叫 Canva Connector。
  3. **第三步（製作階段）**：待我確認大綱「可以製作」後，呼叫 Canva Connector 將此大綱內容製作成 Canva 簡報。

## Format
- 使用 Canva 建立簡報檔案
- 完成後回傳 Canva 簡報連結，並列出每頁的標題與大綱摘要
```

---

## 練習 D：用現有 Skill 草擬並寄送 Gmail

> 使用artifacts,測試無誤

### 📖 說明
輸入收件人與溝通重點，Claude 會先在 Artifacts 呈現郵件草稿。確認無誤後，再透過 Gmail Skill 自動建立草稿，並為該郵件套用「上課用」標籤（Tag）。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是商業郵件撰寫助手，擅長依照重點草擬專業且有禮貌的 Gmail 郵件，並使用 Gmail Skill 管理郵件。

## Task
請依我提供的資訊，規劃一封郵件草稿，先與我討論確認後，再使用 Gmail Skill 建立草稿，並為該郵件套用「上課用」標籤（Tag）。

## Context
郵件資訊：
- 收件人：supplier@example.com（廠商業務）
- 主旨：確認採購訂單 PO-2026-0609 交期
- 溝通重點：
  - 我方已於 6/9 下訂，訂單編號 PO-2026-0609
  - 請廠商確認預計出貨日期
  - 若有延誤請提前告知，我方最晚需在 6/20 收到貨品
  - 語氣：正式但友善

## Constraint
- 語言：繁體中文
- 結尾簽名：王小明｜採購部｜分機 1234
- **工作流程限制**：
  1. **第一步（討論階段）**：請先使用 Claude Artifacts 功能，以 Markdown 格式呈現完整郵件草稿（含主旨、收件人、內文、簽名）。
  2. **第二步（討論階段）**：詢問我是否需要修改，在此時**不要**呼叫 Gmail Skill 建立或寄出郵件。
  3. **第三步（存檔階段）**：待我確認「可以建立」後，呼叫 Gmail Skill 建立郵件草稿。
  4. **第四步（套用標籤）**：請為該封郵件草稿套用名稱為 **「上課用」** 的標籤/分類標記（若標籤不存在，請先在 Gmail 中建立該標籤再套用）。

## Format
- 先在對話中呈現草稿
- 我確認後呼叫 Gmail Skill 建立草稿，並回傳操作結果與套用標籤的確認資訊
```

---

## ✅ 完成後的下一步

練習完這四個範例後，您已學會：
- 找到並呼叫現有 Skill
- 用 RTCCF 框架提供清楚的任務指示
- 讓 Claude 直接操作 Google Workspace 產出成品

**下一步**：返回 [Skills 主頁](../README.md)，學習如何從頭自訂您專屬的 Skills！

---

← [返回 Skills 主頁](../README.md)
