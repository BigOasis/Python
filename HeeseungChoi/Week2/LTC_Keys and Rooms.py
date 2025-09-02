from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n  # 방문 체크 배열
        queue = deque()    # BFS에 사용될 큐

        visited[0] = 1     # 0번 방부터 시작
        queue.append(0)    # 0번 방 큐에 삽입

        while queue:
            node = queue.popleft()
            for key in rooms[node]:  # 현재 방에 있는 모든 열쇠
                if not visited[key]:
                    visited[key] = 1
                    queue.append(key)

        return all(visited)  # 모든 방을 방문했는지 확인