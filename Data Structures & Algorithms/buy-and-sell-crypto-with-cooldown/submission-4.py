from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[-1 for i in range(2)] for j in range(n)]

        def dfs(i, canBuy):
            if i >= n:
                return 0
            
            if dp[i][canBuy] != -1:
                return dp[i][canBuy]
            
            if canBuy:
                bought = dfs(i+1, False) - prices[i]
                skipped = dfs(i+1, True)
                dp[i][canBuy] = max(bought, skipped)

            else:
                sold = dfs(i+2, True) + prices[i]
                skipped = dfs(i+1, False)
                dp[i][canBuy] = max(sold, skipped)
            
            return dp[i][canBuy]
        
        dfs(0, True)
        return dp[0][True]
            
            