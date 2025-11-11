"""
리트코드 타겟 넘버
풀이시간: 70분
"""


import heapq
from collections import defaultdict
from typing import List


class Solution:
    def trapRainWater(self, hmap: List[List[int]]) -> int:
        n, m = len(hmap), len(hmap[0])
        ans = 0
        vis = defaultdict(bool)  # 방문 체크용 딕셔너리
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = []

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    heapq.heappush(q, (hmap[i][j], i, j))
                    vis[(i, j)] = True

        # BFS
        while q:
            h, x, y = heapq.heappop(q)

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # 유효 범위 및 방문 확인
                if 0 <= nx < n and 0 <= ny < m and not vis[(nx, ny)]:
                    vis[(nx, ny)] = True
                    # 현재 높이보다 낮으면 물이 고임
                    if hmap[nx][ny] < h:
                        ans += h - hmap[nx][ny]
                        hmap[nx][ny] = h
                    # 다음 탐색 노드 추가
                    heapq.heappush(q, (hmap[nx][ny], nx, ny))

        return ans
