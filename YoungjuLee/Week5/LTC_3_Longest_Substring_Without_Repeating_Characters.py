"""
LeetCode: Longest Substring Without Repeating Characters
30분
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = set()
        l, r = 0, 0
        res = 0
        for r in range(len(s)):
            # 중복이면 left 포인터를 이동시키고 제거
            while s[r] in dict:
                dict.remove(s[l])
                l += 1
            dict.add(s[r])
            res = max(res, r - l + 1)
        return res
