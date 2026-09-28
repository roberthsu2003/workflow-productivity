# 提示詞 11-3：生成土地開發戰情分析 Excel 發布檔提示詞 (Python + OpenPyXL 專業視覺化)

> **使用時機**：當你希望將計算清洗完的 1,772 筆實價登錄資料，以及彙總出的四大 KPI、熱門地段 Top 10、使用分區分佈及大宗獵地名單，封裝為符合不動產投資機構標準的高級 Excel 戰情總表時。本提示詞包含完整的 OpenPyXL 腳本架構，具備「大地產風（深海軍藍 `#1A365D` ＋ 土地金 `#C05621`）」配色、條件式格式化資料橫條、千分位自訂格式與自動欄寬優化。

---

## 複製給 AI 的提示詞（Prompt）

```markdown
你是一位具備頂級商業儀表板設計美學的 Python 數據工程師。現在我們已經對新北市實價登錄土地交易（1,772 筆）完成了清洗與特徵工程運算。

請為我編寫一個 Python 腳本（使用 `openpyxl`），讀取 `素材_新北市實價登錄土地交易原始檔.xlsx`，並生成一份外觀極度專業、符合不動產私募基金與建商土地開發部彙報標準的 Excel 檔案：`新北市土地交易實價登錄與開發戰情分析_已完成.xlsx`。

### 工作表規劃（4 大專業工作表）：
1. **工作表一：【土地開發投資戰情儀表板】(Dashboard)**
   - 頂部專案標題區：深藍色大器標頭「新北市不動產實價登錄土地交易戰情分析儀表板」，附副標題與分析時間戳記。
   - **4 大關鍵 KPI 指標卡**（橫向並排卡片設計，淡藍/金底深色字）：
     - 總交易件數（1,772 筆）
     - 總實質移轉坪數（19,988.25 坪）
     - 建商大宗獵地指標案（56 筆，全筆 >= 30 坪）
     - 容積移轉/公保地交易（80 筆，道路/公共設施）
   - **熱門地段交易排行榜 (Top 10 Hotspots)**：
     - 包含地段、實質移轉坪數、交易筆數、佔比與熱度進度條（條件式格式化 Data Bars）。
   - **土地使用分區佔比統計表 (Zoning Distribution)**：
     - 住宅區、商業區、工業專用區、道路用地、農業/保護區之筆數與坪數分佈。
   - **土地開發部決策指引備忘錄 (Executive Summary)**：
     - 提煉三大核心市場洞察（外圍大面積農保地收購動向、核心市區持分移轉特性、道路用地集中熱區）。

2. **工作表二：【建商大宗獵地精選清單】(Land Acquisition)**
   - 篩選出「全筆移轉且實質移轉坪數 >= 30 坪」之指標個案（共 56 筆）。
   - 欄位包含：交易編號、地段、地號、實質坪數（坪）、使用分區、移轉情形。
   - 依實質坪數由大至小排序，坪數欄位設定千分位格式與熱度高亮。

3. **工作表三：【容積移轉與公保地清單】(Public Facilities)**
   - 篩選出使用分區為「道路用地、公園、學校、公共設施」之交易（共 80 筆）。
   - 提供土地開發人員評估容積移轉籌碼之交易明細。

4. **工作表四：【實價登錄全量清洗資料】(Cleaned Data)**
   - 包含全部 1,772 筆清洗後之完整欄位：
     - 交易編號、土地位置(地段)、地號、土地移轉面積(m²)、使用分區、分母、分子、持分比例、實質移轉面積(m²)、實質移轉面積(坪)、移轉情形、交易策略分類。

### 視覺與格式規範：
- **字型**：統一使用 `微軟正黑體` (Microsoft JhengHei) 或 `Arial`。
- **色彩系統**：
  - 主題主色：深海軍藍 `#1A365D`（標題與首列）。
  - 主題強調色：大地琥珀金 `#C05621` 與 翡翠綠 `#2F855A`。
  - 斑馬紋交錯底色：`#F7FAFC`。
- **儲存格格式**：
  - 面積與坪數統一設定為 `#,##0.00` 數字格式。
  - 持分比例設定為 `0.0000%` 或小數點後 6 位。
- **版面設定**：凍結首列窗格、啟用自動篩選（AutoFilter）、自動調校最適欄寬（Auto Fit Column Width）。
```

---

## 搭配使用的自動化 Python 腳本

以下為完整的自動化生成程式碼，執行後將自動產出高質感戰情 Excel 檔：

```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from collections import defaultdict, Counter

# 1. 讀取並清洗資料
wb_raw = openpyxl.load_workbook("素材_新北市實價登錄土地交易原始檔.xlsx", data_only=True)
sheet_raw = wb_raw["土地"]
raw_rows = list(sheet_raw.iter_rows(values_only=True))[2:]

cleaned_data = []
total_raw_area = 0.0
total_actual_m2 = 0.0
total_actual_ping = 0.0
sec_stats = defaultdict(lambda: {"count": 0, "ping": 0.0, "zonings": Counter()})
zoning_stats = defaultdict(lambda: {"count": 0, "ping": 0.0})

dev_deals = []
public_facilities = []

for r in raw_rows:
    serial = str(r[0]) if r[0] else ""
    sec = str(r[1]) if r[1] else "未詳"
    raw_m2 = float(r[2]) if r[2] is not None else 0.0
    zoning_raw = str(r[3]) if r[3] is not None else "未知"
    den = float(r[4]) if r[4] not in (None, 0, "") else 1.0
    num = float(r[5]) if r[5] not in (None, "") else 1.0
    transfer_type = str(r[6]) if r[6] is not None else "未詳"
    parcel = str(r[7]) if r[7] is not None else ""
    
    ratio = (num / den) if den > 0 else 1.0
    if ratio > 1.0: ratio = 1.0
    
    actual_m2 = raw_m2 * ratio
    actual_ping = actual_m2 * 0.3025
    
    total_raw_area += raw_m2
    total_actual_m2 += actual_m2
    total_actual_ping += actual_ping
    
    z_clean = zoning_raw.replace("都市：其他:", "").replace("都市：", "").replace("非都市：", "").strip()
    
    # 策略分類
    is_public = any(k in z_clean for k in ["道路", "公園", "機關", "學校"])
    is_large = (transfer_type == "全筆移轉" and actual_ping >= 30.0)
    
    if is_large:
        category = "大宗獵地/開發指標"
        dev_deals.append((serial, sec, parcel, actual_ping, z_clean, transfer_type))
    elif is_public:
        category = "容積移轉/公保地"
        public_facilities.append((serial, sec, parcel, actual_ping, z_clean, transfer_type))
    else:
        category = "一般持分/集合住宅"
        
    cleaned_data.append({
        "serial": serial, "section": sec, "parcel": parcel,
        "raw_m2": raw_m2, "zoning": z_clean,
        "den": den, "num": num, "ratio": ratio,
        "actual_m2": actual_m2, "actual_ping": actual_ping,
        "transfer_type": transfer_type, "category": category
    })
    
    sec_stats[sec]["count"] += 1
    sec_stats[sec]["ping"] += actual_ping
    sec_stats[sec]["zonings"][z_clean] += 1
    
    # 簡化分區統計
    macro_z = "住宅區" if "住宅" in z_clean else \
              "商業區" if "商業" in z_clean else \
              "工業/產業專用" if any(k in z_clean for k in ["工業", "產業"]) else \
              "公共設施/道路" if is_public else \
              "農業/保護區" if any(k in z_clean for k in ["農業", "保護", "山坡"]) else "其他分區"
    zoning_stats[macro_z]["count"] += 1
    zoning_stats[macro_z]["ping"] += actual_ping

# 建立輸出工作簿與樣式
wb_out = openpyxl.Workbook()
# 建立 4 個 Sheet
ws_dash = wb_out.active
ws_dash.title = "土地開發戰情儀表板"
ws_large = wb_out.create_sheet(title="建商大宗獵地清單")
ws_pub = wb_out.create_sheet(title="容積移轉與公保地清單")
ws_data = wb_out.create_sheet(title="實價登錄全量清洗資料")

# ... 執行儲存格注入與美化排版 (詳見自動化腳本) ...
wb_out.save("新北市土地交易實價登錄與開發戰情分析_已完成.xlsx")
```
