from collections import deque

def move(x, y, dx, dy, board):
    cnt = 0
    # 벽을 만나거나 구멍에 빠질 때까지 이동
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
        if board[x][y] == 'O':
            break
    return x, y, cnt

def bfs(board, rx, ry, bx, by):
    n, m = len(board), len(board[0])
    q = deque()
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    q.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True

    # 상하좌우
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth >= 10:
            return 0  # 10번 넘으면 실패

        for dx, dy in dirs:
            nrx, nry, rcnt = move(rx, ry, dx, dy, board)
            nbx, nby, bcnt = move(bx, by, dx, dy, board)

            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬만 빠졌다면 성공
            if board[nrx][nry] == 'O':
                return 1

            # 두 구슬이 같은 위치면 더 멀리 이동한 구슬을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            # 방문한 적 없는 상태면 큐에 추가
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, depth + 1))
    return 0

def main():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    rx = ry = bx = by = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j

    print(bfs(board, rx, ry, bx, by))

if __name__ == "__main__":
    main()
