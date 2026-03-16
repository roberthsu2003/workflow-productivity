"""
效能測試腳本
用來測試和比較優化前後的效能差異
"""

import time
from data_processor import main_processing, db


def test_performance():
    """測試處理效能"""
    
    print("=" * 60)
    print("效能測試")
    print("=" * 60)
    
    # 重置查詢計數
    db.query_count = 0
    
    # 測試不同資料量
    test_sizes = [100, 500, 1000]
    
    results = []
    
    for size in test_sizes:
        print(f"\n測試資料量: {size} 筆")
        print("-" * 60)
        
        start_time = time.time()
        elapsed = main_processing(size)
        end_time = time.time()
        
        results.append({
            'size': size,
            'time': elapsed,
            'queries': db.query_count,
            'time_per_record': elapsed / size * 1000  # 毫秒
        })
        
        # 重置查詢計數
        db.query_count = 0
        
        time.sleep(1)  # 稍作休息
    
    # 顯示結果摘要
    print("\n" + "=" * 60)
    print("效能測試結果摘要")
    print("=" * 60)
    print(f"{'資料量':<10} {'總耗時(秒)':<15} {'每筆(毫秒)':<15} {'查詢次數':<10}")
    print("-" * 60)
    
    for result in results:
        print(f"{result['size']:<10} {result['time']:<15.2f} {result['time_per_record']:<15.2f} {result['queries']:<10}")
    
    print("\n💡 提示：")
    print("   1. 觀察查詢次數是否過多（應該是資料量的 2 倍，因為每筆記錄查詢 2 次）")
    print("   2. 觀察處理時間是否過長")
    print("   3. 使用 Claude Code 優化後，應該能減少至少 50% 的處理時間")


if __name__ == "__main__":
    test_performance()
