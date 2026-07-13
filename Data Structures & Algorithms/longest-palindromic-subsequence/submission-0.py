class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # (0, 1) -> palindrome if s[0] == s[1]

        # (0, 2) -> palindrome if (1, 1) is palindrome and s[0] == s[2]
        # (0, 3) -> (0, 1) + (3, 3)
        n = len(s)
        res = 0
        dp = {}
        def dfs(i, j):
            if i > j:
                return 0
            
            if i >= n or j >= n:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i == j:
                return 1
            
            if s[i] != s[j]:
                dp[(i, j)] = max(dfs(i, j-1), dfs(i+1, j))

            else:
                dp[(i, j)] = 2 + dfs(i+1, j-1)
            
            return dp[(i, j)]
        
        for i in range(n):
            res = max(res, dfs(0, i))
        
        return res
            
        
            
            


        