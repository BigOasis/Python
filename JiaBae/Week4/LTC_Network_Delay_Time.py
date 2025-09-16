import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 만들기
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        INF = float('inf')
        dist = [INF] * (n+1)
        dist[k] = 0
        pq = [(0, k)] # 현재까지의 시간, 노드

        while pq:
            cur_t, u = heapq.heappop(pq)
            # 도달할 수 있는 것 중 더 최단인게 오면 
            if cur_t <= dist[u]:
                for v, w in graph[u]:
                    nt = cur_t + w
                    if nt < dist[v]:
                        dist[v] = nt
                        heapq.heappush(pq, (nt, v))

        mx = max(dist[1:])
        return -1 if mx == INF else mx