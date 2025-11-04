"""
프로그래머스 신고결과 받기

풀이시간: 60분
"""


def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n
    reported = {x: 0 for x in id_list}

    for r in set(report):
        a, b = r.split()
        reported[b] += 1

    for r in set(report):
        a, b = r.split()
        if reported[b] >= k:
            answer[id_list.index(a)] += 1

    return answer
