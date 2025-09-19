"""
선수 과목 없는 애들부터 듣기 시작
들을 때마다 연결된 과목의 선수 과목 개수 줄임
다 들으면 성공(True), 못 들으면 사이클 존재(False)
"""

from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        # 그래프 만들기 (b -> a), 진입차수 계산
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1

        # 진입차수 0부터 시작
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        cnt = 0

        while q:
            cur = q.popleft()
            cnt += 1
            for nxt in g[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        # 모든 과목을 들을 수 있으면 True
        return cnt == numCourses
