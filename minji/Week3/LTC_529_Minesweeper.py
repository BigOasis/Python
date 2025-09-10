class Solution:
    def updateBoard(self, board, click):
        n = len(board)
        m = len(board[0])
        x, y = click  # 클릭한 곳 좌표

        # 지뢰 밟으면 게임오버
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        # 방향 (8방향)
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]

        def near_mines(i, j):
            cnt = 0
            for k in range(8):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if board[ni][nj] == 'M':
                        cnt += 1
            return cnt

        def dfs(i, j):
            # 이미 열린 칸이면 그냥 무시
            if board[i][j] != 'E':
                return
            cnt = near_mines(i, j)

            if cnt > 0:
                board[i][j] = str(cnt)
            else:
                board[i][j] = 'B'
                for k in range(8):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m:
                        dfs(ni, nj)

        dfs(x, y)
        return board
