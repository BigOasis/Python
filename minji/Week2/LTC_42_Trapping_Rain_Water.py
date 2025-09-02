# 그냥 막 구했다가 타임아웃나서 투포인터로 바꿔서 풀었음 ㅜㅜ
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         water = 0
        
#         # 각 칸을 돌면서 왼쪽/오른쪽 최대 찾기
#         for i in range(n):
#             left = max(height[:i+1])   # 왼쪽 최대
#             right = max(height[i:])    # 오른쪽 최대
#             water += min(left, right) - height[i]
        
#         return water

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        left_max = [0] * n
        right_max = [0] * n

        # 왼쪽 최대 구하기
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # 오른쪽 최대 구하기
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # 물 계산
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water
