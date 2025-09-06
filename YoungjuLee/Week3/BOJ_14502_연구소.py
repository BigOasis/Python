import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]
empty = [(i, j) for i in range(n) for j in range(m) if g[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if g[i][j] == 2]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = 0  # 새로 세울 수 있는 벽의 개수


def bfs(s):
    tmp = [row[:] for row in g]
    q = deque(virus)
    for x, y in s:
        tmp[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n and 0 <= ny < m
                    and tmp[nx][ny] == 0):
                tmp[nx][ny] = 2  # 감염처리
                q.append((nx, ny))

    return sum(r.count(0) for r in tmp)


all_w = list(combinations(empty, 3))
for w in all_w:
    res = max(res, bfs(w))

print(res)
