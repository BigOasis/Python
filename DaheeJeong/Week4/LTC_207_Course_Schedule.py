from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # 선수과목 0인 과목 큐에 삽입
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0

        # BFS
        while queue:
            course = queue.popleft()
            count += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return count == numCourses
