"""
leetcode: Number of Islands
시간복잡도 : O(m * n) 인접탐색 4는 무시 
dfs(재귀 사용) 방식과 bfs(큐 사용) 방식 
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        n, m = len(grid[0]), len(grid)

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        # dfs
        def dfs(i, j):
            # 종료 조건
            if grid[i][j] == "0" :
                return 
            
            # 방문처리 
            grid[i][j] = "0"
            
            for d in range(4) :
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" :
                    dfs(nx, ny)

        for i in range(m) :
            for j in range(n) :
                if grid[i][j] == "1" :
                    cnt += 1 
                    dfs(i, j)
        return cnt
        
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n, m = len(grid[0]), len(grid)

        # bfs
        def bfs():
            while q :
                x, y = q.popleft()
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)) :
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" :
                        grid[nx][ny] = "0"
                        q.append([nx, ny])

        for i in range(m) :
            for j in range(n) :
                if grid[i][j] == "1" :
                    islands += 1 
                    q = deque([(i, j)])
                    bfs()
        return islands