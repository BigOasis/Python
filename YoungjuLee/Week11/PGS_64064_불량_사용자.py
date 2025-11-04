"""
프로그래머스 스터디문제. 불량 사용자
풀이시간: 60분
"""

from itertools import permutations


def solution(user_id, banned_id):
    ans = set()
    ui = user_id
    bi = banned_id

    for perm in permutations(ui, len(bi)):
        ok = True
        for i in range(len(bi)):
            u = perm[i]
            b = bi[i]

            if len(u) != len(b):
                ok = False
                break

            for j in range(len(u)):
                if b[j] != '*' and b[j] != u[j]:
                    ok = False
                    break
            if not ok:
                break

        if ok:
            ans.add(tuple(sorted(perm)))  # 중복 방지

    return len(ans)
