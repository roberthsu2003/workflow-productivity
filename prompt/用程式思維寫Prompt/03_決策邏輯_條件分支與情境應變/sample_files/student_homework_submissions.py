# ==========================================
# 學生 A（小華）繳交的程式碼
# 狀態：語法錯誤（SyntaxError，第 7 行缺少冒號）
# ==========================================
def calculate_bill_student_a():
    kwh = float(input("請輸入用電度數: "))
    if kwh < 0
        print("用電度數不可為負數！")
    elif kwh <= 120:
        total = kwh * 1.6
        print(f"總電費為 {total} 元")
    else:
        total = 120 * 1.6 + (kwh - 120) * 2.4
        print(f"總電費為 {total} 元")


# ==========================================
# 學生 B（小明）繳交的程式碼
# 狀態：邏輯錯誤（第 22 行未扣除前一級基準度數，導致重複計價）
# ==========================================
def calculate_bill_student_b():
    kwh = float(input("請輸入用電度數: "))
    if kwh < 0:
        print("用電度數不可為負數！")
    elif kwh <= 120:
        total = kwh * 1.6
        print(f"總電費為 {total} 元")
    elif kwh <= 330:
        # 錯誤點：應該是 (kwh - 120) * 2.4，卻寫成 kwh * 2.4
        total = (120 * 1.6) + (kwh * 2.4)
        print(f"總電費為 {total} 元")
    else:
        total = (120 * 1.6) + ((330 - 120) * 2.4) + ((kwh - 330) * 3.5)
        print(f"總電費為 {total} 元")


# ==========================================
# 學生 C（阿美）繳交的程式碼
# 狀態：正確但命名待優化（邏輯完全正確，但變數用 a, b, c，可給予重構建議）
# ==========================================
def calculate_bill_student_c():
    a = float(input("請輸入用電度數: "))
    if a < 0:
        print("用電度數不可為負數！")
    elif a <= 120:
        ans = a * 1.6
        print(f"總電費為 {ans} 元")
    elif a <= 330:
        ans = 120 * 1.6 + (a - 120) * 2.4
        print(f"總電費為 {ans} 元")
    else:
        ans = 120 * 1.6 + 210 * 2.4 + (a - 330) * 3.5
        print(f"總電費為 {ans} 元")
