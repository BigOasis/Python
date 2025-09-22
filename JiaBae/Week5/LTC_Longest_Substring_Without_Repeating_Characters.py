class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 슬라이딩 윈도우
        last = {}
        answer = 0
        l = 0
        
        for r, ch in enumerate(s) :
            if ch in last and last[ch] >= l:
                l = last[ch] + 1

            # 문자의 최신 위치 기록
            last[ch] = r
            answer = max(answer, r-l+1)

        return answer