class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        arrSize = len(prices)

        l = 0
        r = 0

        if arrSize == 1:
            return res
        
        while r < arrSize:
            res = max(res, prices[r] - prices[l])

            if prices[r] <= prices[l]:
                l = r
                r = l + 1

            else:
                r += 1
        
        return res
        
            
        

        