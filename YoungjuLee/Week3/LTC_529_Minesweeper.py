"""
LeetCode 529. Minesweeper
20분
"""
from typing import List
from collections import deque


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        n = len(board)
        m = len(board[0])

        q = deque([(r, c)])

        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

        # M -> X로 바꾸고 종료
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        while q:
            x, y = q.popleft()
            if board[x][y] != 'E': continue

            mine_cnt = 0

            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'M':
                    mine_cnt += 1
            # 지뢰가 있다면 개수로 표시
            if mine_cnt > 0:
                board[x][y] = str(mine_cnt)
            # 없다면 주변 다시 재귀
            else:
                board[x][y] = 'B'
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'E':
                        q.append((nx, ny))
        return board

# board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
# click = [3,0]
# print(Solution().updateBoard(board,click))
