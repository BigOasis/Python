def to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h*3600 + m*60 + s

def to_hhmmss(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def solution(play_time, adv_time, logs):
    # 시간 초단위로변경해서 처리하기
    play = to_seconds(play_time)   # 전체 재생
    adv = to_seconds(adv_time)     # 광고
    
    # 구간별 시청자 변화 기록용 배열
    times = [0] * (play+2)
    
    # 1. 시청자 수 변화 기록
    for log in logs:
        start, end = log.split("-")
        s, e = to_seconds(start), to_seconds(end)
        times[s] += 1
        times[e] -= 1
    
    # 2. 시청자 수 누적
    for i in range(1, play+1):
        times[i] += times[i-1]
    
    # 3. 총 시청 시간 누적
    for i in range(1, play+1):
        times[i] += times[i-1]

    # 4. 광고를 삽입하는 최적의시각 찾기 => 슬라이딩윈도우 써면됨
    max_view = times[adv-1]
    max_start = 0
    for start in range(1, play-adv+1):
        end = start + adv - 1
        current_view = times[end] - times[start-1]
        if current_view > max_view:
            max_view = current_view
            max_start = start
    return to_hhmmss(max_start)
