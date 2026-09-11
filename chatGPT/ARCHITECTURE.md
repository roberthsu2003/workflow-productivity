# ChatGPT 講義架構與學習地圖（一般人日常生產力介面）

本目錄專為 **ChatGPT 現代職場工作流與一般人生產力應用** 量身打造，徹底摒除任何終端機命令（CLI）與寫程式碼的內容，全面回歸一般人在瀏覽器網頁版、桌面版與手機 App 使用的官方圖形化介面。架構對標 `Claude_ai` 的學習進階階梯，引導學員從基礎設定一路晉升至進階多模態與客製化 AI 助理。

---

## 🗺️ 目錄架構一覽

```text
chatGPT/
├── README.md                          # 全教材入口、方案速覽、與 Claude_ai 對照表
├── ARCHITECTURE.md                    # 架構設計、學習進階路徑與模組清單（本文件）
├── 00_Free_Desktop_vs_Web/            # 學生免費版通關指南：桌面版 vs 網頁版額度機制與省額心法
├── 01_Settings/                       # 帳號偏好、隱私安全、資料控制與桌面版快捷操作
├── 02_Personalization/                # 個人化設定（風格語氣/特質/夥伴/關於你）、自訂指令與長期記憶
├── 03_Canvas/                         # Canvas 畫布：雙欄協作、劃記精修、長文寫作與潤飾
├── 05_Advanced_Data_Analysis/         # 免寫程式！數據分析、商務圖表繪製、直接產出 Word/Excel/PPT
│   └── sample_data/                   # 示範銷售與營運數據集（CSV）
├── 06_Custom_GPTs/                    # 零程式碼打造專屬小幫手、知識庫 RAG、分享與發佈
│   └── templates/                     # 實務專用 Prompt 範本庫（公文審查、行銷企劃教練）
├── 07_Projects/                       # ChatGPT 專案資料夾、知識庫集中管理與協作
├── 08_Deep_Research/                  # 即時聯網搜尋（Web Search）+ 多步驟深度研究（Deep Research）
├── 09_Voice_Vision/                   # Advanced Voice Mode 進階語音情境模擬 + 視覺拍照與螢幕辨識
├── 10_Connectors/                     # Google Drive / OneDrive 雲端硬碟直連與跨檔分析
├── 11_Images/                         # ChatGPT Images 2.5 圖像生成、@Sketch 草圖、範本與 Comments 批註修圖
├── student-lab/                       # 學生綜合實戰工作坊（全套綠色家電上市推廣案實做）
│   └── materials/                     # 實作情境與配套素材
├── Troubleshooting/                   # 常見疑難排查（額度上限、聯網異常、解析失敗、幻覺矯正）
└── tools/                             # 輔助維護與測試數據工具
```

---

## 📈 三階段學習路徑

```mermaid
graph TD
    subgraph Phase 1: 基礎核心（所有方案均可上手）
        PRE[00_Free_Desktop_vs_Web<br>免費版桌面 vs 網頁額度心法] --> A[01_Settings<br>隱私安全與桌面版快捷鍵]
        A --> B[02_Personalization<br>個人化風格特質與長期記憶]
        B --> C[03_Canvas<br>畫布人機協作精修長文]
    end

    subgraph Phase 2: 生產力倍增（數據分析與客製化）
        C --> E[05_Advanced_Data_Analysis<br>免寫程式！數據分析與產出 Office]
        B --> F[06_Custom_GPTs<br>零程式碼專屬助理與知識庫]
        B --> G[10_Connectors<br>直連雲端硬碟 Google Drive/OneDrive]
    end

    subgraph Phase 3: 旗艦進階（深度研究、多模態與協作）
        E --> H[07_Projects<br>專案空間集中管理]
        F --> I[08_Deep_Research<br>多步驟深度自主研究代理]
        B --> J[09_Voice_Vision<br>進階語音口說演練與螢幕辨識]
        B --> K[11_Images<br>Images 2.5 圖像生成與批註修圖]
    end

    subgraph 綜合實戰檢驗
        H & I & E & F --> L[student-lab<br>新產品上市綜合專案演練]
    end
```

---

## 🎯 學習成果與能力指標

完成本系列講義學習後，學員將具備以下能力：

1. **資訊安全與隱私防護能力**：清楚知道如何在公務情境中正確關閉資料訓練授權，安全處理公務資料。
2. **高效提示詞架構能力**：熟練掌握 **ROSES 框架**，能在 3 分鐘內引導 ChatGPT 產出結構清晰、符合商務標準的高品質產出。
3. **極致人機協作效率**：善用 **Canvas 雙欄畫布** 進行劃記修改，徹底告別「整篇重新生成」的等待浪費。
4. **數據分析與報表自動產出**：利用 **Advanced Data Analysis**，完全不需懂程式碼，就能自動清洗 Excel 資料，並一鍵產出格式完整的 Word、Excel、PowerPoint 或 PDF 檔案。
5. **打造個人與團隊專屬助理**：運用 **Custom GPTs**，零程式碼將內部 SOP、產品規格書或政策手冊轉化為 24 小時在線的智能專屬專家。
6. **深度調研與決策支援**：善用 **Deep Research** 與即時 Web Search，在數十分鐘內取得詳盡、具真實來源引證的專業產業分析報告。

---

← [返回教材首頁](./README.md)
