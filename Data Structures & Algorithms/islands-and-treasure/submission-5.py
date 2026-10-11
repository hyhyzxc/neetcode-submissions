from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque([])
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        while queue:
            i, j, dist = queue.popleft()
            visited.add((i, j))
            for x, y in dirs:
                nr, nc = i+x, j+y
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == -1:
                    continue
                grid[nr][nc] = min(grid[nr][nc], dist + 1)
                if (nr, nc) not in visited:
                    queue.append((nr, nc, grid[nr][nc]))
                    visited.add((nr, nc))
        
                
        

        
        
