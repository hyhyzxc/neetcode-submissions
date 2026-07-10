import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        minHeap = [(0, 0, 0)] #effort, row, col

        while minHeap:
            effort, r, c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return effort
            
            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            for x, y in directions:
                nr, nc = r+x, c+y
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols and (nr, nc) not in visited:
                    heapq.heappush(minHeap, (max(abs(heights[nr][nc] - heights[r][c]), effort), nr, nc))
        
            

