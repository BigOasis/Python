"""
프로그래머스 76502. 괄호 회전하기
풀이시간: 50분
"""


# 올바른 괄호 문자열인지 확인하는 함수
def ck(li):
    stack = []

    for c in li:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)

        else:
            if len(stack) == 0:
                return False

            compare_c = stack.pop()

            if c == ']' and compare_c != '[':
                return False

            elif c == ')' and compare_c != '(':
                return False

            elif c == '}' and compare_c != '{':
                return False

    return len(stack) == 0


def solution(s):
    ans = 0
    for i in range(len(s)):
        rot = s[i:] + s[:i]  # i만큼 회전
        if ck(rot):
            ans += 1
    return ans
