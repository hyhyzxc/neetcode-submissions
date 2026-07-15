from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([(0, 0, 1)]) # row, col, length
        visited = set()
        if grid[0][0] == 1:
            return -1

        while queue:
            r, c, length = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return length

            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            for x, y in dirs:
                nr, nc = r+x, c+y
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or grid[nr][nc] == 1:
                    continue
                
                queue.append((nr, nc, length + 1))
        
        return -1

