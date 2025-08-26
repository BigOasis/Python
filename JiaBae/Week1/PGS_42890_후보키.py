from itertools import combinations

def solution(relation):
    candidates = []
    n_rows = len(relation)
    n_cols = len(relation[0])
    
    # 모든 조합 생성
    for k in range(1, n_cols+1) :
        for comb in combinations(range(n_cols), k) :
            # 유일성 체크
            projection = [tuple(row[c] for c in comb) for row in relation]
            if len(set(projection)) == n_rows:
            
                # 최소성 체크
                is_minimal = True
                for key in candidates :
                    if set(key).issubset(comb) :
                        is_minimal = False
                        break

                if is_minimal: 
                    candidates.append(comb)
                
    return len(candidates)