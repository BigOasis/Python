class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]

        for n in nums[1:]:
            cur = max(n, cur +n) # 새로 시작 vs 이어서 붙이기
            best = max(best, cur)
        return best
        