class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        if n == 1:
            return 1
        for _ in range(3, n+1):
            a, b = b, a+b
        return b
