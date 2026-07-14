class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        startColor = image[sr][sc]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or image[i][j] != startColor:
                return
            
            visited.add((i, j))
            image[i][j] = color

            for x, y in dirs:
                dfs(i+x, j+y)
        
        dfs(sr, sc)
        return image

