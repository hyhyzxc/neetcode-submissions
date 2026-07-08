import math
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {}
        sumStones = sum(stones)
        target = math.ceil(sumStones / 2)
        n = len(stones)
        
        def dfs(i, total):
            if i >= n or total >= target:
                return abs(total - (sumStones - total))
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total + stones[i]))
            return dp[(i, total)]
        
        return dfs(0, 0)
            