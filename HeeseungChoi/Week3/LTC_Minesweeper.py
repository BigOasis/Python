from collections import deque
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        # 일단 E 면 클릭이 가능한 상태
        # B는 사방이 안전하다는 뜻 8면 전부 안전하다 / 주변 지뢰가 없으면 B
        # 숫자는 근처 지뢰의 개수
        # M은 지뢰이며 발견하면 => X로 변경되며 종료

        m, n = len(board), len(board[0])
        r, c = click

        # 8방향 (상하좌우 + 대각선)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # 좌표 유효성 검사
        def in_bounds(y: int, x: int) -> bool:
            return 0 <= y < m and 0 <= x < n

        # 인접 지뢰('M') 개수 세기
        def count_mines(y: int, x: int) -> int:
            cnt = 0
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if in_bounds(ny, nx) and board[ny][nx] == 'M':
                    cnt += 1
            return cnt

        # 클릭이 지뢰인 경우 → 'X'로 바꾸고 즉시 반환
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        # 클릭이 'E'인 경우 BFS 시작
        q = deque()
        q.append((r, c))
        # 큐에 넣는 즉시 'B'로 바꿔 중복 삽입 방지(방문 마킹)
        board[r][c] = 'B'

        while q:
            y, x = q.popleft()

            # 현재 칸 주변 지뢰 개수 계산
            mines = count_mines(y, x)

          # 주변에 지뢰가 하나 이상 → 숫자로 표기하고 더 확장 X
            if mines > 0:
                board[y][x] = str(mines)
                continue

            # mines == 0 → 빈 칸('B') 유지, 인접 'E'를 큐에 넣어 확장
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if in_bounds(ny, nx) and board[ny][nx] == 'E':
                    # 방문 표시 겸 중복 방지: 큐에 넣는 즉시 'B'로 바꿔둔다
                    board[ny][nx] = 'B'
                    q.append((ny, nx))

        return board

        
        