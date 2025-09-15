from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 만들기
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for a, b in prerequisites: # b -> a
            graph[b].append((a))
            indeg[a] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        finished = []
        
        while q:
            cur = q.popleft()
            finished.append(q)
            for next in graph[cur]:
                indeg[next] -= 1
                if indeg[next] == 0:
                    q.append(next)

        return len(finished) == numCourses