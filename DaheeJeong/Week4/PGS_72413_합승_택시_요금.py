def solution(n, s, a, b, fares):
    INF = int(1e9)

    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    for u, v, cost in fares:
        dist[u][v] = cost
        dist[v][u] = cost

        # 플로이드 워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 경유지점 k를 정해서 s→k→a,b 경로 최소합 계산
    min_cost = INF
    for k in range(1, n + 1):
        cost = dist[s][k] + dist[k][a] + dist[k][b]
        min_cost = min(min_cost, cost)

    return min_cost
