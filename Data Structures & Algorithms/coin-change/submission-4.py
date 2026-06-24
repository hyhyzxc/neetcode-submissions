class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        dp[0] = 0
        
        def dfs(i):
            if i < 0:
                return amount+1
            
            if i in dp:
                return dp[i]
            
            minWays = amount + 1
            for coin in coins:
                if amount - coin >= 0:
                    minWays = min(minWays, dfs(i-coin))
            
            dp[i] = minWays + 1
            return dp[i]
        
        res = dfs(amount)
        return res if res <= amount else -1
            


        