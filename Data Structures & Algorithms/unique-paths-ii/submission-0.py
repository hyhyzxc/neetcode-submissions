class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dp = {}

        if obstacleGrid[0][0] == 1:
            return 0

        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            
            if i >= m or j >= n:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 0
            
            if i < m-1 and obstacleGrid[i+1][j] == 0:
                res += dfs(i+1, j) 
            
            if j < n-1 and obstacleGrid[i][j+1] == 0:
                res += dfs(i, j+1)

            dp[(i, j)] = res
            
            return res
        
        res = dfs(0, 0)
        print(dp)
        return res
                
