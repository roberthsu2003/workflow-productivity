# AI 驅動的成品 (Claude in Claude)：讓小工具內建 AI 大腦

> 深入解析如何在不申請 API Key、不架設後端伺服器的情況下，在 Artifact 內部調用 Claude 模型能力，並了解其費用歸屬與安全防護機制。

---

## 💡 什麼是 Claude in Claude？

以往我們用 Claude 做出來的網頁小工具（如純 HTML/JS 計算機或表格），按按鈕只能執行預先寫好的固定程式邏輯。如果使用者輸入隨興的文字，網頁本身是無法「動腦思考」的。

**Claude in Claude（AI-powered Artifacts）** 讓做出來的成品**直接內建一顆 Claude 的大腦**！

| 比較維度 | 一般前端 Artifact | AI 驅動的 Artifact (Claude in Claude) |
| :--- | :--- | :--- |
| **底層技術** | 純瀏覽器端 HTML/CSS/JavaScript | 瀏覽器前端 ＋ 內嵌 Claude 模型調用 |
| **運算能力** | 僅能處理預設規則、計算、圖表繪製 | 可即時進行文字理解、文章潤飾、翻譯、邏輯分析 |
| **生活比喻** | 一台普通電子計算機 | 一台內建 AI 秘書的智慧機器 |
| **技術門檻** | 免後端、免伺服器 | **同樣免後端、免 API Key、免伺服器** |

---

## 🏢 職場實務情境舉例

1. **公文與簽呈潤飾產生器**：
   同仁在網頁輸入框貼上粗糙草稿，點擊按鈕，網頁內部自動呼叫 Claude 轉化為正式公文格式。
2. **多國語言客服自動回信模擬器**：
   輸入客戶抱怨內容，小工具現場生成繁中、英文、日文三種語調的回覆草稿。
3. **會議逐字稿重點摘要卡**：
   貼上零散的會議語音轉文字，小工具現場萃取行動方針與決議事項。


---

## 🛠️ 核心底層技術：`window.claude.complete()`

在 Claude Artifacts 沙盒環境中，Anthropic 官方注入了一個全域 JavaScript 介面：**`window.claude.complete()`**。
這正是讓前端小工具無需 API Key、免架後端即可調用 Claude 的秘密通道（也被社群稱為「Claude in Claude」或「Claudeception」）！

### 1. 基本語法
```javascript
// 最簡呼叫方式：傳入提示字串，直接 await 等待回傳文字
const result = await window.claude.complete("請將以下文字濃縮為 3 個條列要點：\n" + userInput);
```

> [!TIP]
> **環境防呆提示**：`window.claude` 只存在於 Claude.ai 的 Artifact 預覽環境中。若把網頁存到本機直接用 Chrome 開啟，該物件會是 `undefined`。因此程式中建議加入環境檢查判斷！

---

## 💻 官方推薦實作小範例：公文與草稿 AI 潤飾卡

你可以直接複製以下 Prompt 讓 Claude 產生，或是直接檢視這份標準的前端 HTML 程式碼架構：

### 🎯 如何要求 Claude 幫你製作？（RTCCF 提示詞 Prompt）

```markdown
## Role
你是一位精通前端開發與 AI 應用的資深架構師。

## Task
建立一個單一檔案的 HTML Artifact 小工具：「公文語氣潤飾器」。

## Context
使用者需要將口語、粗糙的備忘草稿，即時轉換為正式、條理分明的公文或簽呈文稿。

## Constraint
1. 必須**使用 Claude Artifacts 內建的 `window.claude.complete()` API** 直接在瀏覽器前端調用 Claude 大腦，免 API Key、免架設後端伺服器。
2. 需加入環境防呆檢測：若 `!window.claude?.complete`，提示使用者需在 Claude.ai 預覽環境中運行。
3. 介面需包含輸入文字框、轉換按鈕、按鈕 Loading 狀態（思考中動畫）、以及結果呈現區域。

## Format
產出為單一 **HTML Artifact**，可在右側側欄即時預覽與測試。
```

### 📋 實測範例文字（可直接複製貼入「原始文字」框）

當您在右側建立並打開小工具後，可以直接複製以下口語草稿，貼進小工具的「原始文字」框中點擊測試：

#### 範例一：召開跨組專案進度檢討會（會議通知）
```text
各組組長注意一下，下週二下午兩點要在三樓第一會議室開下半年的專案進度檢討會，因為處長會親自出席聽取簡報，請大家務必準時到場，切勿遲到。另外每一組都要準備 10 分鐘以內的 PPT 簡報，把目前進度落後的原因跟接下來的追趕改善計畫講清楚，簡報最晚要在下週一中午前寄給秘書彙整，收到請回信確認。
```

#### 範例二：跨單位業務協調與資料索取（公務簽辦）
```text
資訊科你好，我們業務科最近正在整理全單位的無紙化推動成效報告，需要請你們幫忙撈一下過去半年所有同仁線上簽核的總件數跟平均花費時間數據。因為下週三主管會報長官就要看這份統計圖表，時間有點趕，麻煩你們這週五下班前先匯出一份 Excel 寄給承辦人，非常感謝！
```

> [!TIP]
> **預期潤飾效果**：點擊「✨ 潤飾文字」後，內建的 Claude 會將上述口語文字自動轉化為「主旨、說明（條列要點事項）、擬辦」等專業且合乎行政規範的正式公文格式！

---

### 📝 完整實作程式碼範例


<details>
<summary><b>點擊展開查看完整 HTML 程式碼 (Single File)</b></summary>

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>AI 公文語氣潤飾器</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 24px; max-width: 600px; margin: 0 auto; background: #f8fafc; color: #1e293b; }
    .card { background: white; padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    textarea { width: 100%; height: 100px; border: 1px solid #cbd5e1; border-radius: 8px; padding: 12px; font-size: 14px; box-sizing: border-box; resize: vertical; }
    button { margin-top: 12px; width: 100%; padding: 12px; background: #2563eb; color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer; transition: background 0.2s; }
    button:hover { background: #1d4ed8; }
    button:disabled { background: #94a3b8; cursor: not-allowed; }
    .output-box { margin-top: 16px; padding: 16px; background: #f1f5f9; border-radius: 8px; border-left: 4px solid #2563eb; white-space: pre-wrap; min-height: 50px; font-size: 14px; line-height: 1.6; }
  </style>
</head>
<body>

  <div class="card">
    <h2>📝 公文語氣潤飾助手</h2>
    <p style="color: #64748b; font-size: 13px;">免 API Key・直接調用內建 Claude 大腦</p>
    
    <textarea id="userInput" placeholder="請在此貼上隨手記下的草稿、備忘或口語文字..."></textarea>
    <button id="polishBtn" onclick="polishText()">✨ 開始 AI 潤飾</button>

    <div class="output-box" id="result">潤飾後的正式公文將顯示於此...</div>
  </div>

  <script>
    async function polishText() {
      const input = document.getElementById("userInput").value.trim();
      const resultDiv = document.getElementById("result");
      const btn = document.getElementById("polishBtn");

      if (!input) {
        alert("請先輸入內容！");
        return;
      }

      // 1. 環境檢測防呆：確保在 Claude Artifacts 環境中執行
      if (!window.claude || typeof window.claude.complete !== 'function') {
        resultDiv.innerHTML = "⚠️ <b>環境不支援</b>：本功能依賴 Claude Artifacts 內建環境，請直接在 Claude.ai 預覽視窗中使用。";
        return;
      }

      // 2. 切換載入中狀態
      btn.disabled = true;
      btn.innerText = "⏳ Claude 思考潤飾中...";
      resultDiv.innerText = "正在調用 Claude 處理中...";

      try {
        // 3. 核心呼叫：調用 window.claude.complete
        const prompt = `你是一位專業的繁體中文公文與行政幕僚專家。請將以下口語或粗糙草稿改寫為符合正式公文禮節、條理分明且用詞精準的文稿：\n\n【草稿內容】：\n${input}`;
        const aiResponse = await window.claude.complete(prompt);

        // 4. 呈現生成結果
        resultDiv.innerText = aiResponse;
      } catch (err) {
        resultDiv.innerText = "❌ 處理失敗：" + err.message;
      } finally {
        btn.disabled = false;
        btn.innerText = "✨ 開始 AI 潤飾";
      }
    }
  </script>
</body>
</html>
```

</details>


---

## ❓ 關鍵疑惑：不用 API Key，費用算誰的？會不會收到天價帳單？

許多主管與使用者最擔心的就是費用與配額問題。答案是：**請完全放心！絕對不會產生任何超額帳單，也不會把您的個人額度吃光！**

### 1. 您自己在對話中測試
- **扣款機制**：扣的是您自己 Claude 帳號的**「方案訊息配額（Message Limits）」**。
- 與平常在對話框聊天的額度共用同一個額度池。
- **安心保證**：就算額度用滿，系統只是暫時等待重置，**絕不會自動刷您的信用卡**。

### 2. 同事點開公開分享連結（Publish Link）使用
- **防護機制**：Anthropic 官方設有防護牆，外部訪客**不能**透過公開網址無限消耗原作者的 AI 運算資源。
- **使用者自付配額**：當同事點擊需要 AI 動腦的功能時，系統會要求同事**登入同事自己的 Claude 帳號**，消耗的是**「同事自己的用量配額」**，完全不會算在您頭上！

### 3. 原型展示 vs 正式全公司上線的分工
- **前期原型展示（用 Artifacts）**：供長官檢視、開會驗證、少數同仁試用，**成本 $0 元**。
- **全公司數百人正式上線（改接 API）**：若長官決定全機關正式常態使用，應交由 IT 部門改接官方 **Claude API**，由機關/企業統籌編列雲端預算。

---

← [返回 Artifacts 主手冊](../README.md)
