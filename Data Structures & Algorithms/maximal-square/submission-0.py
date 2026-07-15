class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 0 1
        # 1 0
        rows = len(matrix)
        cols = len(matrix[0])

        res = 0
        dp = {}

        def dfs(i, j):
            nonlocal res

            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == "0":
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] = min([dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1)]) + 1

            return dp[(i, j)]
        
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        return res * res