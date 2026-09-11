# ChatGPT 講義架構與學習地圖（三大主題核心體系）

本目錄專為 **ChatGPT 現代職場工作流與一般人生產力應用** 量身打造，徹底摒除任何終端機命令（CLI）與寫程式碼的內容，全面回歸一般人在瀏覽器網頁版、桌面版與手機 App 使用的官方圖形化介面。

全套教材劃分為**三大核心主題**：
1. **主題一：有關於設定和付費機制**
2. **主題二：功能面（基礎免費核心 vs 付費專屬進階）**
3. **主題三：實際範例與綜合實戰**

---

## 🗺️ 目錄架構一覽

```text
chatGPT/
├── README.md                              # 全教材入口、三大主題導覽、方案速覽與功能對照表
├── ARCHITECTURE.md                        # 架構設計、學習進階路徑與模組清單（本文件）
│
├── [主題一：設定和付費機制]
│   ├── 00_Free_Desktop_vs_Web/            # 學生免費版通關指南：桌面版 vs 網頁版額度機制與省額心法
│   ├── 01_Settings/                       # 帳號偏好、隱私安全、資料控制與桌面版快捷操作
│   └── 02_Personalization/                # 個人化設定（風格語氣/特質/夥伴/關於你）、自訂指令與長期記憶
│
├── [主題二：功能面]
│   ├── 03_Canvas/                         # Canvas 畫布：雙欄協作、劃記精修、長文寫作與潤飾
│   ├── 04_Chats/                          # Chats 對話思維、提問架構與追問心法
│   ├── 05_Advanced_Data_Analysis/         # 免寫程式！數據分析、商務圖表繪製、直接產出 Word/Excel/PPT
│   │   └── sample_data/                   # 示範銷售與營運數據集（CSV）
│   ├── 06_Work/                           # 桌面版 Work 工作模式：本機資料夾對接與任務成果交付
│   ├── 07_Projects/                       # ChatGPT 專案資料夾、知識庫集中管理與協作
│   ├── 08_Connectors/                     # Google Drive / OneDrive 雲端硬碟直連與跨檔分析
│   ├── 09_Plugins/                        # 外掛程式生態（Wolfram / Expedia / Zapier 等外部工具）
│   ├── 10_Skills/                         # 技能機制（公文審查、財務檢核等標準化流程自動化）
│   ├── 11_Local_MCP/                      # Local MCP 本機模型上下文協定，私有資料本地安全檢索
│   ├── 12_Custom_GPTs/                    # [付費] 零程式碼打造專屬小幫手、知識庫 RAG、分享與發佈
│   │   └── templates/                     # 實務專用 Prompt 範本庫（公文審查、行銷企劃教練）
│   ├── 13_Web_and_Deep_Research/          # [付費] 即時聯網搜尋（Web Search）+ 多步驟深度研究（Deep Research）
│   ├── 14_Images/                         # ChatGPT Images 2.5 圖像生成、@Sketch 草圖、範本與 Comments 批註修圖
│   └── 15_Voice_Vision/                   # Advanced Voice Mode 進階語音情境模擬 + 視覺拍照與螢幕辨識
│
└── [主題三：實際範例]
    ├── student-lab/                       # 學生綜合實戰工作坊（全套綠色家電上市推廣案實做）
    │   └── materials/                     # 實作情境與配套素材
    ├── Troubleshooting/                   # 常見疑難排查（額度上限、聯網異常、解析失敗、幻覺矯正）
    └── tools/                             # 輔助維護與測試數據工具
```

---

## 📈 三大主題學習進階路徑

```mermaid
graph TD
    subgraph 主題一: 設定和付費機制
        T0[00_Free_Desktop_vs_Web<br>免費版桌面 vs 網頁額度機制] --> T1[01_Settings<br>隱私安全與桌面版快捷鍵]
        T1 --> T2[02_Personalization<br>個人化風格特質與長期記憶]
    end

    subgraph 主題二: 功能面（全方案基礎協作）
        T2 --> F1[03_Canvas<br>雙欄畫布協同打磨]
        F1 --> F2[04_Chats<br>對話提問與追問心法]
        F2 --> F3[05_Advanced_Data_Analysis<br>免寫程式數據分析]
        F3 --> F4[06_Work<br>桌面版本機檔案交付]
        F4 --> F5[07_Projects<br>專案空間集中管理]
        F5 --> F6[08_Connectors<br>直連雲端硬碟 Google/OneDrive]
        F6 --> F7[09_Plugins<br>外掛工具生態]
        F7 --> F8[10_Skills<br>流程標準化技能]
        F8 --> F9[11_Local_MCP<br>本機私有資料連線]
        T2 --> F12[14_Images<br>Images 2.5 圖像生成與批註]
        T2 --> F13[15_Voice_Vision<br>進階原生語音與視覺辨識]
    end

    subgraph 主題二: 功能面（付費專屬進階）
        F5 --> P1[12_Custom_GPTs<br>零程式碼專屬助理與知識庫]
        F2 --> P2[13_Web_and_Deep_Research<br>網站即時搜尋與深度自主調研]
    end

    subgraph 主題三: 實際範例與驗收
        F4 & P1 & P2 & F12 --> LAB[student-lab<br>新產品上市綜合專案實做]
    end
```

---

## 🧭 章節模組索引表

| 主題分類 | 章節代碼 | 章節名稱 | 核心聚焦技能 |
|---|---|---|---|
| **主題一** | 00 | [00_Free_Desktop_vs_Web](./00_Free_Desktop_vs_Web/README.md) | 桌面版（月度倒扣 100%）vs 網頁版（動態冷卻）、省額工作流 |
| **主題一** | 01 | [01_Settings](./01_Settings/README.md) | 帳號偏好、公務機密資料控制（關閉模型訓練）、桌面快捷呼叫 |
| **主題一** | 02 | [02_Personalization](./02_Personalization/README.md) | 基本風格、四大特質微調、夥伴選擇、關於你、自訂指令、長期記憶庫 |
| **主題二** | 03 | [03_Canvas](./03_Canvas/README.md) | **Canvas** 雙欄畫布即時協作、劃記反饋、長度語氣調整與版本恢復 |
| **主題二** | 04 | [04_Chats](./04_Chats/README.md) | 結構化提問框架、情境與邊界設定、換位思考追問技巧 |
| **主題二** | 05 | [05_Advanced_Data_Analysis](./05_Advanced_Data_Analysis/README.md) | 雲端 Python 免寫程式數據分析、圖表繪製、直出 Word/Excel/PPT/PDF |
| **主題二** | 06 | [06_Work](./06_Work/README.md) | 桌面版「工作」模式：對接本機資料夾、多步驟自主執行、交付儀表板 |
| **主題二** | 07 | [07_Projects](./07_Projects/README.md) | 專案資料夾、跨對話知識共享、團隊權限隔離 |
| **主題二** | 08 | [08_Connectors](./08_Connectors/README.md) | 直連 Google Drive 與 OneDrive，跨雲端檔案即時分析 |
| **主題二** | 09 | [09_Plugins](./09_Plugins/README.md) | 外掛程式市集，連接 Wolfram、Expedia、Zapier 等外部工具 |
| **主題二** | 10 | [10_Skills](./10_Skills/README.md) | 標準化工作流技能（公文審查 SOP、財務指標診斷） |
| **主題二** | 11 | [11_Local_MCP](./11_Local_MCP/README.md) | Model Context Protocol 本機伺服器，私有資料不出本機安全檢索 |
| **主題二** | 12 | [12_Custom_GPTs](./12_Custom_GPTs/README.md) | **[付費]** 自建 GPTs、System Prompt、內部知識庫 RAG、Actions API |
| **主題二** | 13 | [13_Web_and_Deep_Research](./13_Web_and_Deep_Research/README.md) | **[付費]** SearchGPT 即時來源查證 + **Deep Research** 深度自主調研 |
| **主題二** | 14 | [14_Images](./14_Images/README.md) | **ChatGPT Images 2.5** 專屬空間、@Sketch 草圖、Comments 區域批註 |
| **主題二** | 15 | [15_Voice_Vision](./15_Voice_Vision/README.md) | **Advanced Voice Mode** 原生情感口說演練 + 螢幕畫面即時辨識 |
| **主題三** | 綜合 | [student-lab](./student-lab/README.md) | 完整綠色家電上市行銷專案端到端 5 大實戰演練 |
| **主題三** | 輔助 | [Troubleshooting](./Troubleshooting/README.md) | 額度上限、聯網異常、檔案解析失敗、幻覺矯正避坑指南 |
