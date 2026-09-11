# ChatGPT 現代職場工作流與生產力實戰全指南

這份講義以 **OpenAI ChatGPT 官方旗艦生態系**（涵蓋 Web 網頁版、macOS / Windows 桌面版與行動版 App 的一般日常圖形介面）為主軸，全面聚焦於職場工作者真實使用的核心能力：**Canvas 雙欄畫布協作**、**Advanced Data Analysis（免寫程式！雲端數據分析與 Office 文件自動生成）**、**Custom Instructions & Memory（個人化與長期記憶）**、**Custom GPTs（零程式碼打造專屬小幫手）**、**Projects 專案空間**、**Deep Research 深度自主研究**、**Voice & Vision（多模態進階語音與視覺辨識）** 以及 **雲端硬碟直連（Connectors）**。

全篇專為一般知識工作者設計，**完全不需寫程式、不需使用終端機（CLI）**。

各單元皆清楚標示適用於 **Free（免費版）**、**Plus（訂閱版）** 或 **Team / Enterprise（團隊企業版）**，方便學員與講師對照使用。

---

## 🎯 方案速覽：Free vs Plus vs Team / Pro

ChatGPT 的方案劃分直接對應功能權限與模型額度。初學者可用 Free 方案完成大部分日常對話、提示詞練習、基礎數據分析與 Canvas 畫布操作；進階職場協作與深度研發則推薦使用 Plus 或 Team 方案。

| 能力與功能模組 | 🟢 Free（免費版） | 🔵 Plus（$20/月） | 🏢 Team / Pro / 企業版 | 本指南章節 |
| :--- | :---: | :---: | :---: | :--- |
| **個人化風格、特質微調與長期記憶** | ✓ | ✓ | ✓（Team 可控） | [02_Personalization](./02_Personalization/README.md) |
| **Canvas 雙欄互動畫布** | ✓（已全面開放） | ✓ | ✓ | [03_Canvas](./03_Canvas/README.md) |
| **Advanced Data Analysis（免寫程式數據分析與 Office 產檔）** | ✓（有次數上限） | ✓ | ✓ | [05_Advanced_Data_Analysis](./05_Advanced_Data_Analysis/README.md) |
| **Custom GPTs（零程式碼客製小幫手）** | 可瀏覽與使用 | 可自建、發佈與使用 | 企業內部專屬發佈與共用 | [06_Custom_GPTs](./06_Custom_GPTs/README.md) |
| **Projects（專案資料夾與知識隔離）** | — | — | ✓（Team/Enterprise 標配） | [07_Projects](./07_Projects/README.md) |
| **Web Search（聯網搜尋即時資訊）** | ✓ | ✓ | ✓ | [08_Deep_Research](./08_Deep_Research/README.md) |
| **Deep Research（多步驟自主深度研究）** | — | ✓（每月額度） | ✓（高額度） | [08_Deep_Research](./08_Deep_Research/README.md) |
| **Advanced Voice Mode（進階原生語音模式）** | ✓（每月體驗預覽） | ✓（每日充裕時間） | ✓ | [09_Voice_Vision](./09_Voice_Vision/README.md) |
| **Vision & 桌面畫面共享** | ✓（基礎識圖） | ✓（支援桌面即時畫面） | ✓ | [09_Voice_Vision](./09_Voice_Vision/README.md) |
| **Connected Apps（Google Drive / OneDrive 直連）** | ✓ | ✓ | ✓（管理員控制） | [10_Connectors](./10_Connectors/README.md) |
| **ChatGPT Images 2.5（圖像生成、草圖與精準批註修圖）** | ✓（基礎體驗額度） | ✓（高額度日常使用） | ✓ | [11_Images](./11_Images/README.md) |
| **資料隱私保障（不將公務數據用於訓練）** | 需手動關閉歷史紀錄 | 需手動設定關閉 | 預設不參與模型訓練 | [01_Settings](./01_Settings/README.md) |

> 💡 **教學與自學指引**：
> - **學生端**：註冊免費版（Free）即可完整實作 01 ~ 03、05 單元的所有基礎操作，並可體驗個人化設定、Canvas 協作、Python 數據分析與多模態影像辨識。
> - **講師端與商務進階**：建議使用 Plus 帳號，以便示範「自建 Custom GPTs 知識庫」、「Deep Research 深度產業報告生成」以及「Advanced Voice Mode 口說情境模擬」。

---

## 🔁 與 Claude_ai 講義之完整功能對照

本教材與本專案同級的 [Claude.ai 實戰全指南](../Claude_ai/README.md) 採用相同的教學層次，方便使用者同時掌握兩大旗艦 AI 平台的異曲同工之妙：

| 職場學習主題 | Claude.ai 對應功能 | ChatGPT 對應功能（本指南） | 核心價值與亮點 |
|---|---|---|---|
| **環境準備與安全** | Settings | [01_Settings](./01_Settings/README.md) | 帳號偏好、關閉資料訓練、桌面版全域快捷鍵（Option+Space） |
| **個人化風格與長期記憶** | Custom Instructions | [02_Personalization](./02_Personalization/README.md) | 最新風格與特質微調（溫暖/熱情/排版/Emoji）、夥伴、關於你 + **Memory 長期跨對話記憶庫** |
| **互動式協作畫布** | Artifacts（側欄動態預覽） | [03_Canvas](./03_Canvas/README.md) | **Canvas** 雙欄畫布：即時反饋、語氣調整、長文精修與版本歷程 |
| **程式運算與檔案生成** | Code Execution（檔案產出） | [05_Advanced_Data_Analysis](./05_Advanced_Data_Analysis/README.md) | **Advanced Data Analysis**：免寫程式，直出圖表與 Word/Excel/PPT/PDF |
| **專屬助理與自訂技能** | Projects + Skills | [06_Custom_GPTs](./06_Custom_GPTs/README.md) | **Custom GPTs**：零程式碼打造專屬小幫手、知識庫 RAG 與外部 API Actions |
| **多專案知識隔離** | Projects（專案沙盒） | [07_Projects](./07_Projects/README.md) | **Projects**：集中管理專案 Chats、共享專案參考文件與自訂 GPTs |
| **深度研究與情報探勘** | Research Mode | [08_Deep_Research](./08_Deep_Research/README.md) | **Deep Research**：自主規劃多輪網路搜尋、交叉驗證數十個網站之綜合報告 |
| **多模態互動與語音** | — | [09_Voice_Vision](./09_Voice_Vision/README.md) | **Advanced Voice Mode** 原生端到端情感語音 + 螢幕即時視覺共享 |
| **外部雲端硬碟整合** | Connectors（Google/Notion）| [10_Connectors](./10_Connectors/README.md) | 直連 Google Drive 與 OneDrive，免下載手動搬運檔案 |
| **視覺素材與圖表生成** | SVG / Mermaid 生成 | [11_Images](./11_Images/README.md) | **ChatGPT Images 2.5**：側欄專屬空間、@Sketch 草圖生成、商業範本與 Comments 精準批註修圖 |

---

## 📚 核心章節導覽

### ⚙️ [01. Settings（環境準備、隱私與安全）](./01_Settings/README.md) — Free / Plus
> 上課第一步：介面語言、深淺主題切換、多因子驗證（2FA）。**公務機密防護關鍵**：如何在 Data Controls 中關閉「改善所有人的模型」，並在 macOS / Windows 安裝桌面版 App，設定 `Option + Space` 全域快捷叫出對話懸浮窗。

### 🧠 [02. Personalization（個人化設定、特質微調與長期記憶）](./02_Personalization/README.md) — Free / Plus
> 打造最懂你的專屬副駕！深入 2026 最新「個人化」面板：自訂**基準風格和語氣**（專業/友善/直率）、微調**細部特質**（溫暖度、熱情度、標題列表排版、Emoji）、選擇**協作夥伴**並填寫**關於你**（稱呼、職業、價值觀）；靈活控制**快速回覆**與**進階功能開關**（網頁搜尋、畫布、語音、檔案庫、連接器），並善用 **自訂指令（Custom Instructions）** 與 **Memory 長期記憶庫**（查詢、注入、單筆刪除與臨時對話保護）。

### 🎨 [03. 討論方式的內容生成：Canvas 畫布協作](./03_Canvas/README.md) — Free / Plus
> **討論式內容生成的 ChatGPT 專屬解法**！核心實作心法：**必須先產生 Markdown 檔案進入右側獨立畫布，人機才能在畫布上進行行內劃重點反饋、調整長度、自動潤稿與反覆打磨，確認定稿後再一鍵下載 Word/Excel/PPT/PDF**！

### 📊 [05. Advanced Data Analysis（免寫程式！數據分析與文件自動化生成）](./05_Advanced_Data_Analysis/README.md) — Free / Plus
> 免安裝本機 Python，由 ChatGPT 在雲端沙盒直接執行運算。實作銷售數據清洗、樞紐分析、產出頂級商業圖表，並直接生成正式 **Word (.docx)**、**Excel (.xlsx)**、**簡報 (.pptx)** 與 **PDF** 供一鍵下載！

### 🤖 [06. Custom GPTs（零程式碼自訂專屬 AI 助理）](./06_Custom_GPTs/README.md) — Free（使用）/ Plus（自建）
> 打造客製化 GPT 助理：設定核心 System Prompt、上傳專業內部規章知識庫（Knowledge Files / RAG）、開啟 Web Search / Code Interpreter / 圖像生成（Images）權限，並可一鍵分享給同事或發布至 GPT Store。

### 📁 [07. Projects（專案資料夾與團隊協作）](./07_Projects/README.md) — Team / Enterprise / Plus
> 擺脫混亂的歷史對話列表！建立專案獨立空間，將同一個客戶、產品線或專案的所有對話、參考文檔與專用 GPTs 統一納管，實現跨對話知識共享與團隊隔離。

### 🔍 [08. Deep Research（即時搜尋與多步驟深度研究代理）](./08_Deep_Research/README.md) — Free（搜尋）/ Plus（深度研究）
> 從單純的「問答」進化為「委託研究」。學習 SearchGPT 的聯網即時檢索與來源查核；進一步掌握 **Deep Research**：AI 會自主規劃多輪搜索路徑、查閱數十個學術與產業網站、交叉驗證數據，產出長達數萬字、附帶完整引用的專業調研報告。

### 🎙️ [09. Voice & Vision（進階語音對話與視覺多模態）](./09_Voice_Vision/README.md) — Free / Plus
> 體驗 **Advanced Voice Mode**：具有自然情緒語調、笑聲、即時打斷機能的端到端語音對話，能扮演英文商務口說教練或模擬客戶面試。搭配手機與桌面版拍照與螢幕共享（Vision），實現手寫筆記秒轉文字、白板草圖即時辨識。

### 🔗 [10. Connectors（雲端硬碟直連與外部應用串接）](./10_Connectors/README.md) — Free / Plus / Team
> 告別繁瑣的手動下載上傳！設定 ChatGPT 直接連接 Google Drive 與 Microsoft OneDrive，對雲端試算表與簡報進行跨檔案綜合分析。

### 🖼️ [11. ChatGPT Images 2.5（圖像生成、草圖與精準批註修圖）](./11_Images/README.md) — Free / Plus
> 側邊欄全新專屬「圖像」入口！體驗生成速度提升 50% 的飛躍進化；善用 **@Sketch 手繪草圖** 直接勾勒版面構圖、套用 **Templates 商務範本**，並透過 **Comments 區域批註** 在圖片特定位置精準微調，維持跨輪次超高畫面一致性。

---

## 🧪 實戰練習與輔助資源

- 🛠️ **[學生實戰工作坊（student-lab）](./student-lab/README.md)**：包含「綠色智慧家電上市推廣案」完整實作專案，整合市場調研、Canvas 文案協作、免寫程式數據分析報表生成與專屬客服 GPT 建立。
- 🚨 **[常見疑難排查（Troubleshooting）](./Troubleshooting/README.md)**：模型額度控制、聯網異常、檔案解析失敗、幻覺矯正與資料安全避坑指南。
- 🧰 **[輔助工具與維護腳本（tools）](./tools/README.md)**：包含架構驗證腳本與示範數據。

---

← [返回專案首頁](../README.md)
