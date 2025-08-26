def solution(k, dungeons):
    def dfs(k, cnt, visited):
        max_cnt = cnt
        length = len(dungeons)
        for i in range(length):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                max_cnt = max(max_cnt, dfs(k - dungeons[i][1], cnt + 1, visited))
                visited[i] = False
        return max_cnt

    visited = [False] * len(dungeons)
    answer = dfs(k, 0, visited)
    return answer