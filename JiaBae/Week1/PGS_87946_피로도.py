"""
Programmers: 피로도
시간복잡도 : O(n! x n), O(n!)
itertools 사용하는 방법 + 백트래킹하는 방법
"""
from itertools import permutations

def solution(k, dungeons):
    answer = 0

    # 가능한 순열 전부 탐색 
    for lists in permutations(dungeons) :
        current = k
        cleared = 0
        for req, cost in lists:
            # 최소 피로도보다 크면
            if current >= req :
                current -= cost
                cleared += 1
            else : 
                break
        answer = max(answer, cleared)
        
        # 빠르게 최대 던전 수 찾으면 바로 return 
        if answer == len(dungeons) :
            return answer
    return answer

# 완전탐색 (백트래킹)
def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    best = 0

    def dfs(cur, cleared):
        nonlocal best
        best = max(best, cleared)
        if best == n:   # 최적 상한(더 이상 못 늘어남)
            return
        for i in range(n):
            req, cost = dungeons[i]
            if not visited[i] and cur >= req:
                visited[i] = True
                dfs(cur - cost, cleared + 1)
                visited[i] = False

    dfs(k, 0)
    return best