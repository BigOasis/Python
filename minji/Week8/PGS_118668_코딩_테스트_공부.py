"""
    DP 풀이 (동적 계획법)

    dp[a][c] = 알고력 a, 코딩력 c에 도달하는 최소 시간
    - 공부: +1 능력, +1 시간
    - 문제풀기: 요구치 충족 시 보상만큼 능력 상승, 시간 +cost
    목표치까지의 최소 시간 구하기
"""
def solution(alp, cop, problems):
    # 목표치 구하기(최대 알고 코딩값)
    goal_alp = max(p[0] for p in problems)
    goal_cop = max(p[1] for p in problems)

    # 시작이 이미 목표 이상이면 끝
    if alp >= goal_alp and cop >= goal_cop:
        return 0

    # 목표 이상은 계산할 필요x
    alp = min(alp, goal_alp)
    cop = min(cop, goal_cop)

    INF = 1e9
    dp = [[INF] * (goal_cop + 1) for _ in range(goal_alp + 1)]
    dp[alp][cop] = 0

    # 모든 상태 탐색
    for a in range(alp, goal_alp + 1):
        for c in range(cop, goal_cop + 1):
            # 현재 최소 시간
            t = dp[a][c]

            # 공부로 한 칸씩 올리기
            if a + 1 <= goal_alp:
                dp[a + 1][c] = min(dp[a + 1][c], t + 1)
            if c + 1 <= goal_cop:
                dp[a][c + 1] = min(dp[a][c + 1], t + 1)

            # 문제 풀기 (조건 만족 시만)
            for req_a, req_c, rwd_a, rwd_c, cost in problems:
                if a >= req_a and c >= req_c:
                    na = min(goal_alp, a + rwd_a)
                    nc = min(goal_cop, c + rwd_c)
                    dp[na][nc] = min(dp[na][nc], t + cost)

    return dp[goal_alp][goal_cop]
