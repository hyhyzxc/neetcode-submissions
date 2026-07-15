class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or grid[i][j] == 0:
                return
            
            visited.add((i, j))

            for x,y in dirs:
                nr, nc = i+x, j+y
                if (nr, nc) not in visited:
                    dfs(nr, nc)
            
        
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        
        for i in range(cols):
            dfs(0, i)
            dfs(rows - 1, i)
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res += 1
        
        return res
            