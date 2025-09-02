"""
리트코드 20번: Valid Parentheses
7분
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        parens = {'{': '}', '(': ')', '[': ']'}

        for ch in s:
            if ch in parens:
                stk.append(ch)
            else:
                if stk and parens[stk[-1]] == ch:
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        return True
