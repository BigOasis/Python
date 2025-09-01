# 처음 풀이
class Solution(object):
    def isValid(self, s):
        arr = []
        for ch in s :
            if ch in "({[" :
                arr.append(ch)
            else : 
                if len(arr) > 0 :
                    prev = arr.pop()
                else : return False
                if ch == ')' and prev != '(' : return False
                elif ch == '}' and prev != "{" : return False
                elif ch == ']' and prev != "[" : return False
        if len(arr) != 0 : return False
        return True
        
# 개선 코드
class Solution(object):
    def isValid(self, s):
        pair = {')': '(', ']': '[', '}': '{'}
        arr = []
        for ch in s :
            if ch in "({[" :
                arr.append(ch)
            else : 
                if not arr or arr[-1] != pair[ch] :
                    return False
                arr.pop()
        return not arr