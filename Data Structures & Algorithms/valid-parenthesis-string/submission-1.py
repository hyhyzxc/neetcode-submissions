from collections import defaultdict
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = {}
        
        def dfs(i, open):
            if open < 0:
                return False
            
            if i >= n:
                return open == 0
            
            if (i, open) in dp:
                return dp[(i, open)]
            
            res = False
            if s[i] == '(':
                res = dfs(i+1, open+1)
            elif s[i] == ')':
                res = dfs(i+1, open-1)
            else:
                res = dfs(i+1, open) or dfs(i+1, open+1) or dfs(i+1, open-1)
            
            dp[(i, open)] = res
            return res
        
        return dfs(0, 0)

            

        