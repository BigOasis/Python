"""
프로그래머스 카드 짝 맞추기

"""
from collections import deque

# 방향 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs
def bfs(board, r, c):
    q = deque([(r[0]), r[1], 0])
    visited = [[0] * 4 for _ in range(4)]
    visited[r[0]][r[1]] = 1

    while q:
        r, c, d = q.popleft()  # 하나빼내기

        # 목표 카드 도착 시 종료
        if (r, c) == c:
            return d

        # 4방향 탐색
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            # 한칸 이동
            if 0 <= nr < 4 and 0 <= nc < 4 and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc, d + 1))

            # ctrl 이동 (한번에)
            while 0 <= nr + dx[i] < 4 and 0 <= nc + dy[i] < 4:
                nr += dx[i]
                nc += dy[i]
                if board[nr][nc] != 0:  # 카드 있으면 멈춤
                    break
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc, d + 1))


def solution(board, r, c):
    answer = 1e9
    nums = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0 and board[i][j] not in nums:
                nums.append(board[i][j])
    # 흠,, 이제 이걸 백트래킹해야하나

    return answer

def bt(nums):
    if not nums:
        return

    for num in nums:
        # p = [(x, y), (x, y)]
        # bt(새보드, 새위치, 나머지들, cnt)
        return

