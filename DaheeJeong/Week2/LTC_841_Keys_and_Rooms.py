class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        length = len(rooms)
        visited = [False] * length

        def dfs(v):
            visited[v] = True
            for room in rooms[v]:
                if not visited[room]:
                    dfs(room)

        dfs(0)
        if all(visited):
            return True
        else:
            return False