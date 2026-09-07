# Scheduled Tasks 與 Automations

- Heartbeat：附著於目前 task，週期醒來檢查狀態，適合監控。
- Cron：獨立工作依固定時間執行，適合可重現的週報或批次流程。

建立前先手動跑通一次，指定資料來源、時區、頻率、完成條件與通知條件。寫入、寄信、發佈或刪除資料時，需要清楚的授權與審核邊界。

```text
每週一上午 9:00（Asia/Taipei）檢查本專案過去一週的變更，
整理完成事項、風險與本週待辦。沒有新變更時不要通知；
若測試失敗或需要人工決策，請在這個 task 提醒我。
```

官方說明：[Scheduled tasks](https://learn.chatgpt.com/docs/automations)

[← 返回索引](../README.md)
