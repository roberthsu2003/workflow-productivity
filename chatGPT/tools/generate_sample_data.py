#!/usr/bin/env python3
"""產生 chatGPT_codex 講義用的示範資料（潮汐物流 / 麥禾烘焙）。

刻意植入教學用的「埋伏」：
  - 東區 8 月準時率崩跌（真異常，可從異常件數與颱風備註佐證）
  - 中區 6 月資料缺漏（空值，不可用 0 代替）
  - 南區單量離群（雙 11 檔期，是真的，不是錯誤）
  - 客訴數與準時率的相關性（可被發現的洞察）
資料皆為教學虛構，與真實公司無關。
"""
import csv
import random
from pathlib import Path

random.seed(20260908)
BASE = Path(__file__).parent

REGIONS = [("North", "北區"), ("Central", "中區"), ("South", "南區"), ("East", "東區")]

# (region_code, month) -> (單量, 準時率, 平均配送時數, 異常件數, 客訴件數, 備註)
BASELINE = {
    "North":   (base := 18500, 97.8, 26.4),
    "Central": (12400, 96.9, 28.1),
    "South":   (15200, 96.2, 31.5),
    "East":    (6800, 95.4, 38.2),
}


def rows_for(months, with_anomalies=True):
    out = []
    for m in months:
        for code, name in REGIONS:
            vol, otr, hrs = BASELINE[code]
            vol = int(vol * random.uniform(0.92, 1.10))
            otr = round(otr + random.uniform(-1.2, 1.2), 1)
            hrs = round(hrs + random.uniform(-2.5, 2.5), 1)
            note = ""

            if with_anomalies:
                # 埋伏一：東區 8 月颱風，準時率崩跌
                if code == "East" and m == 8:
                    otr, hrs, note = 81.3, 62.7, "0812-0815 颱風封路，山區線全面停駛"
                # 埋伏二：中區 6 月系統移轉，資料缺漏
                if code == "Central" and m == 6:
                    out.append([f"2026-{m:02d}", code, name, "", "", "", "", "", "WMS 系統移轉期間未落帳"])
                    continue
                # 埋伏三：南區 11 月雙 11 單量暴增（真實，非錯誤）
                if code == "South" and m == 11:
                    vol = int(vol * 2.35)
                    otr = round(otr - 3.8, 1)
                    note = "雙 11 檔期，單量為平時 2.3 倍"

            abnormal = int(vol * (100 - otr) / 100 * random.uniform(0.55, 0.85))
            # 客訴與異常件數正相關，但比例遠低
            complaints = int(abnormal * random.uniform(0.08, 0.16))
            out.append([f"2026-{m:02d}", code, name, vol, otr, hrs, abnormal, complaints, note])
    return out


HEADER = ["月份", "區域代碼", "區域名稱", "配送單量", "準時率(%)",
          "平均配送時數", "異常件數", "客訴件數", "備註"]


def write_csv(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"  {path.relative_to(BASE)}  ({len(rows)} 列)")


print("產生配送績效資料：")
# Q1 / Q2 分檔（供 Projects BI 範例做跨檔比對）
write_csv(BASE / "Projects/Examples/03_Business_Intelligence/sample_files/配送績效_2026Q1.csv",
          HEADER, rows_for([1, 2, 3]))
write_csv(BASE / "Projects/Examples/03_Business_Intelligence/sample_files/配送績效_2026Q2.csv",
          HEADER, rows_for([4, 5, 6]))
# 全年整併檔（供 Drive 分析與 Visualizations 使用）
full = rows_for(list(range(1, 13)))
write_csv(BASE / "Connectors/01_Google_Workspace/01_Drive_Analysis/sample_files/潮汐物流_2026全年配送績效與客訴分析表.csv",
          HEADER, full)
write_csv(BASE / "Visualizations/Examples/01_Delivery_Dashboard/sample_files/delivery_performance_2026.csv",
          HEADER, full)

# 區域代碼對照表
print("產生區域代碼對照表：")
zone_rows = [
    ["North", "北區", "基隆市、臺北市、新北市、桃園市", "1", "是"],
    ["Central", "中區", "新竹縣市、苗栗縣、臺中市、彰化縣、南投縣", "2", "是"],
    ["South", "南區", "雲林縣、嘉義縣市、臺南市、高雄市、屏東縣", "2", "部分"],
    ["East", "東區", "宜蘭縣、花蓮縣、臺東縣", "3", "否"],
    ["Islands", "離島", "澎湖縣、金門縣、連江縣", "5", "否"],
]
write_csv(BASE / "Projects/Examples/03_Business_Intelligence/sample_files/區域代碼對照表.csv",
          ["區域代碼", "區域名稱", "涵蓋縣市", "標準工作天", "支援當日配"], zone_rows)

# 庫存監控資料（供 Automations 範例）
print("產生庫存監控資料：")
items = [
    ("BX-1001", "標準紙箱 60cm", 8400, 3000, 1250),
    ("BX-1002", "標準紙箱 40cm", 12600, 4000, 1880),
    ("BX-1003", "冷鏈保溫箱", 640, 800, 145),      # 已低於安全水位
    ("TP-2001", "封箱膠帶(箱)", 3200, 1200, 410),
    ("TP-2002", "易碎品標籤(捲)", 180, 500, 95),    # 已低於安全水位
    ("PL-3001", "棧板 標準規格", 520, 300, 22),
    ("CL-4001", "乾冰(kg)", 240, 200, 118),        # 2 天內將歸零
    ("BG-5001", "防撞氣泡袋(包)", 6800, 2500, 720),
]
inv_rows = []
for sku, name, stock, safety, daily in items:
    days = round(stock / daily, 1) if daily else ""
    inv_rows.append([sku, name, stock, safety, daily, days,
                     "低於安全水位" if stock < safety else ""])
write_csv(BASE / "Automations/Examples/02_Inventory_Monitor/sample_files/inventory_status.csv",
          ["料號", "品名", "目前庫存", "安全水位", "日均耗用", "預估可用天數", "狀態"], inv_rows)

# 麥禾烘焙門市銷售（供 Canva / Visualizations / 品牌章節）
print("產生麥禾烘焙銷售資料：")
stores = [("MH-TP01", "台北信義店", "北區"), ("MH-TP02", "台北大安店", "北區"),
          ("MH-NT01", "新北板橋店", "北區"), ("MH-TY01", "桃園中壢店", "北區"),
          ("MH-TC01", "台中西屯店", "中區"), ("MH-TC02", "台中北屯店", "中區"),
          ("MH-TN01", "台南東區店", "南區"), ("MH-KH01", "高雄左營店", "南區")]
products = [("蜜香紅茶生吐司", 180), ("海鹽奶油卷", 45), ("桂圓核桃法國", 220),
            ("經典可頌", 65), ("秋栗蒙布朗", 145)]
sale_rows = []
for q in ["2026Q1", "2026Q2", "2026Q3"]:
    for sid, sname, region in stores:
        for pname, price in products:
            # 秋栗蒙布朗為 Q3 秋季新品，Q1/Q2 無銷售
            if pname == "秋栗蒙布朗" and q != "2026Q3":
                continue
            qty = int(random.uniform(800, 4200) * (1.25 if region == "北區" else 1.0))
            revenue = qty * price
            margin = round(random.uniform(0.38, 0.61), 3)
            sale_rows.append([q, sid, sname, region, pname, price, qty, revenue, margin])
write_csv(BASE / "Visualizations/Examples/02_Brand_Sales_Site/sample_files/maiho_store_sales.csv",
          ["季度", "門市代碼", "門市名稱", "區域", "品項", "單價", "銷售數量", "銷售金額", "毛利率"],
          sale_rows)

# GitHub issue backlog（供 Connectors/03_GitHub）
print("產生 GitHub Issue 資料：")
issues = [
    [412, "結帳頁選門市自取仍計算運費", "bug", "open", "2026-08-14", 23, "P1", "客訴 8 件，影響營收"],
    [418, "Safari 17 結帳頁版面溢出", "bug", "open", "2026-08-19", 7, "P2", ""],
    [421, "希望支援超商取貨", "feature", "open", "2026-08-21", 41, "P2", "業務端多次反映"],
    [423, "配送查詢 API 回應超過 3 秒", "performance", "open", "2026-08-22", 12, "P1", "尖峰時段惡化"],
    [427, "文件：AGENTS.md 缺少 e2e 測試說明", "docs", "open", "2026-08-25", 2, "P3", ""],
    [430, "移除 moment.js 相依", "tech-debt", "open", "2026-08-27", 5, "P3", "包體積 -180KB"],
    [431, "登入後偶爾跳回首頁", "bug", "open", "2026-08-28", 18, "P1", "無法穩定重現"],
    [433, "後台匯出 CSV 中文亂碼", "bug", "open", "2026-08-29", 9, "P2", "缺 BOM"],
    [435, "新增深色模式", "feature", "open", "2026-09-01", 33, "P3", ""],
    [436, "訂單編號在通知信中顯示為 undefined", "bug", "open", "2026-09-02", 15, "P1", ""],
    [438, "升級 Node.js 22", "chore", "open", "2026-09-03", 1, "P3", ""],
    [439, "地址自動補完會蓋掉使用者手動輸入", "bug", "open", "2026-09-04", 11, "P2", ""],
]
write_csv(BASE / "Connectors/03_GitHub/01_Issue_Triage/sample_files/tideflow_issue_backlog.csv",
          ["編號", "標題", "類型", "狀態", "建立日期", "留言數", "現有優先度", "備註"], issues)

print("\n完成。")
