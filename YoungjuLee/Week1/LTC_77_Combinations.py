"""
리트코드 78번: Combinations
"""
from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return [list(c) for c in combinations(range(1, n+1),k)]

print(Solution().combine(4,2))
