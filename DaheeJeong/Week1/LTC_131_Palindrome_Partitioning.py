from itertools import combinations


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def dfs(start):
            if start == n:
                ans.append(path[:])
                return

            for end in range(start, n):
                if pal[start][end]:
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        n = len(s)
        # pal[i][j]: s[i..j]가 팰린드롬인지
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        ans = []
        path = []

        dfs(0)
        return ans