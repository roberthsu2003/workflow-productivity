# Claude_AI

## Chats（對話）

Claude 的主要互動介面：你在這裡與模型來回對話、提問、下指令，並可搭配上傳檔案、使用側邊欄與其他功能。對話可獨立存在，也可放在 **Projects（專案）** 內以沿用專案知識與自訂指示。

**使用情境（舉例）：** 臨時查詢與釋疑；單次草擬公文／郵件；上傳 PDF、試算表請摘要或改寫；依 [Chats 範例](./Chats/README.md) 用 **RTCCF** 指定產出 Markdown 或 Office／PDF 檔；不確定會延續多輪時，可先從一般對話試起再決定是否開 **Project**。

**主題資料夾：** [Chats](./Chats/README.md)

## Projects（專案）

**專案**是專用工作區：可設定**自訂指示**（語氣、規則、角色），並上傳**專案知識**檔案（文件、資料、程式碼等），讓 Claude 在該專案底下的所有對話中持續參考同一份背景脈絡。適合長期主題、固定流程或需要穩定「專案記憶」的工作。（官方文件亦將 Skills 與 Projects 區分：Projects 偏向靜態、持續載入的背景知識。）

**使用情境（舉例）：** 同一計畫或報告需**數週至數月**反覆修訂；上傳**格式範本、內規、KPI 定義**後，每則對話都沿用；團隊共用語氣與簽核用語時，在自訂指示一次寫清；與 **Skills** 二選一時：**固定背景**用專案，**依任務才載入的流程**用技能。

**主題資料夾：** [Projects](./Projects/README.md)

## Artifacts（成品／Artifact）

**Artifacts** 是在對話中產生的**獨立內容區塊**，可包含程式碼、文件、圖表或可互動的網頁式介面；透過對話描述需求，Claude 可生成並在側邊預覽、編輯與分享。適合快速做出原型、小工具、視覺化或可供他人開啟的成品。（實際可用格式與發佈／分享方式依方案與產品更新為準，請以 [Claude 說明中心](https://support.claude.com) 為準。）

**使用情境（舉例）：** 要做**可點選、可預覽**的網頁小工具或流程圖（HTML／React／Mermaid 等）；**內嵌對話式 AI** 的原型（官方教學常見）；需**發佈連結**給同事試用；純文字即可完成的內容則不必強制開 Artifact。

**主題資料夾：** [Artifacts](./Artifacts/README.md)

## Connectors（連接器）

**Connectors** 透過 **Model Context Protocol（MCP）** 把 Claude 接到外部工具與資料：可讀取雲端檔案、郵件、行事曆、程式庫等，並在對話中執行對應操作；部分整合亦支援在對話裡呈現 **MCP Apps**（圖表、表單等互動介面）。類型包含官方預建整合（如 Google Workspace、GitHub、Slack、Microsoft 365）、遠端 MCP、目錄中的第三方連接器等。免費與付費方案可使用的連接器範圍不同，請以官方文件為準。

**使用情境（舉例）：** 資料在 **Gmail、Google 日曆、雲端硬碟、GitHub** 等，不想逐段複製貼上；要問「本週會議與衝突」「某封信重點」等**帶出處**的摘要；需在對話中出現**表單或圖表型 MCP App**；內網無法授權連線時則不適用。

**主題資料夾：** [Connectors](./Connectors/README.md)

## Skills（技能）

**Skills** 是內含指示、腳本與資源的資料夾（通常以 `SKILL.md` 描述何時啟用與如何執行），Claude 會依任務**動態載入**相關技能，以節省上下文並提供專門流程（例如文件產出、品牌規範、與特定工具搭配的工作流）。另有 Anthropic 預建技能、合作夥伴技能，以及團隊／企業派發的自訂技能。多為 **Pro、Max、Team、Enterprise** 等付費方案功能，且可能需開啟程式碼執行；細節以 [Skills 說明](https://claude.com/docs/skills/overview) 為準。

**使用情境（舉例）：** 常態產出 **Word／Excel／PowerPoint／PDF**（搭配內建文件技能）；**品牌／公文用語**寫成可載入的規範；可重複的**報表或轉檔流程**（必要時含腳本）；一次性對話、無需封裝時不必另建 Skill。

**主題資料夾：** [Skills](./Skills/README.md)

## Plugins（外掛／套件）

**Plugins** 是可重複使用的**能力套件**：將 MCP **Connectors**、**Skills**、斜線指令（slash commands）、子代理（sub-agents）等打包成單一可安裝、可分享的單元，用來為特定角色或團隊客製化 Claude。官方提供多類範例外掛（如生產力、銷售、資料、法務等），亦可自行建立。目前主要與 **Claude Code**、**Cowork** 等產品深度整合；Cowork 上為付費使用者研究預覽等級功能，實際範圍請見 [Plugins 說明](https://claude.com/docs/plugins/overview)。

**使用情境（舉例）：** 在 **Claude Code** 或 **Cowork** 內，希望**一次安裝**「連線＋技能＋斜線指令」；團隊共用**同一套**銷售／法務／資料流程；需用 **`/` 指令**快速叫出固定工作流；僅使用 **claude.ai 網頁一般聊天**時，通常改以單獨的 **Connectors／Skills** 即可。

**主題資料夾：** [Plugins](./Plugins/README.md)


---

## Cowork

**付費方案**（依訂閱與 [定價](https://claude.com/pricing) 為準）。Cowork 為多步驟代理工作區：可透過 **Connectors** 等進行**連線與查詢**（外部工具／資料來源），並在授權與設定範圍內**讀寫、整理本機資料夾**內的檔案（實際可存取路徑依產品與權限為準）。下列僅列介面分類。

- Scheduled
- Dispatch
- Ideas
- Customize
    - Connectors
    - Skills
    - Plugins

---

## Code

**Claude Code** 為**程式開發情境**的代理工具（常見於**終端機**與 **VS Code／JetBrains** 等 IDE 外掛）：在**本機專案目錄**內讀寫與瀏覽程式碼、搭配 **Git**、執行指令與測試；**Plugins** 則可打包 **Connectors**（MCP）、**Skills**、斜線指令與子代理，用來銜接外部服務與團隊慣例。**付費方案**依訂閱與授權為準（見 [定價](https://claude.com/pricing)）。下列僅列介面分類，供備查。

- Scheduled
- Dispatch
- Customize
    - Connectors
    - Skills
    - Plugins
