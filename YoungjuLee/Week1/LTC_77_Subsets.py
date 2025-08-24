"""
리트코드 77번: Subsets
13분
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        n = len(nums)
        for msk in range(1 << n):
            subset = []
            for i in range(n):
                if msk & (1 << i):
                    subset.append(nums[i])
            res.append(list(subset))
        return res

print(Solution().subsets([1,2,3]))