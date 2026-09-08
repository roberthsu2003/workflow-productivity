# tools

講義維護用的輔助腳本，**不是教材內容**。

| 檔案 | 用途 | 需要的套件 |
| :--- | :--- | :--- |
| `generate_sample_data.py` | 產生 CSV 資料 | 無（標準庫） |
| `generate_office_files.py` | 產生 xlsx / pptx / docx / png 示範檔 | openpyxl、python-pptx、python-docx、pillow |
| `generate_skill_templates.py` | 產生 skill 範本與模擬掃描件 | openpyxl、pillow |
| `validate_structure.py` | 檢查必備章節、案例入口、空目錄與相對連結 | 無（標準庫） |

## 驗證整套講義架構

```bash
python3 chatGPT_codex/tools/validate_structure.py
```

成功時會列出通過檢查的必備目錄、Markdown 與全部檔案數；失敗時會逐項列出缺少的入口或失效連結。

## 重新產生示範資料

```bash
cd chatGPT_codex

# 1. CSV（不需額外套件）
python3 tools/generate_sample_data.py

# 2. Office 格式與圖片（需建虛擬環境）
python3 -m venv /tmp/codexdocs
/tmp/codexdocs/bin/pip install openpyxl python-pptx python-docx pillow
/tmp/codexdocs/bin/python tools/generate_office_files.py
/tmp/codexdocs/bin/python tools/generate_skill_templates.py
```

腳本使用固定亂數種子（`20260908`），**每次執行結果完全相同**，因此重新產生不會造成講義與資料不一致。

### 資料中刻意植入的「教學埋伏」

修改腳本時請保留這三項，多個章節的解答都依賴它們：

| 埋伏 | 位置 | 用於教什麼 |
| :--- | :--- | :--- |
| **真異常** | 東區 2026-08，準時率 81.3%，備註「颱風封路」 | 有證據支持的真實異常 |
| **離群但正常** | 南區 2026-11，單量 2.3 倍，備註「雙 11 檔期」 | 數字奇怪 ≠ 有問題 |
| **資料缺漏** | 中區 2026-06，整列空白，備註「WMS 移轉未落帳」 | **不可用 0 代替或內插** |

依賴這些埋伏的章節：
- [Drive 跨檔分析](../Connectors/01_Google_Workspace/01_Drive_Analysis/README.md)
- [商業情報](../Projects/Examples/03_Business_Intelligence/README.md)
- [配送績效互動儀表板](../Visualizations/Examples/01_Delivery_Dashboard/README.md)

---

← [返回索引](../README.md)
