# 學生除錯手冊

## 先執行這五個檢查

```bash
pwd
git status --short
node --version
npm test
npm run lint
```

保留實際輸出與錯誤訊息。不要只說「不能用」，也不要在不理解原因時重裝整套工具。

## 常見問題

### `node: command not found` 或版本小於 20

安裝 Node.js 20 以上版本，再重新開啟終端機。這個專案沒有 npm dependencies，不需要執行 `npm install`。

### `Author identity unknown`

不必修改全域 Git 設定。`scripts/bootstrap.sh` 已用本專案限定的示範身分建立第一次 commit。若自行 commit，可使用：

```bash
git -c user.name="Codex Student" -c user.email="student@example.invalid" commit -m "描述"
```

### `not a git repository`

確認目前在 `tideflow-portal` 副本內，然後執行 `./scripts/bootstrap.sh`。

### `Permission denied: ./scripts/bootstrap.sh`

執行 `sh scripts/bootstrap.sh`。GitHub 下載 ZIP 有時不保留 executable bit。

### Worktree 顯示 branch already checked out

同一分支不能同時被兩個 worktree 使用。先用 `git worktree list` 找到占用位置，改用新的分支名稱；不要直接刪除 `.git/worktrees`。

### 週報出現 `EEXIST`

產生器刻意禁止覆寫既有週報。保留原檔並換一個全新專案副本，或完成進階題：已存在時新增 `_v2` 檔。

### Connector、Remote 或 Automation 看不到

這通常與方案、產品介面、漸進式開放或組織政策有關。先完成章節的「離線模式」；不要為了交作業購買方案。需要真實服務時，再由教師提供共同環境或管理員授權。

### Codex 想執行超出範圍的命令

不要核准。要求它說明命令用途、目標路徑與替代方案，或把 task 改成只讀診斷。外部寄送、merge、付款、刪除與權限變更都必須由人確認。

### 結果與參考答案不同

先比對事實與驗收條件，不比對文句。若使用即時網路資料，記錄查詢日期與來源；即時結果本來就可能不同。

← [返回教材首頁](../README.md) ｜ [參考答案](../Answer_Key/README.md)
