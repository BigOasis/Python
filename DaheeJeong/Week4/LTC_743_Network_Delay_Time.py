import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # 그래프 구성
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        # 다익스트라
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for nei, w in graph[node]:
                new_time = time + w
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))

        # 결과 계산
        max_time = max(dist.values())
        return max_time if max_time < float('inf') else -1
