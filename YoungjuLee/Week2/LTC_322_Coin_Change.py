"""
리트코드 322번: Coin Change
20~
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10 ** 12
        dp = [0] + [INF] * amount
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] != INF else -1

# coins = [1, 2, 5]
# amount = 11
# print(Solution().coinChange(coins, amount))
