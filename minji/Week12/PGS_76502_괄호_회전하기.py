def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        rotated = s[i:] + s[:i]
        stack = []
        valid = True
        
        for ch in rotated:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    valid = False
                    break
                top = stack.pop()
                if (ch == ')' and top != '(') or \
                   (ch == ']' and top != '[') or \
                   (ch == '}' and top != '{'):
                    valid = False
                    break
        if valid and not stack:
            answer += 1
    
    return answer
