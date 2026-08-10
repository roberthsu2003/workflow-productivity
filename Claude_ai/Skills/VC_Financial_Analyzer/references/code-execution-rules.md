# 🐍 Python Code Execution 與圖表視覺化規範 (Code Execution Rules)

在 `VC_Financial_Analyzer` 中，所有數據計算與視覺化圖表產出均需通過 Python 代碼執行環境 (Code Interpreter) 處理。請遵守以下規範以確保精準度與專業質感。

---

## 1. 代碼執行基本規範 (Python Guidelines)

1. **模組導入與異常處理**：
   - 統一使用 `pandas`, `numpy`, `matplotlib`, `seaborn`, `openpyxl` 等標準資料科學庫。
   - 所有檔案讀取 `pd.read_excel()` 必須封裝於 `try-except` 區塊，若找不到工作表或欄位缺漏，需印出明確錯訊。
2. **多工作表 (Multi-Sheet) 處理 SOP**：
   ```python
   import pandas as pd
   
   # 自動讀取 Excel 所有工作表名稱
   excel_file = pd.ExcelFile("uploaded_financials.xlsx")
   sheet_names = excel_file.sheet_names
   print(f"偵測到工作表：{sheet_names}")
   ```
3. **數值格式化處理**：
   - 金額數據輸出時一律格式化為千分位，如 `$1,250,000` 或 `NT$ 4,500,000`。
   - 百分比一律保留小數點後 1-2 位，如 `78.5%`。

---

## 2. 圖表視覺化風格規範 (Matplotlib / Seaborn Styles)

為符合創投 (VC) 簡報與 IC 委員會的高階視覺要求，圖表設計必須遵循以下 Aesthetics：

1. **配色方案 (Color Palette)**：
   - 採用專業創投冷色調與高對比警訊色：
     - 主數據（營收/現金餘額）：濃郁海軍藍 (`#1F4E79`) 或 深青綠 (`#008080`)
     - 次數據（成本/費用）：灰色 (`#808080`) 或 鐵灰 (`#4A5568`)
     - 警訊/燒錢 (Burn/Loss)：暗紅 (`#C00000`) 或 珊瑚紅 (`#E53E3E`)
     - 正向/盈利 (Profit/Growth)：翠綠 (`#2E7D32`)
2. **圖表樣式與佈局**：
   - 使用 `plt.style.use('seaborn-v0_8-whitegrid')` 或自訂乾淨背景。
   - 顯示 Data Labels (數據標籤)，避免讀者需要目測座標軸。
   - 設置 Title、X Label、Y Label，並加粗重要數據趨勢。
3. **中文/雙語字體渲染 (Font Support)**：
   - 避免 matplotlib 輸出中文字體時出現口口亂碼，請加入字體設定：
     ```python
     import matplotlib.pyplot as plt
     
     plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'DejaVu Sans', 'PingFang TC', 'Microsoft JhengHei']
     plt.rcParams['axes.unicode_minus'] = False
     ```

---

## 3. 常見財務圖表模板代碼 (Chart Code Templates)

### 📈 1. 營收 vs OpEx vs 淨利 趨勢圖 (Revenue & Expense Trend)
```python
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(figsize=(10, 5))

# 柱狀圖：總營收與總費用
ax1.bar(df['月份'], df['總營收'], label='Total Revenue', color='#1F4E79', alpha=0.85, width=0.4)
ax1.bar(df['月份'], df['總營業費用'], label='Total OpEx', color='#C00000', alpha=0.5, width=0.4)

ax1.set_ylabel('Amount (USD)', fontsize=12)
ax1.legend(loc='upper left')

# 折線圖：EBITDA / 淨損益
ax2 = ax1.twinx()
ax2.plot(df['月份'], df['EBITDA'], label='EBITDA', color='#2E7D32', marker='o', linewidth=2.5)
ax2.set_ylabel('EBITDA (USD)', fontsize=12)
ax2.legend(loc='upper right')

plt.title('Monthly Financial Performance Trend', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('financial_trend.png', dpi=300)
```

### 📉 2. 期末現金餘額 vs Cash Runway 趨勢圖
```python
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.fill_between(df['月份'], df['期末現金餘額'], color='#1F4E79', alpha=0.3)
ax1.plot(df['月份'], df['期末現金餘額'], color='#1F4E79', marker='s', label='Cash Balance')
ax1.set_ylabel('Ending Cash (USD)', fontsize=12)

# 紅色虛線：6個月安全警戒線
ax2 = ax1.twinx()
ax2.plot(df['月份'], df['Runway Months'], color='#E53E3E', linestyle='--', linewidth=2, label='Runway (Months)')
ax2.axhline(y=6, color='red', linestyle=':', label='6-Mo Safety Limit')
ax2.set_ylabel('Runway (Months)', fontsize=12)

plt.title('Cash Balance & Runway Burn Analysis', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('cash_runway_chart.png', dpi=300)
```
