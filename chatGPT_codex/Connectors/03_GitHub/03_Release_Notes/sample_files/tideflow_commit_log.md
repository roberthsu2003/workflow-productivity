# `tideflow-portal` Commit 歷史

> ⚠️ 教學用虛構資料。
>
> 版本區間：`v2.7.0` → `v2.8.0`（2026-08-25 ～ 2026-09-05）
> 產生方式：`git log v2.7.0..HEAD --pretty=format:"%h %ad %an %s" --date=short`

---

```
a3f81c2  2026-09-05  陳柏宇   fix(checkout): 門市自取時不再計算運費 (#412)
7e42d19  2026-09-05  陳柏宇   test(checkout): 補上 PICKUP 情境的回歸測試
c91b7a4  2026-09-04  林思妤   perf(api): 配送查詢加上區域代碼索引，P95 從 3.2s 降到 480ms (#423)
0d5e3f8  2026-09-04  林思妤   chore(db): 新增 migration 20260904_add_shipment_region_idx
b82c4e1  2026-09-04  王冠廷   fix(notify): 修正訂單編號在通知信中顯示 undefined (#436)
5a17d90  2026-09-03  王冠廷   fix(export): 後台匯出 CSV 加上 UTF-8 BOM，解決中文亂碼 (#433)
e64f2b3  2026-09-03  林思妤   refactor(lib): 抽出 formatCurrency，統一金額顯示格式
1c98d47  2026-09-02  陳柏宇   fix(address): 地址自動補完不再覆蓋使用者手動輸入 (#439)
9f3a5e6  2026-09-02  張雅涵   feat(checkout): 新增超商取貨選項（7-11、全家） (#421)
4b7d1c8  2026-09-02  張雅涵   test(checkout): 超商取貨的端對端測試
2e8f9a5  2026-09-01  王冠廷   chore(deps): 升級 Node.js 22.8.0 LTS (#438)
6d4c7b2  2026-09-01  王冠廷   chore(deps): 升級 typescript 5.6.3、vitest 2.1.1
8a15e3f  2026-08-29  林思妤   fix(auth): 修正 session token 未正確續期導致偶爾跳回首頁 (#431)
3c9b6d4  2026-08-29  林思妤   test(auth): 補上 session 續期的回歸測試
f72e8a1  2026-08-28  陳柏宇   style(ui): 統一按鈕圓角與間距
d15a4c7  2026-08-28  張雅涵   docs(agents): AGENTS.md 補上 e2e 測試說明 (#427)
0e83b96  2026-08-27  王冠廷   refactor(lib): 移除 moment.js，改用 date-fns (#430)
7c2d5f0  2026-08-27  王冠廷   chore: 移除 moment.js 相依，包體積減少 182KB
b4e91a3  2026-08-26  林思妤   fix(safari): 修正 Safari 17 結帳頁版面溢出 (#418)
a8f37c5  2026-08-26  陳柏宇   ci: 加入 Safari 的視覺回歸測試
5e1b8d9  2026-08-25  張雅涵   feat(admin): 後台新增配送績效匯出功能
2f6c4a0  2026-08-25  張雅涵   chore: 調整 eslint 規則，禁止 console.log
```

---

## 補充資訊（供改寫參考）

### 使用者可感知的變更

| Commit | 使用者會注意到什麼 |
| :--- | :--- |
| `a3f81c2` | 選門市自取時，結帳金額不再多算 80 元運費 |
| `c91b7a4` | 配送查詢頁面明顯變快 |
| `b82c4e1` | 訂單通知信裡的訂單編號正常顯示了 |
| `5a17d90` | 後台匯出的 CSV 用 Excel 開啟不再是亂碼 |
| `1c98d47` | 手動輸入的地址不會被自動補完蓋掉 |
| `9f3a5e6` | **新功能**：結帳可選 7-11 或全家取貨 |
| `8a15e3f` | 登入後不會偶爾莫名跳回首頁 |
| `b4e91a3` | Safari 使用者的結帳頁版面正常了 |
| `5e1b8d9` | **新功能**：後台可匯出配送績效報表 |

### 使用者感受不到的變更

`7e42d19`、`0d5e3f8`、`4b7d1c8`、`e64f2b3`、`2e8f9a5`、`6d4c7b2`、`3c9b6d4`、`f72e8a1`、`d15a4c7`、`0e83b96`、`7c2d5f0`、`a8f37c5`、`2f6c4a0`

（測試、migration、重構、依賴升級、CI、文件、樣式微調）

### ⚠️ 需要特別處理的兩項

> **`8a15e3f` session token 未正確續期**
> 這是**安全性相關**的修正。對外說明時：
> - 不要詳述漏洞細節（避免提供攻擊線索）
> - 但要讓使用者知道「建議重新登入」
>
> **`2e8f9a5` 升級 Node.js 22.8.0**
> 這是執行環境變更。**自架部署的客戶需要知道**，SaaS 使用者不需要。
> Release note 若同時面向兩種讀者，需分段處理。

---

*本檔案為 ChatGPT Codex 教學講義之示範資料，內容為虛構。*
