# TideFlow Portal 教學專案

零外部套件的 Node.js 練習專案，用來重現 Codex 教材中的讀檔、改檔、測試、PR review、worktree 與週報自動化。

## 快速開始

```bash
./scripts/bootstrap.sh
npm test
npm run lint
npm start
```

瀏覽器開啟 `http://127.0.0.1:3000/health`，應看到 `{"status":"ok"}`。

## 目錄

- `src/`：運費、訂單金額與 HTTP server
- `test/`：Node 內建測試
- `data/`：離線營運資料、Issue、PR 與 commit 偽資料
- `scripts/`：初始化、檢查與週報產生器
- `reports/`：產出位置，只保留 `.gitkeep`

## 刻意保留的練習問題

`src/checkout/calcTotal.js` 有四個 code review 問題；這是教材題目，不是 production code。不要輸入真實姓名、卡號或訂單資料。
