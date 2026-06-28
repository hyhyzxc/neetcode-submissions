class Solution:
    def change(self, amount: int, coins: List[int]) -> int:        
        dp = {}

        def dfs(i, amount):
            if amount < 0 or i >= len(coins):
                return 0
            
            if amount == 0:
                return 1
            
            if (i, amount) in dp:
                return dp[(i, amount)]
            
            # take the current coin
            res = dfs(i, amount - coins[i])

            # skip the current coin
            res += dfs(i+1, amount)

            dp[(i, amount)] = res
            return res
        
        return dfs(0, amount)
