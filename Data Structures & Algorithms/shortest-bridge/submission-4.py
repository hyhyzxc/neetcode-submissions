from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # find one island first
        # use bfs and add neighbouring water nodes until we get a land node that is not part of the first island
        n = len(grid)
        islandNodes = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= n or (i, j) in islandNodes or grid[i][j] == 0:
                return
            
            islandNodes.add((i, j))

            for x, y in dirs:
                dfs(i+x, j+y)
        
        islandRow, islandCol = (0, 0)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    islandRow, islandCol = i, j
                    break
        
        dfs(islandRow, islandCol)
                    

        queue = deque([])
        visited = set()

        for node in islandNodes:
            queue.append((node[0], node[1], 0))
            visited.add(node)
        
        while queue:
            row, col, bridgeLength = queue.popleft()

            visited.add((row, col))

            for x, y in dirs:
                newRow, newCol = row + x, col + y
                if newRow < 0 or newRow >= n or newCol < 0 or newCol >= n or (newRow, newCol) in visited:
                    continue
                
                if grid[newRow][newCol]:
                    return bridgeLength
                
                visited.add((newRow, newCol))
                queue.append((newRow, newCol, bridgeLength + 1))

            
