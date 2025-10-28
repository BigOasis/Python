"""
프로그래머스 388353. 지게차와 크레인

풀이시간: 80분 over
"""

from collections import deque


def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    arr = [list(row) for row in storage]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 현재 창고에서 외부 공기와 연결된 칸을 찾는 함수
    def bfs_outside():

        visited = [[False] * m for _ in range(n)]
        q = deque()

        # 창고의 가장자리에서 시작 (외부와 닿은 위치)
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if arr[i][j] == '.':  # 외부 공기
                        q.append((i, j))
                        visited[i][j] = True

        # BFS로 외부 공기와 연결된 모든 '.' 찾기
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx, ny))
        return visited

    # 모든 출고 요청 순서대로 처리
    for req in requests:
        target = req[0]  # 출고할 알파벳 종류

        # 크레인 요청 (두 글자)
        if len(req) == 2:
            # 같은 알파벳 전부 제거
            for i in range(n):
                for j in range(m):
                    if arr[i][j] == target:
                        arr[i][j] = '.'

        # 지게차 요청 (한 글자)
        else:
            visited = bfs_outside()  # 외부 공기와 연결된 위치 표시

            # 외부와 닿아있는 같은 알파벳만 제거
            for i in range(n):
                for j in range(m):
                    if arr[i][j] == target:
                        for dx, dy in dirs:
                            nx, ny = i + dx, j + dy
                            if not (0 <= nx < n and 0 <= ny < m) or (0 <= nx < n and 0 <= ny < m and visited[nx][ny]):
                                arr[i][j] = '.'
                                break

                                # 남은 컨테이너 개수 세기
    return sum(1 for i in range(n) for j in range(m) if arr[i][j] != '.')
