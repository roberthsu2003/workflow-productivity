# Projects 與工作環境

Codex project 通常是一個 saved local folder 或 Git repository，讓 task 能讀檔、執行命令並產生可檢查的變更。

| 環境 | 適合情境 | 特性 |
|---|---|---|
| Local / checkout | 直接處理目前目錄 | 看得到未提交變更，不能覆蓋使用者工作 |
| Worktree | 同一 repo 平行開發 | 分支與檔案隔離，適合多 task |
| Cloud | 遠端或跨裝置工作 | 需可重現的依賴、環境與 secrets |

## 教材範例

- [行政營運](./Examples/01_Office_Administration/README.md)
- [品牌與行銷](./Examples/02_Brand_and_Marketing/README.md)
- [商業情報](./Examples/03_Business_Intelligence/README.md)

repo 應提供 `README.md`、`AGENTS.md`、安裝/測試命令與可驗收結果；API key、token 和客戶機密不可提交到 Git。

[← 返回索引](../README.md)
