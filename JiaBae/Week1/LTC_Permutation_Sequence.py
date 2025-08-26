"""
leetcode: Permutation Sequence
시간복잡도 : O(n!)
itertools 사용 방식
"""
from itertools import permutations

class Solution(object):
    def getPermutation(self, n, k):
        cnt = 0 
        for p in permutations(range(1, n+1)) :
            cnt += 1
            if cnt == k :
                return "".join(map(str, p))
        