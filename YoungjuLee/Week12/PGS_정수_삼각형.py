"""
프로그래머스 정수삼각형
풀이시간: 60분
"""


def solution(triangle):
    dp = triangle
    depth = len(dp)
    for i in range(1, depth):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == i:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])
    return max(dp[depth - 1])
