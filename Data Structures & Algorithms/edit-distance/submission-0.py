class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        dp = {}
        # dp[i][j] -> number of operations to make word1[:i] to become word2[:j]

        def dfs(i, j):
            if i >= n1 and j >= n2:
                return 0

            elif i >= n1 and j < n2:
                return n2 - j
            
            elif i < n1 and j >= n2:
                return n1 - i
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if word1[i] == word2[j]:
                res = dfs(i+1, j+1)
            
            else:
                insert = dfs(i, j+1)
                replace = dfs(i+1, j+1)
                delete = dfs(i+1, j)
                res = min(insert, replace, delete) + 1
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0)
