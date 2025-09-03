"""
LeetCode 200. Number of Islands
20분
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        n, m = len(grid), len(grid[0])

        def dfs(x, y):
            if (x < 0 or x >= n or y < 0 or y >= m
                    or grid[x][y] == "0"): return
            grid[x][y] = "0"
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island += 1

        return island
