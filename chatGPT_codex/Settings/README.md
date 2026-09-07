# Codex Settings、Permissions 與 Sandbox

Codex 設定分為桌面 UI 與 `~/.codex/config.toml`。重要概念包括 model/reasoning、filesystem sandbox、approvals、network、MCP 與 notifications。

建議日常使用 workspace-write，只寫入專案與暫存目錄；對外網路、套件安裝、GUI、自動發佈與破壞性命令保留核准。Secrets 放環境變數或 secret store，不寫進設定範例或 Git。團隊規則寫 `AGENTS.md`，個人偏好留在個人設定。

官方說明：[Config basics](https://learn.chatgpt.com/docs/config-file/config-basic) · [Permissions](https://learn.chatgpt.com/docs/permissions)

[← 返回索引](../README.md)
