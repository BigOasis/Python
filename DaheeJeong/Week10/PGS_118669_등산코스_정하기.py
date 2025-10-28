import heapq


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    summits = set(summits)
    INF = int(1e9)
    dist = [INF] * (n + 1)
    pq = []

    for g in gates:
        dist[g] = 0
        heapq.heappush(pq, (0, g))

    while pq:
        intensity, node = heapq.heappop(pq)
        if dist[node] < intensity or node in summits:
            continue
        for nxt, cost in graph[node]:
            new_intensity = max(intensity, cost)
            if dist[nxt] > new_intensity:
                dist[nxt] = new_intensity
                heapq.heappush(pq, (new_intensity, nxt))

    ans = [0, INF]
    for s in sorted(list(summits)):
        if dist[s] < ans[1]:
            ans = [s, dist[s]]
    return ans
