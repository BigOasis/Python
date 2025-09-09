class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        cnt = 0

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != "1":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    dfs(row, col)
                    cnt += 1

        return cnt