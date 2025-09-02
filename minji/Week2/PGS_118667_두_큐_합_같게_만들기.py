# 합이 다르면 큰쪽에서 작은쪽으로 숫자를 옮긴다.
# 두 큐합 총합을 먼저 구해보고 홀수면 -1 리턴(애초에 같아질 수없음)
# deque써서 pop/append
# 합이 같아질때까지 계속 실행하되 리미트를 줘서 무한루프 방지

from collections import deque

def solution(queue1, queue2):
    # 큐로 변환
    q1 = deque(queue1)
    q2 = deque(queue2)

    s1, s2 = sum(q1), sum(q2)
    total = s1 + s2

    # 홀수면 불가능하니까 -1 리턴
    if total % 2 != 0:
        return -1

    target = total // 2
    cnt = 0
    limit = len(q1) * 3  # 무한루프방지! 

    # 시뮬레이션 돌려봐
    while cnt <= limit:
        if s1 == target:
            return cnt
        if s1 > target:  # q1에서 빼서 q2에 넣기
            x = q1.popleft()
            q2.append(x)
            s1 -= x
            s2 += x
        else:            # q2에서 빼서 q1에 넣기
            x = q2.popleft()
            q1.append(x)
            s2 -= x
            s1 += x
        cnt += 1

    return -1
