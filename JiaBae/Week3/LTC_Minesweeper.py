class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        r, c = click
        mine_board = [[0] * n for _ in range(m)]

        # 지뢰 발견하면 끝
        if board[r][c] == 'M' :
            board[r][c] = 'X'
            return board

        # 지뢰 찾아서 주변 digit 으로 변경
        for i in range(m) :
            for j in range(n) :
                if board[i][j] == 'M' :
                    for nx, ny in ((i+1, j), (i-1, j), (i, j+1), (i, j-1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)) :
                        if 0 <= nx < m and 0 <= ny < n :
                            mine_board[nx][ny] += 1
        
        # E가 드러날 경우 재귀
        q = []
        if board[r][c] == 'E' :
            # 인접 지뢰 있으면 종료
            if mine_board[r][c] != 0 :
                board[r][c] = str(mine_board[r][c])
                return board
            # 인접 지뢰 없으면    
            board[r][c] = 'B' 
            q.append((r, c))

            while q :
                x, y = q.pop()
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)) :
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'E' :
                        if mine_board[nx][ny] == 0 :
                            board[nx][ny] = 'B' 
                            q.append((nx, ny))
                        else :
                            board[nx][ny] = str(mine_board[nx][ny])
            return board
        