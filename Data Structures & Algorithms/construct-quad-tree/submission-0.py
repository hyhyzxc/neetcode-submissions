"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(r, c, n):
            target = grid[r][c]
            allSame = True

            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != target:
                        allSame = False
                        break
            
            if allSame:
                return Node(target, True, None, None, None, None)
            
            root = Node(0, 0, None, None, None, None)
            root.topLeft = dfs(r, c, n//2)
            root.topRight = dfs(r, c + n//2, n//2)
            root.bottomLeft = dfs(r + n//2, c, n//2)
            root.bottomRight = dfs(r + n//2, c + n//2, n//2)
            return root
        
        return dfs(0, 0, len(grid))
