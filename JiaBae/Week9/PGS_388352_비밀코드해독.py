from itertools import combinations

def solution(n, q, ans):
    set_q = [set(row) for row in q]
    m = len(q)
    
    cnt = 0
    # 1~n까지 모든 조합에 대해
    for c in combinations(range(1, n+1), 5):
        set_c = set(c)
        flag = True
        
        for i in range(m):
            if len(set_c & set_q[i]) != ans[i]:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt