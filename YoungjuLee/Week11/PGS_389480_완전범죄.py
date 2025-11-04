"""
프로그래머스 완전범죄

풀이시간: 60분
"""


def solution(info, n, m):

    dp = [1e9] * m
    dp[0] = 0

    for a, b in info:
        new_dp = [1e9] * m
        for j in range(m):
            if dp[j] >= n:
                continue
            if dp[j] + a < n:
                new_dp[j] = min(new_dp[j], dp[j] + a)
            if j + b < m:
                new_dp[j + b] = min(new_dp[j + b], dp[j])
        dp = new_dp

    res = min(dp)

    return res if res < n else -1