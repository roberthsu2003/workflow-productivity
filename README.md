# 生成式AI全面探索:技術、應用與未來趨勢

## 🎯 目標

### 思維升級：Copilot ≠ Autopilot

![思維升級：Copilot ≠ Autopilot；Human-in-the-loop](./assets/Human-in-loop.png)

> **核心觀念：Human-in-the-loop（人類參與決策循環）**  
> **Copilot**：人是機長，AI 負責輔助導航與草稿，**人保留最終決策權**。  
> **Autopilot**：在公務與職場情境中，若**完全放手**交給 AI、不審閱、不負責，將帶來**極高風險**。

✔ 把 AI 當成**每天並肩工作的副駕（Copilot）**，而不是取代你思考的「全自動」

✔ 用 AI **減少重複、瑣碎、低價值工作**（AI 協助約 80%，你聚焦約 20% 的方針、取捨與責任）

✔ 知道如何把 AI **嵌入既有流程，而不是額外負擔**

✔ 具備 AI 素養：**會下指令、會檢核、會修正**，不被新工具牽著走

✔ **使用免費方案**，零成本學習 AI 應用（有大量**需求**可再訂閱付費方案）

---

## 80/20 原則的應用（仍由人類負責最後一哩）

1. **讓 AI 做可重複、可驗證的基礎工作**：格式、結構、初稿與彙整
2. **你負責創意與決策**：方向、風格、合規與風險判斷、**最終品質與交付責任**
3. **持續優化 Prompt**：指令越清楚，副駕越能對齊你的意圖；產出後仍要**人類審閱**再對外使用

---
## 簡單AI應用

- [代理式AI模型基本概念](./生成式AI模型基本概念/README.md)  
  了解 LLM 從「模型」到「應用程式」的演進，掌握 AI 工具的本質與能力邊界

- [prompt工程指南](./prompt/README.md)   
  輸入格式、系統提示詞、ROSES 框架與 4 要素，學會正確下指令讓 AI 產出更好

- [討論方式的內容生成](./討論方式的內容生成/README.md)  
  善用 Canvas、畫布、Artifacts 與 AI 反覆討論，產出docx,xlsx,pptx,pdf,markdown,網頁等格式 

## 常見的AI應用

- [個人知識庫](./RAG的應用/README.md)  
  檢索增強生成（RAG）與知識庫實作；範例素材見 [知識庫原始檔](./RAG的應用/知識庫原始檔/README.md)

- 簡報和資訊圖表  
  - [簡報和資訊圖表的差異](./簡報和資訊圖表/簡報和資訊圖表的差異.md) 
  - [簡報的生成](./簡報和資訊圖表/簡報的生成.md) 
  - [全自動資訊圖表的生成](./簡報和資訊圖表/全自動資訊圖表的生成.md) 

- 會議應用
	- [mp3->會議紀錄與摘要](./會議紀錄與摘要/README.md)
 
- [儲存與重複使用 AI 提示詞](./儲存與重複使用AI提示詞/README.md)  
  Gemini Gem、ChatGPT 自訂、Claude 專案 — 建立可重複使用的 AI 助手


- [連結應用程式](./連結應用程式/README.md)  
  連結應用程式的生成

- [影音生成應用程式](./影音生成/README.md)  
  影音生成的生成

- [資料搜尋的應用](./資料收集/README.md)

- [開放來源 Skills 生態與應用](./open_source_skills/README.md)  
  探索官方與開源社群 Skills、安裝匯入、安全評估與自訂貢獻工作流


---

## 🤖 主流 AI 應用程式與進階代理平台

針對現代職場兩大主流 AI 旗艦生態系，深入解析其核心功能、方案差異、自動化工作流與實務落地指引：

### 🟣 [Claude.AI 實戰全指南](./Claude_ai/README.md)
* **定位與核心優勢**：Anthropic 旗艦生成式 AI，以頂級邏輯推理、超長脈絡窗口與卓越的中文理解著稱。
* **重點核心單元**：
  - 💬 **[Chats & RTCCF 框架](./Claude_ai/Chats/README.md)**：精準提示詞工程，直接產出 Word / Excel / PPT / PDF 正式商務檔案。
  - 🎨 **[Artifacts 側欄成品](./Claude_ai/Artifacts/README.md)**：即時互動視覺化網頁、React 元件、SVG 與 Mermaid 圖表。
  - 📁 **[Projects 知識庫沙盒](./Claude_ai/Projects/README.md)**：跨對話記憶共享、專屬系統指示與團隊協作空間。
  - 🔌 **[Connectors & 本地 MCP](./Claude_ai/Connectors/README.md)**：安全授權連接 Slack、Google Workspace 與本機檔案資料庫。
  - ⚡ **[自訂 Skills 實戰體系](./Claude_ai/Skills/README.md)**：自訂 `SKILL.md`，由淺入深掌握「模仿者 ➔ 創作者 ➔ 整合者 ➔ 自動化專家」四階進化。
  - 💼 **[企業級進階代理](./Claude_ai/cowork/README.md)**：深入探索 Cowork、Claude Code、Scheduled 排程任務與 Computer Use。

### 🟢 [ChatGPT & Codex 智慧協作指南](./chatGPT_codex/README.md)
* **定位與核心優勢**：OpenAI 旗艦多模態生態系，結合強大的 GPT-4o / o1 深度思考模型、進階資料分析（Advanced Data Analysis）與龐大 GPTs 生態。
* **重點核心單元**：
  - 🧠 **進階資料分析 (Data Analysis)**：直覺上傳試算表與數據檔，AI 自動撰寫 Python 清洗資料、繪製互動圖表與統計建模。
  - 🛠️ **Custom GPTs 助手打造**：免寫程式自訂專屬角色、掛載知識庫與呼叫 Action API，客製化辦公室專用小幫手。
  - 💻 **Codex & 程式協作**：輔助程式設計、自動生成自動化腳本、SQL 語法優化與工作流程排程。
  - 🔍 **Canvas 畫布協作**：在獨立介面中與 AI 進行長文本寫作、程式碼細緻重構與段落即時微調。

---

- [實作任務](./實作任務/README.md)  
  15 個任務導向工作流：會議紀錄、簡報、資料分析、郵件、企劃書、知識庫等

---

### 免費方案使用技巧
1. **分散使用**：不同工具用於不同場景，避免單一工具額度耗盡
2. **批次處理**：累積多個任務一次處理，提高效率
3. **本地優先**：敏感資料使用 Ollama，一般資料用雲端工具
4. **善用額度**：定期檢查各工具的免費額度使用狀況

### 資料安全提醒
- ⚠️ **敏感資料**：使用 Ollama 本地處理，不上傳雲端
- ✅ **一般資料**：可使用 ChatGPT、Claude、Gemini 免費版

---

#### [企業專案](./企業專案/)

---

