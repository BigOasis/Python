class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        max_seq, seq, now = 0, 1, sorted_nums[0]
        for num in sorted_nums:
            if num == now + 1:
                seq += 1
            else:
                max_seq = max(max_seq, seq)
                seq = 1
            now = num
        max_seq = max(max_seq, seq)
        return max_seq

