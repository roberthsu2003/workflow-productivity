# 01. Settings（環境準備、隱私與安全）

> 🟢 **適用方案**：Free / Plus / Team / Enterprise 全方案適用

上課與日常使用的第一步，就是確保 ChatGPT 的操作環境符合個人使用習慣，並落實公務情境中的**資料隱私與機密防護**。

---

## 🛡️ 公務必讀：資料控制（Data Controls）與隱私防護

在公務或商業環境中使用 AI 工具，最關鍵的第一步就是**防止商業敏感數據被用於模型再訓練**。

### 1. 關閉「改善所有人的模型（Improve the model for everyone）」
- **操作路徑**：點擊左下角頭像（或個人名稱）→ **Settings（設定）** → **Data Controls（資料控制）**。
- **關鍵設定**：
  - **Improve the model for everyone**：請將此選項**關閉（Off）**。
  - 關閉後，您的對話內容與上傳檔案將不會被 OpenAI 用於訓練未來的新模型，確保您的公務提問與內部資料安全。
  - *附註*：若您使用的是 **ChatGPT Team / Enterprise** 企業方案，OpenAI 預設即承諾不會使用任何商業對話與文件訓練模型。

### 2. 臨時對話（Temporary Chat）
- 若您臨時需要處理一份極度機敏的草稿或進行一次性試算，可開啟「Temporary Chat（臨時對話）」。
- 該模式下的對話不會出現在歷史紀錄中，不會被用於訓練模型，也不會觸發 Memory（長期記憶）的更新。

### 3. 匯出與清除對話（Export & Clear Chats）
- 在 Data Controls 介面中，可點擊 **Export data**，系統會將帳號內的所有對話紀錄打包成 JSON 與 HTML 檔案發送至您的信箱。
- 可選擇 **Delete account**（刪除帳號）或清空特定對話歷史。

---

## 🎨 外觀、語言與個人化設定

### 1. 外觀主題與語言偏好
- **Theme（主題）**：支援 Dark（深色模式）、Light（淺色模式）或 System（跟隨作業系統設定），長時間閱讀建議使用深色模式保護視力。
- **Language（語言）**：支援繁體中文（繁體中文），切換後介面按鈕與系統提示將以繁體中文顯示。

### 2. 帳號安全防護：多因子驗證（2FA）
- 進入 **Settings** → **Security**。
- 開啟 **Two-Factor Authentication (2FA)**，使用 Google Authenticator 或 1Password 等驗證器 App 掃描 QR Code，避免帳號因密碼外洩而遭到盜用。

---

## 💻 ChatGPT 桌面版（Desktop App）高效操作秘技

OpenAI 推出了專為 **macOS** 與 **Windows** 設計的 ChatGPT 官方桌面應用程式，具備瀏覽器網頁版無法比擬的極致工作流體驗：

### 1. 全域快捷對話懸浮窗（Option + Space）
- 在 macOS 上按下快捷鍵 `Option + Space`（Windows 為 `Alt + Space`），即可在任何工作畫面正中央叫出隨行對話框。
- 閱讀長篇 PDF、撰寫郵件或查閱網頁時，免切換視窗，隨時隨地按下快捷鍵提問或翻譯，使用完畢直接按下 `Esc` 縮回。

### 2. 螢幕畫面選取與即時提問（Take Screenshot / Screen Share）
- 在桌面版對話框內點擊迴紋針圖示，選擇 **Take Screenshot**，可自由圈選當前螢幕任一區域（如複雜的圖表、報錯視窗、設計草圖），ChatGPT 會立即針對截圖進行視覺分析。

### 3. 伴隨模式（Companion Window）
- 可將 ChatGPT 視窗設定為「置頂於其他視窗之上」，方便一邊撰寫報告，一邊隨時參考 AI 整理的要點。

---

## 📋 上課前自我檢查清單（Checklist）

在進入後續章節練習前，請確認您已完成以下檢查：

- [ ] 已在 **Data Controls** 確認關閉模型訓練選項（或使用 Team/Enterprise 企業帳號）。
- [ ] 已將介面語言切換為習慣之語言。
- [ ] 已完成 2FA 雙因子安全驗證。
- [ ] （推薦）已下載安裝 ChatGPT 官方桌面版 App，並成功使用快捷鍵呼叫出懸浮對話框。

---

← [上一章：架構總覽](../ARCHITECTURE.md) ｜ [下一章：02. Personalization 個人化設定與長期記憶 →](../02_Personalization/README.md)
