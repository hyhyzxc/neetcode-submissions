from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        rows = len(grid)
        cols = len(grid[0])

        queue = deque([])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        visited = set()
        while queue:
            i, j = queue.popleft()
            visited.add((i, j))
            for x, y in directions:
                newI, newJ = i+x, j+y
                if (newI >= 0 and newJ >= 0 and newI < rows and newJ < cols and
                (newI, newJ) not in visited and grid[newI][newJ] != -1):
                    queue.append((newI, newJ))
                    grid[newI][newJ] = min(grid[newI][newJ], 1 + grid[i][j])
        
