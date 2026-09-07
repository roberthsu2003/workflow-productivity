# Files、Preview、Visualizations 與 Sites

Claude Artifacts 在 Codex 沒有完全同名的一對一功能：

- 文件／程式：建立 workspace 檔案並在 Codex 預覽。
- 圖表、互動解說、模擬：使用 Visualization。
- 完整網站或內部工具：使用 Sites 建構並視需要發佈。
- 圖片：使用 ImageGen；PDF、Word、試算表、簡報使用相應 artifact skill。

```text
讀取 sample_files/sales.csv，建立可互動的季度營收視覺化：
可切換地區、顯示營收與毛利率，並附三點洞察。不要更動原始 CSV。
```

驗收時確認數字可追溯、單位與空值處理清楚；公開發佈前移除敏感資料。

[← 返回索引](../README.md)
