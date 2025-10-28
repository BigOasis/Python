"""
프로그래머스 81303. 표 편집

풀이시간: 50분
"""


def solution(n, k, cmd):
    # 링크드리스트
    pre = [i - 1 for i in range(n)]
    nxt = [i + 1 for i in range(n)]
    nxt[-1] = -1

    cur = k # 현재 위치 저장
    stk = [] # 삭제된 행 복구용 스택

    for c in cmd:
        if c[0] == 'U':
            x = int(c[2:])
            for _ in range(x):
                cur = pre[cur]

        elif c[0] == 'D':
            x = int(c[2:])
            for _ in range(x):
                cur = nxt[cur]

        elif c[0] == 'C':
            stk.append((cur, pre[cur], nxt[cur]))
            if pre[cur] != -1:
                nxt[pre[cur]] = nxt[cur]
            if nxt[cur] != -1:
                pre[nxt[cur]] = pre[cur]
            cur = nxt[cur] if nxt[cur] != -1 else pre[cur]

        elif c[0] == 'Z':
            c, p, n_ = stk.pop()
            if p != -1:
                nxt[p] = c
            if n_ != -1:
                pre[n_] = c

    ans = ['O'] * n
    for i, _, _ in stk:
        ans[i] = 'X'

    return ''.join(ans)
