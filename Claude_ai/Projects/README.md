# Projects（專案）：您的雲端專屬知識沙盒

**Projects** 是 Claude 提供的一種**持久化、規模化**的雲端工作方式。如果您覺得一般對話像是在路邊攤快餐，那麼 **Project** 就像是您擁有一間專屬的實驗室。

---

## 🛠️ 客製化專案能力 (Capabilities)

Projects 最強大的特性之一，就是可以為每個專案量身打造它的**「工具箱」**。

### 1. 專屬 Connectors
您可以為每個專案**獨立勾選**要開啟哪些連線（如：Google Drive, GitHub）。

---

## 🔐 安全性與 Token 儲存：鑰匙放在哪？

當您在專案中使用連線時，學生常會擔心：「我的權限（Token）安全嗎？它存放在哪裡？」

### 1. 遠端連線 (Remote Connectors / OAuth)
當您授權 Claude 存取雲端服務（如 Supabase, Gmail）時：
- **儲存位置**：儲存在 **Anthropic 雲端伺服器的加密保險箱 (Secure Vault)** 中。
- **運作邏輯**：因為專案是在雲端執行的，雲端的 Claude 需要這把「鑰匙」才能即時讀取資料。
- **安全性**：Token 與您的帳號綁定，且僅在您授權的專案中有效。

### 2. 本地連線 (Local MCP)
當您讓專案調用您電腦上的 MCP 伺服器時：
- **儲存位置**：**完全儲存在您的本機電腦**（macOS Keychain 或 Windows Credential Manager）。
- **運作邏輯**：資料在本地處理，雲端伺服器不持有任何長期存取鑰匙。

---

## 🧠 Projects 的本質是什麼？

這是在雲端建立一個 **Sandbox（沙盒）** 嗎？**答案是肯定的，但它是「知識層面」的沙盒：**

1.  **雲端知識沙盒 (Knowledge Sandbox)**：專案空間隔離，上傳檔案僅限專案內存取。
2.  **行為約束器 (Custom Instructions)**：定義沙盒內的物理規則與角色。
3.  **運算沙盒 (Execution Sandbox)**：內建 Analysis Tool 執行 Python 運算。

---

## 🚀 快速開始：專案指令範例 (Examples)

為了讓學生能快速體驗 Projects 的強大，我們準備了三個不同領域的範例。您可以直接點擊進入，**複製內容並貼到專案的 Instructions 欄位**：

1.  [**💼 專業辦公行政助手**](./Examples/Office_Assistant.md)：適合上班族，處理郵件潤飾、會議紀錄與文件整理。
2.  [**✍️ 社群行銷文案大師**](./Examples/Marketing_Copywriter.md)：適合社群小編，快速產出多平台引流文案。
3.  [**🎓 英語學習與口語教練**](./Examples/English_Learning.md)：適合學生，將 Claude 變成您的私人語言導師。

---

## 💡 進階技巧：專案隔離 (Project Isolation)

**善用專案隔離提升 AI 效能**：建議針對不同任務建立獨立專案，並僅為其啟用必要的 **Connectors**。這能避免過多的工具定義（Tool Definitions）擠壓系統 Token 空間，防止單一對話的背景資訊過於臃腫，進而維持 AI 的推理精確度與反應速度。

---

← [返回上層：Claude_AI 索引](../README.md)
