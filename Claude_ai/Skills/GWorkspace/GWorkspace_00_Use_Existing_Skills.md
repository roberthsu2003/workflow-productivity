# 實作範例 0：使用現有的 Skill（Google Workspace 入門）

> 🟢 **方案需求**：Free（需先在 Settings 開啟 Skills 與程式碼執行）  
> 🔗 **前置準備**：在 Settings → Connectors 完成 Google Workspace（Google Drive、Gmail）授權

這是學習 Skills 的**第一步**：不需要自己建立，先學會找到合適的現有 Skill 並直接呼叫。  
以下四個練習對應 **Google Docs、Google Sheets、Google Slides、Gmail**，每個都附有可直接複製使用的 RTCCF Prompt。

---

## 🛠️ 前置步驟（只需做一次）

1. 開啟 **Claude Desktop** → **Settings** → **Skills**
2. 確認已開啟 **Skills** 與 **程式碼執行（Code Execution）** 兩個開關
3. 前往 **Settings** → **Connectors** → 連接 **Google Workspace**（授權 Drive、Docs、Sheets、Slides、Gmail）
4. 完成後，在對話框輸入 `/` 可預覽目前可用的 Skill 清單

---

## 練習 A：用現有 Skill 建立 Google Docs 會議紀錄

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

### 📖 說明
輸入任務清單，Skill 自動建立含狀態欄位的 Google Sheets 試算表，方便追蹤進度。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是辦公室行政助手，擅長使用 Google Sheets 建立任務追蹤表。

## Task
請將我提供的任務清單，建立成 Google Sheets 試算表，
完成後回傳試算表連結。

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

## Format
- 建立 Google Sheets 試算表
- 完成後回傳連結，並列出已建立的欄位清單
```

---

## 練習 C：用現有 Skill 建立 Google Slides 簡報大綱

### 📖 說明
輸入簡報主題與要點，Skill 自動建立有固定結構的 Google Slides 投影片，省去從空白開始的時間。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是簡報設計助手，擅長將要點轉化為結構清晰的 Google Slides 投影片。

## Task
請依我提供的主題與要點，建立一份 Google Slides 簡報，
完成後回傳簡報連結。

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
- 簡報命名：「2026 Q2 業務成果報告」

## Format
- 建立 Google Slides 簡報
- 完成後回傳連結，並列出每頁的標題與要點摘要
```

---

## 練習 D：用現有 Skill 草擬並寄送 Gmail

### 📖 說明
輸入收件人與溝通重點，Skill 自動草擬專業郵件並可直接透過 Gmail 寄出，不需要自己開信箱。

### 📋 RTCCF Prompt（直接複製使用）

```markdown
## Role
你是商業郵件撰寫助手，擅長依照重點草擬專業且有禮貌的 Gmail 郵件。

## Task
請依我提供的資訊，草擬一封 Gmail 郵件，
確認內容無誤後透過 Gmail 寄出。

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
- 寄出前先顯示完整草稿讓我確認

## Format
- 先顯示完整郵件草稿（含主旨、稱謂、正文、簽名）
- 我確認後再透過 Gmail 寄出
- 完成後回傳寄出時間與收件人
```

---

## ✅ 完成後的下一步

練習完這四個範例後，您已學會：
- 找到並呼叫現有 Skill
- 用 RTCCF 框架提供清楚的任務指示
- 讓 Claude 直接操作 Google Workspace 產出成品

**下一步**：前往 [實作練習：Google Workspace Skills](./README.md)，學習如何調整 Skill 來符合您的部門習慣。

← [返回 Skills 索引](../README.md)
