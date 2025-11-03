"""
프로그래머스 디스크 컨트롤러

풀이시간: 70분
"""

import heapq


def solution(jobs):
    t = 0
    f = 0
    h = []
    tot = 0
    pre = -1

    while f < len(jobs):
        # 요청된 작업 중 현재 시점에 처리 가능한 작업을 힙에 추가 (소요시간 기준 정렬)
        for j in jobs:
            if pre < j[0] <= t:
                heapq.heappush(h, [j[1], j[0]])

        if len(h) > 0:
            # 가장 짧은 작업 먼저 수행
            cur = heapq.heappop(h)
            pre = t
            t += cur[0]
            tot += (t - cur[1])  # 대기시간 + 처리시간
            f += 1
        else:
            # 처리 가능한 작업이 없으면 시간 1 증가
            t += 1

    return int(tot / len(jobs))
