"""
LeetCode 632. Smallest Range Covering Elements from K Lists

풀이시간: 70분
"""
import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
         :type nums: List[List[int]]
         :rtype: List[int]
         """
        heap = []
        max_val = -10 ** 9

        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            max_val = max(max_val, arr[0])

        res = [-10 ** 9, 10 ** 9]

        while True:
            min_val, i, j = heapq.heappop(heap)
            # 현재 범위 갱신
            if max_val - min_val < res[1] - res[0]:
                res = [min_val, max_val]
            # 다음 원소가 없으면 종료
            if j + 1 == len(nums[i]):
                break
            nxt = nums[i][j + 1]
            heapq.heappush(heap, (nxt, i, j + 1))
            max_val = max(max_val, nxt)

        return res
