class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(i, j):
            nonlocal res
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                print(i, j)
                res += 1
                return

            if (i, j) in visited:
                return

            visited.add((i, j))

            for x, y in directions:
                if (i+x, j+y) not in visited:
                    dfs(i+x, j+y)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
        
        return res




            

