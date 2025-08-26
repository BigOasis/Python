"""
리트코드 131번: Palindrome Partitioning
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True

        res = []
        tmp = []

        def dfs(i):
            if i == n:
                res.append(tmp[:])
                return
            else:
                for j in range(i, n):
                    if dp[i][j]:
                        tmp.append(s[i:j+1])
                        dfs(j+1)
                        tmp.pop()
        dfs(0)
        return res
# s = "aab"
# print(Solution().partition(s))
