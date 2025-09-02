"""
LeetCode 841: Keys and Rooms
25분
"""

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        stk = [0]
        visited[0] = True

        while stk:
            cur = stk.pop()
            for nxt in rooms[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stk.append(nxt)

        for v in visited:
            if not v:
                return False
        return True


print(Solution().canVisitAllRooms([[1], [2], [3], []]))
