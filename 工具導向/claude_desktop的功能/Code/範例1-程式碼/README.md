# 範例程式碼說明

這個資料夾包含一個有 bug 的 Python 程式碼範例，用於演示 Claude Code 的除錯功能。

## 檔案說明

- `grade_calculator.py`: 成績計算模組，包含多個有 bug 的函式
- `main.py`: 主程式，用來示範錯誤情況

## 如何執行

```bash
# 進入這個資料夾
cd 範例1-程式碼

# 執行主程式（會出現錯誤）
python main.py
```

## 已知問題

1. **`calculate_average()` 函式**：當傳入包含字串或 None 的列表時會出現 `TypeError`
2. **`calculate_total()` 函式**：同樣的問題
3. **缺少資料驗證**：函式沒有檢查輸入資料的有效性

## 修復目標

使用 Claude Code 修復這些問題，讓函式能夠：
- 正確處理混合類型的列表（只計算數字部分）
- 忽略 None 值
- 提供清楚的錯誤訊息（如果需要）
- 保持原本的功能不變
