def solution(total_time, adv_time, records):

    total_time = to_seconds(total_time)
    adv_time = to_seconds(adv_time)
    timeline = [0] * (total_time + 1)

    for record in records:
        s, e = record.split('-')
        s = to_seconds(s)
        e = to_seconds(e)
        timeline[s] += 1
        timeline[e] -= 1

    for i in range(1, len(timeline)):
        timeline[i] += timeline[i - 1]

    for i in range(1, len(timeline)):
        timeline[i] += timeline[i - 1]

    best_sum = 0
    start_point = 0
    for i in range(adv_time - 1, total_time):
        if i >= adv_time:
            cur = timeline[i] - timeline[i - adv_time]
            if best_sum < cur:
                best_sum = cur
                start_point = i - adv_time + 1
        else:
            if best_sum < timeline[i]:
                best_sum = timeline[i]
                start_point = i - adv_time + 1

    return to_hms(start_point)


def to_seconds(hms):
    h, m, s = hms.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def to_hms(sec):
    h = sec // 3600
    h = f'0{h}' if h < 10 else str(h)
    sec %= 3600
    m = sec // 60
    m = f'0{m}' if m < 10 else str(m)
    sec %= 60
    s = f'0{sec}' if sec < 10 else str(sec)
    return f"{h}:{m}:{s}"
