def solution(n, s, a, b, fares):
    # 무한대 설정하기
    # 약간고민포인트.. 
    # 무한대를 설정하는것보다 아예 접근 불가능한 None으로 설정하면? => 매번 None을 조건문으로 걸러야해서 길어짐..
    INF = int(1e9)

    # 거리 배열 초기화
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    # 자기 자신까지 비용은 0
    for i in range(1, n+1):
        dist[i][i] = 0
    
    # 주어진 간선 정보 반영
    for u, v, w in fares:
        dist[u][v] = w
        dist[v][u] = w  # 양방향
    
    # 플로이드 워셜을 써서 모든 지점에서 모든 지점까지의 최단 거리 구하기
    for k in range(1, n+1):       # 거쳐가는 노드
        for i in range(1, n+1):   # 출발 노드
            for j in range(1, n+1):  # 도착 노드
            # 최단 거리가 k를 거쳐가는게 더 짧은거리라면 교체
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # 합승 지점 고르기
    answer = INF
    for k in range(1, n+1):
        cost = dist[s][k] + dist[k][a] + dist[k][b]
        if cost < answer:
            answer = cost
    
    return answer
