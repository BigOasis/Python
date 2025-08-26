"""
leetcode: Word Search
시간복잡도 : O(m x n x 3^L)
dfs + 백트래킹 
"""

class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y, idx) :
            # dfs 진행 조건 - board 값이 글자와 같은지 확인
            if board[x][y] != word[idx] :
                return False
            # 끝나는 조건
            if idx == len(word) - 1 :
                return True

            # dfs 진행이 가능하면
            visited[x][y] = True

            for i in range(4) :
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] :
                    if dfs(nx, ny, idx + 1) :
                        return True
            visited[x][y] = False
            return False

        for i in range(m) :
            for j in range(n) :
                if dfs(i, j, 0) :
                    return True
        return False