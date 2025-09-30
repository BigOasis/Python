    # 초기값으로 모든 시간들을 초로 만들기 위한 함수 작성
def time_to_sec(time:str):
    h,m,s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s
    
    # 다시 시간으로 환산 함수 작성
def sec_to_time(num:int):
    h = f'{num // 3600:02d}'              
    m = f'{(num % 3600) //60:02d}'       
    s = f'{(num % 3600) %60:02d}'
    return ':'.join([h, m, s]) 

def solution(play_time, adv_time, logs):
    #광고시간과 실제 시간 같으면 바로
    if play_time == adv_time: return '00:00:00'
    
    # 시간을 초로 환산해서 비교진행
    answer = 0
    adv_sec = time_to_sec(adv_time)
    play_sec = time_to_sec(play_time)
    sec = [0] * (play_sec + 1)
    
    # logs는 시청 시작-종료 시간을 나타내는 문자열 리스트
    for i in  range(len(logs)):
        s,e = map(time_to_sec, logs[i].split('-'))
        # 시작 시간에는 +1, 종료 시간에는 -1 
        sec[s] += 1
        sec[e] -= 1
        
    # 누적합 1차: 각 초마다 "현재 시청자 수"를 계산
    for i in range(1,len(sec)):
        sec[i] += sec[i-1]
        
    # 누적합 2차: 각 초까지의 "누적 시청 시간"을 계산
    for i in range(1, len(sec)):
        sec[i] += sec[i-1]
        
    max_time = 0
    
    # 광고가 들어갈 수 있는 모든 끝점 i에 대해 [i-adv_sec+1, i] 구간 합 계산
    for i in range(adv_sec-1, play_sec):
        if i >= adv_sec:
            time = sec[i] - sec[i-adv_sec]
        else:
            # 처음부터 광고가 시작되는 경우
            time = sec[i]

        # 최대 시청 시간을 갱신하면 광고 시작 시간을 저장
        if max_time < time:
            max_time = time
            answer = i-adv_sec+1

    # 최종 광고 시작 시간 변환 진행
    return sec_to_time(answer)
        
    
    
    
   