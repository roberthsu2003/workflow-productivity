"""
建立範例資料檔案
執行此腳本會建立測試用的 CSV 檔案
"""

import csv
import os


def create_sample_data():
    """建立範例 CSV 資料檔案"""
    
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)
    
    # 建立學生資料
    students_file = os.path.join(data_dir, 'students.csv')
    with open(students_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'score', 'class'])
        writer.writeheader()
        writer.writerows([
            {'name': '張三', 'score': '85', 'class': 'A班'},
            {'name': '李四', 'score': '92', 'class': 'A班'},
            {'name': '王五', 'score': '78', 'class': 'B班'},
            {'name': '趙六', 'score': '95', 'class': 'A班'},
            {'name': '錢七', 'score': 'abc', 'class': 'B班'},  # 無效資料
            {'name': '孫八', 'score': '88', 'class': 'B班'},
        ])
    print(f"✓ 已建立: {students_file}")
    
    # 建立員工資料
    employees_file = os.path.join(data_dir, 'employees.csv')
    with open(employees_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'salary', 'department'])
        writer.writeheader()
        writer.writerows([
            {'name': '陳一', 'salary': '50000', 'department': '工程部'},
            {'name': '林二', 'salary': '60000', 'department': '行銷部'},
            {'name': '黃三', 'salary': '55000', 'department': '工程部'},
            {'name': '吳四', 'salary': '-1000', 'department': '行銷部'},  # 無效資料
            {'name': '周五', 'salary': '70000', 'department': '管理部'},
        ])
    print(f"✓ 已建立: {employees_file}")
    
    # 建立產品資料
    products_file = os.path.join(data_dir, 'products.csv')
    with open(products_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'price', 'category'])
        writer.writeheader()
        writer.writerows([
            {'name': '筆記型電腦', 'price': '35000', 'category': '電子產品'},
            {'name': '滑鼠', 'price': '500', 'category': '電子產品'},
            {'name': '鍵盤', 'price': '1200', 'category': '電子產品'},
            {'name': '螢幕', 'price': '8000', 'category': '電子產品'},
            {'name': '無效商品', 'price': 'invalid', 'category': '其他'},  # 無效資料
        ])
    print(f"✓ 已建立: {products_file}")
    
    print("\n✅ 所有範例資料檔案已建立完成！")
    print("   現在可以執行 main.py 來測試資料處理功能")


if __name__ == "__main__":
    create_sample_data()
