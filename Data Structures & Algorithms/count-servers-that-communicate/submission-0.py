class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rowCount = [0] * rows
        colCount = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and max(rowCount[i], colCount[j]) > 1:
                    res += 1
        
        return res