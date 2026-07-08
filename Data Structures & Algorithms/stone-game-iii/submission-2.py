class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        #let alice be positive, bob be negative
        # if result = 0 -> tie, if > 0 -> alice, if < 0 -> bob
        # [5,-1,-5,2]
        # 5 -> -1 -> -5 -> 2 (bob)
        # 5, -1 -> -5, 2 (alice)
        # 5,-1,-5 -> 2 (bob)

        #alice wants to max score, bob wants to min score
        # at each move, there are 3 choices -> take 1, 2 or 3 stones

        n = len(stoneValue)
        dp = {}

        def dfs(i):
            if i >= n:
                return 0
            
            if i in dp:
                return dp[i]
    
            res = float("-inf")

            take1 = stoneValue[i] - dfs(i+1) if i < n else float('-inf')
            take2 = stoneValue[i] + stoneValue[i+1] - dfs(i+2) if i < n-1 else float('-inf')
            take3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dfs(i+3) if i < n-2 else float('-inf')
            res = max([take1, take2, take3])
            
            dp[i] = res
            return res
        
        for i in range(n-1, -1, -1):
            dfs(i)
        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"



        