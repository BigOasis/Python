from itertools import combinations

def solution(n, q, ans):
    count = 0
    
    # 1~n 중 5개 조합 전부 탐색
    for code in combinations(range(1, n+1), 5):
        code_set = set(code)
        valid = True
        
        # 모든 시도 검사
        for query, res in zip(q, ans):
            if len(code_set & set(query)) != res:
                valid = False
                break
        
        if valid:
            count += 1
    
    return count
