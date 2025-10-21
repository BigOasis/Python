import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

empty = []
virus = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

def spread_virus(temp, virus_list):
    q = deque(virus_list)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))

def get_safe_area(temp):
    cnt = 0
    for i in range(n):
        cnt += temp[i].count(0)
    return cnt

max_safe = 0

for walls in combinations(empty, 3):
    temp = [row[:] for row in lab]
    for x, y in walls:
        temp[x][y] = 1

    spread_virus(temp, virus)
    max_safe = max(max_safe, get_safe_area(temp))

print(max_safe)
