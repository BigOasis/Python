from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # result = [0] * len(temperatures)

        # for i in range (len(temperatures)-1):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j - i
        #             break

        # return result

        # 스택을 활용해서 한번 구해보자~
        
        result = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                result[prev_i] = i-prev_i
            stack.append(i)

        return result




        