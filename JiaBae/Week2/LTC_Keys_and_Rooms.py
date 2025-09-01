"""
leetcode: Keys and Rooms
시간복잡도 : O(n + e) 방이 노드이고 각 방의 키가 간선. 방문하지 않은 곳만 방문하기에 선형 
bfs, dfs
"""
# bfs 방식 (stack 사용)
from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        keys = deque([])
        visited = [False] * n

        def bfs():
            # 초기화 
            visited[0] = True
            keys.extend(rooms[0])

            while keys :
                key = keys.popleft()

                # 처음 방문하는 방이면
                if not visited[key]:
                    visited[key] = True
                    keys.extend(rooms[key])

        bfs()
        return all(visited)
    

# dfs 방식    
class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n

        def dfs(index):
            for room in rooms[index] :
                if not visited[room] :
                    visited[room] = True
                    dfs(room)


        visited[0] = True
        dfs(0)
        return all(visited)