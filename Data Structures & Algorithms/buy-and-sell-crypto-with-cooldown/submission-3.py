from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)

        dp = defaultdict(int)

        def dfs(i, canBuy, buyPrice):
            nonlocal res
            
            if i >= n:
                return 0
            
            if dp[(i, canBuy, buyPrice)] != 0:
                return dp[(i, canBuy, buyPrice)]
            
            if not canBuy:
                # sell it 
                earned = prices[i] - buyPrice
                sold = dfs(i+2, True, 0)

                # don't sell it
                notSold = dfs(i+1, False, buyPrice)

                maxProfit = max(sold + earned, notSold)
                dp[(i, canBuy, buyPrice)] = maxProfit

                res = max(res, maxProfit)
            
            else:
                # buy
                bought = dfs(i+1, False, prices[i])

                # don't buy
                notBought = dfs(i+1, True, 0)

                maxProfit = max(bought, notBought)
                res = max(res, maxProfit)

                dp[(i, canBuy, buyPrice)] = maxProfit
            
            return dp[(i, canBuy, buyPrice)]

        dfs(0, True, 0)

        return res
            

            
