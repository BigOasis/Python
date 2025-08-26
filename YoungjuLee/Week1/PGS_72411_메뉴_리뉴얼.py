"""
프로그래머스 72411번: 메뉴 리뉴얼
"""
from itertools import *
from collections import *


def solution(orders, course):
    answer = []
    for i in course:
        combs = []
        for o in orders:
            order = ''.join(sorted(o))
            combs = combs + list(combinations(order, i))
            # 2가지 이상인것만 고르기
        combs = [''.join(c) for c in combs]
        cnt_arr = defaultdict(int)
        for c in combs:
            cnt_arr[c] += 1

        if not cnt_arr:
            continue
        else:
            max_cnt = max(cnt_arr.values())
            if max_cnt < 2:
                continue
            for k, v in cnt_arr.items():
                if v == max_cnt:
                    answer.append(k)

    return sorted(answer)

# orders = ["XYZ", "XWY", "WXA"]
# course = [2, 3, 4]
# print(solution(orders, course))
