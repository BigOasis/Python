from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 빈칸, 바이러스 따로 저장
blanks = []
viruses = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            blanks.append((i, j))
        elif lab[i][j] == 2:
            viruses.append((i, j))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(board):
    q = deque()
    for v in viruses:
        q.append(v)
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 0:  # 빈칸이면 감염
                    board[nr][nc] = 2
                    q.append((nr, nc))
                    
# 안전 영역 개수 세기
def count_safe(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt

ans = 0
# 빈칸에서 3개 뽑아서 벽 세우기
for walls in combinations(blanks, 3):
    # 연구소 복사
    tmp = [row[:] for row in lab]

    for (r, c) in walls:
        tmp[r][c] = 1

    bfs(tmp)
    safe = count_safe(tmp)

    if safe > ans:
        ans = safe

print(ans)
