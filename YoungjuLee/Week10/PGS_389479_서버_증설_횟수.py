"""
프로그래머스 389479. 서버 증설 횟수

풀이시간: 30분
"""


def solution(players, m, k):
    arr = []
    for pl in players:
        summ = sum((arr + [1])[-k:]) * m
        if summ > pl:
            arr = arr + [0]
        else:
            add = (pl - summ) // m + 1
            arr += [add]
    return sum(arr)
