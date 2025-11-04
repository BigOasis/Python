"""
백준 19238. 스타트 택시
시뮬레이션 + BFS
"""

from collections import deque


def find_nearest(taxi, board, passengers, n):
    """현재 택시 위치에서 가장 가까운 손님 찾기 (거리→행→열 우선)"""
    q = deque([taxi])
    visited = [[0] * n for _ in range(n)]
    visited[taxi[0]][taxi[1]] = 1

    while q:
        nq = deque()
        found = []  # 현재 거리에서 찾은 손님들

        # 같은 거리(한 레벨) 내 처리
        for x, y in q:
            if (x, y) in passengers:
                found.append((x, y))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    nq.append((nx, ny))

        # 이번 거리에서 손님 발견 시 바로 반환
        if found:
            found.sort()
            fx, fy = found[0]
            dist = visited[fx][fy] - 1
            return fx, fy, dist

        q = nq  # 다음 거리로 이동

    return -1, -1, -1


def get_distance(start, end, board, n):
    """손님 출발지 → 목적지 최단거리 BFS"""
    q = deque([(*start, 0)])
    visited = [[0] * n for _ in range(n)]
    visited[start[0]][start[1]] = 1

    while q:
        x, y, d = q.popleft()
        if (x, y) == end:
            return d
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, d + 1))
    return -1


n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
x, y = map(lambda v: int(v) - 1, input().split())
taxi = (x, y)

# 손님 정보 입력
passengers = {}
for _ in range(m):
    a, b, c, d = map(lambda v: int(v) - 1, input().split())
    passengers[(a, b)] = (c, d)

# 손님 m명 모두 태우기
for _ in range(m):
    # 가장 가까운 손님 찾기
    px, py, dist = find_nearest(taxi, board, passengers, n)
    if dist == -1 or fuel < dist:
        print(-1)
        exit()

    # 손님까지 이동
    fuel -= dist
    dest = passengers.pop((px, py))
    taxi = (px, py)

    # 손님 → 목적지 이동
    dist2 = get_distance(taxi, dest, board, n)
    if dist2 == -1 or fuel < dist2:
        print(-1)
        exit()

    # 이동 성공 → 연료 보충 (소모한 만큼 *2)
    fuel -= dist2
    fuel += dist2 * 2
    taxi = dest

print(fuel)
