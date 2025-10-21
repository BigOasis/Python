def solution(info, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)

    max_sheep = 0

    def dfs(node, sheep, wolf, available):
        nonlocal max_sheep

        # 현재 노드의 동물 추가
        if info[node] == 0:  # 양
            sheep += 1
        else:  # 늑대
            wolf += 1

        # 늑대가 양 이상이면 실패
        if wolf >= sheep:
            return

        # 최대 양 갱신
        max_sheep = max(max_sheep, sheep)

        # 현재 노드에서 이동 가능한 후보들 업데이트
        next_nodes = available.copy()
        next_nodes.remove(node)
        next_nodes.extend(graph[node])

        for nxt in next_nodes:
            dfs(nxt, sheep, wolf, next_nodes)

    dfs(0, 0, 0, [0])
    return max_sheep
