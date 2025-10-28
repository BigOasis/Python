def solution(n, k, cmd):
    prev = [i-1 for i in range(n)]
    next = [i+1 for i in range(n)]
    next[n-1] = -1
    alive = [True] * n
    trash = []
    cur = k
    
    for c in cmd:
        parts = c.split()
        move = parts[0]
        
        if move == 'U':
            step = int(parts[1])
            for _ in range(step):
                cur = prev[cur]
        elif move == 'D':
            step = int(parts[1])
            for _ in range(step):
                cur = next[cur]
        elif move == 'C':
            # 현재 행 삭제
            trash.append((cur, prev[cur], next[cur]))
            alive[cur] = False
            # 링크드 리스트 연결
            if prev[cur] != -1:
                next[prev[cur]] = next[cur]
            if next[cur] != -1:
                prev[next[cur]] =prev[cur]
            # 선택 행 이동
            cur = next[cur] if next[cur] != -1 else prev[cur]
        else:
            row, p, n = trash.pop()
            alive[row] = True
            if p != -1:
                next[p] = row
            if n != -1:
                prev[n] = row
            prev[row], next[row] = p, n
            
    
    return ''.join('O' if a else 'X' for a in alive)