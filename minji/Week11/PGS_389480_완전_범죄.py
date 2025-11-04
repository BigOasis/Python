# dfs로 모든 경우의 수 탐색하면 시간초과
# dp로 이미 탐색한 상태 저장하여서 중복탐색을 방지하기

def dfs(a, b, idx, info, n, m, dp):
    global rs
    if idx == len(info):
        if a < n and b < m:
            rs = min(rs, a)
        return

    if (a, b, idx) in dp:
        return
    dp.add((a, b, idx))

    if a >= n or b >= m or a >= rs:
        return

    dfs(a + info[idx][0], b, idx + 1, info, n, m, dp)
    dfs(a, b + info[idx][1], idx + 1, info, n, m, dp)

def solution(info, n, m):
    global rs
    rs = float('inf')
    dp = set()
    dfs(0, 0, 0, info, n, m, dp)
    return rs if rs != float('inf') else -1
