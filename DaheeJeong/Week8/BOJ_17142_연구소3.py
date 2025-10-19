import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

empty_count = 0
virus = []

for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus.append((i, j))
        elif lab[i][j] == 0:
            empty_count += 1

def bfs(active):
    visited = [[-1] * n for _ in range(n)]
    q = deque()

    for x, y in active:
        visited[x][y] = 0
        q.append((x, y))

    infected, time = 0, 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if lab[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    if lab[nx][ny] == 0:
                        infected += 1
                        time = visited[nx][ny]

    if infected == empty_count:
        return time
    else:
        return float('inf')

min_time = float('inf')

for active in combinations(virus, m):
    min_time = min(min_time, bfs(active))

print(-1 if min_time == float('inf') else min_time)
