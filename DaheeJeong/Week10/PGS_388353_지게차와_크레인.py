from collections import deque


def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    arr = [list(row) for row in storage]

    def bfs():
        visited = [[False] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if arr[i][j] == '.':
                        q.append((i, j))
                        visited[i][j] = True

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx, ny))
        return visited

    for req in requests:
        target = req[0]

        if len(req) == 2:  # 크레인 요청
            for i in range(n):
                for j in range(m):
                    if arr[i][j] == target:
                        arr[i][j] = '.'

        else:  # 지게차 요청
            visited = bfs()
            for i in range(n):
                for j in range(m):
                    if arr[i][j] == target:
                        for k in range(4):
                            nx, ny = i + dx[k], j + dy[k]
                            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                                arr[i][j] = '.'
                                break
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != '.':
                count += 1
    return count
