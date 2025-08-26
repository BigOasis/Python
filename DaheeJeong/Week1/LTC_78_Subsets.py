from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums) + 1
        answer = []
        for i in range(length):
            answer.extend(list(combinations(nums, i)))

        return answer
