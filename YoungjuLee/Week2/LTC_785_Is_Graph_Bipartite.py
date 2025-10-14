"""
LeetCode 785. Is Graph Bipartite?
풀이시간: 70분

각 노드에 1, -1을 번갈아 칠해 연결된 노드끼리 다른 색이 되도록 한다.
dfs를 통해 색이 충돌(같은 색 연결)하면 False를 반환
연결 그래프가 아닐 수 있으므로 모든 노드에 대해 검사해야 함
"""
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        def dfs(node, c):
            color[node] = c
            for nxt in graph[node]:
                # 같은 색이면 실패
                if color[nxt] == c:
                    return False
                if color[nxt] == 0 and not dfs(nxt, -c):
                    return False
            return True

        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True
