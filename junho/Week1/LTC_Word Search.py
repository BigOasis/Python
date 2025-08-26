class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0]) # 가로, 세로 크기부터 뽑아내기
        def dfs(r, c, idx):
            # 기저 조건에 도달했을 경우
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False
            
            #"방문했다"라고 표시해 줘야 한다
            temp = board[r][c]
            board[r][c] = "#"

            # 인접한 곳 방문
            found = (dfs(r + 1, c, idx + 1) or
                     dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or
                     dfs(r, c - 1, idx + 1))

            # 백트래킹: 선택한 칸을 해제한다
            board[r][c] = temp
            return found
        
        # 시작되는 문자를 찾기 위해 board를 순회해야 한다
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False