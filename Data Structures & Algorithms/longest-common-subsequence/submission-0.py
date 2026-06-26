class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        dp = [[-1 for i in range(n2)] for j in range(n1)]

        def dfs(i, j):
            if i >= n1 or j >= n2:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            res = 0
            if text1[i] == text2[j]:
                res = 1 + dfs(i+1, j+1)
            else:
                res = max(dfs(i+1, j), dfs(i, j+1))
            
            dp[i][j] = res
            return res
        
        return dfs(0, 0)

        
        

