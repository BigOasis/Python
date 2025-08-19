from itertools import combinations


def solution(relation):
    answer = []
    col, row = len(relation[0]), len(relation)

    # 인덱스 모든 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    # 유일성 만족 여부
    for comb in combi:
        lst = []
        for item in relation:
            print(item)

    return answer