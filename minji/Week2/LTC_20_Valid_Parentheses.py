# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s):
        stack = []  # 여는 괄호들을 담아둘 스택
        pair = {')': '(', '}': '{', ']': '['}  # 닫는 괄호에 짝궁인 여는 괄호 짝지어두기

        for ch in s:
            if ch in pair.values():   # 여는 괄호라면
                stack.append(ch)
            else:                      # 닫는 괄호라면
                if not stack or stack[-1] != pair[ch]:
                    return False       # 스택이 비었거나 짝이 안 맞으면 false
                stack.pop()            # 짝 맞으면 pop

        return len(stack) == 0  # 스택이 비어 있어야 True
