"""
프로그래머스 양과 늑대
80분

- 틀린 이유 ?
    - visited 배열로 방문 여부 관리해서 품
    - 그러나, 경로에 따라 상태(이 문제에선 sheep/wolf 누적) 달라지면
      visited[노드][상태] 또는 백트래킹/비트마스크를 사용해야함.
"""

SHEEP = 0
WOLF = 1


def solution(info, edges):
    n = len(info)
    graph = [[] for _ in range(n)]
    for p, c in edges:
        graph[p].append(c)

    def dfs(node, sheep, wolf, candidates):
        if info[node] == SHEEP:
            sheep += 1
        else:
            wolf += 1

        # 조건 위반 (다 잡아먹힘)
        if wolf >= sheep:
            return 0

        # 다음 다음으로 방문할 수 있는 후보 목록: 현재 노드의 자식들을 추가
        next_cand = candidates + graph[node]
        best = sheep

        for i, nxt in enumerate(next_cand):
            # 선택한 후보 제외한 나머지 후보들과 함께 재귀
            remain = next_cand[:i] + next_cand[i + 1:]
            best = max(best, dfs(nxt, sheep, wolf, remain))

        return best

    return dfs(0, 0, 0, [])

# info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
# edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
# print(solution(info, edges))
