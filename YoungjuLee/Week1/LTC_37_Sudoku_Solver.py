"""
리트코드 37번: Sudoku Solver
"""

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def get_candidates(i, j):
            box_idx = (i // 3) * 3 + j // 3
            return {"1", "2", "3", "4", "5", "6", "7", "8", "9"} - rows[i] - cols[j] - boxes[box_idx]

        def dfs():
            if not empty:
                return True  # 다 채움

            # MRV
            empty.sort(key=lambda x: len(get_candidates(x[0], x[1])))
            i, j = empty.pop(0)

            for num in get_candidates(i, j):
                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3) * 3 + j // 3].add(num)

                if dfs():
                    return True

                # 백트래킹
                board[i][j] = "."
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[(i // 3) * 3 + j // 3].remove(num)

            empty.insert(0, (i, j))
            return False

        dfs()
