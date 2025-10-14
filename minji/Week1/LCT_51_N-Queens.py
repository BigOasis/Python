# N*N 체스판에 N개의 퀸을 서로 공격할 수 없게 놓기
# 퀸은 같은 행/열/대각선에 있으면 공격 가능
# 즉 한 행에는 한 개의 퀸만 놓을 수 있음 = 행은 중복 X니까 열, 대각선만 체크

class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [["."] * n for _ in range(n)]

        def is_safe(row, col):
            # 같은 열에 퀸이 있는지 확인
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            # 왼쪽 위 대각선에 있는지 확인
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1; j -= 1
            # 오른쪽 위 대각선에 있는지 확인
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1; j += 1
            return True

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        backtrack(0)
        return res
