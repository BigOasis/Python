class Solution(object):
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False

        pairs = {')': '(', ']': '[', '}': '{'}
        opens = set(pairs.values())
        stack = []

        for st in s:
            if st in opens:
                stack.append(st)
            else:
                if not stack or stack[-1] != pairs.get(st):
                    return False
                stack.pop()

        if stack:
            return False
        return True