class Solution(object):
    def coinChange(self, coins, amount):
        INF = amount + 1
        dp = [0] + [INF] * amount

        for i in range(1, amount + 1) :
            for c in coins :
                if c <= i :
                    dp[i] = min(dp[i], dp[i-c] + 1)

        return dp[amount] if dp[amount] != INF else -1

