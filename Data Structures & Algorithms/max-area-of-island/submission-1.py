class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        numRows = len(grid)
        numCols = len(grid[0])

        maxSize = 0

        def dfs(r, c, numRows, numCols, grid):
            nonlocal maxSize

            if (r,c) in visited or r < 0 or r >= numRows or c < 0 or c >= numCols or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            currSize = 1
            
            currSize += dfs(r-1, c, numRows, numCols, grid)
            currSize += dfs(r+1, c, numRows, numCols, grid)
            currSize += dfs(r, c-1, numRows, numCols, grid)
            currSize += dfs(r, c+1, numRows, numCols, grid)

            return currSize
        
        for i in range(numRows):
            for j in range(numCols):
                if (i, j) not in visited and grid[i][j] == 1:
                    currSize = dfs(i, j, numRows, numCols, grid)
                    if currSize > maxSize:
                        maxSize = currSize
        
        return maxSize

            
        