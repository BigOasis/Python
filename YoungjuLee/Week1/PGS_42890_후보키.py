from itertools import combinations
# 모든 조합 -> 유일성, 최소성 만족하는것만 거르기

def isSub(a, li):
    """
    a가 li의 부분집합인지 여부 확인
    """
    return set(a).issubset(set(li))


def solution(relation):
    r = len(relation)
    c = len(relation[0])
    keys = []

    for size in range(1, c + 1):
        # 모든 combinations 구하기
        combs = list(combinations(range(c), size))
        for comb in combs:
            # 유일성
            check = []
            for row in relation:
                pick = []
                for col in comb:
                    pick.append(row[col])
                check.append(tuple(pick))
            if len(set(check)) == r:
                # 최소성
                ok = True
                for k in keys:
                    if isSub(k, comb): # 후보키 중복 검사
                        ok = False
                        break
                if ok:
                    keys.append(comb)
    return len(keys)