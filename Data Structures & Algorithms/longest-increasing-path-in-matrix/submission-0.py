class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = {}
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            curr = matrix[i][j]
            
            visited.add((i, j))
            
            up = dfs(i-1, j) if i > 0 and matrix[i-1][j] > curr else 0
            down = dfs(i+1, j) if i < rows - 1 and matrix[i+1][j] > curr else 0
            right = dfs(i, j+1) if j < cols - 1 and matrix[i][j+1] > curr else 0
            left = dfs(i, j-1) if j > 0 and matrix[i][j-1] > curr else 0

            res = max([up, down, left, right]) + 1

            dp[(i, j)] = res

            return res
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
            

        return res
            
