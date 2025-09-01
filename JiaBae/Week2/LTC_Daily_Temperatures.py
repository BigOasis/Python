"""
leetcode: Daily Temperatures
시간복잡도 : O(n) for문 안의 while 영향 안받는 전체가 선형인 구조
스택
"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answers = [0] * n 
        stack = []

        for i in range(n) :
            while stack and temperatures[stack[-1]] < temperatures[i] :
                answers[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)
        
        return answers
        