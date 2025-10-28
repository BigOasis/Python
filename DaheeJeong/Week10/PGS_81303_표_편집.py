def solution(n, k, cmd):
    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    next[-1] = -1
    stack = []
    cur = k

    for c in cmd:
        if c[0] == "U":
            x = int(c.split()[1])
            for _ in range(x):
                cur = prev[cur]
        elif c[0] == "D":
            x = int(c.split()[1])
            for _ in range(x):
                cur = next[cur]
        elif c[0] == "C":
            stack.append((cur, prev[cur], next[cur]))
            if prev[cur] != -1:
                next[prev[cur]] = next[cur]
            if next[cur] != -1:
                prev[next[cur]] = prev[cur]
            cur = next[cur] if next[cur] != -1 else prev[cur]
        else:  # Z (복원)
            i, p, n_ = stack.pop()
            if p != -1:
                next[p] = i
            if n_ != -1:
                prev[n_] = i

    result = ["O"] * n
    for i, _, _ in stack:
        result[i] = "X"
    return "".join(result)
