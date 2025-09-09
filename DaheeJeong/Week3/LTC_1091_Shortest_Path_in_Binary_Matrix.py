from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]
        queue = deque()
        queue.append((0, 0, 1))
        grid[0][0] = 1

        while queue:
            r, c, cnt = queue.popleft()
            if r == n - 1 and c == n - 1:
                return cnt

            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, cnt + 1))
                    grid[nr][nc] = 1

        return -1