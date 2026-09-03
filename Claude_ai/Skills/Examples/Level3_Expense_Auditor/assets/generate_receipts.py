import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "Claude_ai/Skills/Examples/Level3_Expense_Auditor/assets/sample_receipts"
FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
FONT_PATH_HEITI = "/System/Library/Fonts/STHeiti Medium.ttc"

def get_font(size, bold=False):
    try:
        path = FONT_PATH_HEITI if bold else FONT_PATH
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.truetype(FONT_PATH, size)

# 1. 台北市區計程車收據 (計程車專用證明聯)
def create_taxi_receipt():
    w, h = 600, 750
    img = Image.new("RGB", (w, h), "#FAFAF5")
    draw = ImageDraw.Draw(img)
    
    # Outer border
    draw.rectangle([20, 20, w-20, h-20], outline="#4A4A4A", width=2)
    draw.rectangle([25, 25, w-25, h-25], outline="#8A8A8A", width=1)
    
    draw.text((w//2, 60), "台灣大車隊計程車乘車證明", fill="#1A1A1A", font=get_font(28, True), anchor="mt")
    draw.text((w//2, 100), "TAIWAN TAXI RECEIPT", fill="#666666", font=get_font(16), anchor="mt")
    draw.line([40, 130, w-40, 130], fill="#333333", width=2)
    
    details = [
        ("車號 (Plate No.)：", "TDC-8899"),
        ("司機姓名 (Driver)：", "陳建國 (證號 10823)"),
        ("乘車日期 (Date)：", "2026/08/20"),
        ("上車時間 (Start)：", "14:15  台北內湖科技園區"),
        ("下車時間 (End)：", "14:50  台北信義商辦大樓"),
        ("買受人統編 (Tax ID)：", "88888888"),
        ("公務事由備註：", "攜帶 2 箱重量展示樣品拜訪客戶"),
    ]
    
    y = 160
    for label, val in details:
        draw.text((50, y), label, fill="#333333", font=get_font(18, True))
        draw.text((250, y), val, fill="#111111", font=get_font(18))
        y += 45
        
    draw.line([40, y+10, w-40, y+10], fill="#333333", width=1)
    y += 40
    
    # Amount Box
    draw.rectangle([50, y, w-50, y+100], fill="#EEF2F7", outline="#1B365D", width=2)
    draw.text((70, y+35), "車資總計 (Total)：", fill="#1B365D", font=get_font(24, True))
    draw.text((w-80, y+30), "NT$ 380", fill="#B80D0D", font=get_font(32, True), anchor="rt")
    
    # Stamp
    stamp_center = (w-120, h-120)
    draw.ellipse([w-190, h-180, w-50, h-60], outline="#C0392B", width=3)
    draw.text((stamp_center[0], stamp_center[1]-30), "台灣大車隊", fill="#C0392B", font=get_font(18, True), anchor="mm")
    draw.text((stamp_center[0], stamp_center[1]), "車輛稽核章", fill="#C0392B", font=get_font(18, True), anchor="mm")
    draw.text((stamp_center[0], stamp_center[1]+28), "2026.08.20", fill="#C0392B", font=get_font(14), anchor="mm")
    
    img.save(os.path.join(OUTPUT_DIR, "01_taxi_receipt_nt380.png"))

# 2. 台灣高鐵票根 (標準車廂對號座)
def create_thsr_ticket():
    w, h = 800, 480
    img = Image.new("RGB", (w, h), "#FFF7EE")
    draw = ImageDraw.Draw(img)
    
    # Border & THSR Header banner
    draw.rectangle([15, 15, w-15, h-15], outline="#E65100", width=3)
    draw.rectangle([15, 15, w-15, 80], fill="#F57C00")
    draw.text((35, 30), "台灣高鐵 Taiwan High Speed Rail", fill="#FFFFFF", font=get_font(26, True))
    draw.text((w-35, 35), "購票證明聯 / 乘車票", fill="#FFF3E0", font=get_font(18), anchor="rt")
    
    # Train Info
    draw.text((50, 110), "台北 TAIPEI", fill="#212121", font=get_font(32, True))
    draw.text((250, 115), "->", fill="#E65100", font=get_font(28, True))
    draw.text((310, 110), "台中 TAICHUNG", fill="#212121", font=get_font(32, True))
    
    draw.text((50, 170), "乘車日期： 2026/08/21", fill="#333333", font=get_font(20, True))
    draw.text((350, 170), "車次： 0625 車次", fill="#333333", font=get_font(20, True))
    draw.text((580, 170), "開車： 08:31", fill="#333333", font=get_font(20, True))
    
    draw.rectangle([45, 215, w-45, 290], fill="#FFFFFF", outline="#DDDDDD")
    draw.text((70, 235), "車廂： 05 車 (標準車廂)", fill="#E65100", font=get_font(22, True))
    draw.text((360, 235), "座位： 08A 號 (對號座)", fill="#212121", font=get_font(22, True))
    draw.text((640, 235), "全票", fill="#555555", font=get_font(22))
    
    draw.line([45, 320, w-45, 320], fill="#E0E0E0", width=2)
    
    draw.text((50, 345), "買受人統一編號： 88888888", fill="#1B365D", font=get_font(20, True))
    draw.text((50, 385), "票號： 2190-4820-1093-08", fill="#666666", font=get_font(16))
    draw.text((50, 415), "備註： 差旅洽公標準車廂", fill="#666666", font=get_font(16))
    
    draw.text((w-60, 360), "票價： NT$ 700", fill="#C62828", font=get_font(34, True), anchor="rt")
    
    img.save(os.path.join(OUTPUT_DIR, "02_thsr_ticket_nt700.png"))

# 3. 台中市區 Uber 電子乘車收據
def create_uber_receipt():
    w, h = 600, 780
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    # Header black bar
    draw.rectangle([0, 0, w, 90], fill="#000000")
    draw.text((40, 25), "Uber", fill="#FFFFFF", font=get_font(36, True))
    draw.text((w-40, 35), "電子乘車收據 (行程已結束)", fill="#AAAAAA", font=get_font(16), anchor="rt")
    
    # Fare
    draw.text((w//2, 130), "行程總費用", fill="#666666", font=get_font(18), anchor="mt")
    draw.text((w//2, 165), "NT$ 560", fill="#000000", font=get_font(42, True), anchor="mt")
    draw.line([40, 235, w-40, 235], fill="#EEEEEE", width=2)
    
    details = [
        ("乘車時間：", "2026/08/21 17:40"),
        ("上車地點：", "台中高鐵站 3 號出口"),
        ("下車地點：", "台中市西屯區市政路 108 號"),
        ("服務類別：", "Uber 菁英優步 (Elite)"),
        ("統一編號：", "88888888 (宇聯科技股份有限公司)"),
        ("事由說明：", "（未填寫任何事由說明）"),
    ]
    
    y = 260
    for label, val in details:
        draw.text((50, y), label, fill="#666666", font=get_font(17))
        color = "#D32F2F" if "未填寫" in val else "#111111"
        draw.text((180, y), val, fill=color, font=get_font(17, True if "未填寫" in val else False))
        y += 48
        
    draw.line([40, y+10, w-40, y+10], fill="#EEEEEE", width=2)
    y += 35
    
    # Breakdown
    draw.text((50, y), "基本車資與里程費", fill="#444444", font=get_font(18))
    draw.text((w-50, y), "NT$ 490", fill="#111111", font=get_font(18), anchor="rt")
    y += 40
    draw.text((50, y), "尖峰加成動態調價", fill="#444444", font=get_font(18))
    draw.text((w-50, y), "NT$ 70", fill="#111111", font=get_font(18), anchor="rt")
    y += 50
    
    # Notice
    draw.rectangle([40, y, w-40, y+110], fill="#FFF9C4", outline="#FBC02D")
    draw.text((60, y+20), "【審核提醒】：", fill="#B71C1C", font=get_font(18, True))
    draw.text((60, y+55), "單趟金額已超過內部規範 NT$ 500 上限，且無事由說明", fill="#5D4037", font=get_font(15))
    draw.text((60, y+80), "依規定需自付差額 NT$ 60 或經權責主管簽核補件。", fill="#5D4037", font=get_font(15))
    
    img.save(os.path.join(OUTPUT_DIR, "03_uber_receipt_nt560.png"))

# 4. 商務宴客電子發票證明聯 (2人 NT$2,800)
def create_dinner_invoice():
    w, h = 550, 850
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    # Border
    draw.rectangle([10, 10, w-10, h-10], outline="#CCCCCC", width=1)
    
    draw.text((w//2, 40), "鼎極頂級牛排館 台中旗艦店", fill="#000000", font=get_font(24, True), anchor="mt")
    draw.text((w//2, 80), "電子發票證明聯", fill="#000000", font=get_font(26, True), anchor="mt")
    draw.text((w//2, 120), "115 年 07-08 月份", fill="#000000", font=get_font(22, True), anchor="mt")
    draw.text((w//2, 160), "AB-89102374", fill="#000000", font=get_font(32, True), anchor="mt")
    
    draw.text((40, 220), "2026-08-21 20:15:30", fill="#333333", font=get_font(16))
    draw.text((40, 250), "隨機碼： 5821   總計： NT$ 2,800", fill="#111111", font=get_font(18, True))
    draw.text((40, 280), "賣方： 54982103 (鼎極餐飲股份有限公司)", fill="#333333", font=get_font(16))
    draw.text((40, 310), "買方統編： 88888888", fill="#1B365D", font=get_font(19, True))
    
    # Barcodes
    draw.rectangle([40, 350, w-40, 400], fill="#000000")
    for i in range(50, w-50, 8):
        draw.line([i, 350, i, 400], fill="#FFFFFF", width=3)
        
    draw.line([40, 430, w-40, 430], fill="#333333", width=2)
    
    # Items
    draw.text((40, 450), "品名", fill="#333333", font=get_font(17, True))
    draw.text((320, 450), "數量", fill="#333333", font=get_font(17, True))
    draw.text((w-40, 450), "小計", fill="#333333", font=get_font(17, True), anchor="rt")
    
    items = [
        ("商業精選菲力牛排套餐", "1", "1,250"),
        ("主廚特製海陸龍蝦套餐", "1", "1,350"),
        ("服務費 10%", "1", "200"),
    ]
    
    y = 490
    for name, qty, sub in items:
        draw.text((40, y), name, fill="#222222", font=get_font(17))
        draw.text((330, y), qty, fill="#222222", font=get_font(17))
        draw.text((w-40, y), sub, fill="#222222", font=get_font(17), anchor="rt")
        y += 40
        
    draw.line([40, y+10, w-40, y+10], fill="#333333", width=2)
    y += 30
    draw.text((40, y), "總計 (Total)", fill="#000000", font=get_font(24, True))
    draw.text((w-40, y), "NT$ 2,800", fill="#B80D0D", font=get_font(28, True), anchor="rt")
    
    y += 60
    draw.rectangle([35, y, w-35, y+95], fill="#E8F5E9", outline="#4CAF50")
    draw.text((50, y+15), "【業務公務宴客事由說明】：", fill="#1B5E20", font=get_font(17, True))
    draw.text((50, y+45), "招待對象：台中國際開發 王總經理 1 人，我方業務 1 人（共 2 人）", fill="#2E7D32", font=get_font(15))
    draw.text((50, y+70), "人均消費 NT$ 1,400，符合業務宴客 NT$ 1,500/人 之規範。", fill="#2E7D32", font=get_font(15))
    
    img.save(os.path.join(OUTPUT_DIR, "04_client_dinner_nt2800.png"))

# 5. 加班誤餐電子發票 (單人 NT$850 超標)
def create_overbudget_meal_invoice():
    w, h = 550, 800
    img = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([10, 10, w-10, h-10], outline="#CCCCCC", width=1)
    draw.text((w//2, 40), "老乾杯日式燒肉 信義本店", fill="#000000", font=get_font(24, True), anchor="mt")
    draw.text((w//2, 80), "電子發票證明聯", fill="#000000", font=get_font(26, True), anchor="mt")
    draw.text((w//2, 120), "115 年 07-08 月份", fill="#000000", font=get_font(22, True), anchor="mt")
    draw.text((w//2, 160), "CD-19385024", fill="#000000", font=get_font(32, True), anchor="mt")
    
    draw.text((40, 220), "2026-08-22 21:30:10", fill="#333333", font=get_font(16))
    draw.text((40, 250), "隨機碼： 3192   總計： NT$ 850", fill="#111111", font=get_font(18, True))
    draw.text((40, 280), "賣方： 29401823 (乾杯餐飲股份有限公司)", fill="#333333", font=get_font(16))
    draw.text((40, 310), "買方統編： 88888888", fill="#1B365D", font=get_font(19, True))
    
    # Barcodes
    draw.rectangle([40, 350, w-40, 400], fill="#000000")
    for i in range(50, w-50, 8):
        draw.line([i, 350, i, 400], fill="#FFFFFF", width=3)
        
    draw.line([40, 430, w-40, 430], fill="#333333", width=2)
    
    draw.text((40, 450), "品名", fill="#333333", font=get_font(17, True))
    draw.text((320, 450), "數量", fill="#333333", font=get_font(17, True))
    draw.text((w-40, 450), "小計", fill="#333333", font=get_font(17, True), anchor="rt")
    
    items = [
        ("特選和牛燒肉便當", "1", "750"),
        ("生啤酒一杯 (加班飲用)", "1", "100"),
    ]
    
    y = 490
    for name, qty, sub in items:
        draw.text((40, y), name, fill="#222222", font=get_font(17))
        draw.text((330, y), qty, fill="#222222", font=get_font(17))
        draw.text((w-40, y), sub, fill="#222222", font=get_font(17), anchor="rt")
        y += 40
        
    draw.line([40, y+10, w-40, y+10], fill="#333333", width=2)
    y += 30
    draw.text((40, y), "總計 (Total)", fill="#000000", font=get_font(24, True))
    draw.text((w-40, y), "NT$ 850", fill="#B80D0D", font=get_font(28, True), anchor="rt")
    
    y += 60
    draw.rectangle([35, y, w-35, y+95], fill="#FFEBEE", outline="#EF5350")
    draw.text((50, y+15), "【財務審核注意】：", fill="#C62828", font=get_font(17, True))
    draw.text((50, y+45), "同仁申報事由：個人週六加班誤餐（1 人）", fill="#B71C1C", font=get_font(15))
    draw.text((50, y+70), "日常公務用餐上限 NT$ 600，超額 NT$ 250 須列超標自負。", fill="#B71C1C", font=get_font(15))
    
    img.save(os.path.join(OUTPUT_DIR, "05_overbudget_dinner_nt850.png"))

if __name__ == "__main__":
    create_taxi_receipt()
    create_thsr_ticket()
    create_uber_receipt()
    create_dinner_invoice()
    create_overbudget_meal_invoice()
    print("Updated receipts regenerated successfully!")
