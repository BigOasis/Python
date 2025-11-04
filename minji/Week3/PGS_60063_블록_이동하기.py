from collections import deque

def solution(board):
    N = len(board)
    drdc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(0, 0, 1, 0)])
    visited = set([(0, 0, 1)])

    while queue:
        r1, c1, d, move = queue.popleft()
        r2, c2 = r1 + drdc[d][0], c1 + drdc[d][1]

        if (r1 == N - 1 and c1 == N - 1) or (r2 == N - 1 and c2 == N - 1):
            return move
        
        # 네방향 이동
        for k in range(4):
            nr1, nc1 = r1 + drdc[k][0], c1 + drdc[k][1]
            nr2, nc2 = r2 + drdc[k][0], c2 + drdc[k][1]

            # 두칸 모두 보드 안에있고 벽이아니어야함
            if 0 <= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N:
                if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                    if (nr1, nc1, d) not in visited:
                        visited.add((nr1, nc1, d))
                        queue.append((nr1, nc1, d, move + 1))

        # 회전 90도로
        nd = d ^ 1
        for k in range(4):
            nr1, nc1 = r1 + drdc[k][0], c1 + drdc[k][1]
            nr2, nc2 = r2 + drdc[k][0], c2 + drdc[k][1]
            if not (0 <= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N):
                continue

            # 벽이면 회전 불가능
            if board[nr1][nc1] == 1 or board[nr2][nc2] == 1:
                continue

            # 아래/오른쪽 회전
            if d + k == 1:
                if (r1, c1, nd) not in visited:
                    visited.add((r1, c1, nd))
                    queue.append((r1, c1, nd, move + 1))
                if (r2, c2, nd) not in visited:
                    visited.add((r2, c2, nd))
                    queue.append((r2, c2, nd, move + 1))

            # 위/왼쪽 회전
            elif d + k == 3:
                if (nr1, nc1, nd) not in visited:
                    visited.add((nr1, nc1, nd))
                    queue.append((nr1, nc1, nd, move + 1))
                if (nr2, nc2, nd) not in visited:
                    visited.add((nr2, nc2, nd))
                    queue.append((nr2, nc2, nd, move + 1))
    return -1
