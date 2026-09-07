# ChatGPT Codex 教學講義

這套教材以 **ChatGPT 桌面版中的 Codex** 為主，並補充 Codex CLI、IDE extension 與 cloud。內容依 `Claude_ai` 的功能地圖建立，但採用 OpenAI 實際的名稱與操作方式。

> 最後查核：2026-09-07。介面與方案可能更新，授課前請查看 [OpenAI 官方 Codex 文件](https://learn.chatgpt.com/docs)。

## 功能對照

| Claude_ai 單元 | ChatGPT Codex 對應 | 教材 |
|---|---|---|
| Chats | Tasks / chats、提示詞、附件 | [Tasks](./Tasks/README.md) |
| Artifacts | Files、Preview、Visualizations、Sites | [Visualizations](./Visualizations/README.md) |
| Projects | Projects、local/worktree/cloud | [Projects](./Projects/README.md) |
| Connectors | Apps、plugins、MCP | [Connectors](./Connectors/README.md) |
| Skills | `SKILL.md` skills | [Skills](./Skills/README.md) |
| Plugins | Skills + MCP server + optional UI | [Plugins](./Plugins/README.md) |
| Local MCP | MCP 設定與本機工具 | [MCP](./MCP/README.md) |
| Claude in Chrome | Browser / browser extension / computer use | [Browser](./Browser/README.md) |
| Cowork / Code | Desktop、CLI、IDE、local/worktree/cloud | [Workspaces](./Workspaces/README.md) |
| Scheduled | Scheduled tasks / heartbeat / cron | [Automations](./Automations/README.md) |
| Dispatch | Remote / cloud tasks、跨裝置接續 | [Remote](./Remote/README.md) |
| Settings | `config.toml`、permissions、sandbox、network | [Settings](./Settings/README.md) |
| Custom Instructions | `AGENTS.md`（目錄作用域） | [Agent Configuration](./Agent_Configuration/README.md) |

## 建議學習順序

1. [快速開始](./Quickstart/README.md) → [Tasks](./Tasks/README.md)
2. [Projects](./Projects/README.md) → [Agent Configuration](./Agent_Configuration/README.md)
3. [Skills](./Skills/README.md) → [Connectors](./Connectors/README.md) → [MCP](./MCP/README.md)
4. [Automations](./Automations/README.md)

Codex 是會讀檔、改檔、執行命令與驗證結果的代理，不只是程式碼聊天室。專案規則放 `AGENTS.md`；跨專案重複流程做成 Skill；外部服務優先使用已安裝的 app/plugin，沒有現成整合時再評估 MCP。

[← 返回專案首頁](../README.md)
