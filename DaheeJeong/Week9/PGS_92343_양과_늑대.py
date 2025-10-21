def solution(info, edges):
    n = len(info)
    g = [[] for _ in range(n)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)

    best = dict()
    answer = 0

    start_mask = 1 << 0
    start_sheep = 1 - info[0]  # info: 0=양, 1=늑대
    start_wolf  = info[0]
    best[start_mask] = start_sheep

    from collections import deque
    stack = deque()
    stack.append((start_mask, start_sheep, start_wolf))

    while stack:
        mask, sheep, wolf = stack.pop()
        if sheep > answer:
            answer = sheep

        next_nodes = set()
        for u in range(n):
            if mask & (1 << u):
                for v in g[u]:
                    if not (mask & (1 << v)):
                        next_nodes.add(v)

        for v in next_nodes:
            ns = sheep + (1 if info[v] == 0 else 0)
            nw = wolf + (1 if info[v] == 1 else 0)
            if ns <= nw:
                continue
            nmask = mask | (1 << v)

            if best.get(nmask, -1) >= ns:
                continue
            best[nmask] = ns
            stack.append((nmask, ns, nw))

    return answer