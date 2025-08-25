"""
리트코드 60번: Permutation Sequence
"""
from itertools import permutations


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]
        arr = sorted(permutations(nums))
        return ''.join(arr[k - 1])

n,k=3,3
print(Solution().getPermutation(n,k))
