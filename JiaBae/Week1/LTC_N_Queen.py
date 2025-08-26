"""
leetcode: N Queen
시간복잡도 : 최악은 O(n ^ n) 이지만 가지치기 때문에 O(n! x n)
dfs 백트래킹 
"""
class Solution(object):
    def solveNQueens(self, n):
        result = []
        board = [["."] * n for _ in range(n)]
        
        def is_available(r, c) :
            # 같은 열에 퀸이 있는지 검사
            for i in range(n):
                if board[i][c] == 'Q' :
                    return False

            # 좌 대각선 위로 퀸이 있는지 검사
            i, j = r-1, c-1
            while i >= 0 and j >= 0 :
                if board[i][j] == 'Q' :
                    return False
                i -= 1
                j -= 1
            
            # 우 대각선 위로 퀸이 있는지 검사
            i, j = r-1, c + 1
            while i >= 0 and j < n :
                if board[i][j] == 'Q' :
                    return False
                i -= 1
                j += 1
            
            return True

        def dfs(r) :
            # 솔루션 찾은 경우
            if r == n :
                result.append([''.join(row) for row in board])
                return 

            # 한 줄 어떻게 배치할지 
            for c in range(n) :
                if is_available(r, c) :
                    board[r][c] = 'Q'
                    dfs(r+1)
                    board[r][c] = '.'
        dfs(0)
        
        return result