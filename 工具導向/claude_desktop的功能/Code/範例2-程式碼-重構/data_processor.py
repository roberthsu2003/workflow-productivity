"""
資料處理模組
這個模組包含多個處理 CSV 資料的函式，但有很多重複的程式碼
"""

import csv
import os


def process_student_data(input_file, output_file):
    """
    處理學生資料：讀取 CSV、驗證、轉換、寫入
    
    這個函式有很多重複的邏輯，可以重構
    """
    # 讀取 CSV 檔案
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"檔案不存在: {input_file}")
    
    students = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)
    
    # 驗證資料
    valid_students = []
    for student in students:
        if 'name' in student and 'score' in student:
            try:
                score = float(student['score'])
                if score >= 0 and score <= 100:
                    valid_students.append(student)
            except ValueError:
                pass  # 跳過無效的分數
    
    # 轉換資料格式
    processed_data = []
    for student in valid_students:
        processed_data.append({
            'name': student['name'].strip(),
            'score': float(student['score']),
            'grade': 'A' if float(student['score']) >= 90 else 'B' if float(student['score']) >= 80 else 'C' if float(student['score']) >= 70 else 'D' if float(student['score']) >= 60 else 'F'
        })
    
    # 寫入檔案
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        if processed_data:
            writer = csv.DictWriter(f, fieldnames=['name', 'score', 'grade'])
            writer.writeheader()
            writer.writerows(processed_data)
    
    return len(processed_data)


def process_employee_data(input_file, output_file):
    """
    處理員工資料：讀取 CSV、驗證、轉換、寫入
    
    這個函式與 process_student_data 有大量重複的程式碼
    """
    # 讀取 CSV 檔案
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"檔案不存在: {input_file}")
    
    employees = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            employees.append(row)
    
    # 驗證資料
    valid_employees = []
    for employee in employees:
        if 'name' in employee and 'salary' in employee:
            try:
                salary = float(employee['salary'])
                if salary >= 0:
                    valid_employees.append(employee)
            except ValueError:
                pass  # 跳過無效的薪資
    
    # 轉換資料格式
    processed_data = []
    for employee in valid_employees:
        processed_data.append({
            'name': employee['name'].strip(),
            'salary': float(employee['salary']),
            'department': employee.get('department', 'Unknown').strip()
        })
    
    # 寫入檔案
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        if processed_data:
            writer = csv.DictWriter(f, fieldnames=['name', 'salary', 'department'])
            writer.writeheader()
            writer.writerows(processed_data)
    
    return len(processed_data)


def process_product_data(input_file, output_file):
    """
    處理產品資料：讀取 CSV、驗證、轉換、寫入
    
    這個函式與其他處理函式有大量重複的程式碼
    """
    # 讀取 CSV 檔案
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"檔案不存在: {input_file}")
    
    products = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    
    # 驗證資料
    valid_products = []
    for product in products:
        if 'name' in product and 'price' in product:
            try:
                price = float(product['price'])
                if price >= 0:
                    valid_products.append(product)
            except ValueError:
                pass  # 跳過無效的價格
    
    # 轉換資料格式
    processed_data = []
    for product in valid_products:
        processed_data.append({
            'name': product['name'].strip(),
            'price': float(product['price']),
            'category': product.get('category', 'Uncategorized').strip()
        })
    
    # 寫入檔案
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        if processed_data:
            writer = csv.DictWriter(f, fieldnames=['name', 'price', 'category'])
            writer.writeheader()
            writer.writerows(processed_data)
    
    return len(processed_data)
