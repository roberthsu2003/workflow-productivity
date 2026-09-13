# 📈 範例 3：跨來源財務對帳、自動程式運算與營運圖表產出

> 🟠 **難度等級**：**Level 3（進階分析・數據對帳）**  
> 💻 **適用平台**：Claude 全平台（Desktop / Web / Mobile / Chrome 側邊欄）  
> 💼 **適用角色**：財務長 (CFO)、財務分析師 (FP&A)、營運總監 (COO)、創投風控經理、電商對帳人員。  
> 🎯 **核心體驗**：
> - 🤖 **背景自動寫 Python 運算 (Agentic Code Execution)**：告別大語言模型「計算數字會胡言亂語」的刻板印象，Cowork 會自主在雲端隔離沙盒中撰寫 Python 程式碼，交叉合併多份 CSV 進行精確數學計算。
> - 🔍 **異常超支與虧損自動警報 (Deficit & Overrun Detection)**：自動找出達成率落後、預算嚴重超支的危險部門。
> - 📊 **自動繪製專業視覺化圖表 (Data Visualization)**：生成並匯入包含長條圖與折線圖的營運趨勢對比圖。

---

## 🎭 職場痛點劇場：董事會前夕的對帳噩夢

> *「下週一就是 Q3 季末董事會，CEO 交代：『把會計系統導出的實際支出，跟業務部 CRM 的業績目標拉出來對一下，算清楚各部門達成率，還有我們的現金還能燒幾個月（Cash Runway）！』」*  
> *你手上有兩份不同系統匯出的 CSV，欄位名稱不同、月份分開。你打開 Excel 寫 VLOOKUP，一下公式報錯 `#N/A`，一下算錯淨利。好不容易拉出來的圖表，還被財務長指出數值加總對不上……*

**把這兩份 CSV 丟進 Claude Cowork，讓 AI 背景自動寫 Python 程式碼，30 秒產出零誤差的董事會級財務報告！**

---

## 📦 快速開始：下載練習素材壓縮檔 (Quick Download)

> [!TIP]
> 💡 **免手動建立！已為您打包完整測試素材壓縮檔**：  
> 本範例已在目錄中預先準備好打包好的壓縮檔：[`sample_files.zip`](./sample_files.zip)  
> - **直接下載**：學員可直接下載此 `sample_files.zip`，解壓縮後即可獲得包含 `sample_files/` 完整測試目錄（內含實際流水帳 `q3_financial_raw.csv` 與業績目標表 `crm_sales_target.csv`）。
> - **一鍵還原環境**：在練習完數據對帳與圖表繪製後，若想重新演練或測試不同提示詞，只需再次解壓縮 `sample_files.zip` 覆蓋，即可秒速重置至最乾淨的初始狀態！

---

## 🔄 執行前後視覺化對比 (Before vs. After)

```
【執行前：兩份不同業務系統導出的分散數據】
03_Financial_Report/
├── sample_files.zip                  ⭐【練習素材壓縮包：整包下載解壓/一鍵重置】
└── sample_files/
    ├── q3_financial_raw.csv          (實際財務流水：各月營收、費用、現金餘額、Net Burn)
    └── crm_sales_target.csv          (業務銷售目標：各月預估營收、預算上限、毛利目標)
```

⬇️ **透過 Cowork 背景 Code Execution 交叉比對產出** ⬇️

#### 【產出：高階管理層財務摘要、超支警報與營收對比圖表】

| 部門 | 目標營收 (USD) | 實際營收 (USD) | 達成率 | 費用超支狀況 | 風險狀態 |
|:---|:---:|:---:|:---:|:---:|:---:|
| **SaaS 訂閱** | $375,000 | $405,000 | **108.0%** | +$15,000 | 🟢 表現優異（超額達成） |
| **硬體設備** | $150,000 | $113,000 | **75.3%** | +$32,000 | 🔴 嚴重虧損預警（連續擴大） |

> **💡 關鍵財務營運指標 (KPIs)**：
> - **全公司 Q3 總營收**：$518,000 USD（整體目標達成率 98.7%）
> - **硬體部門累計淨虧損**：-$84,000 USD（9 月單月燒錢暴增至 $45,000）
> - **期末現金餘額**：$1,680,000 USD
> - **現金跑道 (Cash Runway)**：預估剩餘 **20.0 個月**（需立即整頓硬體供應鏈止血）
> - 📈 **自動產出圖表**：`q3_revenue_vs_target_chart.png`（已自動繪製並嵌入報告中）

---

## 🧠 Cowork 代理執行管線 (Agent Execution Pipeline)

```mermaid
flowchart TD
    Start["📥 載入 q3_financial_raw.csv 與 crm_sales_target.csv"] --> Plan["📝 規劃比對架構：SaaS vs 硬體部門"]
    Plan --> GenCode["🐍 背景自主撰寫 Python Pandas 運算腳本"]
    GenCode --> Sandbox["⚡ 雲端沙盒執行代碼 (Code Execution)"]
    Sandbox --> CalcResult["🔢 計算達成率、超支差距、Net Burn 與 Cash Runway"]
    Sandbox --> Plot["📊 調用 Matplotlib 繪製雙部門營收/費用對比圖表"]
    CalcResult --> CrossCheck{"🔍 數據自檢比對"}
    Plot --> CrossCheck
    CrossCheck -->|發現硬體部門連續 3 個月虧損擴大| Alert["🔴 觸發高階風控警報"]
    Alert --> Report["📄 整合撰寫 Q3 財務經營分析報告"]
    Report --> Deliver["✅ 交付 Markdown 報告與嵌入圖表"]
```

---

## 🪄 （選用進階）自然語言 ➔ RTCCF 結構化轉換術 (Optional)

> [!NOTE]
> 💡 **真實職場視角：同仁通常不懂 RTCCF，該怎麼辦？**  
> 在真實工作場景中，主管交代財務分析時通常也是口語指令：  
> *「把這兩張表對一下，看看 SaaS 跟硬體部門誰沒達標、超支多少，算一下我們的現金還能燒多久，畫張圖給老闆看！」*  
> 
> **面對這個情況，您有兩種最舒服的做法：**
> 1. **做法 A（直接使用現成 Prompt）**：直接複製下方已經為您精心調校好的 RTCCF Prompt，省時又精準。
> 2. **做法 B（讓 AI 幫您轉化・一鍵變專業）**：先在一般對話（Chat）中，丟出您的隨興口語，讓 Claude 充當您的「提示詞架構師」，把白話文自動翻譯擴充為工業級 RTCCF 指令，再貼進 Cowork 執行！

<details>
<summary><b>點擊展開：如何用一句指令讓 Claude 將「口語白話」轉成「RTCCF」並以 Artifact 協作？</b></summary>

<br>

若您平常有其他自訂財務對帳任務，可在 **Chat** 模式中貼上這段元提示詞（Meta-Prompt）：

```text
我即將使用 Claude Cowork 執行跨表格財務對帳與營運分析任務。

請幫我把以下這段口語需求，轉換擴充為嚴謹、不易出錯的「RTCCF 結構化提示詞（Role, Task, Context, Constraint, Format）」。

【重要要求】：
請將轉換後的提示詞內容，儲存為一個名為「financial_analysis_prompt.md」的 Markdown 檔案（以 Artifact 模式產出），方便我在右側視窗直接預覽與人機協作微調。

──────────────────────────────────────────────────────────
【我的原始口語需求】：
「把會計系統導出的實際支出 q3_financial_raw.csv，跟業務部 CRM 的業績目標 crm_sales_target.csv 拉出來對一下，
算清楚 SaaS 和硬體部門各月達成率與費用超支。
用 Python 算我們的現金還能燒幾個月（Cash Runway），
畫一張營收長條對比圖，最後針對硬體部門持續虧損給 3 個止血改善建議。」
──────────────────────────────────────────────────────────
```

<br>

> 💡 **核心密技：為什麼要特別指定「儲存為 Markdown 檔 (Artifact)」？**  
> - **啟動右側 Artifact 畫布**：在 Claude 介面中，只有產出為獨立的 Markdown Artifact 文件，畫面右側才會展開專屬的預覽面板。  
> - **實現原地人機協作 (In-place Edit)**：您可以直接在右側畫布上**反白選取任何一段提示詞或財務報告分析章節**，點擊浮現的「Edit with Claude」輸入修改意見，Claude 就會原地修訂該段落，達成流暢的雙向人機協同調校！

<br>

</details>

---

## 🤖 Cowork 實戰 Prompt（RTCCF 結構 - 亦可直接複製使用）

請在 **Cowork 模式** 下，上傳本資料夾中的 `q3_financial_raw.csv` 與 `crm_sales_target.csv`（或直接掛載 `sample_files/` 目錄），並輸入以下 Prompt（若不想手寫或轉換，直接複製這段即可）：

```text
【Role】
你是一名擁有 CPA 執照的資深企業財務分析師兼營運風控主管（Financial Controller）。

【Task】
請讀取上傳的 q3_financial_raw.csv 與 crm_sales_target.csv 兩份檔案，透過背景撰寫 Python 程式碼（Code Execution）執行精密交叉比對，完成以下 Q3 財務營運分析：
1. 以「月份」與「部門」為維度交叉比對，計算各部門的「目標營收達成率 (%)」、「費用超支金額 (實際費用 - 預算上限)」與「毛利現況」。
2. 評估全公司財務健全度：計算全季總營收、總費用、總淨損益，並依據 9 月底的期末現金餘額與平均月燒錢率，精準試算「可支撐營運月數（Cash Runway）」。
3. 產生一張「各部門 Q3 實際營收 vs 目標營收長條對比圖」，清晰標註數值並嵌入報告中。
4. 針對「硬體設備部門」連續虧損擴大的現象，提出 3 個具體且具可操作性的止血改善建議。

【Context】
- 上傳檔案 1：q3_financial_raw.csv (實際各月財務數據)
- 上傳檔案 2：crm_sales_target.csv (各月營運目標與預算)

【Constraint】
- 所有百分比、超支金額與 Cash Runway 必須 100% 透過 Python 程式碼計算，嚴禁臆測推算。
- 若硬體部門出現淨虧損，必須在報告中以 🔴 高度警訊標註。
- 使用繁體中文輸出。

【Format】
產出一份結構完整的 Markdown 專業報告，包含：
1. 【Q3 財務績效執行摘要卡】（總營收、達成率、Cash Runway）
2. 【部門維度對比總表】（SaaS 訂閱 vs 硬體設備）
3. 【視覺化圖表展示】
4. 【重大財務警訊剖析與 3 大改善處方】
```

---

## 🚀 學員實戰動手做 4 步驟

0. **下載／確認練習素材**：
   - 確保本範例目錄中具備 `sample_files/` 測試資料夾。若您是從遠端單獨下載或需要重置，可直接下載解壓縮 [`sample_files.zip`](./sample_files.zip) 取得完整練習檔。
1. **開啟 Claude 介面切換至 Cowork**：
   - 登入 [claude.ai](https://claude.ai) 或開啟桌面應用，在訊息輸入框左下角切換為 **Cowork**。
2. **載入練習資料**：
   - 桌面端：工作目錄指定本機的 `Claude_ai/cowork/Examples/03_Financial_Report/sample_files/`。
   - 網頁端：將 `q3_financial_raw.csv` 與 `crm_sales_target.csv` 拖曳上傳至對話框。
3. **送出 Prompt 啟動程式運算**：
   - 貼上上述 RTCCF Prompt 送出，觀察 Claude 如何自主編寫 Python 程式碼進行數據交叉比對與圖表繪製。
4. **🔥 殺手級功能實戰：展開程式碼查看運算細節 (View Code)**：
   - 在執行過程中或成果交付後，點擊 Claude 畫面上的「View code」或「Analysis」。
   - 您會親眼看見 Claude 自動寫出的 Pandas 合併計算與 Matplotlib 繪圖程式碼，體驗**零數學幻覺、完全可驗證審計**的強大威力！

---

## 💡 避坑指南與核心收穫 (Tips & Takeaways)

> [!TIP]
> 1. **大語言模型算術不可靠？交給 Code Execution！**  
>    在純文字 Chat 模式下，LLM 遇到多位數除法或複合公式容易產生幻覺。在 Cowork 中，指定「透過背景撰寫 Python 程式碼」，Claude 會將計算交給真實的 Python 解譯器，保證 100% 精準。
> 2. **跨檔案鍵值合併 (Key Merge)**：  
>    只要在 Prompt 中指明共同欄位（如「月份」與「部門」），Cowork 會自動完成類似 SQL `JOIN` 或 Excel `VLOOKUP` 的操作，免去手動整理欄位的苦工。
> 3. **隨時可復原與一鍵重置**：  
>    - 若在練習數據分析或微調報告時改動了原始檔案，直接將目錄內的 [`sample_files.zip`](./sample_files.zip) 解壓縮覆蓋，立即還原最乾淨的初始練習環境！

---

[← 上一篇：範例 2 客訴情緒診斷與原地微調](../02_Customer_Feedback/) ｜ [返回 Cowork 主頁](../../README.md) ｜ [下一篇：範例 4 產業情報監測與定時晨報 →](../04_Daily_News_Brief/)
