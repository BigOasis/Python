class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = i원을 만들 때 최소 동전 수
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0원은 동전 0개

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
