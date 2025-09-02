class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)  # 각 방을 방문했는지? 체크하는 배열 - 기본값 false
        visited[0] = True  # 0번 방은 처음부터 열려있으니까 true처리

        def dfs(room):
            for key in rooms[room]:  # 방 안에 있는 열쇠들
                if not visited[key]:  # 아직 안 들어간 방이면
                    visited[key] = True
                    dfs(key)  # 재귀 호출

        dfs(0)  # 0번 방부터 시작
        return all(visited)  # 모든 방을 방문했으면 True
