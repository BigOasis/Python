"""
광고삽입
60분
"""


def solution(play_time, adv_time, logs):
    # 재생 시간 (초 단위 변환)
    h, m, s = map(int, play_time.split(':'))
    play_arr = h * 3600 + m * 60 + s

    # 광고 시간 (초 단위 변환)
    h2, m2, s2 = map(int, adv_time.split(':'))
    adv_arr = h2 * 3600 + m2 * 60 + s2

    arr = [0] * (play_arr + 2)

    # 차분 배열로 변화 기록
    for log in logs:
        sh, sm, ss = map(int, log[:8].split(':'))
        eh, em, es = map(int, log[9:].split(':'))
        s = sh * 3600 + sm * 60 + ss
        e = eh * 3600 + em * 60 + es
        arr[s] += 1
        arr[e] -= 1

    # 각 초 시청자 수 누적합
    for i in range(1, play_arr + 1):
        arr[i] += arr[i - 1]

    # 총 시청 시간 누적합
    res = [0] * (play_arr + 2)
    for i in range(1, play_arr + 1):
        res[i] = res[i - 1] + arr[i - 1]

    max_time = 0
    ans = 0
    for start in range(0, play_arr - adv_arr + 1):
        end = start + adv_arr
        cur = res[end] - res[start]
        if cur > max_time:
            max_time, ans = cur, start

    h = ans // 3600
    ans %= 3600
    m = ans // 60
    s = ans % 60
    return f"{h:02}:{m:02}:{s:02}"
