# ChatGPT 現代職場工作流與生產力實戰全指南

這份講義以 **OpenAI ChatGPT 官方旗艦生態系**（涵蓋 Web 網頁版、macOS / Windows 桌面版與行動版 App 的一般日常圖形介面）為主軸，全面聚焦於職場工作者真實使用的核心能力：**Canvas 雙欄畫布協作**、**Advanced Data Analysis（免寫程式！雲端數據分析與 Office 文件自動生成）**、**Custom Instructions & Memory（個人化與長期記憶）**、**Custom GPTs（零程式碼打造專屬小幫手）**、**Projects 專案空間**、**Deep Research 深度自主研究**、**Voice & Vision（多模態進階語音與視覺辨識）** 以及 **雲端硬碟直連（Connectors）**。

全篇專為一般知識工作者設計，**完全不需寫程式、不需使用終端機（CLI）**。

各單元皆清楚標示適用於 **Free（免費版）**、**Plus（訂閱版）** 或 **Team / Enterprise（團隊企業版）**，方便學員與講師對照使用。

---

## 🎯 方案速覽：Free vs Plus vs Team / Pro

ChatGPT 的方案劃分直接對應功能權限與模型額度。初學者可用 Free 方案完成大部分日常對話、提示詞練習、基礎數據分析與 Canvas 畫布操作；進階職場協作與深度研發則推薦使用 Plus 或 Team 方案。

| 能力與功能模組 | 🟢 Free（免費版） | 🔵 Plus（$20/月） | 🏢 Team / Pro / 企業版 | 本指南章節 |
| :--- | :---: | :---: | :---: | :--- |
| **通用多工模式（快速回覆、多模態）** | ✓（動態額度限制） | ✓（高用量額度） | ✓（極高額度） | [02_Chats](./02_Chats/README.md) |
| **深度思考推理模式（多步邏輯推理）** | ✓（基礎額度） | ✓（充裕額度） | ✓（專屬額度） | [02_Chats](./02_Chats/README.md) |
| **Canvas 雙欄互動畫布** | ✓（已全面開放） | ✓ | ✓ | [03_Canvas](./03_Canvas/README.md) |
| **Custom Instructions & Memory（長期記憶）** | ✓ | ✓ | ✓（Team 可控） | [04_Custom_Instructions_Memory](./04_Custom_Instructions_Memory/README.md) |
| **Advanced Data Analysis（免寫程式數據分析與 Office 產檔）** | ✓（有次數上限） | ✓ | ✓ | [05_Advanced_Data_Analysis](./05_Advanced_Data_Analysis/README.md) |
| **Custom GPTs（零程式碼客製小幫手）** | 可瀏覽與使用 | 可自建、發佈與使用 | 企業內部專屬發佈與共用 | [06_Custom_GPTs](./06_Custom_GPTs/README.md) |
| **Projects（專案資料夾與知識隔離）** | — | — | ✓（Team/Enterprise 標配） | [07_Projects](./07_Projects/README.md) |
| **Web Search（聯網搜尋即時資訊）** | ✓ | ✓ | ✓ | [08_Deep_Research](./08_Deep_Research/README.md) |
| **Deep Research（多步驟自主深度研究）** | — | ✓（每月額度） | ✓（高額度） | [08_Deep_Research](./08_Deep_Research/README.md) |
| **Advanced Voice Mode（進階原生語音模式）** | ✓（每月體驗預覽） | ✓（每日充裕時間） | ✓ | [09_Voice_Vision](./09_Voice_Vision/README.md) |
| **Vision & 桌面畫面共享** | ✓（基礎識圖） | ✓（支援桌面即時畫面） | ✓ | [09_Voice_Vision](./09_Voice_Vision/README.md) |
| **Connected Apps（Google Drive / OneDrive 直連）** | ✓ | ✓ | ✓（管理員控制） | [10_Connectors](./10_Connectors/README.md) |
| **DALL·E 3（商業圖像生成與畫筆局部修圖）** | 限每日 2~3 張 | ✓（高額度日常使用） | ✓ | [11_DALL_E](./11_DALL_E/README.md) |
| **資料隱私保障（不將公務數據用於訓練）** | 需手動關閉歷史紀錄 | 需手動設定關閉 | 預設不參與模型訓練 | [01_Settings](./01_Settings/README.md) |

> 💡 **教學與自學指引**：
> - **學生端**：註冊免費版（Free）即可完整實作 01 ~ 05 單元的所有基礎操作，並可體驗 Canvas 協作、Python 數據分析與多模態影像辨識。
> - **講師端與商務進階**：建議使用 Plus 帳號，以便示範「自建 Custom GPTs 知識庫」、「Deep Research 深度產業報告生成」以及「Advanced Voice Mode 口說情境模擬」。

---

## 🔁 與 Claude_ai 講義之完整功能對照

本教材與本專案同級的 [Claude.ai 實戰全指南](../Claude_ai/README.md) 採用相同的教學層次，方便使用者同時掌握兩大旗艦 AI 平台的異曲同工之妙：

| 職場學習主題 | Claude.ai 對應功能 | ChatGPT 對應功能（本指南） | 核心價值與亮點 |
|---|---|---|---|
| **環境準備與安全** | Settings | [01_Settings](./01_Settings/README.md) | 帳號偏好、關閉資料訓練、桌面版全域快捷鍵（Option+Space） |
| **對話與提示詞架構** | Chats（RTCCF 框架） | [02_Chats](./02_Chats/README.md) | ROSES 與 RTCCF 框架、通用多工 vs 深度思考模式選用 |
| **互動式協作畫布** | Artifacts（側欄動態預覽） | [03_Canvas](./03_Canvas/README.md) | **Canvas** 雙欄畫布：即時反饋、語氣調整、長文精修與版本歷程 |
| **個人化風格與記憶** | Custom Instructions | [04_Custom_Instructions_Memory](./04_Custom_Instructions_Memory/README.md) | 雙區塊自訂指示 + **Memory 長期跨對話記憶庫**管理 |
| **程式運算與檔案生成** | Code Execution（檔案產出） | [05_Advanced_Data_Analysis](./05_Advanced_Data_Analysis/README.md) | **Advanced Data Analysis**：免寫程式，直出圖表與 Word/Excel/PPT/PDF |
| **專屬助理與自訂技能** | Projects + Skills | [06_Custom_GPTs](./06_Custom_GPTs/README.md) | **Custom GPTs**：零程式碼打造專屬小幫手、知識庫 RAG 與外部 API Actions |
| **多專案知識隔離** | Projects（專案沙盒） | [07_Projects](./07_Projects/README.md) | **Projects**：集中管理專案 Chats、共享專案參考文件與自訂 GPTs |
| **深度研究與情報探勘** | Research Mode | [08_Deep_Research](./08_Deep_Research/README.md) | **Deep Research**：自主規劃多輪網路搜尋、交叉驗證數十個網站之綜合報告 |
| **多模態互動與語音** | — | [09_Voice_Vision](./09_Voice_Vision/README.md) | **Advanced Voice Mode** 原生端到端情感語音 + 螢幕即時視覺共享 |
| **外部雲端硬碟整合** | Connectors（Google/Notion）| [10_Connectors](./10_Connectors/README.md) | 直連 Google Drive 與 OneDrive，免下載手動搬運檔案 |
| **視覺素材與圖表生成** | SVG / Mermaid 生成 | [11_DALL_E](./11_DALL_E/README.md) | **DALL·E 3**：商業簡報插圖、品牌視覺概念與畫筆局部重繪（Inpainting） |

---

## 📚 核心章節導覽

### ⚙️ [01. Settings（環境準備、隱私與安全）](./01_Settings/README.md) — Free / Plus
> 上課第一步：介面語言、深淺主題切換、多因子驗證（2FA）。**公務機密防護關鍵**：如何在 Data Controls 中關閉「改善所有人的模型」，並在 macOS / Windows 安裝桌面版 App，設定 `Option + Space` 全域快捷叫出對話懸浮窗。

### 🟢 [02. Chats（對話、思考模式與提示詞工程）](./02_Chats/README.md) — Free / Plus
> 掌握 ChatGPT 兩大運算模式：**通用多工旗艦模式**（日常文案、郵件、多模態圖片/檔案處理）與 **深度思考推理模式（Reasoning）**（專注於複雜邏輯、合規審查與決策推演）。掌握職場必備 **ROSES 框架**（Role, Objective, Scenario, Expected Outcome, Steps），輕鬆應對複雜商務溝通。

### 🎨 [03. 討論方式的內容生成：Canvas 畫布協作](./03_Canvas/README.md) — Free / Plus
> **討論式內容生成的 ChatGPT 專屬解法**！核心實作心法：**必須先產生 Markdown 檔案進入右側獨立畫布，人機才能在畫布上進行行內劃重點反饋、調整長度、自動潤稿與反覆打磨，確認定稿後再一鍵下載 Word/Excel/PPT/PDF**！

### 🧠 [04. Custom Instructions & Memory（個人化設定與長期記憶）](./04_Custom_Instructions_Memory/README.md) — Free / Plus
> 讓 ChatGPT 成為懂你的專屬秘書。精準設定 Custom Instructions 的兩大區塊（你的背景與期待的回覆格式）；解密 ChatGPT 的 **Memory（記憶）機制**，學會如何查詢、手動注入、單筆刪除與重置長期記憶，避免資訊混淆。

### 📊 [05. Advanced Data Analysis（免寫程式！數據分析與文件自動化生成）](./05_Advanced_Data_Analysis/README.md) — Free / Plus
> 免安裝本機 Python，由 ChatGPT 在雲端沙盒直接執行運算。實作銷售數據清洗、樞紐分析、產出頂級商業圖表，並直接生成正式 **Word (.docx)**、**Excel (.xlsx)**、**簡報 (.pptx)** 與 **PDF** 供一鍵下載！

### 🤖 [06. Custom GPTs（零程式碼自訂專屬 AI 助理）](./06_Custom_GPTs/README.md) — Free（使用）/ Plus（自建）
> 打造客製化 GPT 助理：設定核心 System Prompt、上傳專業內部規章知識庫（Knowledge Files / RAG）、開啟 Web Search / Code Interpreter / DALL·E 權限，並可一鍵分享給同事或發布至 GPT Store。

### 📁 [07. Projects（專案資料夾與團隊協作）](./07_Projects/README.md) — Team / Enterprise / Plus
> 擺脫混亂的歷史對話列表！建立專案獨立空間，將同一個客戶、產品線或專案的所有對話、參考文檔與專用 GPTs 統一納管，實現跨對話知識共享與團隊隔離。

### 🔍 [08. Deep Research（即時搜尋與多步驟深度研究代理）](./08_Deep_Research/README.md) — Free（搜尋）/ Plus（深度研究）
> 從單純的「問答」進化為「委託研究」。學習 SearchGPT 的聯網即時檢索與來源查核；進一步掌握 **Deep Research**：AI 會自主規劃多輪搜索路徑、查閱數十個學術與產業網站、交叉驗證數據，產出長達數萬字、附帶完整引用的專業調研報告。

### 🎙️ [09. Voice & Vision（進階語音對話與視覺多模態）](./09_Voice_Vision/README.md) — Free / Plus
> 體驗 **Advanced Voice Mode**：具有自然情緒語調、笑聲、即時打斷機能的端到端語音對話，能扮演英文商務口說教練或模擬客戶面試。搭配手機與桌面版拍照與螢幕共享（Vision），實現手寫筆記秒轉文字、白板草圖即時辨識。

### 🔗 [10. Connectors（雲端硬碟直連與外部應用串接）](./10_Connectors/README.md) — Free / Plus / Team
> 告別繁瑣的手動下載上傳！設定 ChatGPT 直接連接 Google Drive 與 Microsoft OneDrive，對雲端試算表與簡報進行跨檔案綜合分析。

### 🖼️ [11. DALL·E 3（商業視覺生成與局部重繪）](./11_DALL_E/README.md) — Plus
> 掌握精準的圖像生成 Prompt 語法，生成商業報告插圖、行銷社群貼圖與概念視覺；善用內建「畫筆工具（Inpainting）」進行局部選取重繪，無痕替換畫面物件或修飾細節。

---

## 🧪 實戰練習與輔助資源

- 🛠️ **[學生實戰工作坊（student-lab）](./student-lab/README.md)**：包含「綠色智慧家電上市推廣案」完整實作專案，整合市場調研、Canvas 文案協作、免寫程式數據分析報表生成與專屬客服 GPT 建立。
- 🚨 **[常見疑難排查（Troubleshooting）](./Troubleshooting/README.md)**：模型額度控制、聯網異常、檔案解析失敗、幻覺矯正與資料安全避坑指南。
- 🧰 **[輔助工具與維護腳本（tools）](./tools/README.md)**：包含架構驗證腳本與示範數據。

---

← [返回專案首頁](../README.md)
