"""
리트코드 46번: Permutations
"""
from itertools import permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permutations(nums, len(nums)))
nums=[1,2,3]
print(Solution().permute(nums))
