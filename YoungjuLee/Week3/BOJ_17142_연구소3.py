import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

virus = [(i, j) for i in range(n) for j in range(n) if g[i][j] == 2]
empty_cnt = sum(r.count(0) for r in g)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = sys.maxsize

if empty_cnt == 0:
    print(0)
    exit()


def bfs(active):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    infected = 0
    last_time = 0

    for x, y in active:
        q.append((x, y))
        visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n and 0 <= ny < n
                    and visited[nx][ny] == -1 and g[nx][ny] != 1):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

                if g[nx][ny] == 0:
                    infected += 1
                    last_time = visited[nx][ny]

    return last_time if infected == empty_cnt else sys.maxsize


for c in combinations(virus, m):
    res = min(res, bfs(c))

print(res if res != sys.maxsize else -1)
