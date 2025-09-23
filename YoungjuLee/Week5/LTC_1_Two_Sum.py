"""
LeetCode 1번: Two Sum
해시테이블로 풀기
15분
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            if num in table:
                return [table[num], i]
            table[target - num] = i
