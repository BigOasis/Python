class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        # 땅을 다 물로 바꿔버리는 함수 (발견하면 연결된 땅을 그냥 물로 만들어!!!)
        def sink(r, c):
            if r < 0 or r >= row_len or c < 0 or c >= col_len:
                return
            if grid[r][c] == "0":
                return
            
            # 땅을 물로 바꾸기
            grid[r][c] = "0"
            
            # 네 방향 다 확인하기
            sink(r+1, c)
            sink(r-1, c)
            sink(r, c+1)
            sink(r, c-1)
        
        count = 0
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1":   # 땅 발견!
                    count += 1
                    sink(r, c)  # 근처 다 물로 바꿔버림
                    
        return count
