# 實作練習：使用現有的 Skill（溝通與內容實戰）

> 🟢 **方案需求**：Free（需先在 Settings 開啟 Skills 與程式碼執行）  
> 💬 **溝通主軸**：教導 Claude 透過官方的溝通與內容 Skills，在團隊協作、公告發佈與日常溝通中，維持一致的專業語氣、格式與團隊趣味。

本章節介紹如何呼叫官方在溝通與內容類別提供的 3 個 Skills：**doc-coauthoring、internal-comms、slack-gif-creator**。以下提供每個 Skill 的操作說明與直接複製使用的 RTCCF Prompt。

---

## 🛠️ 前置步驟（只需做一次）

1. 開啟 **Claude Desktop** 或 Web 版的 **Settings**
2. 確認已在 `Capabilities` 開啟 **Code execution and file creation** 
3. 完成後即可直接在對話中以 Prompt 觸發 Skill（網頁版介面無斜線 `/` 指令選單，Skills 會在背景自動識別並觸發執行）。

---

## 練習 A：使用 `doc-coauthoring` 進行保留個人風格的長文修飾

### 📖 說明
一般的 AI 在潤飾文章時，很容易把個人風格抹除，讓文章變得「非常像 AI 寫的機器話」。`doc-coauthoring` 的核心邏輯是**協作而非全面改寫**。它會深入理解並保留作者原有的語氣與寫作風格 (Author's Voice)，並以旁註、微調建議的方式協助長篇文稿（如部落格文章、專欄、演講稿）的優化。

### 📋 RTCCF Prompt（直接複製使用）

本範例採用 **RTCCF 模型** 組織提示詞結構（其中 **R、C、C、F 為 Optional 選填**，學員可依需求調整；`Task` 為核心必要項目）。

```markdown
## Role (Optional)
你是資深編輯與寫作教練，
擅長調用 doc-coauthoring 技能進行長文編修，能在優化語句結構的同時，完整保留作者獨特的個人文風。

## Task
請幫我潤飾我寫的這篇關於「數位游牧心路歷程」的短文。
請先使用 Artifacts 展示你的編修建議，並透過 doc-coauthoring 確保修改程度適中，保留我原本比較隨性、口語的文風。

## Context (Optional)
原始文章段落：
「老實說，剛開始出來當自由工作者，每天在咖啡廳抱著筆電，看起來超酷的對吧？
但其實心裡慌得要死。沒有了公司每個月固定入帳的薪水，看到下個月接案的空檔，真的會焦慮到失眠。
不過，熬過前半年後，當你建立起自己的接案節奏，那種時間自由的感覺，真的是在辦公室打卡上班無法比擬的。
我想分享的是，自由的代價是自律，如果你還沒準備好面對焦慮，先別急著裸辭。」

## Constraint (Optional)
- 語言：繁體中文
- 編修規定：
  1. 請調用 doc-coauthoring 技能分析我原本段落的語氣特質（例如：口語、真誠、略帶自嘲、具啟發性）。
  2. 請以「微調建議」的形式在 Artifacts 呈現，使用對比表格或旁註指出修改原因。
  3. 嚴禁將語氣改寫成冰冷的官方公文風格。

## Format (Optional)
- 在 Artifact 中以 Markdown 格式呈現「原文字段落 vs. 建議潤飾段落」對比與編修理由
- 回傳簡要總結你如何透過 doc-coauthoring 保留我的寫作聲音 (Voice)
```

---

## 練習 B：使用 `internal-comms` 標準化企業內部公告

### 📖 說明
在辦公室中，對內溝通的效率至關重要。`internal-comms` 能夠確保全員公告、週報、專案狀態更新等格式具備高可讀性，使用清晰的條列式、時間線與責任劃分，避免冗長無重點的文字干擾工作節奏。

### 📋 RTCCF Prompt（直接複製使用）

本範例採用 **RTCCF 模型** 組織提示詞結構（其中 **R、C、C、F 為 Optional 選填**，學員可依需求調整；`Task` 為核心必要項目）。

```markdown
## Role (Optional)
你是企業內部溝通經理 (Internal Communications Manager)，
擅長運用 internal-comms 技能將複雜的業務變更轉化為清晰、重點突出的全員公告。

## Task
請幫我撰寫一封關於「公司內部 ERP 系統升級與停機維護」的全員通知信件。

## Context (Optional)
變更資訊：
- 主題：ERP 系統升級 2.0 版
- 停機時間：2026-07-10 (五) 18:00 至 2026-07-12 (日) 23:59
- 受影響範圍：採購模組、請假系統、財務報銷系統此期間無法登入。
- 緊急聯絡人：IT 部門小張（分機 8888）。

## Constraint (Optional)
- 語言：繁體中文
- 公告結構（需調用 internal-comms 規範）：
  1. **TL;DR (重點摘要)**：放在最頂部，用 3 句話講完時間與影響。
  2. **重要時間線**：使用 Markdown 表格或區塊呈現停機與恢復時間。
  3. **替代方案**：說明若此期間有緊急請假或採購需求，員工該如何處理。
  4. 語氣：專業、肯定、易讀，並適當加粗關鍵日期。

## Format (Optional)
- 以 Markdown 格式輸出公告全文 Artifact
- 完成後簡要說明此公告符合哪些 internal-comms 的高效溝通原則
```

---

## 練習 C：使用 `slack-gif-creator` 製作團隊互動動態 GIF

### 📖 說明
團隊溝通不僅要高效，也要有趣。`slack-gif-creator` 能夠在 Claude 的伺服器端動態生成適合 Slack 尺寸與格式的動態 GIF 貼圖（如慶祝、歡迎、感謝等），非常適合用於增進遠距團隊的氛圍。

### 📋 RTCCF Prompt（直接複製使用）

本範例採用 **RTCCF 模型** 組織提示詞結構（其中 **R、C、C、F 為 Optional 選填**，學員可依需求調整；`Task` 為核心必要項目）。

```markdown
## Role (Optional)
你是團隊氛圍大師，
擅長調用 slack-gif-creator 技能製作活潑、有趣的 Slack 動態 GIF 貼圖，為團隊日常溝通增添溫度。

## Task
我們團隊最近迎來了一位新工程師「小明」，
請使用 slack-gif-creator 幫我製作一張適合在 Slack #welcome 頻道發佈的「熱烈歡迎 (Warm Welcome)」動態 GIF 貼圖。

## Context (Optional)
畫面元素與文案：
- 文案內容：「Welcome, Xiaoming! 🚀」
- 視覺風格：太空科技感、帶有火箭發射或星星閃爍的動態背景。
- 尺寸：適合 Slack 貼圖大小（例如 128x128 像素或 256x256 像素）。

## Constraint (Optional)
- 語言：英文文案（Welcome, Xiaoming!），繁體中文操作說明
- 技術要求：
  1. 調用 slack-gif-creator 技能在背景執行 Python 程式碼，使用 `Pillow` 圖形庫生成多幀動態圖片。
  2. 確保 GIF 循環播放平滑。
  3. 檔案大小適中，適合直接在 Slack 預覽下載。

## Format (Optional)
- 呼叫技能在伺服器端產生實體 GIF 檔案，並提供直接下載連結
- 在對話中顯示生成的 GIF 動態圖預覽
```

---

## ✅ 完成後的下一步

恭喜您完成了溝通與內容類別的實作！現在您已經具備：
- 寫出保留作者聲音的優雅長文編修技巧。
- 製作精準、不冗長且高可讀性的內部通知。
- 運用自動化繪圖產出好玩的 Slack 動態 GIF。

這完成了官方提供的全部四大領域 Skills 練習。現在您可以返回 [Skills 主頁](../README.md)，瀏覽底部的**十個辦公室真實工作流範例**，將這些單一技能組合起來，解決更複雜的辦公室自動化任務！

---

← [返回 Skills 主頁](../README.md)
