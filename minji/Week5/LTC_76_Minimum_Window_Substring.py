from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)   # 필요한 문자 개수
        missing = len(t)    # 아직 못 채운 문자 수
        left = 0
        res = ""            # 결과 문자열
        min_len = float('inf')
        
        for right in range(len(s)):
            ch = s[right]
            if need[ch] > 0:   # 필요한 문자면
                missing -= 1
            need[ch] -= 1      # 윈도우에 추가
            
            # 다 채웠으면 이제 왼쪽 줄여보기
            while missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]
                
                # 왼쪽 문자 빼기
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        
        return res
if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    print(sol.minWindow(s, t))
