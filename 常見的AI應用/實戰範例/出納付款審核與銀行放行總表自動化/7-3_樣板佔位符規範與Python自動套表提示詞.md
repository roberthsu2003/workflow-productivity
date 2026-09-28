# 7-3 樣板佔位符規範與 Python 自動套表提示詞

> 🏆 **本單元核心靈魂**：**Template Placeholder（樣板佔位符）與動態資料列擴展（Dynamic Row Expansion）**  
> 告別「業餘寫死儲存格座標（Hardcoded Coordinates）」的脆弱腳本，邁向能隨意適應 5 筆、50 筆甚至 100 筆傳票的企業級高強韌度自動套表！

---

## 💡 為什麼專業的自動化必須具備「Template Placeholder」觀念？

在企業實務中，出納或行政人員常常需要將 ERP 資料填入公司固定的銀行樣板。許多人初學 Python 或讓 AI 寫腳本時，最常犯的致命錯誤就是**寫死座標（例如 `ws.cell(row=4, column=1) = ...`）**：
* ❌ **致命盲點 1：資料筆數變動即崩潰**  
  若樣板原本在第 4 列到第 8 列預留 5 行空白，第 9 列是「合計」，第 11 列是「簽核欄」。如果本次批次有 20 筆傳票，寫死座標的程式會**直接把「合計列」與「老闆簽名欄」硬生生覆蓋抹消**！
* ❌ **致命盲點 2：財務調整樣式即報銷**  
  如果財務主管哪天在表頭上方插入一列「公司統一編號」，所有 hardcoded 的 row index 全部偏移一列，整個程式徹底故障！
* ✅ **Template Placeholder 解法（樣板驅動文件生成）**：
  1. **職責分離**：樣板視覺（字型、色彩、Logo、簽核欄位）100% 由業務人員在 Excel 裡維護；程式只認**佔位符（Placeholder）**。
  2. **動態行擴展（Dynamic Row Insertion）**：在資料區設定一行「樣式錨點（Anchor Row）」，Python 依實際筆數動態呼叫 `insert_rows` 將下方內容優雅下推，自動繼承字型與邊框，並動態改寫合計 SUM 算式！

---

## 📐 樣板佔位符設計規範（以《樣板_臺企銀單筆付款放行總表.xlsx》為例）

| 佔位符層次 | 標記欄位 | 說明與作用 |
| :--- | :--- | :--- |
| **純量佔位符**<br/>*(Scalar Placeholder)* | `{{FORM_ID}}`<br/>`{{NOTE}}` | 位於表頭或備註。Python 透過全表字串搜尋替換，不論儲存格搬到何處皆能自動命中。 |
| **動態樣板行錨點**<br/>*(Row Template Anchor)* | `{{SEQ}}`<br/>`{{VOUCHER_NO}}`<br/>`{{PAY_DATE}}`<br/>`{{SUMMARY}}`<br/>`{{INCOME}}`<br/>`{{UNPAID}}`<br/>`{{FEE}}`<br/>`{{TOTAL_PAYABLE}}` | 位於明細列起點（如 Row 4）。該行已預先設定好**微軟正黑體、薄灰邊框、置中/靠右、千分位格式（`#,##0`）**。Python 提取其格式作為樣板，動態複製並擴展至 N 筆資料。 |
| **動態公式錨點**<br/>*(Dynamic Formula)* | `=SUM(E4:E4)` | 合計列的 SUM 公式。程式根據動態推移後的起始與結束列，自動改寫為 `=SUM(E{start}:E{end})`。 |

---

## 💬 一鍵執行 Python 套表提示詞（傳送給 AI 執行）

```markdown
請擔任 Python 資料處理專家，針對《素材_應付明細_台幣.xlsx》與《樣板_臺企銀單筆付款放行總表.xlsx》，撰寫並執行 openpyxl 自動套表腳本，生成最終發布檔《出納付款放行總表_已完成.xlsx》：

【業務與資料邏輯】
1. 指定付款到期日：篩選「2026/09/30」（或由參數指定）。
2. GroupBy 分組：依「傳票號碼 + 帳款對象」進行分組，計算發票張數與本幣應付金額加總。
3. 摘要規則：格式化為「應付 [帳款對象]（N筆發票）」。

【Template Placeholder 套表規範（關鍵核心）】
1. 替換純量佔位符：
   - 將樣板內的 `{{FORM_ID}}` 替換為 `FIN115-175`。
   - 將 `{{NOTE}}` 替換為 `本期手續費由公司負擔；單筆大額款項請主管覆核放行。`
2. 定位樣式錨點列：
   - 尋找包含 `{{SEQ}}` 之列（即資料樣板列），提取該列 1~10 欄之字型（Font）、邊框（Border）、對齊（Alignment）與數字格式（Number Format）。
3. 動態行擴展（Dynamic Row Expansion）：
   - 若分組後傳票有 N 筆（N > 1），使用 `ws.insert_rows(tmpl_row + 1, amount=N - 1)` 動態下推下方內容。
   - 逐列寫入序號、傳票號碼、支付日、摘要、本期未付金額、手續費（0）、本期應付公式（`=F{row}+G{row}`）。
   - 將預先提取的樣板格式逐格套用至新插入之儲存格，設定列高為 32。
4. 動態合計公式與簽核欄保護：
   - 自動更新合計列（Summary Row）之 SUM 算式為 `=SUM(F{start}:F{end})`，確保完全覆蓋所有資料列。
   - 確保底部的「核准 / 覆核 / 審核 / 經辦」簽章區域完整保留且自然下推。

請直接執行 Python 腳本並輸出完成檔案！
```

---

## 🐍 核心 Python 自動套表引擎源碼

以下即為完整的生產級 Python 處理腳本，已模組化封裝：

```python
import copy
from collections import defaultdict
import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side


def generate_payment_release_sheet(
    data_path: str,
    template_path: str,
    output_path: str,
    target_date: str = '2026/09/30',
    form_id: str = 'FIN115-175',
    note: str = None,
):
  # 1. 讀取 ERP 原始資料並依 (傳票號碼, 廠商代號) 進行 GroupBy
  wb_data = openpyxl.load_workbook(data_path, data_only=True)
  ws_data = wb_data.active
  rows = list(ws_data.iter_rows(values_only=True))
  header = rows[0]

  col_due_date = header.index('付款到期日')
  col_voucher = header.index('傳票號碼')
  col_vendor = header.index('帳款對象')
  col_amt = header.index('本幣應付金額')

  matched_rows = [r for r in rows[1:] if r[col_due_date] == target_date]
  if not matched_rows:
    raise ValueError(f'找不到指定到期日 {target_date} 的付款資料！')

  grouped = defaultdict(list)
  for r in matched_rows:
    voucher = r[col_voucher]
    vendor = r[col_vendor]
    grouped[(voucher, vendor)].append(r)

  records = []
  for (voucher, vendor), items in grouped.items():
    records.append({
        'voucher': voucher,
        'vendor': vendor,
        'inv_count': len(items),
        'amount': sum(float(it[col_amt] or 0) for it in items),
    })

  # 2. 載入帶有 Template Placeholder 的樣板
  wb_tmpl = openpyxl.load_workbook(template_path)
  ws = wb_tmpl.active

  # 替換純量佔位符並尋找動態資料列錨點 {{SEQ}}
  tmpl_row_idx = None
  for r in range(1, ws.max_row + 1):
    for c in range(1, ws.max_column + 1):
      val = ws.cell(r, c).value
      if isinstance(val, str):
        if '{{FORM_ID}}' in val:
          ws.cell(r, c).value = val.replace('{{FORM_ID}}', form_id)
        if '{{NOTE}}' in val:
          default_note = '本期手續費由公司負擔；請主管覆核放行。'
          ws.cell(r, c).value = val.replace('{{NOTE}}', note or default_note)
        if '{{SEQ}}' in val:
          tmpl_row_idx = r

  if tmpl_row_idx is None:
    raise ValueError('樣板中找不到 {{SEQ}} 錨點列！')

  # 3. 提取樣板錨點列之單元格樣式
  cell_styles = []
  for c in range(1, 11):
    src = ws.cell(tmpl_row_idx, c)
    cell_styles.append({
        'font': copy.copy(src.font),
        'border': copy.copy(src.border),
        'alignment': copy.copy(src.alignment),
        'number_format': src.number_format,
    })

  n_records = len(records)

  # 4. 動態向下擴展列數（保護簽核欄）
  if n_records > 1:
    ws.insert_rows(tmpl_row_idx + 1, amount=n_records - 1)

  # 5. 填入明細資料並套用樣式
  for i, rec in enumerate(records):
    cur_row = tmpl_row_idx + i
    ws.row_dimensions[cur_row].height = 32

    row_vals = [
        i + 1,  # 序號
        rec['voucher'],  # 傳票編號
        target_date,  # 支付日
        f"應付 {rec['vendor']}（{rec['inv_count']}筆發票）",  # 摘要
        None,  # 本期收入
        rec['amount'],  # 本期未付
        0,  # 手續費
        f'=F{cur_row}+G{cur_row}',  # 應付合計公式
        None,  # 結餘
        None,  # 銀行交易序號
    ]

    for c in range(1, 11):
      cell = ws.cell(cur_row, c)
      cell.value = row_vals[c - 1]
      st = cell_styles[c - 1]
      if st['font']:
        cell.font = copy.copy(st['font'])
      if st['border']:
        cell.border = copy.copy(st['border'])
      if st['alignment']:
        cell.alignment = copy.copy(st['alignment'])
      if st['number_format']:
        cell.number_format = st['number_format']

  # 6. 動態改寫合計列 SUM 公式
  summary_row = tmpl_row_idx + n_records
  start_row = tmpl_row_idx
  end_row = tmpl_row_idx + n_records - 1

  ws.cell(summary_row, 5).value = f'=SUM(E{start_row}:E{end_row})'
  ws.cell(summary_row, 6).value = f'=SUM(F{start_row}:F{end_row})'
  ws.cell(summary_row, 7).value = f'=SUM(G{start_row}:G{end_row})'
  ws.cell(summary_row, 8).value = f'=SUM(H{start_row}:H{end_row})'

  wb_tmpl.save(output_path)
  print(f'✅ 成功產出：{output_path}（共 {n_records} 筆傳票放行）')


if __name__ == '__main__':
  generate_payment_release_sheet(
      data_path='素材_應付明細_台幣.xlsx',
      template_path='樣板_臺企銀單筆付款放行總表.xlsx',
      output_path='出納付款放行總表_已完成.xlsx',
      target_date='2026/09/30',
  )
```
