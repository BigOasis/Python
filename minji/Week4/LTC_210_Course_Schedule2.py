# 207. Course Schedule 과 동일하지만 이번에는 수강 순서도 반환해야함
# list로 반환, 불가능하면 빈 리스트 반환하기

from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
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
        
        order = []  # 수강 순서를 저장할 리스트
        
        while q:
            cur = q.popleft()
            order.append(cur)  # 수강한 과목 기록
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        # 모든 과목을 다 들었다면 order 반환, 아니면 불가능해서 [] 리턴
        return order if len(order) == numCourses else []
