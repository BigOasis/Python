"""
leetcode: Subsets
시간복잡도 : O(n x 2^n)
combinations 사용 방식
"""
from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        result = []
        for k in range(len(nums) + 1) :
            for c in combinations(nums, k) :
                result.append(list(c))
        return result
        