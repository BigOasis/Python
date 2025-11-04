def solution(info, n, m):
    INF = 10**9

    if n <= 0 or m <= 0:
        return -1

    dp = [INF] * n
    dp[0] = 0

    for a_i, b_i in info:
        new_dp = [INF] * n
        for a_used in range(n):
            if dp[a_used] == INF:
                continue

            # 1) 이번 물건을 A가 훔침
            na = a_used + a_i
            if na < n:
                # B 흔적은 변화 없음
                if dp[a_used] < m and dp[a_used] < new_dp[na]:
                    new_dp[na] = dp[a_used]

            # 2) 이번 물건을 B가 훔침
            nb = dp[a_used] + b_i
            if nb < m:
                # A 흔적은 변화 없음
                if nb < new_dp[a_used]:
                    new_dp[a_used] = nb

        dp = new_dp

    # 가능한 상태 중 A 흔적이 가장 작은 것 반환
    for a_used in range(n):
        if dp[a_used] < m:
            return a_used
    return -1