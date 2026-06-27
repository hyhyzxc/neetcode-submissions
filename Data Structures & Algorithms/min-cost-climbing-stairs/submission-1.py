class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        n = len(cost)

        if n <= 2:
            return min(cost)

        dp[n-2] = cost[n-2]
        dp[n-1] = cost[n-1]

        for i in range(n-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])