"""
leetcode: Permutations
시간복잡도 : O(n! x n^2)
직접 구현 방식 + permutations 사용 방식
"""
class Solution(object):
    def permute(self, nums):
        result = []
        temp = []
        def dfs () :
            if len(temp) == len(nums) :
                result.append(temp[:])
                return
            for num in nums :
                if num not in temp :
                    temp.append(num)
                    dfs()
                    temp.pop()
        dfs()
        return result

# itertools 라이브러리 사용해서 푸는 방법        
from itertools import permutations

class Solution(object):
    def permute(self, nums):
        return[ list(p) for p in permutations(nums)]
        