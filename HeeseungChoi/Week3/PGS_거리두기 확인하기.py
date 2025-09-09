from collections import deque

# 특정 대기실 p(5x5)에서 거리두기가 잘 지켜지고 있는지 확인하는 BFS 함수
def bfs(p):
    start = []
    
    # 1. 대기실에서 'P'(사람) 좌표들을 모두 찾는다
    for i in range(5): 
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    # 2. 각 사람(P) 좌표를 시작점으로 BFS 탐색
    for s in start:
        queue = deque([s])                   # 시작 좌표를 큐에 삽입
        visited = [[0]*5 for i in range(5)]  # 방문 여부 기록
        distance = [[0]*5 for i in range(5)] # 시작점으로부터 거리 기록
        visited[s[0]][s[1]] = 1              # 시작점 방문 처리
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            # 4방향 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # (nx, ny)가 격자 범위 안이고 아직 방문하지 않은 경우
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    
                    # 빈 테이블("O")일 경우, 계속 탐색 가능
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])             
                        visited[ny][nx] = 1                 
                        distance[ny][nx] = distance[y][x] + 1 
                    
                    # 다른 사람("P")을 만났을 때
                    # 현재 위치까지의 거리가 1 이하라면
                    # 거리두기 위반 → 바로 0 반환
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


# 여러 대기실을 검사
def solution(places):
    answer = []
    
    # 각 대기실마다 BFS 
    for i in places:
        answer.append(bfs(i))
    
    return answer
