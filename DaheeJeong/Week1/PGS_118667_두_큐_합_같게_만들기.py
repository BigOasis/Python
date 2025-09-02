from collections import deque


def solution(queue1, queue2):
    answer = 0
    if sum(queue1) + sum(queue2) % 2 == 1:
        return -1

    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(q1)
    s2 = sum(q2)

    for _ in range(len(queue1) * 4):
        if s1 == s2:
            return answer
        elif s1 > s2:
            pp = q1.popleft()
            q2.append(pp)
            s1 -= pp
            s2 += pp
        else:
            pp = q2.popleft()
            q1.append(pp)
            s1 += pp
            s2 -= pp
        answer += 1
    return -1