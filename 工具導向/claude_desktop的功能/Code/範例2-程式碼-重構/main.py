"""
主程式：示範資料處理功能
這個程式展示如何使用重複的資料處理函式
"""

from data_processor import process_student_data, process_employee_data, process_product_data
import os


def main():
    """主函式：示範各種資料處理"""
    
    # 建立測試資料目錄
    data_dir = 'data'
    output_dir = 'output'
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    print("=== 資料處理示範 ===\n")
    
    # 範例 1：處理學生資料
    print("1. 處理學生資料...")
    student_input = os.path.join(data_dir, 'students.csv')
    student_output = os.path.join(output_dir, 'students_processed.csv')
    
    if os.path.exists(student_input):
        count = process_student_data(student_input, student_output)
        print(f"   ✓ 成功處理 {count} 筆學生資料")
        print(f"   ✓ 輸出檔案: {student_output}\n")
    else:
        print(f"   ⚠ 找不到輸入檔案: {student_input}\n")
    
    # 範例 2：處理員工資料
    print("2. 處理員工資料...")
    employee_input = os.path.join(data_dir, 'employees.csv')
    employee_output = os.path.join(output_dir, 'employees_processed.csv')
    
    if os.path.exists(employee_input):
        count = process_employee_data(employee_input, employee_output)
        print(f"   ✓ 成功處理 {count} 筆員工資料")
        print(f"   ✓ 輸出檔案: {employee_output}\n")
    else:
        print(f"   ⚠ 找不到輸入檔案: {employee_input}\n")
    
    # 範例 3：處理產品資料
    print("3. 處理產品資料...")
    product_input = os.path.join(data_dir, 'products.csv')
    product_output = os.path.join(output_dir, 'products_processed.csv')
    
    if os.path.exists(product_input):
        count = process_product_data(product_input, product_output)
        print(f"   ✓ 成功處理 {count} 筆產品資料")
        print(f"   ✓ 輸出檔案: {product_output}\n")
    else:
        print(f"   ⚠ 找不到輸入檔案: {product_input}\n")
    
    print("=== 完成 ===")
    print("\n💡 提示：這些函式有很多重複的程式碼，可以使用 Claude Code 進行重構！")


if __name__ == "__main__":
    main()
