import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))
        
        prob = [0.0] * n
        prob[start] = 1.0
        
        # 우선순위 큐에 (확률, 노드) 형태로 삽입
        pq = [(-1.0, start)]
        
        while pq:
            cur_p, node = heapq.heappop(pq)
            cur_p = -cur_p # 부호 반전
            
            # 목표 노드에 도달하면 바로 반환
            if node == end:
                return cur_p
            
            # 이미 더 큰 확률로 방문한 적 있다면 패스
            if cur_p < prob[node]:
                continue
            
            # 인접 노드 탐색
            for nxt, p in graph[node]:
                new_p = cur_p * p
                if new_p > prob[nxt]:
                    prob[nxt] = new_p
                    heapq.heappush(pq, (-new_p, nxt))
        
        return 0.0
