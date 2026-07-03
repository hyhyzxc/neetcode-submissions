class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs(i, j):
            if i >= rows or i < 0 or j >= cols or j < 0 or (i, j) in visited or grid[i][j] == '0':
                return

            visited.add((i, j))
            for x, y in directions:
                newRow, newCol = i+x, j+y
                dfs(newRow, newCol)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    dfs(i, j)
        
        return res
            


            

        