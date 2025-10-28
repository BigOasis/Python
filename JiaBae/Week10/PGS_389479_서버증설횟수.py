def solution(players, m, k):
    answer = 0
    n = len(players)
    
    # 서버 개수
    server = [0] * (n)
    
    # 매 시간대마다
    for i in range(n):
        
        # 서버 갯수가 가용 불가한 경우
        if players[i] // m > server[i]:
            
            # 서버 증설
            need_server = players[i] // m - server[i] # 필요한 서버 갯수 계산
            answer += need_server
            
            # 서버 k 시간동안 유지 
            for j in range(i, i+k):
                if j < n :
                    server[j] += need_server
    
    return answer