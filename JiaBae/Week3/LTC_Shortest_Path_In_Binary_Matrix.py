from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]

        def bfs() :
            # 첫번째 셀 방문처리
            if grid[0][0] == 0 :
                visited[0][0] = True
                q = deque([(0, 0, 1)])
            else : return -1

            while q :
                x, y, dist = q.popleft()

                # 끝나는 조건
                if x == n-1 and y == n-1 :
                    return dist

                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)) :
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and not visited[nx][ny] :
                        visited[nx][ny] = True
                        q.append((nx, ny, dist+1))
            return -1

        return bfs()
    
        