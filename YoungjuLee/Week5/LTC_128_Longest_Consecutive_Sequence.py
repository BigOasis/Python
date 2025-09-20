"""
LeetCode Longest Consecutive Sequence
1136~
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        arr = set(nums)

        for num in arr:
            if num - 1 not in arr:
                tmp = 1
                cur = num
                while cur + 1 in arr:
                    cur += 1
                    tmp += 1
                res = max(res, tmp)

        return res
