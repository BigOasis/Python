"""
LeetCode 743. Network Delay Time
442~
"""
from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v, w in times:
            g[u].append([v, w])

        # 최소힙
        pq = [(0, k)]
        INF = int(1e9)
        dist = [INF] * (n + 1)
        dist[k] = 0
        res = 0

        while pq:
            t, nod = heapq.heappop(pq)

            if t > dist[nod]:
                continue
            for nxt, w in g[nod]:
                if t + w < dist[nxt]:
                    dist[nxt] = t + w
                    heapq.heappush(pq, (dist[nxt], nxt))

        res = max(dist[1:])
        return res if res < INF else -1
