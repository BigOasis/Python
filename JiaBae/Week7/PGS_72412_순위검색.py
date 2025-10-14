from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    table = defaultdict(list)

    # 지원자 정보 전처리
    for s in info:
        lang, job, career, food, score = s.split()
        score = int(score)
        attrs = [lang, job, career, food]

        # 비트마스크(0=원래값, 1='-')
        for mask in range(16):
            key = []
            for i in range(4):
                if (mask >> i) & 1:
                    key.append('-')
                else:
                    key.append(attrs[i])
            table[tuple(key)].append(score)

    # 이진 탐색을 위해 정렬
    for key in table:
        table[key].sort()

    # 질의 처리
    ans = []
    for q in query:
        q = q.replace(" and ", " ")
        *conds, x = q.split()
        x = int(x)
        key = tuple(conds)

        scores = table.get(key, [])
        idx = bisect_left(scores, x)
        ans.append(len(scores) - idx)

    return ans