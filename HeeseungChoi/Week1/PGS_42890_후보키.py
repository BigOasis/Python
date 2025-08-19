from itertools import combinations

def solution(relation):
    rows = len(relation)          # 행 개수 (레코드 수)
    cols = len(relation[0])       # 열 개수 (속성 수)
    candidate_keys = []           # 후보키들을 저장할 리스트

    # 1. 1개부터 전체 열까지 가능한 조합을 만들기
    for i in range(1, cols + 1):
        for cols_comb in combinations(range(cols), i): 

            # 2. 현재 조합으로 각 행의 값을 묶어서 튜플로 만들어버리기
            keys = [tuple([row[col] for col in cols_comb]) for row in relation]

            # 3. 유일성_ 모든 튜플이 다르게
            if len(set(keys)) != rows:
                continue 

            # 4. 최소성 검사_이미 있는 후보키가 포함되어 있지 않게....
            is_minimal = True
            for key in candidate_keys:
                if set(key).issubset(set(cols_comb)):
                    is_minimal = False
                    break

            # 5. 유일성 + 최소성 통과하면 후보키로 등록
            if is_minimal:
                candidate_keys.append(cols_comb)

    # 6. 후보키 개수 리턴
    return len(candidate_keys)