def solution(n, k, command):
    linked_list = {i: [i - 1, i + 1, False] for i in range(n)}
    linked_list[0][0] = -1       # 첫 행은 이전 없음
    linked_list[n - 1][1] = -1   # 마지막 행은 다음 없음
    deleted = []                 # 삭제 스택
    curr = k                     # 현재 위치

    for cmd in command:
        if cmd[0] == 'U':
            move = int(cmd[2:])
            for _ in range(move):
                curr = linked_list[curr][0]

        elif cmd[0] == 'D':
            move = int(cmd[2:])
            for _ in range(move):
                curr = linked_list[curr][1]

        elif cmd[0] == 'C':  # 삭제
            prev, nxt, _ = linked_list[curr]
            deleted.append((curr, prev, nxt))
            linked_list[curr][2] = True  # 삭제 표시

            # 위아래 링크 연결
            if prev != -1:
                linked_list[prev][1] = nxt
            if nxt != -1:
                linked_list[nxt][0] = prev

            # 이동 (아래가 있으면 아래로, 없으면 위로)
            curr = nxt if nxt != -1 else prev

        elif cmd[0] == 'Z':  # 복구
            node, prev, nxt = deleted.pop()
            linked_list[node][2] = False
            if prev != -1:
                linked_list[prev][1] = node
            if nxt != -1:
                linked_list[nxt][0] = node

    # 결과 문자열 생성
    result = []
    for i in range(n):
        result.append('X' if linked_list[i][2] else 'O')
    return ''.join(result)
