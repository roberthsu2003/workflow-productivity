"""
主程式：示範成績計算功能
執行此程式會出現 TypeError 錯誤
"""

from grade_calculator import calculate_average, calculate_total, get_highest_score, get_lowest_score


def main():
    """主函式：示範各種成績計算"""
    
    # 範例 1：正常情況（全部是數字）
    print("=== 範例 1：正常情況 ===")
    scores1 = [85, 90, 78, 92, 88]
    try:
        avg1 = calculate_average(scores1)
        print(f"成績列表: {scores1}")
        print(f"平均成績: {avg1}")
        print(f"最高分: {get_highest_score(scores1)}")
        print(f"最低分: {get_lowest_score(scores1)}")
    except Exception as e:
        print(f"錯誤: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 範例 2：有問題的情況（包含字串和數字）
    print("=== 範例 2：混合類型（會出錯）===")
    scores2 = [85, 90, "未考試", 78, 92, "缺考", 88]
    try:
        avg2 = calculate_average(scores2)
        print(f"成績列表: {scores2}")
        print(f"平均成績: {avg2}")
    except Exception as e:
        print(f"❌ 錯誤發生: {type(e).__name__}: {e}")
        print("\n這就是需要修復的 bug！")
    
    print("\n" + "="*50 + "\n")
    
    # 範例 3：包含 None 值的情況
    print("=== 範例 3：包含 None 值（也會出錯）===")
    scores3 = [85, None, 90, 78, None, 92]
    try:
        avg3 = calculate_average(scores3)
        print(f"成績列表: {scores3}")
        print(f"平均成績: {avg3}")
    except Exception as e:
        print(f"❌ 錯誤發生: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
