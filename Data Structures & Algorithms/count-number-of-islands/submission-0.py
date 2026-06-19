class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numRows = len(grid)
        numCols = len(grid[0])

        def dfs(r, c, numRows, numCols, grid):
            if (r,c) in visited or r < 0 or r >= numRows or c < 0 or c >= numCols or grid[r][c] == "0":
                return
            
            visited.add((r,c))
            dfs(r-1, c, numRows, numCols, grid)
            dfs(r+1, c, numRows, numCols, grid)
            dfs(r, c-1, numRows, numCols, grid)
            dfs(r, c+1, numRows, numCols, grid)

        res = 0
        
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j, numRows, numCols, grid)
                    res += 1
        
        return res
            

        