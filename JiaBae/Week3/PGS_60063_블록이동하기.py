from collections import deque

def solution(board):
    N = len(board)
    
    def free(x, y):
        return 0 <= x < N and 0 <= y < N and board[x][y] == 0
    
    start = tuple(sorted(((0, 0), (0, 1))))
    q = deque([(start, 0)])
    visited = {start}
        
    while q :
        (a, b), cnt = q.popleft()
        (x1, y1), (x2, y2) = a,b
        
        # 끝나는 조건 (하나라도 도착지점에 닿으면)
        if (x1, y1) == (N-1, N-1) or (x2, y2) == (N-1, N-1) : return cnt
        
        # 1) 4방향 평행이동
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy
            if free(nx1, ny1) and free(nx2, ny2):
                ns = tuple(sorted(((nx1, ny1), (nx2, ny2))))
                if ns not in visited:
                    visited.add(ns)
                    q.append((ns, cnt + 1))
                
       # 2) 회전
        if x1 == x2:  # 가로 상태 -> 위/아래로 세로 회전
            for sgn in (-1, 1):  # 위(-1), 아래(+1)
                nx = x1 + sgn
                # 회전 방향의 두 칸이 모두 비어 있어야 함
                if free(nx, y1) and free(nx, y2):
                    # (x1,y1)을 축으로 회전
                    ns1 = tuple(sorted(((x1, y1), (nx, y1))))
                    if ns1 not in visited:
                        visited.add(ns1)
                        q.append((ns1, cnt + 1))
                    # (x2,y2)을 축으로 회전
                    ns2 = tuple(sorted(((x2, y2), (nx, y2))))
                    if ns2 not in visited:
                        visited.add(ns2)
                        q.append((ns2, cnt + 1))
        else:  # y1 == y2, 세로 상태 -> 좌/우로 가로 회전
            for sgn in (-1, 1):  # 좌(-1), 우(+1)
                ny = y1 + sgn
                if free(x1, ny) and free(x2, ny):
                    ns1 = tuple(sorted(((x1, y1), (x1, ny))))
                    if ns1 not in visited:
                        visited.add(ns1)
                        q.append((ns1, cnt + 1))
                    ns2 = tuple(sorted(((x2, y2), (x2, ny))))
                    if ns2 not in visited:
                        visited.add(ns2)
                        q.append((ns2, cnt + 1))