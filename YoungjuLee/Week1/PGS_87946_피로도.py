"""
프로그래머스 87946번: 피로도
"""
from itertools import permutations


def solution(k, dungeons):
    res = 0

    for order in permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0
        for n, c in order:
            if hp >= n:
                hp -= c
                cnt += 1
            else:
                break
        res = max(res, cnt)

    return res
