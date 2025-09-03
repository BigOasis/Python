class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        result = [""] * n
        
        for i, ch in enumerate(s) :
            if ch == '(' :
                stack.append(i)

            elif ch == ')' and stack:
                result[stack.pop()] = '('
                result[i] = ch
        answer = 0
        cnt = 0
        for ch in result :
            if ch == '' :
                cnt = 0
            else :
                cnt += 1
                answer = max(answer, cnt)
        return answer
        
# 개선 코드
# 마지막으로 매칭이 끊긴 위치를 기억 
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]         # 기준점
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)     # 기준점 갱신
                else:
                    ans = max(ans, i - st[-1])  # 현재 i에서 끝나는 최장 길이
        return ans