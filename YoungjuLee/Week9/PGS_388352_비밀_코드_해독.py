"""
프로그래머스 388352. 비밀 코드 해독

40분
"""

from itertools import combinations


def solution(n, q, ans):
    answer = 0
    arr = [i for i in range(1, n + 1)]
    m = len(ans)
    idx = [i for i in range(m) if ans[i] == 0]

    # 조합에 사용할 필요 없는 숫자 제거
    for i in idx:
        for j in q[i]:
            if j in arr:
                arr.remove(j)

    for c in combinations(arr, 5):
        for i in range(m):
            cnt = sum(1 for j in q[i] if j in c)
            if cnt != ans[i]:
                break
        else:
            answer += 1

    return answer
