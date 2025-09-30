class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # 이동은 오른쪽 또는 아래로만 가능
        # 첫째 행과 첫번째 열의 경우의 수는 전부 1

        dp = [[1] * n for _ in range(m)]

        # (1,1) 부터 시작해서 경우의 수는 아래로 내려가거나, 오른쪽으로 가거나 즉 위경우 + 왼쪽 경우의 수

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]