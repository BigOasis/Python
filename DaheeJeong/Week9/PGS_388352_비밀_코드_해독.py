from itertools import combinations


def solution(n, q, ans):
    answer = 0

    for comb in combinations(range(1, n + 1), 5):
        flag = True
        for i, qq in enumerate(q):
            cnt = 0
            for j in range(5):
                if comb[j] in qq:
                    cnt += 1
            if cnt != ans[i]:
                flag = False
                break
        if flag:
            answer += 1

    return answer