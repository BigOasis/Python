"""
LeetCode 739: Daily Temperatures
16분

단조 감소 스택:
- 스택에는 '아직 더 따뜻한 날을 못 찾은 인덱스'만 쌓임
- 항상 온도가 내림차순으로 유지됨
- 더 따뜻한 날이 오면 스택에서 꺼내며 답을 채움
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []  # 단조 감소 스택(인덱스 저장)

        for i, t in enumerate(temperatures):
            # 현재 온도가 더 따뜻하면, 스택에서 꺼내 답 확정
            while stk and temperatures[stk[-1]] < t:
                j = stk.pop()
                res[j] = i - j
            # i번째 날은 아직 더 따뜻한 날을 못 찾음 → 스택에 넣고 대기
            stk.append(i)
        return res

# print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
