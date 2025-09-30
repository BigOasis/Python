from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost의 길이가 계단의 수 / len(cost)
        # 계단의 경우의 수는 dp[stair-1]  / dp[stair-2] 두가지

        stair = len(cost)
        dp = [0] * stair
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2,stair):
            dp[i] = cost[i] + min(dp[i-1] ,dp[i-2])

        # 마지막 계단에서 끝나는 게 아니라,
        # 꼭대기에 올라가야 하므로 마지막 두 계단 중 최소값 선택

        return min(dp[stair-1] ,dp[stair-2])

