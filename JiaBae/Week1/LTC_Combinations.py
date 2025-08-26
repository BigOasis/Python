"""
leetcode: Combinations
시간복잡도 : Θ(k x C(n, k))
직접 구현 방식 + combinations 사용 방식
"""
class Solution(object):
    def combine(self, n, k):
        result = []
        temp = []
        def dfs(idx) :
            # 가능한 조합 나오면 result에 저장 
            if len(temp) == k :
                result.append(temp[:])
                return

            for i in range(idx, n+1) :
                temp.append(i)
                dfs(i+1)
                temp.pop()
        
        dfs(1)
        return result
        
# 라이브러리 사용하여 푸는 법
from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        return [list(c) for c in combinations(range(1, n+1), k)]

        