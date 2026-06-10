import json
import sys

def main():
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            print("錯誤：請提供有效的任務工時 JSON 資料。")
            return
        
        tasks = json.loads(input_data)
        total_hours = sum(task.get("hours", 0) for task in tasks)
        
        print("\n📊 創新科技專案工時統計分析 📊")
        print("=" * 40)
        for task in tasks:
            name = task.get("name", "未命名任務")
            hours = task.get("hours", 0)
            percentage = (hours / total_hours) * 100 if total_hours > 0 else 0
            bar_length = int(percentage / 5)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            print(f"| {name:<12} | {hours:>2} 小時 | {percentage:>5.1f}% | {bar} |")
        print("=" * 40)
        print(f"總計工時      : {total_hours:>2} 小時")
    except Exception as e:
        print(f"計算錯誤: {e}")

if __name__ == "__main__":
    main()
