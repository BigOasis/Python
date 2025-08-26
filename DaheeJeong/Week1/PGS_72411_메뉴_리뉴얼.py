from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []

    # 각 코스 메뉴 오름차순을 위해 정렬
    for i, order in enumerate(orders):
        orders[i] = sorted(order)

    for i in course:
        # 각 후보 코스 조합 횟수 저장할 딕셔너리 생성
        cand_course = defaultdict(int)
        for order in orders:
            for comb in combinations(order, i):
                c = "".join(comb)
                cand_course[c] += 1

        if not cand_course:
            continue

        # 주문 횟수 내림차순으로 정렬
        sorted_cand_course = sorted(cand_course.items(), key=lambda x: -x[1])
        max_cnt = max(sorted_cand_course[0][1], 2)
        for s in sorted_cand_course:
            if s[1] < max_cnt:
                break
            answer.append(s[0])
    return sorted(answer)