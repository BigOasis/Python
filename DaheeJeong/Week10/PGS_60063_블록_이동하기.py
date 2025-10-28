from collections import deque


def get_next(pos, board):
    next_pos = []
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})

    if x1 == x2:
        for d in [-1, 1]:
            if board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0:
                next_pos.append({(x1, y1), (x1 + d, y1)})
                next_pos.append({(x2, y2), (x2 + d, y2)})
    else:
        for d in [-1, 1]:
            if board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0:
                next_pos.append({(x1, y1), (x1, y1 + d)})
                next_pos.append({(x2, y2), (x2, y2 + d)})
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for nxt in get_next(pos, new_board):
            if nxt not in visited:
                visited.append(nxt)
                q.append((nxt, cost + 1))
