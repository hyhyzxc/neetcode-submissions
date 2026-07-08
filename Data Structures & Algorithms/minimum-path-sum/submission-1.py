import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = {}

        def dfs(i, j):
            if i == rows - 1 and j == cols - 1:
                return grid[rows-1][cols-1]
            
            if i >= rows or j >= cols:
                return float("inf")
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = min(dfs(i, j+1), dfs(i+1, j)) + grid[i][j]
            dp[(i, j)] = res

            return res
        
        return dfs(0, 0)
