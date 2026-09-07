# MCP（Model Context Protocol）

MCP 讓 Codex 連接本機或遠端工具與資料來源，適合公司內部 API、資料庫或沒有現成 plugin 的系統。

- 工具名稱與描述要清楚，參數使用嚴格 schema。
- 查詢與寫入工具分開；危險操作要求確認。
- 回傳最少必要資料，避免 secrets 與個資外洩。
- 明確處理認證、逾時、重試、稽核與錯誤。

一般設定位於 `~/.codex/config.toml`。欄位與 CLI 指令可能更新，請依 [官方 MCP 文件](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) 設定，不要照抄不明來源的 token 或啟動命令。

[← 返回索引](../README.md)
