class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if (i, j) in visited or i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
                return
            
            visited.add((i, j))

            for x, y in neighbours:
                dfs(i+x, j+y)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        
        return res
            

            


            

        