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
    # info 전처리
    for s in info:
        w = s.split()
        cond, score = w[:-1], int(w[-1])
        # '-' 포함 가능한 모든 조합
        for n in range(5):
            for c in combinations(range(4), n):
                t = cond[:]
                for i in c: t[i] = '-'
                db.setdefault(''.join(t), []).append(score)
    # 점수 정렬
    for v in db.values(): v.sort()

    res = []
    for q in query:
        q = q.replace(' and ', ' ').split()
        key, target = ''.join(q[:-1]), int(q[-1])
        s = db.get(key, [])
        # 기준 점수 이상인 사람 수 (이진 탐색)
        res.append(len(s) - bisect_left(s, target))
    return res
