import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        # 그래프 만들기
        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 거리 배열 (처음에는 무한대로 주기)
        INF = float('inf')
        dist = [INF] * (n+1)
        dist[k] = 0  # 시작점은 0
        
        # 다익스트라 ->최소 힙 (우선순위 큐)
        heap = []
        heapq.heappush(heap, (0, k))  # (현재 거리, 노드)
        
        while heap:
            cur_dist, node = heapq.heappop(heap) # 가장 가까운 노드를 꺼내!
            
            # 이미 더 짧은 거리로 방문한 적 있으면 스킵
            if cur_dist > dist[node]:
                continue
            
            # 인접 노드들 확인
            for nxt, w in graph[node]:
	            # 현재 거리+간선가중치 < 기존 거리  라면 갱신
                if dist[nxt] > cur_dist + w:
                    dist[nxt] = cur_dist + w
                    # 큐에 새로운 거리와 노드 넣기
                    heapq.heappush(heap, (dist[nxt], nxt))
        
        # 1번부터 n번까지 확인
        max_time = max(dist[1:])  # 0번 노드는 안쓰니까 [1:]
        
        # 만약 도달못한 노드가있다면 INF상태일 것. 하나라도 있으면 -1
        return max_time if max_time != INF else -1
