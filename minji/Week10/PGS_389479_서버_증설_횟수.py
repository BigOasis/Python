def solution(players, m, k):
    n = len(players)
    expire = [0] * (n + k + 1)  # 만료 예약용
    current_servers = 0
    answer = 0

    for i in range(n):
        # 만료된 서버 제거
        current_servers -= expire[i]

        # 필요한 서버 수 계산
        needed = players[i] // m
        
        # 부족하면 증설
        if current_servers < needed:
            diff = needed - current_servers
            answer += diff
            current_servers += diff
            expire[i + k] += diff  # k시간 후 만료 예약

    return answer
