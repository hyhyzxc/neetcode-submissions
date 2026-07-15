class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        def dfs(i, j):

            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0, False
            
            if grid[i][j] == 0:
                return 0, True
            
            visited.add((i, j))

            res = 1
            isEnclave = True
            for x, y in dirs:
                newRow, newCol = i+x, j+y
                if (newRow, newCol) not in visited:
                    count, enclave = dfs(newRow, newCol)
                    if not enclave:
                        isEnclave = False
                    res += count

            return res, isEnclave
        
        res = 0

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    count, isEnclave = dfs(i, j)
                    if isEnclave:
                        res += count
        
        return res