"""
프로그래머스 타겟 넘버
풀이시간: 30분
"""


def solution(numbers, target):
    answer = 0
    arr = [0]
    for num in numbers:
        tmp = []
        for parent in arr:
            tmp.append(parent + num)
            tmp.append(parent - num)
        arr = tmp
    for leaf in arr:
        if leaf == target:
            answer += 1
    return answer