from itertools import combinations


def solution(relation):
    answer = []  # 후보키 목록(조합)을 담음
    col, row = len(relation[0]), len(relation)

    # 인덱스 모든 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    for comb in combi:
        # 최소성 만족 여부: 기존 후보키가 현재 조합의 부분집합이면 스킵
        if any(set(ck).issubset(comb) for ck in answer):
            continue

        # 유일성 만족 여부
        keys = set()
        for item in relation:
            keys.add(tuple(item[i] for i in comb))

        if len(keys) == row:
            answer.append(comb)

    return len(answer)