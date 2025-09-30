class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        one, two = 1, 2
        for i in range(3, n + 1):
            one, two = two, one + two

        return two