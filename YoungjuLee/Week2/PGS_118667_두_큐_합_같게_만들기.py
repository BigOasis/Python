"""
프로그래머스 두 큐 합 같게 만들기
80분
"""

from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)

    if (sum1 + sum2) % 2 != 0:
        return -1

    while True:
        if answer == 3 * len(queue1):
            return -1

        if sum1 > sum2:
            a = q1.popleft()
            q2.append(a)
            sum1 -= a
            sum2 += a
        elif sum1 < sum2:
            a = q2.popleft()
            q1.append(a)
            sum1 += a
            sum2 -= a
        else:
            return answer
        answer += 1
