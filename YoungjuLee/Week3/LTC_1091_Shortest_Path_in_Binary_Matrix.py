"""
LeetCode 200. Shortest Path in Binary Matrix
45분
"""
from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        dx = [1, 1, 1, -1, -1, -1, 0, 0]
        dy = [0, 1, -1, 0, 1, -1, 1, -1]

        # 초기화
        q = deque([(0, 0, 1)])
        grid[0][0] = 1

        while q:
            x, y, dist = q.popleft()
            if (x, y) == (n - 1, n - 1):
                return dist

            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = 1  # 방문 처리
                    q.append((nx, ny, dist + 1))

        return -1
