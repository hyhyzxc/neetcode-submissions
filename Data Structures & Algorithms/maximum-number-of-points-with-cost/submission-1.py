class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
            #            o
            #      /     |.     \
            #     1.     2.      3
            #    /|\    /|\     /|\
            #   1 5 1  1 5 1   1 5 1
            #  /|\
            # 3 1 1

            # height of tree: number of rows
            # each node has number of cols possible choices

        rows = len(points)
        cols = len(points[0])
        dp = {}

        def dfs(r, c):
            if r >= rows:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            currPoints = 0

            for nextCol in range(cols):
                currPoints = max(points[r][c] + dfs(r + 1, nextCol) - abs(c - nextCol), currPoints)
            
            dp[(r, c)] = currPoints
            
            return currPoints
        
        res = 0

        for c in range(cols):
            res = max(res, dfs(0, c))
        
        return res

