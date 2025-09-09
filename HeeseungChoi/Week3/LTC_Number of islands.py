from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0  # 최종 섬의 개수를 저장할 변수
        M = len(grid)     # 행(row)의 길이
        N = len(grid[0])  # 열(column)의 길이

        # 방문 여부를 기록하는 2차원 배열
        visited = [[False] * N for _ in range(M)]
        
        # BFS 함수 정의
        def bfs(x, y):
            # 상, 좌, 우, 하 (4방향 탐색용 좌표 이동값)
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]

            visited[x][y] = True  # 시작 지점 방문 처리
            q = deque()
            q.append((x, y))  # 큐에 시작 좌표 추가

            while q:
                cur_x, cur_y = q.popleft()  # 현재 좌표 꺼내기
                for i in range(4):  # 4방향 탐색
                    nx, ny = cur_x + dx[i], cur_y + dy[i]
                    # 격자 범위 안에 있는지 체크
                    if 0 <= nx < M and 0 <= ny < N:
                        # 아직 방문하지 않았고, 땅("1")인 경우
                        if grid[nx][ny] == "1" and not visited[nx][ny]:
                            visited[nx][ny] = True  # 방문 처리
                            q.append((nx, ny))      # 큐에 추가
                            
        # 전체 격자를 탐색
        for i in range(M):
            for j in range(N):
                # 새로운 섬의 시작점("1")을 찾았고 아직 방문하지 않았다면
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)   # BFS 탐색으로 섬 전체를 방문 처리
                    islands += 1  # 섬 개수 증가
        
        return islands  # 최종 섬의 개수 반환