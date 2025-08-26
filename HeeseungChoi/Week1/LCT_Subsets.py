from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(start, visited):
            result.append(visited)

            for i in range (start , len(nums)):
                dfs(i+1, visited + [nums[i]])

        dfs(0,[])
        return result
        