from collections import deque


def solution(warehouse, order):
    n, m = len(warehouse), len(warehouse[0])
    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True
    total = 0

    while q:
        x, y = q.popleft()
        total += warehouse[x][y]

        for dx, dy in [(1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if order[nx][ny] >= order[x][y]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return total
