class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0 or (i, j) in visited:
                return 0
            
            visited.add((i, j))

            area = 1

            for x, y in neighbours:
                area += dfs(i+x, j+y)
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, dfs(i, j))
        
        return res

            
        