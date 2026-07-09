class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        #     1
        #   1.    2
        #  1. 2. 1 2 3 4
        n = len(piles)
        dp = {}

        def dfs(isAlice, i, M):
            if i >= n:
                return 0
            
            if (isAlice, i, M) in dp:
                return dp[(isAlice, i, M)]
            
            totalStones = 0
            res = 0 if isAlice else float("inf")

            for j in range(2 * M):
                if i+j < n:
                    totalStones += piles[i+j]
                    if isAlice:
                        res = max(res, dfs(not isAlice, i+j+1, max(j+1, M)) + totalStones)
                    else:
                        res = min(res, dfs(not isAlice, i+j+1, max(j+1, M)))
            dp[(isAlice, i, M)] = res
            return res
        
        return dfs(True, 0, 1)

            
        