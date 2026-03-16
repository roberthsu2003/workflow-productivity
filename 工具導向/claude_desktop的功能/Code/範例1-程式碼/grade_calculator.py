"""
成績計算模組
這個模組包含計算學生成績的函式
"""


def calculate_average(scores):
    """
    計算成績的平均值
    
    參數:
        scores: 包含成績的列表
    
    回傳:
        平均成績（浮點數）
    
    注意: 這個函式有 bug，無法正確處理混合類型的列表
    """
    total = 0
    count = 0
    
    for score in scores:
        total += score  # Bug: 如果 scores 中有字串，這裡會出錯
        count += 1
    
    if count == 0:
        return 0
    
    return total / count


def calculate_total(scores):
    """
    計算成績總分
    
    參數:
        scores: 包含成績的列表
    
    回傳:
        總分
    """
    total = 0
    for score in scores:
        total += score  # 同樣的問題：無法處理字串
    return total


def get_highest_score(scores):
    """
    取得最高成績
    
    參數:
        scores: 包含成績的列表
    
    回傳:
        最高成績
    """
    if not scores:
        return None
    
    return max(scores)


def get_lowest_score(scores):
    """
    取得最低成績
    
    參數:
        scores: 包含成績的列表
    
    回傳:
        最低成績
    """
    if not scores:
        return None
    
    return min(scores)
