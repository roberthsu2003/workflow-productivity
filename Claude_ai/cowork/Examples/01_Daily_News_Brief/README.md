# 📰 範例 1：每日產業情報與競品自動彙整工作流

> 🟢 **適用方案**：Max / Pro / Team / Enterprise (Cowork Beta)  
> 💼 **適用角色**：創投分析師、行銷企劃、市場研究員、行政祕書。  
> 🎯 **核心體驗**：學員完全不需要寫程式，只需上傳監測目標，Cowork 即可自主檢索網路新聞、過濾雜訊、套用樣板產出晨報，並可設定每日定時排程。

---

## 📁 練習檔說明 (`sample_files/`)

進行本練習前，請先下載並查看本資料夾下的練習檔案：
1. [industry_keywords.txt](./sample_files/industry_keywords.txt)：包含學員關注的產業關鍵字與剔除條件（如智慧醫療、AI 認證、創投趨勢）。
2. [daily_news_template.md](./sample_files/daily_news_template.md)：晨報產出的標準 Markdown 格式樣板。

---

## 🤖 Cowork RTCCF 實戰 Prompt

將以下 Prompt 複製至 Cowork 視窗中（並上傳上述兩份練習檔）：

```text
【Role】
你是一名專職的科技產業情報與創投競品分析師。

【Task】
請根據我上傳的 industry_keywords.txt 中的關鍵字與監測目標，搜尋最新 24 小時內的產業新聞與市場動態。過濾剔除公關炒作稿後，將重點摘要填入 daily_news_template.md 樣板中，產出一份「每日產業情報與競品趨勢簡報」。

【Context】
- 上傳檔案 1：industry_keywords.txt (關鍵字與過濾條件)
- 上傳檔案 2：daily_news_template.md (輸出格式樣板)

【Constraint】
- 新聞必須為最新 24 小時內發布之內容。
- 數據與事實須 100% 精準，附上來源網站連結。
- 依據影響力標示 🔴 高 (重大融資/法規突破)、🟡 中 (產品更新)、🟢 標準 (一般市場動態)。
- 使用繁體中文輸出。

【Format】
完全套用 daily_news_template.md 樣板格式。
```

---

## 🚀 學員操作 3 步驟

1. **開啟 Cowork**：登入 [claude.ai](https://claude.ai) 點選切換至 **Cowork** 工作空間。
2. **上傳檔案與貼上 Prompt**：將 `industry_keywords.txt` 與 `daily_news_template.md` 拖入對話框，貼上上述 RTCCF Prompt。
3. **啟動或設定定時排程**：
   - 點選執行：觀看 Cowork 自主搜尋網路並填入 Markdown 晨報。
   - 點選排程 (Schedule)：設定「每工作日早上 08:30 自動執行」，以後每天上班前就能在雲端自動收到新鮮晨報！

---

← [返回 Cowork 主頁](../../README.md) | 🏠 [返回專案總首頁](../../../README.md)
