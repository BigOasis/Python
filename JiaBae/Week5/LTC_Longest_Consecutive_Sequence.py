class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            # num 이 시작점인 경우
            if num-1 not in nums:
                cur = num
                cnt = 1
                while cur+1 in nums:
                    cur += 1
                    cnt += 1
                longest = max(longest, cnt)

        return longest