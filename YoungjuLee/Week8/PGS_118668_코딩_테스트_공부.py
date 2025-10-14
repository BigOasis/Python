"""
프로그래머스 118668. 코딩 테스트 공부
"""

INF = 10 ** 9


def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    for p in problems:
        if p[0] > max_alp:
            max_alp = p[0]
        if p[1] > max_cop:
            max_cop = p[1]

    # 현재 능력치가 이미 목표보다 높으면 자름
    if alp > max_alp:
        alp = max_alp
    if cop > max_cop:
        cop = max_cop

    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            # 공부해서 능력치 올리기 (비용 1)
            if a + 1 <= max_alp and dp[a + 1][c] > dp[a][c] + 1:
                dp[a + 1][c] = dp[a][c] + 1
            if c + 1 <= max_cop and dp[a][c + 1] > dp[a][c] + 1:
                dp[a][c + 1] = dp[a][c] + 1

            # 문제 풀어서 능력치 올리기
            for prob in problems:
                min_alp = prob[0]  # 문제당 최소 알고력
                min_co = prob[1]  # 문제당 최소 코딩력
                gain_alp = prob[2]  # 문제당 풀 시 증가하는 알고력
                gain_cop = prob[3]  # 문제당 풀 시 증가하는 코딩력
                time_cost = prob[4]  # 문제당 푸는데 걸리는 시간

                if a >= min_alp and c >= min_co:
                    next_alp = a + gain_alp
                    next_cop = c + gain_cop

                    # 각 알. 코딩력이 목표 이상으로 넘어가지 않도록 해야함
                    if next_alp > max_alp:
                        next_alp = max_alp
                    if next_cop > max_cop:
                        next_cop = max_cop

                    # 더 적은 시간으로 도달 가능한 경우 갱신
                    if dp[next_alp][next_cop] > dp[a][c] + time_cost:
                        dp[next_alp][next_cop] = dp[a][c] + time_cost

    return dp[max_alp][max_cop]
