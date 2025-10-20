"""
LeetCode 210. Course Schedule II

위상 정렬
70분
"""

from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 그래프 초기화
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses  # 각 노드의 진입차수

        for a, b in prerequisites:
            graph[b].append(a)  # b를 먼저 들어야 a 가능!
            indegree[a] += 1  # a 진입차수 증가

        # 바로 들을 수 있는 과목부터 시작
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []

        # bfs
        while q:
            cur = q.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                indegree[nxt] -= 1  # 선수 과목 하나 이수 → 진입차수 감소
                if indegree[nxt] == 0:  # 새로 들을 수 있게 되면 큐에 추가
                    q.append(nxt)

        return res if len(res) == numCourses else []
