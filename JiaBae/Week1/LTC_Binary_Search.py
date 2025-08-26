"""
leetcode: Binary Search
시간복잡도 : O(logN)
이진탐색
"""
class Solution(object):
    def search(self, nums, target):
        def dfs(start, end) :
            # target이 존재하지 않는 경우
            if start > end :
                return -1
            mid = (start + end) // 2
            # target 을 찾은 경우
            if nums[mid] == target :
                return mid
            # mid 보다 target 이 큰 경우
            elif nums[mid] < target : 
                return dfs(mid + 1, end)
            # mid 보다 target이 작은 경우
            else :
                return dfs(start, mid - 1)
        return dfs(0, len(nums) - 1)
            
        