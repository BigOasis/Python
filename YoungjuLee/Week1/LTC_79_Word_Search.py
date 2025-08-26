"""
리트코드 79번: Word Search
30분
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r, c = len(board), len(board[0])
        visited = [[False] * c for _ in range(r)]

        def dfs(i, j, k):
            if k == len(word):
                return True
            # 범위를 벗어나거나
            if i < 0 or i >= r or j < 0 or j >= c:
                return False
            # 방문했거나 단어와 일치하지 않는 경우
            if visited[i][j] or board[i][j] != word[k]:
                return False

            visited[i][j] = True
            res = (dfs(i + 1, j, k + 1) or
                   dfs(i - 1, j, k + 1) or
                   dfs(i, j + 1, k + 1) or
                   dfs(i, j - 1, k + 1))
            visited[i][j] = False
            return res

        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    return True
        return False

# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# print(Solution().exist(board, "ABCCED"))
