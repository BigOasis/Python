"""
프로그래머스 택배 배달과 수거하기

45분
그리디
"""


def solution(cap, n, deliveries, pickups):
    answer = 0
    d_cap, p_cap = 0, 0  # 배달 및 수거 남은 용량

    for i in range(n - 1, -1, -1):  # 가장 먼 집부터
        d_cap -= deliveries[i]
        p_cap -= pickups[i]

        # 남은 상자가 없을 때까지 반복
        while d_cap < 0 or p_cap < 0:
            d_cap += cap
            p_cap += cap
            answer += (i + 1) * 2  # 왕복 거리라서 *2
    return answer
