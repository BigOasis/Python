from itertools import combinations

def solution(relation):
    candidate_key_cnt = 0
    n_rows = len(relation)
    n_cols = len(relation[0])
    
    # 모든 조합 생성
    for i in range(1, n_cols + 1) :
        for comb in combinations(range(n_cols), i) :
            print(comb)
            # 유일성 검사
            
            # 최소성 검사
                
    return candidate_key_cnt