"""
리트코드 32번: Longest Valid Parentheses
28붐
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = [-1]
        res = 0
        n = len(s)

        for i in range(n):
            if s[i] == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    cur = i - stk[-1]
                    if cur > res:
                        res = cur
        return res


# print(Solution().longestValidParentheses(")()())"))
