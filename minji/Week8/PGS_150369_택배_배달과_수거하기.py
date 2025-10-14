def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0  # 배달할거
    p = 0  # 수거할거
    
    # 가장 먼 집부터 갈라고 끝부분부터 역순으로 처리하기
    for i in range(n-1, -1, -1):
        d += deliveries[i]
        p += pickups[i]
        
        # d 또는 p 중 하나라도 아직 처리해야 하면
        while d > 0 or p > 0:
            # 한 번 왕복 (물류창고 → 집 (i) → 물류창고)
            answer += (i + 1) * 2
            d -= cap
            p -= cap
    
    return answer
