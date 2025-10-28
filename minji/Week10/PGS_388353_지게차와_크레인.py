def solution(storage, requests):
    # 빈 값으로 storage 래핑
    empty_row = ["-" * len(storage[0])]
    storage = empty_row + storage + empty_row
    storage = [list("-" + row + "-") for row in storage]
    
    N, M = len(storage), len(storage[0])
    move = [(1,0), (0,1), (-1,0), (0,-1)]
    
    # 요청 처리
    for req in requests:
        t = req[0]
        
        # 요청이 알파벳 2개인 경우, 전부 삭제
        if len(req) == 2:
            for i in range(N):
                for j in range(M):
                    if storage[i][j] == t:
                        storage[i][j] = "-"
        else: # 알파벳 1개 요청인 경우, 바깥에서 접근 가능한 부분만 삭제
            visited = [[False] * M for _ in range(N)]
            q = [(0, 0)]
            # BFS
            del_list = []
            while q:
                # 방문 체크
                x, y = q.pop()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                
                # 탐색
                for a, b in move:
                    dx, dy = x+a, y+b
                    # 경계 체크
                    if dx >= N or dx < 0 or dy >= M or dy < 0:
                        continue
                
                    # 타입 비교 후 제거 목록에 추가
                    if storage[dx][dy] == t:
                        del_list.append((dx, dy))
                    
                    # 다음 탐색 후보지 추가
                    if visited[dx][dy] or storage[dx][dy] != "-":
                        continue
                    
                    q.append((dx, dy))
            
            # 컨테이너 제거
            for x, y in del_list:
                storage[x][y] = "-"
                
    # 결과 반환
    result = 0
    for i in range(N):
        for j in range(M):
            if storage[i][j] != "-":
                result += 1
    return result