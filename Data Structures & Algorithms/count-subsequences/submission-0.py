class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        
        dp = {}

        def dfs(i, j):
            if j >= n2:
                return 1
            
            if i >= n1:
                return 0
            
            if (i,j) in dp:
                return dp[(i, j)]

            res = 0
            if s[i] != t[j]:
                res = dfs(i+1, j)
            else:
                res += dfs(i+1, j+1)
                res += dfs(i+1, j)
            
            dp[(i,j)] = res
            
            return res
        
        return dfs(0, 0)
        
