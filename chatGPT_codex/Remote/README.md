# Remote 與跨裝置工作

Codex 可把工作放到 cloud environment，或從其他裝置建立及接續 task。這與 Claude Dispatch 的目標相近，但操作單位是 project、task 與 environment。

使用前確認：

- Cloud 可安裝依賴並執行測試。
- secrets 透過安全設定提供，不寫入 Prompt 或 repo。
- 任務不依賴尚未同步的本機檔案。
- 清楚指定是否允許 push、PR、寄信或發佈；未授權時只產出草稿。

[← 返回索引](../README.md)
