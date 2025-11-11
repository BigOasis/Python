def solution(info, n, m):
    length = len(info)
    INF = float('inf')
    # dp[i][b]: i개 아이템까지 처리했을 때, B의 누적 흔적이 b일 때 A의 최소 누적 흔적
    dp = [[INF] * m for _ in range(length+1)]
    dp[0][0] = 0

    for i, trace in enumerate(info):
        cost_a, cost_b = trace
        for b in range(m):
            if dp[i][b] == INF:
                continue
            # case 1: 아이템 i를 A가 맡는 경우
            new_a = dp[i][b] + cost_a
            if new_a < n:
                dp[i + 1][b] = min(dp[i + 1][b], new_a)
            # case 2: 아이템 i를 B가 맡는 경우
            new_b = b + cost_b
            if new_b < m:
                dp[i + 1][new_b] = min(dp[i + 1][new_b], dp[i][b])

    answer = min(dp[-1])
    return answer if answer != INF else -1
