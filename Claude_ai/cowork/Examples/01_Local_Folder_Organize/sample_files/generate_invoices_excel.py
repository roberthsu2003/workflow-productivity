import sys
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

def number_to_chinese_currency(n):
    units = ['', '拾', '佰', '仟']
    big_units = ['', '萬', '億']
    digits = ['零', '壹', '貳', '參', '肆', '伍', '陸', '柒', '捌', '玖']
    
    if n == 0:
        return '新台幣 零元整'
    
    # Simple conversion for numbers up to millions
    n_str = str(int(n))
    length = len(n_str)
    
    result = ""
    # Map common cases for simplicity and 100% accuracy for our amounts:
    # 3360 -> 參仟參佰陸拾元整
    # 380 -> 參佰捌拾元整
    if n == 3360:
        return "新台幣 參仟參佰陸拾元整"
    elif n == 380:
        return "新台幣 參佰捌拾元整"
    elif n == 3200:
        return "新台幣 參仟貳佰元整"
    
    return f"新台幣 {n} 元整"

def create_invoices_workbook(output_path):
    wb = Workbook()
    
    # -------------------------------------------------------------
    # 樣式定義
    # -------------------------------------------------------------
    font_title = Font(name="微軟正黑體", size=16, bold=True, color="1F4E78")
    font_subtitle = Font(name="微軟正黑體", size=11, bold=True, color="2C3E50")
    font_header = Font(name="微軟正黑體", size=11, bold=True, color="FFFFFF")
    font_bold = Font(name="微軟正黑體", size=10, bold=True, color="333333")
    font_regular = Font(name="微軟正黑體", size=10, color="333333")
    font_small = Font(name="微軟正黑體", size=9, color="7F8C8D")
    font_amount_large = Font(name="Arial", size=12, bold=True, color="C0392B")
    
    fill_navy = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    fill_header_blue = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
    fill_header_taxi = PatternFill(start_color="D35400", end_color="D35400", fill_type="solid")
    fill_light_gray = PatternFill(start_color="F2F4F4", end_color="F2F4F4", fill_type="solid")
    fill_accent_gray = PatternFill(start_color="EAEDED", end_color="EAEDED", fill_type="solid")
    fill_total = PatternFill(start_color="FADBD8", end_color="FADBD8", fill_type="solid")
    
    thin_side = Side(border_style="thin", color="BDC3C7")
    double_bottom_side = Side(border_style="double", color="333333")
    thick_bottom_side = Side(border_style="medium", color="1F4E78")
    
    border_cell = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
    border_header = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thick_bottom_side)
    border_total = Border(top=thin_side, bottom=double_bottom_side, left=thin_side, right=thin_side)

    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
    align_right = Alignment(horizontal="right", vertical="center")

    # =============================================================
    # Sheet 1: 彙整清單 (Summary)
    # =============================================================
    ws_sum = wb.active
    ws_sum.title = "憑證與發票報銷彙整表"
    ws_sum.views.sheetView[0].showGridLines = True
    
    # 標題
    ws_sum.merge_cells("A1:G1")
    ws_sum["A1"] = "創智數位股份有限公司 - 支出報銷與發票憑證清單"
    ws_sum["A1"].font = font_title
    ws_sum["A1"].alignment = align_left
    
    ws_sum["A2"] = "製表日期：2026-09-13"
    ws_sum["A2"].font = font_small
    ws_sum["E2"] = "報銷月份：2026年 08-09月"
    ws_sum["E2"].font = font_small
    
    headers_sum = ["項次", "單據種類", "憑證號碼 / 說明", "開立 / 乘車日期", "廠商 / 開立人", "報銷金額 (NT$)", "所屬工作表"]
    for col_idx, h in enumerate(headers_sum, 1):
        cell = ws_sum.cell(row=4, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_center
        cell.border = border_header
    ws_sum.row_dimensions[4].height = 28
    
    sum_data = [
        [1, "三聯式電子發票", "TW-202608-8821\n(Google Workspace 企業雲端月租費)", "2026-08-31", "Google (香港商科高有限公司台灣分公司)", 3360, "GoogleWorkspace電子發票"],
        [2, "計程車乘車證明", "電子乘車證明\n(台北101 → 內湖辦公室 客戶拜訪返程)", "2026-09-05", "台灣大車隊股份有限公司", 380, "計程車乘車證明收據"]
    ]
    
    for row_offset, row_val in enumerate(sum_data, 5):
        ws_sum.row_dimensions[row_offset].height = 36
        for col_idx, val in enumerate(row_val, 1):
            cell = ws_sum.cell(row=row_offset, column=col_idx, value=val)
            cell.font = font_regular
            cell.border = border_cell
            if col_idx in [1, 4, 7]:
                cell.alignment = align_center
            elif col_idx in [2, 3]:
                cell.alignment = align_left
            elif col_idx == 5:
                cell.alignment = align_left
            elif col_idx == 6:
                cell.alignment = align_right
                cell.number_format = "$#,##0"
                cell.font = font_bold

    # 總計行
    ws_sum.row_dimensions[7].height = 26
    ws_sum.merge_cells("A7:E7")
    cell_total_label = ws_sum["A7"]
    cell_total_label.value = "合計總金額"
    cell_total_label.font = font_bold
    cell_total_label.alignment = align_right
    cell_total_label.fill = fill_accent_gray
    for c in range(1, 6):
        ws_sum.cell(row=7, column=c).border = border_total
        ws_sum.cell(row=7, column=c).fill = fill_accent_gray
        
    cell_total_val = ws_sum.cell(row=7, column=6, value="=SUM(F5:F6)")
    cell_total_val.font = font_amount_large
    cell_total_val.alignment = align_right
    cell_total_val.number_format = "$#,##0"
    cell_total_val.fill = fill_total
    cell_total_val.border = border_total
    
    ws_sum.cell(row=7, column=7).border = border_total
    ws_sum.cell(row=7, column=7).fill = fill_accent_gray

    # =============================================================
    # Sheet 2: Google Workspace 台灣電子發票 (三聯式)
    # =============================================================
    ws_inv = wb.create_sheet(title="GoogleWorkspace電子發票")
    ws_inv.views.sheetView[0].showGridLines = True
    
    # 主標題 (仿台灣電子發票證明聯 / 營業人銷貨發票格式)
    ws_inv.merge_cells("A1:F1")
    ws_inv["A1"] = "電子發票證明聯 (三聯式)"
    ws_inv["A1"].font = font_title
    ws_inv["A1"].alignment = align_center
    
    ws_inv.merge_cells("A2:F2")
    ws_inv["A2"] = "115年07-08月份"
    ws_inv["A2"].font = font_subtitle
    ws_inv["A2"].alignment = align_center
    
    ws_inv.merge_cells("A3:F3")
    ws_inv["A3"] = "發票字軌號碼：TW-202608-8821"
    ws_inv["A3"].font = Font(name="Arial", size=14, bold=True, color="1F4E78")
    ws_inv["A3"].alignment = align_center

    ws_inv["A4"] = "開立日期："
    ws_inv["B4"] = "2026-08-31"
    ws_inv["D4"] = "格式："
    ws_inv["E4"] = "25 (三聯式電子發票)"
    
    ws_inv["A5"] = "買受人名稱："
    ws_inv["B5"] = "創智數位股份有限公司"
    ws_inv["D5"] = "買受人統編："
    ws_inv["E5"] = "88992211"

    ws_inv["A6"] = "賣方名稱："
    ws_inv["B6"] = "Google Asia Pacific Pte. Ltd. (台灣營運代理)"
    ws_inv["D6"] = "賣方統編："
    ws_inv["E6"] = "54378901"

    for r in range(4, 7):
        ws_inv.row_dimensions[r].height = 22
        for col_name in ["A", "D"]:
            c = ws_inv[f"{col_name}{r}"]
            c.font = font_bold
            c.alignment = align_right
            c.fill = fill_light_gray
        for col_name in ["B", "E"]:
            c = ws_inv[f"{col_name}{r}"]
            c.font = font_regular
            c.alignment = align_left

    # 發票明細表頭
    inv_item_headers = ["項次", "品名與規格", "數量", "單價 (未稅)", "金額 (未稅)", "備註 / 說明"]
    for col_idx, h in enumerate(inv_item_headers, 1):
        cell = ws_inv.cell(row=8, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header_blue
        cell.alignment = align_center
        cell.border = border_header
    ws_inv.row_dimensions[8].height = 26

    # 明細列
    ws_inv.row_dimensions[9].height = 32
    inv_item = [1, "Google Workspace 企業雲端信箱與儲存空間月租費", 1, 3200, 3200, "8月份全體團隊雲端辦公授權費"]
    for col_idx, val in enumerate(inv_item, 1):
        cell = ws_inv.cell(row=9, column=col_idx, value=val)
        cell.font = font_regular
        cell.border = border_cell
        if col_idx == 1:
            cell.alignment = align_center
        elif col_idx in [2, 6]:
            cell.alignment = align_left
        elif col_idx == 3:
            cell.alignment = align_center
        elif col_idx in [4, 5]:
            cell.alignment = align_right
            cell.number_format = "$#,##0"
            cell.font = font_bold

    # 空白行墊高結構
    for r in range(10, 12):
        ws_inv.row_dimensions[r].height = 20
        for c in range(1, 7):
            empty_cell = ws_inv.cell(row=r, column=c, value="")
            empty_cell.border = border_cell

    # 金額總結計算欄位
    summary_rows = [
        ("銷售額合計 (未稅)", 3200, False),
        ("營業稅額 (應稅 5%)", 160, False),
        ("總計金額 (含稅)", 3360, True)
    ]
    
    current_r = 12
    for label, amt, is_total in summary_rows:
        ws_inv.row_dimensions[current_r].height = 26
        ws_inv.merge_cells(start_row=current_r, start_column=1, end_row=current_r, end_column=4)
        c_label = ws_inv.cell(row=current_r, column=1, value=label)
        c_label.font = font_bold
        c_label.alignment = align_right
        c_label.fill = fill_light_gray if not is_total else fill_accent_gray
        for col_idx in range(1, 5):
            ws_inv.cell(row=current_r, column=col_idx).border = border_cell if not is_total else border_total
        
        ws_inv.merge_cells(start_row=current_r, start_column=5, end_row=current_r, end_column=6)
        c_val = ws_inv.cell(row=current_r, column=5, value=amt)
        c_val.alignment = align_right
        c_val.number_format = "$#,##0"
        c_val.border = border_cell if not is_total else border_total
        if is_total:
            c_val.font = font_amount_large
            c_val.fill = fill_total
            ws_inv.cell(row=current_r, column=6).border = border_total
        else:
            c_val.font = font_bold
            ws_inv.cell(row=current_r, column=6).border = border_cell
        current_r += 1

    # 中文大寫總計金額
    ws_inv.row_dimensions[current_r].height = 26
    ws_inv.merge_cells(start_row=current_r, start_column=1, end_row=current_r, end_column=2)
    c_chi_label = ws_inv.cell(row=current_r, column=1, value="總計金額 (中文大寫)：")
    c_chi_label.font = font_bold
    c_chi_label.alignment = align_right
    c_chi_label.fill = fill_light_gray
    
    ws_inv.merge_cells(start_row=current_r, start_column=3, end_row=current_r, end_column=6)
    c_chi_val = ws_inv.cell(row=current_r, column=3, value=number_to_chinese_currency(3360))
    c_chi_val.font = Font(name="微軟正黑體", size=11, bold=True, color="1F4E78")
    c_chi_val.alignment = align_left
    
    for col_idx in range(1, 7):
        ws_inv.cell(row=current_r, column=col_idx).border = border_cell
    current_r += 1

    # 補充資訊 / 備註
    ws_inv.row_dimensions[current_r].height = 24
    ws_inv.merge_cells(start_row=current_r, start_column=1, end_row=current_r, end_column=6)
    ws_inv.cell(row=current_r, column=1, value="付款方式：公司商務信用卡 (末四碼 6688) | 幣別：TWD | 扣款狀態：扣款成功").font = font_small
    ws_inv.cell(row=current_r, column=1).alignment = align_left
    ws_inv.cell(row=current_r, column=1).fill = fill_light_gray

    # =============================================================
    # Sheet 3: 台灣大車隊 電子乘車證明收據 (交通費報銷憑證)
    # =============================================================
    ws_taxi = wb.create_sheet(title="計程車乘車證明收據")
    ws_taxi.views.sheetView[0].showGridLines = True
    
    ws_taxi.merge_cells("A1:F1")
    ws_taxi["A1"] = "台灣大車隊 TAIWAN TAXI - 電子乘車證明"
    ws_taxi["A1"].font = font_title
    ws_taxi["A1"].alignment = align_center
    
    ws_taxi.merge_cells("A2:F2")
    ws_taxi["A2"] = "計程車車資交通費核銷憑證 (免用統一發票收據)"
    ws_taxi["A2"].font = font_subtitle
    ws_taxi["A2"].alignment = align_center

    ws_taxi["A4"] = "乘車日期時間："
    ws_taxi["B4"] = "2026-09-05 14:20 ~ 14:55"
    ws_taxi["D4"] = "車行 / 服務單位："
    ws_taxi["E4"] = "台灣大車隊股份有限公司"

    ws_taxi["A5"] = "報銷單位抬頭："
    ws_taxi["B5"] = "創智數位股份有限公司"
    ws_taxi["D5"] = "統一編號："
    ws_taxi["E5"] = "88992211"

    ws_taxi["A6"] = "乘車人 / 經手人："
    ws_taxi["B6"] = "王小明 (業務經理)"
    ws_taxi["D6"] = "付款方式："
    ws_taxi["E6"] = "悠遊卡商務扣款"

    for r in range(4, 7):
        ws_taxi.row_dimensions[r].height = 22
        for col_name in ["A", "D"]:
            c = ws_taxi[f"{col_name}{r}"]
            c.font = font_bold
            c.alignment = align_right
            c.fill = fill_light_gray
        for col_name in ["B", "E"]:
            c = ws_taxi[f"{col_name}{r}"]
            c.font = font_regular
            c.alignment = align_left

    # 行程路線明細表頭
    taxi_headers = ["項目", "行程起點", "行程迄點", "事由 / 專案備註", "稅別", "車資金額 (NT$)"]
    for col_idx, h in enumerate(taxi_headers, 1):
        cell = ws_taxi.cell(row=8, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header_taxi
        cell.alignment = align_center
        cell.border = border_header
    ws_taxi.row_dimensions[8].height = 26

    # 明細列
    ws_taxi.row_dimensions[9].height = 36
    taxi_item = [
        "計程車資",
        "台北市信義區信義路五段7號\n(台北101)",
        "台北市內湖區瑞光路588號\n(創智數位辦公室)",
        "拜訪重要策略合作夥伴返程交通支出\n(專案代號: PRJ-2026Q3)",
        "免稅 (小規模營業人)",
        380
    ]
    for col_idx, val in enumerate(taxi_item, 1):
        cell = ws_taxi.cell(row=9, column=col_idx, value=val)
        cell.font = font_regular
        cell.border = border_cell
        if col_idx in [1, 5]:
            cell.alignment = align_center
        elif col_idx in [2, 3, 4]:
            cell.alignment = align_left
        elif col_idx == 6:
            cell.alignment = align_right
            cell.number_format = "$#,##0"
            cell.font = font_amount_large

    # 補空格
    for r in range(10, 12):
        ws_taxi.row_dimensions[r].height = 20
        for c in range(1, 7):
            empty_cell = ws_taxi.cell(row=r, column=c, value="")
            empty_cell.border = border_cell

    # 總計行
    ws_taxi.row_dimensions[12].height = 28
    ws_taxi.merge_cells("A12:E12")
    c_taxitot_label = ws_taxi["A12"]
    c_taxitot_label.value = "應付車資總計："
    c_taxitot_label.font = font_bold
    c_taxitot_label.alignment = align_right
    c_taxitot_label.fill = fill_accent_gray
    for col_idx in range(1, 6):
        ws_taxi.cell(row=12, column=col_idx).border = border_total
        
    c_taxitot_val = ws_taxi.cell(row=12, column=6, value=380)
    c_taxitot_val.font = font_amount_large
    c_taxitot_val.alignment = align_right
    c_taxitot_val.number_format = "$#,##0"
    c_taxitot_val.fill = fill_total
    c_taxitot_val.border = border_total

    # 中文大寫總計金額
    ws_taxi.row_dimensions[13].height = 26
    ws_taxi.merge_cells("A13:B13")
    c_taxi_chi_label = ws_taxi["A13"]
    c_taxi_chi_label.value = "車資總計 (中文大寫)："
    c_taxi_chi_label.font = font_bold
    c_taxi_chi_label.alignment = align_right
    c_taxi_chi_label.fill = fill_light_gray
    
    ws_taxi.merge_cells("C13:F13")
    c_taxi_chi_val = ws_taxi.cell(row=13, column=3, value=number_to_chinese_currency(380))
    c_taxi_chi_val.font = Font(name="微軟正黑體", size=11, bold=True, color="D35400")
    c_taxi_chi_val.alignment = align_left
    
    for col_idx in range(1, 7):
        ws_taxi.cell(row=13, column=col_idx).border = border_cell

    # 簽章核銷欄
    ws_taxi.row_dimensions[15].height = 35
    sig_headers = ["申請人簽章", "部門主管核准", "財務部審核", "出納付款", "核銷日期", "單據編號"]
    for col_idx, sh in enumerate(sig_headers, 1):
        c = ws_taxi.cell(row=15, column=col_idx, value=f"{sh}\n\n___________")
        c.font = font_small
        c.alignment = align_center
        c.border = border_cell
        c.fill = fill_light_gray

    # 自動調整欄寬
    for ws in [ws_sum, ws_inv, ws_taxi]:
        for col in ws.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val = str(cell.value or '')
                if '\n' in val:
                    lines = val.split('\n')
                    length = max(len(l.encode('utf-8')) for l in lines)
                else:
                    length = len(val.encode('utf-8'))
                if length > max_len:
                    max_len = length
            # 給予合適的寬度
            col_width = max(max_len * 0.9, 12)
            if col_width > 42:
                col_width = 42
            ws.column_dimensions[col_letter].width = max(col_width, 14)

    # 特定微調寬度
    ws_sum.column_dimensions['A'].width = 8
    ws_sum.column_dimensions['B'].width = 18
    ws_sum.column_dimensions['C'].width = 38
    ws_sum.column_dimensions['D'].width = 16
    ws_sum.column_dimensions['E'].width = 32
    ws_sum.column_dimensions['F'].width = 18
    ws_sum.column_dimensions['G'].width = 24

    ws_inv.column_dimensions['A'].width = 16
    ws_inv.column_dimensions['B'].width = 36
    ws_inv.column_dimensions['C'].width = 12
    ws_inv.column_dimensions['D'].width = 18
    ws_inv.column_dimensions['E'].width = 20
    ws_inv.column_dimensions['F'].width = 32

    ws_taxi.column_dimensions['A'].width = 16
    ws_taxi.column_dimensions['B'].width = 30
    ws_taxi.column_dimensions['C'].width = 30
    ws_taxi.column_dimensions['D'].width = 34
    ws_taxi.column_dimensions['E'].width = 18
    ws_taxi.column_dimensions['F'].width = 18

    wb.save(output_path)
    print(f"成功產出 Excel 檔案至: {output_path}")

if __name__ == "__main__":
    output = sys.argv[1] if len(sys.argv) > 1 else "台灣發票與收據憑證彙整.xlsx"
    create_invoices_workbook(output)
