# TideFlow Portal 協作規則

## Commands

- Test: `npm test`
- Lint: `npm run lint`
- Start: `npm start`
- Weekly report: `npm run report`

## Working rules

- 修改前先讀相關測試；修改後執行 `npm test` 與 `npm run lint`。
- 金額一律以整數「分」儲存與計算，不使用浮點數。
- 不得把個資、卡號、token 或密碼寫入 log、fixture、commit 或報告。
- SQL 不可用字串拼接；非同步呼叫必須 await 或明確處理 rejection。
- Bug fix 必須補回歸測試。除非 task 明確要求，不做無關重構。
- `data/` 是唯讀輸入；報告只能新增到 `reports/`。
- 缺漏值保持缺漏並標示原因，不可填 0 或自行推估。
