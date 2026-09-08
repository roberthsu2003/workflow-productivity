# 學生實作參考答案

請先自行完成，再用本頁驗收。答案著重「應觀察到什麼」，不要求文字完全相同。

## Quickstart

- 專案用途：零依賴 Node.js 教學 portal。
- 啟動：`npm start`；測試：`npm test`；檢查：`npm run lint`。
- `src/checkout/calcTotal.js` 是刻意保留的 review 題，不應在第一次 README 小修改時順手修掉。
- `git diff --check`、`npm test`、`npm run lint` 都應成功。

## Agent Configuration

有效規則至少包含：修改後跑測試、金額用整數分、不得記錄個資、SQL 不得拼接、非同步必須處理錯誤、資料缺漏不可補 0。

## PR Review

`src/checkout/calcTotal.js` 應辨識出：

1. SQL 使用字串拼接，有 injection 風險。
2. 金額用 `parseFloat` 與浮點數累加。
3. `updateOrderCache` 沒有 `await` 或 rejection handling。
4. log 洩漏持卡人與卡號。
5. 若 PR 宣稱是 bug fix，還缺回歸測試。

本題只要求 review；不要直接修改程式。每一項意見都應包含規則、檔案位置、風險、具體修法與嚴重度。

## Worktree

完成後 `git worktree list` 應至少有三筆，且三個路徑分別位於不同分支。任一 worktree 的未提交修改不應出現在另外兩個工作目錄。合併前每個分支都要通過 `npm test`。

## Weekly Ops Brief

在全新副本執行 `npm run report`，預期產生 `reports/2026-W36_週報.md`，內容應指出：

- 4 筆 commit。
- 1 個測試失敗 PR。
- 1 個超過 7 天未更新 PR。
- 1 筆配送資料缺漏，且沒有填成 0。
- 2 個開放 Issue。
- 東區準時率低於 95%，需要追蹤。

同一路徑再次執行會因禁止覆寫而失敗，這是安全機制，不是 bug。進階題可讓學生實作 `_v2` 命名規則。

## Connector 離線模式

- Gmail：只產生草稿，不寄送；需區分客訴、一般詢問及敏感資料。
- Calendar：只提出時段建議，不替任何人接受或取消會議。
- Canva：品牌色、產品名稱、日期和價格都要與品牌 JSON 及企劃書交叉核對。
- GitHub：可用 `data/issues.csv`、`data/pull_requests.csv` 與 `data/commits.md` 代替真實 API；所有網址使用 `.invalid`，不可當成真實連結。

## 自我評分

| 項目 | 配分 |
|---|---:|
| 使用正確輸入，未編造缺漏事實 | 25 |
| 遵守讀寫範圍與安全限制 | 20 |
| 產出格式完整 | 20 |
| 驗證命令確實執行並附結果 | 20 |
| 能說明未完成項目與原因 | 15 |

80 分以上視為通過；若洩漏敏感資料、未經授權送出外部動作或把缺漏填成 0，該次實作直接不通過。

← [返回教材首頁](../README.md)
