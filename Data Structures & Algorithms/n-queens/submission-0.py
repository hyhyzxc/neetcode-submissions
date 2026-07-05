from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # convert input n to a grid of n x n
        # each slot (i, j) -> 0 (empty), 1(has a queen), -1 (cannot put queen)
        # for each column:
        # select a valid slot
        # mark those blocked with -1
        # perform backtracking for each column, if no slots, return

        grid = [[0 for i in range(n)] for j in range(n)]
        res = []

        def markBlocked(i, j, grid):
            for row in range(i+1, n):
                grid[row][j] = -1
            
            for col in range(j+1, n):
                grid[i][col] = -1
            
            row, col = i+1, j+1
            while row < n and col < n:
                grid[row][col] = -1
                row += 1
                col += 1
            
            row, col = i-1, j+1
            while row >= 0 and col < n:
                grid[row][col] = -1
                row -= 1
                col += 1
        
        def convert(grid):
            res = []
            for i in range(n):
                currRow = []
                for j in range(n):
                    if grid[i][j] == 1:
                        currRow.append('Q')
                    else:
                        currRow.append('.')
                res.append(''.join(currRow))
            return res

        # i -> column that we are at
        def backtrack(col, grid):
            if col >= n:
                res.append(convert(grid))
                return
            for row in range(n):
                if grid[row][col] == 0:
                    grid[row][col] = 1
                    newGrid = deepcopy(grid)
                    markBlocked(row, col, newGrid)
                    backtrack(col + 1, newGrid)
                    grid[row][col] = 0
        
        backtrack(0, grid)
        return res

        