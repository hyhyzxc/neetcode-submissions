from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        
        while queue:
            r, c, dist = queue.popleft()
            res = max(res, dist)

            for x, y in dirs:
                nr, nc = r+x, c+y
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visited or grid[nr][nc] == 0:
                    continue
                queue.append((nr, nc, dist + 1))
                grid[nr][nc] = 2
                visited.add((nr, nc))
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return res



        


        
