class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r,c,idx):
            # 단어 전체를 찾았으면 성공!
            if idx == len(word):
                return True
            # 범위를 벗어나거나
            if r < 0 or r >= rows or c < 0 or c >=cols:
                return False
            # 문자가 다르면 실패
            if board[r][c] != word[idx]:
                return False
						
            #@로 변경하여 방문처리하기
            temp = board[r][c]
            board[r][c] = '@'

            #위치에서 동서남북 탐색
            found = (
                dfs(r+1,c,idx+1) or
                dfs(r-1,c,idx+1) or
                dfs(r,c+1,idx+1) or
                dfs(r,c-1,idx+1)
            )
            # 백트래킹으로 원상복구하기
            board[r][c] = temp
            
            return found
        #모든 경우의 수의 위치에서 시작시도하기
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
                    
        return False
        
# s = Solution()
# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]

# result = s.exist(board, "ABCCED")
# print('결과', result)
