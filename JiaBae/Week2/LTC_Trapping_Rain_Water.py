class Solution(object):
    def trap(self, height):
        stack = []  
        water = 0

        for i, h in enumerate(height):
            # 오른쪽 벽이 더 높아지는 순간, 가운데를 채움
            while stack and height[stack[-1]] < h:
                mid = stack.pop()             # 바닥
                if not stack:                 # 왼쪽 벽이 없으면 종료
                    break
                left = stack[-1]              # 왼쪽 벽
                width = i - left - 1
                bounded = min(height[left], h) - height[mid]
                if bounded > 0:
                    water += width * bounded
            stack.append(i)

        return water