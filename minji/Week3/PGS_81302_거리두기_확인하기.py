from collections import deque

def check(place):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':  # 사람 발견
                q = deque()
                q.append((i, j, 0))  # (x, y, 거리)
                visited = [[False]*5 for _ in range(5)]
                visited[i][j] = True
                
                while q:
                    x, y, dist = q.popleft()
                    if dist >= 2:
                        continue  # 거리가 2 초과면 더 탐색 안함
                    
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                            if place[nx][ny] == 'X':  # 파티션
                                continue
                            if place[nx][ny] == 'P':  # 사람 발견
                                return 0  # 거리두기 위반
                            q.append((nx, ny, dist + 1))
                            visited[nx][ny] = True
    return 1

def solution(places):
    result = []
    for place in places:
        result.append(check(place))
    return result
