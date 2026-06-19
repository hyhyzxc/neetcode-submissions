class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacifics = set()
        atlantics = set()

        numRows = len(heights)
        numCols = len(heights[0])
        
        def pDfs(r, c, numRows, numCols, heights):
            if (r,c) in visited or r < 0 or c < 0 or r >= numRows or c >= numCols:
                return
            
            pacifics.add((r,c))
            visited.add((r,c))

            currHeight = heights[r][c]

            pDfs(r-1, c, numRows, numCols, heights) if r > 0 and heights[r-1][c] >= currHeight else None
            pDfs(r+1, c, numRows, numCols, heights) if r < numRows - 1 and heights[r+1][c] >= currHeight else None
            pDfs(r, c-1, numRows, numCols, heights) if c > 0 and heights[r][c-1] >= currHeight else None
            pDfs(r, c+1, numRows, numCols, heights) if c < numCols - 1 and heights[r][c+1] >= currHeight else None

        def aDfs(r, c, numRows, numCols, heights):
            if (r,c) in visited or r < 0 or c < 0 or r >= numRows or c >= numCols:
                return
            
            atlantics.add((r,c))
            visited.add((r,c))

            currHeight = heights[r][c]

            aDfs(r-1, c, numRows, numCols, heights) if r > 0 and heights[r-1][c] >= currHeight else None
            aDfs(r+1, c, numRows, numCols, heights) if r < numRows - 1 and heights[r+1][c] >= currHeight else None
            aDfs(r, c-1, numRows, numCols, heights) if c > 0 and heights[r][c-1] >= currHeight else None
            aDfs(r, c+1, numRows, numCols, heights) if c < numCols - 1 and heights[r][c+1] >= currHeight else None
        
        visited = set()
        for i in range(numCols):
            pDfs(0, i, numRows, numCols, heights)
        for i in range(numRows):
            pDfs(i, 0, numRows, numCols, heights)
        visited.clear()
        for i in range(numCols):
            aDfs(numRows - 1, i, numRows, numCols, heights)
        for i in range(numRows):
            aDfs(i, numCols - 1, numRows, numCols, heights)
        
        return list(atlantics.intersection(pacifics))

            