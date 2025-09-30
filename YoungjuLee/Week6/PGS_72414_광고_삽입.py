"""
광고삽입
60분
"""


def solution(play_time, adv_time, logs):
    # 재생 시간
    h, m, s = map(int, play_time.split(':'))
    play_arr = h * 3600 + m * 60 + s

    # 광고 시간
    h2, m2, s2 = map(int, adv_time.split(':'))
    adv_arr = h2 * 3600 + m2 * 60 + s2

    arr = [0] * (play_arr + 2)

    # 시청자 변화 기록
    for log in logs:
        h1, s1, s1 = map(int, log[:8].split(':'))
        h2, s2, s2 = map(int, log[9:].split(':'))
        s = h1 * 3600 + s1 * 60 + s1
        e = h2 * 3600 + s2 * 60 + s2
        # difference array
        arr[s] += 1
        arr[e] -= 1

    for i in range(1, play_arr + 1):
        arr[i] += arr[i - 1]
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
