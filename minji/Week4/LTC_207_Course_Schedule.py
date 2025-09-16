from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # 그래프(인접 리스트) + 진입 차수 배열
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # 간선 추가
        for a, b in prerequisites:
            graph[b].append(a)   # b -> a
            indegree[a] += 1     # a의 진입 차수 증가
        
        # 진입 차수 0인 것부터 큐에 넣음
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0  # 몇 과목을 들었는지
        
        while q:
            cur = q.popleft()
            count += 1
            # 현재 과목을 들었으니, 연결된 다음 과목들의 진입 차수 감소시키기
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        # 다 들었으면 True, 아니면 False
        return count == numCourses
