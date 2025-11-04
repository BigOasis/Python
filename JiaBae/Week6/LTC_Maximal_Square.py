class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n= len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        best = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 위, 왼, 좌상
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    best = max(best, dp[i][j])
        return best**2