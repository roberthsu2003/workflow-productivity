# 9-2 AI 產出之 HTML 與 CSS 網格排版生成提示詞

> 🏆 **本單元核心觀念**：**為什麼「HTML/CSS 網頁技術」是 AI 製作商業資訊圖表的最佳引擎？**  
> 告別傳統繪圖軟體微調像素的繁瑣，讓 AI 在後台利用現代網頁排版標準（Flexbox / Grid），精確建構出零跑版、高保真的戰情看板！

---

## 💡 為什麼要用 HTML/CSS 來繪製資訊圖表？

許多人好奇：「資訊圖表不是用 PPT 或 Photoshop 做的嗎？為什麼要寫成網頁 HTML/CSS？」  
在 AI 自動化領域，**HTML/CSS 是全世界最強大的圖表渲染引擎**：

1. **容器與網格（Grid / Flexbox）天生防跑版**：  
   在 PPT 中拉方塊容易因文字長度不同而歪斜；但 HTML 的 `display: flex` 與 `grid-cols-2` 能保證兩張卡片永遠絕對對齊、比例完美 1:1。
2. **顏色、圓角與陰影極致細膩**：  
   CSS 支援精準的色碼（如 `#0B2545`）、圓角（`border-radius: 12px`）與微陰影（`box-shadow`），能輕易做出高級商務 UI 質感。
3. **長條圖百分比直接程式化**：  
   長條圖的長度不需要手動拉，直接在 CSS 中寫入 `style="width: 78%;"`，就能以數學級的精準度呈現真實數據！

---

## 📋 HTML/CSS 視覺重構提示詞（傳送給 AI 執行）

若需要讓 AI 生成乾淨獨立的 HTML/CSS 視覺頁面，可直接使用以下提示詞：

```text
請擔任資深前端視覺設計師，依據我上傳的《參考範本_看板2_量價走勢與YoY.jpg》以及 Excel 數據，產出一份獨立完整的單一 HTML 檔案（內嵌 TailwindCSS 與 Chart.js）：

【版面規格要求】
1. 畫布尺寸：設定為固定寬度 1920px、高度 1080px（標準 16:9 高清比例），背景為白色與淺灰色（#F5F7FA）。
2. 頂部 Header：
   - 包含深海藍色橫幅、星嵐大飯店標題與「2026年 1-8月 訂房成效分析 By Book Day (Actual A)」。
   - 右側保留手寫金色標語「More Than A Stay」。
3. 中間雙看板佈局（並排兩大白色卡片）：
   - 左卡片【圖表 1 | 2026年 1-8月 Actual(A) 訂房表現】：繪製間數（藍色折線）與營收（紅色折線）之雙軸走勢圖。
   - 右卡片【圖表 2 | 2025 vs 2026 訂房表現 (1-8月)】：繪製間數與營收之對比柱狀圖，並在上方標註紅色彩帶標籤「+50.5%」與「+56.7%」。
4. 底部重點指標條：
   - 放置 3 個指標區塊：累計訂房間數（1,562 間）、累計營業收入（890 萬元）、文字結論分析。
5. 底部 Footer：
   - 深海藍色橫條，標註星嵐大飯店 Logo 與品牌口號「美好，從星嵐開始」。

請產出完整的 HTML 原始碼！
```

---

## 🎨 AI 轉換後的 HTML/CSS 骨架範例（秒懂排版邏輯）

學生不需要親自手寫這段代碼，AI 在後台會自動組裝出如下乾淨結構：

```html
<!-- 1920x1080 滿版畫布 -->
<div class="w-[1920px] h-[1080px] bg-gray-50 flex flex-col justify-between font-sans">
  
  <!-- 頂部品牌 Header -->
  <header class="bg-[#0B2545] text-white px-12 py-6 flex justify-between items-center">
    <div class="flex items-center space-x-4">
      <img src="logo.png" class="h-10" />
      <h1 class="text-3xl font-bold">2026年 1-8月 訂房成效分析</h1>
    </div>
    <span class="text-[#C5A880] italic text-2xl font-serif">More Than A Stay</span>
  </header>

  <!-- 中間內容：雙欄卡片 Grid -->
  <main class="grid grid-cols-2 gap-8 px-12 py-6 flex-1">
    <!-- 左卡片：量價雙軸走勢圖 -->
    <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
      <h2 class="text-xl font-bold text-[#0B2545] border-b pb-3">圖表 1 | 2026年1-8月 訂房表現</h2>
      <div id="chart-left" class="h-80">...雙軸折線圖...</div>
    </div>

    <!-- 右卡片：YoY 對比柱狀圖 -->
    <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
      <h2 class="text-xl font-bold text-[#0B2545] border-b pb-3">圖表 2 | 2025 vs 2026 比較</h2>
      <div id="chart-right" class="h-80">...YoY 長條圖...</div>
    </div>
  </main>

  <!-- 底部品牌 Footer -->
  <footer class="bg-[#0B2545] text-gray-300 px-12 py-4 text-sm flex justify-between">
    <span>STARSHORE HOTEL 星嵐大飯店</span>
    <span>美好，從星嵐開始</span>
  </footer>
</div>
```

此網頁結構完成後，緊接著就能交由下一步的**無頭瀏覽器**進行全自動拍照截圖！
