class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}
        
        def dfs(i, j, k):
            if k >= len(s3):
                return True
            
            if (i < len(s1) and s1[i] != s3[k]) and (j < len(s2) and s2[j] != s3[k]):
                return False
            
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = res or dfs(i+1, j, k+1)
            
            if j < len(s2) and s2[j] == s3[k]:
                res = res or dfs(i, j+1, k+1)
            
            dp[(i,j,k)] = res

            return res
        
        return dfs(0, 0, 0)
            

            

        

        