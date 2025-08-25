"""
leetcode: Sudoku Solver
시간복잡도 : 최악의 경우 O(9 ^ 빈칸의 갯수)
dfs 백트래킹
"""
class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # 비어있는 칸 구하기
        empty = []
        for i in range(9) :
            for j in range(9) :
                v = board[i][j]
                if board[i][j] == "." :
                    empty.append((i, j))
                else: 
                    rows[i].add(v)
                    cols[j].add(v)
                    boxes[(i // 3) * 3 + (j // 3)].add(v)
        
        def dfs(idx) :
            # 끝나는 조건
            if idx == len(empty) :
                return True

            i , j = empty[idx]
            b = (i // 3) * 3 + (j // 3)
            for n in "123456789" :
                if n not in rows[i] and n not in cols[j] and n not in boxes[b] :
                    board[i][j] = n
                    rows[i].add(n); cols[j].add(n); boxes[b].add(n)
                    if dfs(idx+1) :
                        return True
                    board[i][j] = "."
                    rows[i].remove(n); cols[j].remove(n); boxes[b].remove(n)
            return False
        
        dfs(0)

        