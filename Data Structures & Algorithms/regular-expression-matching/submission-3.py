class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)

        dp = {}

        def dfs(i, j):
            if j >= n2:
                return i >= n1

            if (i, j) in dp:
                return dp[(i, j)]
            
            res = False
            
            match = i < n1 and (s[i] == p[j] or p[j] == '.')

            if j < n2 - 1 and p[j+1] == '*':
                res = dfs(i, j+2) or (match and dfs(i+1, j))
            else:
                if match:
                    res = dfs(i+1, j+1)
                else:
                    res = False

            dp[(i, j)] = res

            return dp[(i, j)]
        
        return dfs(0, 0)
            
