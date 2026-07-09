class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        res = float('-inf')
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            takeFirst = -dfs(l+1, r) + piles[l]
            takeLast = -dfs(l, r-1) + piles[r]

            dp[(l, r)] = max(takeFirst, takeLast)

            return dp[(l, r)]
        
        score = dfs(0, len(piles) - 1)

        return True if score >= 0 else False




        