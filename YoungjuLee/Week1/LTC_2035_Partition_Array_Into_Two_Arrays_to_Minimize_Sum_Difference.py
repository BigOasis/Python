"""
LeetCode 2035. Partition Array Into Two Arrays to Minimize Sum Difference
배열을 두 부분으로 나누었을 때,
두 부분의 합 차이가 가장 작아야 한다.

풀이시간: 80분
"""
from typing import List
from itertools import combinations
import bisect

# 부분집합의 합
def cal_sum(arr):
    res = [[] for _ in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        for c in combinations(arr, i):
            res[i].append(sum(c))
    return res


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # 배열 반으로 나누기
        n = len(nums) // 2
        l, r = nums[:n], nums[n:]

        total = sum(nums)
        target = total / 2

        sum1 = cal_sum(l)
        sum2 = cal_sum(r)

        for arr in sum2:
            arr.sort()

        res = 1e9

        # 왼쪽-i개,  오른쪽 n-i개
        for i in range(n + 1):
            for s in sum1[i]:
                idx = bisect.bisect_left(sum2[n - i], target - s)
                for j in [idx - 1, idx]:
                    if 0 <= j < len(sum2[n - i]):
                        tmp = s + sum2[n - i][j]
                        diff = abs(total - 2 * tmp)
                        res = min(res, diff)
        return int(res)
