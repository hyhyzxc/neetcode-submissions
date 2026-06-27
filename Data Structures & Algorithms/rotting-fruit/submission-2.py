from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        dp = [[-1 for i in range(cols)] for j in range(rows)]

        queue = deque([])
        distances = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dp[i][j] = 1000
                elif grid[i][j] == 2:
                    dp[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()
            visited.add((i, j))

            for x, y in distances:
                newI, newJ = i+x, j+y
                if (newI >= 0 and newI < rows and newJ >= 0 and newJ < cols
                and (newI, newJ) not in visited and grid[newI][newJ] != 0):
                    queue.append((newI, newJ))
                    dp[newI][newJ] = min(dp[newI][newJ], dp[i][j] + 1)
        
        for i in range(rows):
            for j in range(cols):
                if dp[i][j] == 1000:
                    return -1
                res = max(dp[i][j], res)
        
        return res



        
