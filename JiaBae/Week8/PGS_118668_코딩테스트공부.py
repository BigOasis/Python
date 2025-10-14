def solution(alp, cop, problems):
    # 목표치
    maxA = max([p[0] for p in problems] + [alp])
    maxC = max([p[1] for p in problems] + [cop])

    # 초기값 캡핑
    alp = min(alp, maxA)
    cop = min(cop, maxC)

    INF = 10**9
    dp = [[INF] * (maxC + 1) for _ in range(maxA + 1)]
    dp[alp][cop] = 0

    for i in range(alp, maxA + 1):
        for j in range(cop, maxC + 1):
            cur = dp[i][j]
            if i < maxA:
                dp[i + 1][j] = min(dp[i + 1][j], cur + 1)   # 알고 공부
            if j < maxC:
                dp[i][j + 1] = min(dp[i][j + 1], cur + 1)   # 코딩 공부

            # 문제 풀기
            for reqA, reqC, rA, rC, cost in problems:
                if i >= reqA and j >= reqC:
                    ni = min(maxA, i + rA)
                    nj = min(maxC, j + rC)
                    if dp[ni][nj] > cur + cost:
                        dp[ni][nj] = cur + cost

    return dp[maxA][maxC]