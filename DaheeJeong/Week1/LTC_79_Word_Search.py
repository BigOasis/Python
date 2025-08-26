class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        visited = [[False] * n for _ in range(m)]

        def dfs(idx, x, y):
            if idx == len(word) - 1:
                return True

            visited[x][y] = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if board[nx][ny] == word[idx + 1]:
                        if dfs(idx + 1, nx, ny):
                            return True
            visited[x][y] = False
            return False

        first = word[0]
        for i in range(m):
            for j in range(n):
                if board[i][j] == first:
                    if dfs(0, i, j):
                        return True
        return False
