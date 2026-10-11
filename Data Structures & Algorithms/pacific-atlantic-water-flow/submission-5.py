class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j, isPacific):
            if i < 0 or j < 0 or i >= rows or j >= cols or ((i, j) in pacific if isPacific else (i, j) in atlantic):
                return
            
            pacific.add((i, j)) if isPacific else atlantic.add((i, j))

            for x, y in dirs:
                nr, nc = i+x, j+y
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or ((nr, nc) in pacific if isPacific else (nr, nc) in atlantic) or heights[nr][nc] < heights[i][j]:
                    continue
                dfs(nr, nc, isPacific)
        
        for i in range(cols):
            dfs(0, i, True)
            dfs(rows - 1, i, False)
        
        for i in range(rows):
            dfs(i, 0, True)
            dfs(i, cols - 1, False)
        
        return list(pacific.intersection(atlantic))
