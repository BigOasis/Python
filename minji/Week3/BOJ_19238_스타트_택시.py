#손님 고르기, 목적지까지의 최단거리 구하기: BFS
#연료 관리

from collections import deque
import sys
input = sys.stdin.readline

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())
r, c = r - 1, c - 1

passengers = {}
for _ in range(M):
    a, b, x, y = map(int, input().split())
    passengers[(a-1, b-1)] = (x-1, y-1)

dirs = [(-1,0),(0,-1),(0,1),(1,0)]

# BFS 최단거리 계산
def bfs(sr, sc):
    dist = [[-1]*N for _ in range(N)]
    q = deque([(sr, sc)])
    dist[sr][sc] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N and board[nr][nc]==0 and dist[nr][nc]==-1:
                dist[nr][nc] = dist[r][c]+1
                q.append((nr, nc))
    return dist

# 손님 수 만큼 반복
for _ in range(M):
    # 현재 위치에서 모든 칸까지의 최단거리 구하기
    dist = bfs(r, c)
    # 태울 손님 고르기
    cand = []
    for (sr, sc), (er, ec) in passengers.items():
        d = dist[sr][sc]
        if d != -1:
            cand.append((d, sr, sc))

    # 태울 손님이 없으면 종료한다
    if not cand: print(-1); exit()

    # 거리, 행, 열 기준으로 정렬하여 우선순위가 가장 높은 손님 선택
    cand.sort()
    d, sr, sc = cand[0]
    if fuel < d: print(-1); exit()
    fuel -= d
    r, c = sr, sc

    # 목적지까지 최단거리 구하기
    dist = bfs(r, c)
    er, ec = passengers[(sr, sc)]
    d = dist[er][ec]
    if d == -1 or fuel < d: print(-1); exit()
    fuel += d
    r, c = er, ec
    del passengers[(sr, sc)]

print(fuel)
