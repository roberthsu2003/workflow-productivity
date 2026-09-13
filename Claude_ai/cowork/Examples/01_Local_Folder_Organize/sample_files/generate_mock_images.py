import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_mock_invoices():
    output_dir = "/Users/roberthsu2003/Documents/GitHub/workflow-productivity/Claude_ai/cowork/Examples/01_Local_Folder_Organize/sample_files/raw_downloads"
    os.makedirs(output_dir, exist_ok=True)
    
    font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
    font_path_light = "/System/Library/Fonts/Hiragino Sans GB.ttc"
    
    # -------------------------------------------------------------
    # 1. Google Workspace 台灣電子發票證明聯 (INV_2026_08_GoogleWorkspace.png)
    # -------------------------------------------------------------
    img_w, img_h = 580, 1060
    # 微暖熱感應紙背景底色
    img1 = Image.new("RGB", (img_w, img_h), color=(252, 252, 250))
    draw1 = ImageDraw.Draw(img1)
    
    f_title = ImageFont.truetype(font_path, 28)
    f_sub = ImageFont.truetype(font_path, 20)
    f_inv_no = ImageFont.truetype(font_path, 32)
    f_body_bold = ImageFont.truetype(font_path, 17)
    f_body = ImageFont.truetype(font_path_light, 16)
    f_small = ImageFont.truetype(font_path_light, 13)
    f_tiny = ImageFont.truetype(font_path_light, 11)
    
    # 外框陰影與微紙張邊界
    draw1.rectangle([10, 10, img_w-10, img_h-10], outline=(210, 210, 205), width=2)
    
    y = 35
    # 標題
    draw1.text((img_w//2, y), "Google Cloud 台灣營運代理", fill=(40, 40, 40), font=f_sub, anchor="mm")
    y += 35
    draw1.text((img_w//2, y), "電子發票證明聯", fill=(20, 20, 20), font=f_title, anchor="mm")
    y += 35
    draw1.text((img_w//2, y), "115年 07-08 月份", fill=(30, 30, 30), font=f_sub, anchor="mm")
    y += 42
    draw1.text((img_w//2, y), "TW-2026088821", fill=(10, 10, 10), font=f_inv_no, anchor="mm")
    y += 38
    
    # 發票中繼資料
    draw1.text((45, y), "2026-08-31 16:45:20", fill=(50, 50, 50), font=f_body)
    draw1.text((360, y), "格式：25 (三聯式)", fill=(50, 50, 50), font=f_body)
    y += 28
    draw1.text((45, y), "隨機碼：6688", fill=(50, 50, 50), font=f_body)
    draw1.text((360, y), "總計：NT$ 3,360", fill=(20, 20, 20), font=f_body_bold)
    y += 28
    draw1.text((45, y), "賣方：54378901", fill=(50, 50, 50), font=f_body)
    draw1.text((360, y), "買方：88992211", fill=(20, 20, 20), font=f_body_bold)
    y += 32
    draw1.text((45, y), "買受人：創智數位股份有限公司", fill=(30, 30, 30), font=f_body_bold)
    y += 38

    # 繪製模擬條碼 (Barcode)
    barcode_w = 480
    barcode_x = 50
    import random
    random.seed(202608)
    for bx in range(barcode_x, barcode_x + barcode_w, 4):
        w_bar = random.choice([1, 2, 3])
        if random.random() > 0.2:
            draw1.rectangle([bx, y, bx + w_bar, y + 42], fill=(20, 20, 20))
    y += 55

    # 繪製兩個 QR Code
    qr_left = qrcode.make("TW-2026088821:1150831:6688:3200:3360:88992211:54378901:g8X9p==").resize((130, 130))
    qr_right = qrcode.make("**Google Workspace Monthly Subscription Fee:1:3200").resize((130, 130))
    img1.paste(qr_left, (75, y))
    img1.paste(qr_right, (370, y))
    y += 145

    # 虛線分隔
    def draw_dashed_line(d, y_pos, w):
        for x in range(35, w - 35, 12):
            d.line([(x, y_pos), (x + 7, y_pos)], fill=(160, 160, 160), width=1)

    draw_dashed_line(draw1, y, img_w)
    y += 22
    
    # 明細表頭
    draw1.text((img_w//2, y), "** 銷 售 明 細 清 單 **", fill=(40, 40, 40), font=f_body_bold, anchor="mm")
    y += 30
    draw1.text((45, y), "品名 / 規格", fill=(70, 70, 70), font=f_small)
    draw1.text((370, y), "數量", fill=(70, 70, 70), font=f_small)
    draw1.text((460, y), "小計", fill=(70, 70, 70), font=f_small)
    y += 24
    draw_dashed_line(draw1, y, img_w)
    y += 20

    # 明細內容
    draw1.text((45, y), "Google Workspace 企業雲端月租費", fill=(30, 30, 30), font=f_body_bold)
    draw1.text((380, y), "1", fill=(30, 30, 30), font=f_body)
    draw1.text((440, y), "3,200", fill=(30, 30, 30), font=f_body_bold)
    y += 26
    draw1.text((45, y), "說明：8月份全體團隊雲端辦公授權費", fill=(100, 100, 100), font=f_small)
    y += 32
    draw_dashed_line(draw1, y, img_w)
    y += 22

    # 金額總計欄
    draw1.text((45, y), "銷售額合計 (未稅)：", fill=(50, 50, 50), font=f_body)
    draw1.text((440, y), "NT$ 3,200", fill=(40, 40, 40), font=f_body)
    y += 28
    draw1.text((45, y), "營業稅額 (5% 應稅)：", fill=(50, 50, 50), font=f_body)
    draw1.text((440, y), "NT$   160", fill=(40, 40, 40), font=f_body)
    y += 28
    draw1.text((45, y), "總計金額 (含稅)：", fill=(20, 20, 20), font=f_body_bold)
    draw1.text((435, y), "NT$ 3,360", fill=(190, 30, 30), font=ImageFont.truetype(font_path, 20))
    y += 32
    draw1.text((45, y), "中文大寫：新台幣 參仟參佰陸拾元整", fill=(40, 40, 40), font=f_body_bold)
    y += 32
    draw_dashed_line(draw1, y, img_w)
    y += 20

    # 備註
    draw1.text((45, y), "付款方式：公司商務信用卡 (末四碼 6688)", fill=(70, 70, 70), font=f_small)
    y += 22
    draw1.text((45, y), "交易序號：TXN-20260831-GWS-9902", fill=(90, 90, 90), font=f_tiny)
    y += 20
    draw1.text((45, y), "本電子發票證明聯由財政部電子發票整合服務平台留存備查", fill=(110, 110, 110), font=f_tiny)
    
    p1 = os.path.join(output_dir, "INV_2026_08_GoogleWorkspace.png")
    img1.save(p1, quality=95)
    print("Saved:", p1)

    # -------------------------------------------------------------
    # 2. 台灣大車隊 電子乘車證明 (taxi_receipt_20260905.png)
    # -------------------------------------------------------------
    img2_w, img2_h = 560, 960
    img2 = Image.new("RGB", (img2_w, img2_h), color=(253, 253, 248))
    draw2 = ImageDraw.Draw(img2)
    
    draw2.rectangle([10, 10, img2_w-10, img2_h-10], outline=(215, 215, 210), width=2)
    
    y = 35
    draw2.text((img2_w//2, y), "台灣大車隊 TAIWAN TAXI", fill=(210, 80, 20), font=f_title, anchor="mm")
    y += 32
    draw2.text((img2_w//2, y), "電子乘車證明 (計程車客運車資收據)", fill=(50, 50, 50), font=ImageFont.truetype(font_path, 18), anchor="mm")
    y += 25
    draw2.text((img2_w//2, y), "客服中心：手機直撥 55688 | 統編：80287879", fill=(110, 110, 110), font=f_tiny, anchor="mm")
    y += 24
    draw_dashed_line(draw2, y, img2_w)
    y += 22

    # 基本乘車資訊
    draw2.text((45, y), "車牌號碼：TDC-8899", fill=(30, 30, 30), font=f_body_bold)
    draw2.text((330, y), "司機代號：09812", fill=(30, 30, 30), font=f_body)
    y += 28
    draw2.text((45, y), "乘車日期：2026-09-05", fill=(30, 30, 30), font=f_body)
    draw2.text((330, y), "車型：Toyota Cross", fill=(70, 70, 70), font=f_small)
    y += 28
    draw2.text((45, y), "乘車時間：14:20 ~ 14:55 (共 35 分鐘)", fill=(40, 40, 40), font=f_body)
    y += 30
    draw_dashed_line(draw2, y, img2_w)
    y += 20

    # 行程起迄
    draw2.text((45, y), "【行程記錄】", fill=(210, 80, 20), font=f_body_bold)
    y += 26
    draw2.text((55, y), "起點：台北市信義區信義路五段7號 (台北101)", fill=(30, 30, 30), font=f_small)
    y += 26
    draw2.text((55, y), "迄點：台北市內湖區瑞光路588號 (創智數位辦公室)", fill=(30, 30, 30), font=f_small)
    y += 30
    draw_dashed_line(draw2, y, img2_w)
    y += 20

    # 報銷資訊
    draw2.text((45, y), "【報銷對象資訊】", fill=(50, 50, 50), font=f_body_bold)
    y += 26
    draw2.text((55, y), "買受單位：創智數位股份有限公司", fill=(30, 30, 30), font=f_body)
    y += 26
    draw2.text((55, y), "統一編號：88992211", fill=(30, 30, 30), font=f_body_bold)
    y += 26
    draw2.text((55, y), "乘 車 人：王小明 (業務經理)", fill=(40, 40, 40), font=f_body)
    y += 26
    draw2.text((55, y), "事由備註：拜訪策略夥伴返程 (專案: PRJ-2026Q3)", fill=(70, 70, 70), font=f_small)
    y += 30
    draw_dashed_line(draw2, y, img2_w)
    y += 22

    # 車資金額
    draw2.text((45, y), "車資總計：", fill=(20, 20, 20), font=ImageFont.truetype(font_path, 20))
    draw2.text((360, y), "NT$ 380 元", fill=(200, 40, 20), font=ImageFont.truetype(font_path, 24))
    y += 36
    draw2.text((45, y), "車資中文大寫：新台幣 參佰捌拾元整", fill=(40, 40, 40), font=f_body_bold)
    y += 28
    draw2.text((45, y), "稅別：小規模營業人 (免用統一發票 / 免稅)", fill=(90, 90, 90), font=f_small)
    y += 26
    draw2.text((45, y), "付款方式：悠遊卡商務扣款 (卡號末四碼 3218)", fill=(50, 50, 50), font=f_body)
    y += 26
    draw2.text((45, y), "扣款狀態：扣款成功 (交易授權碼: TC9051455)", fill=(40, 120, 40), font=f_small)
    y += 32

    # QR Code
    qr_taxi = qrcode.make("https://www.taiwantaxi.com.tw/receipt?id=TDC8899_202609051455&amt=380").resize((110, 110))
    img2.paste(qr_taxi, (img2_w//2 - 55, y))
    y += 120
    draw2.text((img2_w//2, y), "掃描 QR Code 查驗電子乘車證明", fill=(120, 120, 120), font=f_tiny, anchor="mm")
    y += 24
    draw2.text((img2_w//2, y), "本收據依加值型及非加值型營業稅法規定，為法定會計報銷憑證", fill=(130, 130, 130), font=f_tiny, anchor="mm")

    p2 = os.path.join(output_dir, "taxi_receipt_20260905.png")
    img2.save(p2, quality=95)
    print("Saved:", p2)

if __name__ == "__main__":
    generate_mock_invoices()
