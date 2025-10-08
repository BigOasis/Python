import math

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    cars = []          # 차량 번호 목록
    times = []         # 누적 주차 시간
    enter = []         # 현재 주차 중인 차량 정보 [번호, 입차시각]
    
    # "HH:MM" 분 단위 변환 함수
    def to_min(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m
    
    for rec in records:
        t, num, status = rec.split()
        time = to_min(t)
        
        if num not in cars:     # 처음 보는 차량이면 등록
            cars.append(num)
            times.append(0)
        
        idx = cars.index(num)   # 차량 인덱스 찾기
        
        if status == "IN":
            enter.append([num, time])
        else:
            # 입차 목록에서 해당 차량 찾기
            for e in enter:
                if e[0] == num:
                    in_time = e[1]
                    enter.remove(e)
                    break
            times[idx] += time - in_time  # 누적 주차시간 추가
    
    # 출차 안 한 차량은 23:59 처리하래
    end = to_min("23:59")
    for e in enter:
        num, in_time = e
        idx = cars.index(num)
        times[idx] += end - in_time
    
    # 요금 계산
    result = []
    for num, t in sorted(zip(cars, times)):
        if t <= base_time:
            fee = base_fee
            # fee = 기본요금
        else:
            fee = base_fee + math.ceil((t - base_time) / unit_time) * unit_fee
            # 기본요금 + ceil((total_time[car]-기본시간)/단위시간)*단위요금
        result.append(fee)
    
    return result
