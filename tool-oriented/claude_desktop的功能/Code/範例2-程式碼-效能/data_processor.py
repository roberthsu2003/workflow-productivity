"""
資料處理模組 - 有效能問題的版本
這個模組包含處理大量資料的函式，但有效能瓶頸
"""

import json
import os
import time


# 模擬資料庫查詢（實際應用中可能是真實的資料庫）
class MockDatabase:
    """模擬資料庫類別"""
    
    def __init__(self):
        self.data = {}
        self.query_count = 0
    
    def get_user_info(self, user_id):
        """模擬資料庫查詢 - 每次查詢都有延遲"""
        self.query_count += 1
        time.sleep(0.001)  # 模擬資料庫查詢延遲（1毫秒）
        return {
            'id': user_id,
            'name': f'User_{user_id}',
            'email': f'user_{user_id}@example.com'
        }
    
    def get_order_info(self, order_id):
        """模擬訂單查詢 - 每次查詢都有延遲"""
        self.query_count += 1
        time.sleep(0.001)  # 模擬資料庫查詢延遲（1毫秒）
        return {
            'id': order_id,
            'user_id': order_id % 1000,
            'amount': order_id * 10,
            'status': 'completed' if order_id % 2 == 0 else 'pending'
        }


# 全域資料庫實例
db = MockDatabase()


def process_single_record(record_id):
    """
    處理單一筆記錄
    
    問題：這個函式在迴圈中被呼叫，每次都進行獨立的資料庫查詢
    這會導致 N+1 查詢問題，效能很差
    """
    # 查詢使用者資訊
    user_info = db.get_user_info(record_id % 1000)
    
    # 查詢訂單資訊
    order_info = db.get_order_info(record_id)
    
    # 處理資料
    processed = {
        'record_id': record_id,
        'user_name': user_info['name'],
        'user_email': user_info['email'],
        'order_amount': order_info['amount'],
        'order_status': order_info['status'],
        'total': user_info['id'] + order_info['amount']
    }
    
    return processed


def save_to_file(data, filename):
    """
    將資料寫入檔案
    
    問題：每次寫入都開啟和關閉檔案，應該使用批次寫入
    """
    with open(filename, 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
        f.write('\n')


def main_processing(record_count=10000):
    """
    主要處理函式 - 處理大量資料
    
    問題：
    1. 在迴圈中進行資料庫查詢（N+1 問題）
    2. 每次處理都寫入檔案（應該批次寫入）
    3. 沒有快取機制，重複查詢相同資料
    4. 沒有使用批次處理
    
    這個函式處理 10,000 筆資料需要約 30 秒
    """
    print(f"開始處理 {record_count} 筆資料...")
    start_time = time.time()
    
    output_file = 'output/processed_data.jsonl'
    os.makedirs('output', exist_ok=True)
    
    # 清除舊檔案
    if os.path.exists(output_file):
        os.remove(output_file)
    
    # 處理每一筆記錄
    for i in range(1, record_count + 1):
        # 處理單一記錄
        processed = process_single_record(i)
        
        # 寫入檔案（每次都開啟和關閉檔案，效能很差）
        save_to_file(processed, output_file)
        
        # 每 1000 筆顯示進度
        if i % 1000 == 0:
            elapsed = time.time() - start_time
            print(f"已處理 {i}/{record_count} 筆資料，耗時 {elapsed:.2f} 秒")
    
    total_time = time.time() - start_time
    print(f"\n✅ 處理完成！")
    print(f"   總共處理: {record_count} 筆")
    print(f"   總耗時: {total_time:.2f} 秒")
    print(f"   平均每筆: {total_time/record_count*1000:.2f} 毫秒")
    print(f"   資料庫查詢次數: {db.query_count}")
    print(f"   輸出檔案: {output_file}")
    
    return total_time


if __name__ == "__main__":
    # 測試處理 1000 筆資料（完整測試用 10000 筆）
    main_processing(1000)
