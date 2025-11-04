class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n  # dp[i]: nums[i]로 끝나는 LIS 길이
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]: 
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)