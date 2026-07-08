class Solution:
    def numSquares(self, n: int) -> int:
        # 1, 4, 9, 16, 25

        # f(13) = f(9) + f(4) = 2

        # f(6) = f(4) + f(2) + f(1)

        # get the perfect square that is greatest and is <= n

        # recursively call dfs(i) where i = n - largest perfect square

        # for example: f(13) = f(4) + f(0)
        perfectSquares = []

        dp = {}

        for i in range(1, n+1):
            if i * i > n:
                break
            perfectSquares.append(i * i)
        
        perfectSquares.sort(reverse = True)

        def dfs(i):
            if i <= 0:
                return 0

            if i in dp:
                return dp[i]
            
            res = float("inf")
            for num in perfectSquares:
                if i - num >= 0:
                    res = min(res, 1 + dfs(i - num))
            
            dp[i] = res
            return res
        
        return dfs(n)

        




                    