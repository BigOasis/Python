"""
LeetCode 76번: Minimum_Window_Substring.py
슬라이딩 윈도우 + 투포인터
45분
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chs = [0] * 128  # t의 각 문자 저장 (영어 대소문자 아스키)
        l = 0
        max_len, max_l = len(s) + 1, 0
        cnt = len(t)  # 아직 충족해야 하는 문자 개수

        for ch in t:
            chs[ord(ch)] += 1

        for r, ch in enumerate(s):
            # 필요한 문자라면
            if chs[ord(ch)] > 0:
                cnt -= 1

            chs[ord(ch)] -= 1

            while cnt == 0:
                if r - l + 1 < max_len:
                    max_len, max_l = r - l + 1, l
                chs[ord(s[l])] += 1
                if chs[ord(s[l])] > 0:  # 필요한 문자를 빼버린 경우
                    cnt += 1
                l += 1

        if max_len == len(s) + 1:
            return ""
        else:
            return s[max_l:max_l + max_len]
