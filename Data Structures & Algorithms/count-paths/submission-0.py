class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]

        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            
            if (i == m - 1 and j == n - 1):
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            down = dfs(i+1, j)
            right = dfs(i, j+1)

            dp[i][j] = down + right
            return dp[i][j]
        
        return dfs(0, 0)
            

            

            


            
            
        