from collections import defaultdict
import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')]  * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        cur_d, u = heapq.heappop(pq)
        if cur_d <= dist[u]:
            for v, w in graph[u]:
                new_d = cur_d + w
                if new_d < dist[v]:
                    dist[v] = new_d
                    heapq.heappush(pq, (new_d, v))
    return dist

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for c, d, w in fares:
        graph[c].append((d, w))
        graph[d].append((c, w))
        
    ds = dijkstra(n, graph, s)
    da = dijkstra(n, graph, a)
    db = dijkstra(n, graph, b)
    
    answer = min(ds[k] + da[k] + db[k] for k in range(1, n+1))
    return answer