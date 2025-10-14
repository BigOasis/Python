def solution(cap, n, deliveries, pickups):
    i = n -1 # 배달
    j = n - 1 # 수거
    
    # 0 제외한 뒤쪽 가장 먼 거리 찾기
    while i >= 0 and deliveries[i] == 0:
        i -= 1
    while j >= 0 and pickups[j] == 0:
        j -= 1
        
    ans = 0
    while i >= 0 or j >= 0:
        # 가장 멀리 가야하는 집
        far = max(i, j) + 1
        ans += 2 * far
        
        # 배달
        load = cap
        while i >= 0 and load > 0:
            if deliveries[i] == 0:
                i -= 1
                continue
            take = min(deliveries[i], load)
            deliveries[i] -= take
            load -= take
            if deliveries[i] == 0:
                i -= 1
                
        # 수거
        space = cap
        while j >= 0 and space > 0:
            if pickups[j] == 0:
                j -= 1
                continue
            take = min(pickups[j], space)
            pickups[j] -= take
            space -= take
            if pickups[j] == 0:
                j -= 1
            
        # 다음 배달할 곳 찾기 
        while i >= 0 and deliveries[i] == 0:
            i -= 1
        while j >= 0 and pickups[j] == 0:
            j -= 1
    
    return ans