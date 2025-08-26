def solution(k, dungeons):
    n = len(dungeons) # 전체 던전개수
    visited = [False] * n  # 방문여부
    best = 0 # 지금까지 탐험한 던전의 최댓값 저장 변수

    def dfs(stamina, cleared): #현재 피로도와 탐험개수를 받아서 탐색하는 재귀함수 dfs 선언
        nonlocal best # 바깥에 선언된 변수를 dfs에서도 사용가능하게 함
        # 현재 탐색 루트가 더 길다면 최댓값 갱신
        if cleared > best:
            best = cleared

        # 더 들어갈 수 있으면 계속 탐색함
        for i in range(n):
            req, cost = dungeons[i]
            if not visited[i] and stamina >= req:
                visited[i] = True
                dfs(stamina - cost, cleared + 1)
                visited[i] = False  # 백트래킹

    dfs(k, 0)
    return best