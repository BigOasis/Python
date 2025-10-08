"""
프로그래머스 주차요금계산
80분

딕셔너리
"""

import math


def solution(fees, records):
    # fees = [기본시간, 기본요금, 단위시간, 단위요금]
    base_t, base_f, unit_t, unit_f = fees
    # 입차정보 / 누적시간
    in_d, total = {}, {}

    for r in records:
        t, c, a = r.split()
        h, m = map(int, t.split(':'))
        t = h * 60 + m
        if a == 'IN':
            in_d[c] = t
        else:
            total[c] = total.get(c, 0) + t - in_d.pop(c)

    # 입차된 후에 출차된 내역이 없다면, 23:59로 처리
    for c, t in in_d.items():
        total[c] = total.get(c, 0) + (23 * 60 + 59 - t)

    # 오름차순 정렬
    ans = []
    for c in sorted(total):
        time = total[c]
        if time <= base_t:
            fee = base_f
        else:
            fee = base_f + math.ceil((time - base_t) / unit_t) * unit_f
        ans.append(fee)
    return ans
