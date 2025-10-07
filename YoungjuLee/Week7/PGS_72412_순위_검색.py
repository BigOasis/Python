"""
프로그래머스 순위 검색
80분

점수 리스트를 key마다 점수를 오름차순 정렬 후 이진 탐색(bisect_left)
점수 ≥ 기준점수인 사람 수를 계산
"""

from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    db = {}

    # info 전처리: 각 지원자의 모든 조건 조합을 key로 저장
    for i in info:
        data = i.split()
        cond, score = data[:-1], int(data[-1])
        for n in range(5):  # '-'로 대체할 조건 개수 (0~4)
            for c in combinations(range(4), n):
                tmp = cond[:]
                for idx in c: tmp[idx] = '-'
                key = ''.join(tmp)
                db.setdefault(key, []).append(score)

    # 2️점수 리스트 정렬 (이진 탐색용)
    for v in db.values():
        v.sort()

    ans = []

    for q in query:
        q = q.replace(' and ', '').split()
        key, target = ''.join(q[:-1]), int(q[-1])
        if key in db:
            s = db[key]
            # target 이상 점수를 가진 사람 수 계산
            i = bisect_left(s, target)
            ans.append(len(s) - i)
        else:
            ans.append(0)
    return ans
