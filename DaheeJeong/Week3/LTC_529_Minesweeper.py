class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        rows, cols = len(board), len(board[0])
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        def count_mines(r, c):
            cnt = 0
            for i in range(8):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    cnt += 1
            return cnt

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if board[r][c] != 'E':
                return

            mines = count_mines(r, c)
            if mines > 0:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for i in range(8):
                    dfs(r + dr[i], c + dc[i])

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(r, c)

        return board
