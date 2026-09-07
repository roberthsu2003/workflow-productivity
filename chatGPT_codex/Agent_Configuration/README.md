# 使用 AGENTS.md 設定代理

`AGENTS.md` 記錄每次任務都應遵守的專案規則，如建置命令、架構邊界、程式風格與驗證要求。

```markdown
# AGENTS.md
## Project
- 使用 Node.js 22 與 npm。
- 原始碼位於 `src/`，測試位於 `tests/`。
## Commands
- 安裝：`npm ci`
- 測試：`npm test`
## Rules
- 不修改公開 API，除非任務明確要求。
- 修正 bug 時加入回歸測試。
- 不提交 `.env` 或 token。
```

較深層目錄的 `AGENTS.md` 可補充子目錄規則。規則應具體、可執行；單次任務細節不要永久寫入。

官方說明：[Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

[← 返回索引](../README.md)
