# OAuth 2.0 授權機制與安全控解

在 AI 與雲端服務整合的世界中，**OAuth 2.0** 是最核心的安全標準。它讓 Claude 能夠在「不得知您密碼」的前提下，獲得您的授權來存取特定的資料。

這份文件將以 **Supabase** 為例，深入探討 OAuth 的運作方式，以及它與 **MCP (Model Context Protocol)** 權限機制的協作。

---

## 為什麼需要 OAuth？（代客泊車的比喻）

想像您將車交給**代客泊車員**：
- **傳統做法（不安全）**：您交出整串鑰匙（包含家門、保險箱鑰匙）。他可以開走您的車，甚至進去您的家。
- **OAuth 做法（安全）**：您交給他一把「泊車專用鑰匙」。這把鑰匙**只能發動車子**，且**不能開後車廂**，並在**一小時後失效**。

在 Connectors 的情境中：
- **您**：車主。
- **Claude**：代客泊車員。
- **Supabase / Google**：汽車與停車場。
- **Access Token (存取權杖)**：那把限權、限時的專用鑰匙。

---

## 為什麼 Connectors 能運作？（技術底層的對接）

### 1. Claude Desktop 作為「OAuth Client」
**Claude Desktop** 內建了符合標準的 OAuth 客戶端功能。它懂得如何發起授權請求、開啟瀏覽器引導您登入、並安全地管理 Token。

### 2. Supabase 作為「OAuth Server」
**Supabase** 提供了完整的 OAuth 伺服器功能（基於 GoTrue/Auth 模組）。它負責驗證您的身分並核發鑰匙給 Claude。

---

## 🛠️ MCP Tools —— AI 的「功能清單」

當您完成 OAuth 授權後，Claude 就正式「握有了鑰匙」。接著，它會透過 **MCP (Model Context Protocol)** 協議來查看這個連線具體能做什麼。

### Tools 與功能的關係
您在 Claude Desktop 介面上看到的 **Tools**（例如：`Confirm cost understanding`, `Generate TypeScript types`），本質上就是 **MCP Server 所提供的一系列「函數 (Functions)」**。

- **MCP Server** = 功能的提供者（如 Supabase 整合程式）。
- **Tools** = 伺服器開放出來的「個別能力」。
- **Tool Permissions** = 每一項能力的「安全開關」。

---

## 🔐 核心重點：OAuth Scope vs. Claude Connector 控管

當我們談論「權限」時，實際上存在兩個不同層級的安全檢查。

### 🧠 一句話總結
- **OAuth Scope**：決定 Claude 「**技術上能不能做**」（外部權限）。
- **Connector / Tool 設定**：決定 Claude 「**行為上願不願意幫你做**」（內部控管）。

---

## 🔁 實戰案例：Supabase 資料操作

假設您的 **OAuth Token** 擁有完整權限，但您在 **Claude Tool Permissions** 做了以下設定：

| 工具功能 (MCP Tool) | 安全設定圖示 | 結果 |
| :--- | :--- | :--- |
| **查詢資料 (SELECT)** | ✅ (Always allow) | 直接執行並顯示結果。 |
| **修改 Schema / 刪除** | ✋ (Needs approval) | AI 會暫停並跳出視窗請您確認。 |
| **敏感管理操作** | 🚫 (Blocked) | 即使技術上可行，AI 也被禁止執行。 |

---

## 🎯 教學用的三層安全模型

```mermaid
graph TD
    A[1. OAuth 權限 - Supabase 層] -->|定義| B(能力：你可以做什麼)
    B --> C[2. MCP Tools 設定 - Claude 層]
    C -->|定義| D(規則：AI 被允許做什麼)
    D --> E[3. 使用者確認 - 人類層]
    E -->|決定| F(行動：最後要不要做)
```

1.  **OAuth (Supabase)**：賦予 AI 「能力」。
2.  **MCP Tools (Claude)**：將能力拆解為具體的「工具」，並設定行為限制。
3.  **使用者確認 (Human-in-the-loop)**：人進行「最後把關」。

---

## 🔥 技術總結

- **Access Token**：安全儲存在本地（Keychain/Credential Manager）。
- **MCP Server**：透過 Tools 曝露功能。
- **權限控制**：是為了防止 AI 誤操作，實現 AI 安全中的「人在回路」。

---

← [返回 Connectors README](./README.md)
