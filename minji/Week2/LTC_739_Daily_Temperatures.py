# https://leetcode.com/problems/daily-temperatures/description/
# class Solution:
#     def dailyTemperatures(self, temperatures):
#         n = len(temperatures)
#         result = [0] * n

#         # 하나씩 보면서 뒤에 따뜻한 날 있는지 찾기
#         for i in range(n):
#             found = False   # 따뜻한 날을 찾았는지 표시하기위해 플래그 뒀음
#             for j in range(i+1, n):
#                 if temperatures[j] > temperatures[i]:
#                     result[i] = j - i
#                     found = True
#                     break
#             if not found:
#                 result[i] = 0  # 기본값으로 0
#         return result
# 그냥 하나씩 찾다가 타임아웃.. 스택으로 변경

class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []  # 인덱스저장 스택

        for i in range(n):
            # 지금 온도가 스택 마지막 인덱스의 온도보다 크면
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index  # 며칠 기다렸는지 계산
            stack.append(i)  # 현재 인덱스를 스택에 넣음

        return result
