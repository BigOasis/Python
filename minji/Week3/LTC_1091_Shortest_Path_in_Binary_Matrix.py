from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        # 시작이나 끝이 막혀있으면 바로 불가능
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # 8방향 (상하좌우 + 대각선)
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        q = deque([(0, 0, 1)])  # (행, 열, 거리)
        grid[0][0] = 1  # 방문 표시

        while q:
            # BFS여서 큐에서 꺼낼 때는 무조건 popleft() 사용
            r, c, d = q.popleft()

            if r == n-1 and c == n-1:  # 도착 지점
                return d

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, d+1))

        return -1  # 도착 불가
