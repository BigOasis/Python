from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # 필요한 문자 개수
        need = Counter(t)
        ch_count = {}
        have = 0
        needCount = len(need)
        l = 0
        res, resLen = [-1, -1], float("inf")

        for r, ch in enumerate(s):
            # 개수 세기
            ch_count[ch] = ch_count.get(ch, 0) + 1

            if ch in need and ch_count[ch] == need[ch]:
                have += 1
            
            # 단어 다 있으면 
            while have == needCount:
                # 더 짧은 윈도우면 갱신
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l +1

                # 왼쪽 축소
                ch_count[s[l]] -= 1
                if s[l] in need and ch_count[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""