from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        N = len(grid)
        visited = set()
        dx = [1, 1, 1, -1, -1, -1, 0, 0]
        dy = [0, 1, -1, 0, 1, -1, 1, -1]
        que = deque([(0, 0, 1)])
        
        while que:
            y, x, cur = que.popleft()
            
            if grid[y][x] == 1:     continue
            if (y, x) in visited:   continue
            if (y, x) == (N-1, N-1):
                return cur
            
            visited.add((y, x))
            
            for t in range(8):
                newY, newX = y+dy[t], x+dx[t]
                if 0 <= newY < N and 0 <= newX < N:
                    que.append((newY, newX, cur+1))
        
        return -1