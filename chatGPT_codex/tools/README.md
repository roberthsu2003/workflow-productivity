# tools（講義維護與數據工具）

本目錄包含教材維護與測試示範數據產生腳本，供講師或維護者使用。

---

## 🛠️ 工具清單

| 檔案 | 用途 | 說明 |
| :--- | :--- | :--- |
| **`validate_structure.py`** | 講義架構與連結完整性檢驗 | 檢查所有章節 README.md 是否齊全、是否有空目錄或 Markdown 死連結。 |
| **`generate_office_files.py`** | 產生 Word / Excel / PPT 測試範例檔 | 產生辦公室檔案供課堂練習上傳與分析。 |
| **`generate_sample_data.py`** | 產生模擬商務銷售數據 CSV | 快速產生結構化資料集供數據分析章節使用。 |

---

## 🔍 執行架構驗證

在終端機中執行：

```bash
python3 tools/validate_structure.py
```

驗證器會自動檢查各單元檔案齊全度與相對連結有效性。

---

← [返回全講義首頁](../README.md)
